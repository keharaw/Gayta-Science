#importing required packages
import config
import tweepy
import pandas as pd

# Accessing the Twitter API
client = tweepy.Client(bearer_token=config.bearer_token, 
                       consumer_key=config.api_key, 
                       consumer_secret=config.api_key_secret, 
                       access_token=config.access_token, 
                       access_token_secret=config.access_token_secret)

 # outlining the key words and the outputs we want from our search
query = "(lgbt OR lgbtq OR lgbtq+ OR transgender OR bisexual OR gay OR trans OR queer OR lesbian) ((soccer OR football OR (world cup)) OR qatar) -is:retweet"

tweet_fields=["id", "text", "author_id", "context_annotations","created_at", "entities","public_metrics" , "lang", "geo", "possibly_sensitive"]
                      
# Obtaining the tweets that match our requirements and paginating through
lgbt_tweets = [tweet for tweet in tweepy.Paginator(client.search_recent_tweets, 
                                                  query=query, 
                                                  tweet_fields=tweet_fields,
                                                  user_fields="location",
                                                   expansions=["geo.place_id","author_id"],
                                                   place_fields=['place_type', 'geo'],
                                                   max_results=100,
                                                   limit=1000).flatten()]

# Saving as a dataframe and storing within a CSV
df1 = pd.DataFrame([{field: tweet[field]  for field in tweet_fields} for tweet in lgbt_tweets])
df1.to_csv('sample_6_dec_2.csv', index=False)

# performing the same code again approximately 7 days after and saving as csv
df2 = pd.DataFrame([{field: tweet[field]  for field in tweet_fields} for tweet in lgbt_tweets])
df2.to_csv('sample_15_dec_1.csv', index=False)

# performing the same process for World Cup Tweets

query1 = "-(lgbt OR lgbtq OR lgbtq+ OR transgender OR bisexual OR gay OR trans OR queer OR lesbian) ((soccer OR football OR (world cup)) OR qatar) -is:retweet"

tweet_fields=["id", "text", "author_id", "context_annotations","created_at", "entities","public_metrics" , "lang", "geo", "possibly_sensitive"]

world_cup_tweets = [tweet for tweet in tweepy.Paginator(client.search_recent_tweets, 
                                                  query=query1, 
                                                  tweet_fields=tweet_fields,
                                                  user_fields="location",
                                                   expansions=["geo.place_id","author_id"],
                                                   place_fields=['place_type', 'geo'],
                                                   max_results=100,
                                                   limit=300).flatten()]
df3 = pd.DataFrame([{field: tweet[field]  for field in tweet_fields} for tweet in world_cup_tweets])

df3.to_csv('world_cup_no_lgbt_tweets.csv', index=False)

# Merging the data for LGBT and World Cup tweets into one csv
# Load the first dataset
df1 = pd.read_csv('sample_6_dec_2.csv')

# Load the second dataset
df2 = pd.read_csv('sample_15_dec_1.csv')

# Merge the two datasets
df_merged = pd.concat([df1, df2])
df_merged.to_csv('lgbt_world_cup_tweets.csv', index=False)

# Describing Data

# importing the libraries that we will use to visualise the data.
import matplotlib.pyplot as plt 
from plotnine import *

# importing csv that contains the dataset of tweets related to both LGBT and the World Cup
df_lgbt = pd.read_csv('lgbt_world_cup_tweets.csv', parse_dates=['created_at'])
# importing csv that contains the dataset of tweets related to only World Cup and excluding lgbt
df_wc = pd.read_csv('world_cup_no_lgbt_tweets.csv', parse_dates=['created_at'])

# getting a line graph to show the distribution of tweets for LGBT and WC

plot_df1 = (
     df_lgbt.groupby(pd.Grouper(key="created_at", freq='1D'))
       .apply(lambda x: pd.Series({"count": len(x), "pctg": f"{100*(len(x)/df_lgbt.shape[0]):.2f} %"})).reset_index()
)

g1 = (
    ggplot(plot_df1, aes(x="created_at", y="count", label="count"))
    + geom_line(color="#1DA1F2")
    + geom_text(aes(y="count+300"))
    + geom_point(color="#1DA1F2") 

    + theme_bw()
    + theme(figure_size=[10, 8]) 
    + labs(x="Day", y="Count")
)

# Show the plot
g1
# Save the lot
g1.save(filename = "line_chart_tweet_count_A.png")

# Getting a pie chart of the language breakdown for tweets about LGBT and the World Cup

plot_df2 = (
     df_lgbt.groupby(pd.Grouper(key="lang"))
       .apply(lambda x: pd.Series({"count": len(x), "pctg": f"{100*(len(x)/df_lgbt.shape[0]):.2f}"})).reset_index()
)

# turning percentage into float
plot_df2["pctg"] = plot_df2["pctg"].astype(float)

print(plot_df2)

plt.figure(figsize=(10,10))

# Plot the pie chart
plt.pie(plot_df2["count"],autopct=None, labels=None)

# Format the labels
labels = ["{} ({:.2f}%)".format(l, p) for l, p in zip(plot_df2["lang"], plot_df2["pctg"])]


# Add a legend to the pie chart
plt.legend(plot_df2["lang"], title="Languages", loc="upper left", bbox_to_anchor=(1,1), ncol=2, labels=labels)

# save
plt.savefig("df_both_language_pie_chart.png", bbox_inches='tight')

# Show the pie chart
plt.show()

# Doing the same but for World Cup only tweets

plot_df3 = (
     df_wc.groupby(pd.Grouper(key="lang"))
       .apply(lambda x: pd.Series({"count": len(x), "pctg": f"{100*(len(x)/df_wc.shape[0]):.2f}"})).reset_index()
)

# turning percentage into float
plot_df3["pctg"] = plot_df3["pctg"].astype(float)

print(plot_df3)

plt.figure(figsize=(10,10))

# Plot the pie chart
plt.pie(plot_df3["count"],autopct=None, labels=None)

# Format the labels
labels = ["{} ({:.2f}%)".format(l, p) for l, p in zip(plot_df3["lang"], plot_df3["pctg"])]


# Add a legend to the pie chart
plt.legend(plot_df3["lang"], title="Languages", loc="upper left", bbox_to_anchor=(1,1), ncol=2, labels=labels)

plt.savefig("df_wc_language_pie_chart.png", bbox_inches='tight')

# Show the pie chart
plt.show()

# CLEANING TWEETS AND CREATING VISUALISATIONS

# import required packages
import re
import numpy as np
import gensim
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
nltk.download('omw-1.4')
nltk.download('averaged_perceptron_tagger')

# Removing irrelevant Spam tweets that pollute our dataset.
sequence = '#sbsworldcup #u2 #shaunswalue #u2worldexclusive #u2australia #swalue #gay'
df_lgbt = df_lgbt[~df_lgbt['text'].str.contains(sequence)]

# Keeping tweets that are not possibly sensitive because they are sexually explicit
df_lgbt= df_lgbt.loc[df_lgbt['possibly_sensitive'] != True]

# keeping english tweets only because our focus is on english words
df_lgbt = df_lgbt.loc[df_lgbt['lang'] == 'en']

# A list of contractions from http://stackoverflow.com/questions/19790188/expanding-english-language-contractions-in-python
contractions = {
"ain't": "am not",
"aren't": "are not",
"can't": "cannot",
"can't've": "cannot have",
"'cause": "because",
"could've": "could have",
"couldn't": "could not",
"couldn't've": "could not have",
"didn't": "did not",
"doesn't": "does not",
"don't": "do not",
"hadn't": "had not",
"hadn't've": "had not have",
"hasn't": "has not",
"haven't": "have not",
"he'd": "he would",
"he'd've": "he would have",
"he'll": "he will",
"he's": "he is",
"how'd": "how did",
"how'll": "how will",
"how's": "how is",
"i'd": "i would",
"i'll": "i will",
"i'm": "i am",
"i've": "i have",
"isn't": "is not",
"it'd": "it would",
"it'll": "it will",
"it's": "it is",
"let's": "let us",
"ma'am": "madam",
"mayn't": "may not",
"might've": "might have",
"mightn't": "might not",
"must've": "must have",
"mustn't": "must not",
"needn't": "need not",
"oughtn't": "ought not",
"shan't": "shall not",
"sha'n't": "shall not",
"she'd": "she would",
"she'll": "she will",
"she's": "she is",
"should've": "should have",
"shouldn't": "should not",
"that'd": "that would",
"that's": "that is",
"there'd": "there had",
"there's": "there is",
"they'd": "they would",
"they'll": "they will",
"they're": "they are",
"they've": "they have",
"wasn't": "was not",
"we'd": "we would",
"we'll": "we will",
"we're": "we are",
"we've": "we have",
"weren't": "were not",
"what'll": "what will",
"what're": "what are",
"what's": "what is",
"what've": "what have",
"where'd": "where did",
"where's": "where is",
"who'll": "who will",
"who's": "who is",
"won't": "will not",
"wouldn't": "would not",
"you'd": "you would",
"you'll": "you will",
"you're": "you are"
}

# A function to preprocess the tweets

def text_preprocessing(text):
    #Remove unwanted characters, stopwords, and format the text to create fewer nulls word embeddings
    # Convert words to lower case
    text = text.lower()
    # Expand contractions
    if True:
        text = text.split()
        new_text = []
        for word in text:
            if word in contractions:
                new_text.append(contractions[word])
            else:
                new_text.append(word)
        text = " ".join(new_text)
    # Format words and remove unwanted characters, removing mentions and hashtags
    text = re.sub(r'https?:\/\/.*[\r\n]*', '', text, flags=re.MULTILINE)
    text = re.sub(r'\<a href', ' ', text)
    text = re.sub(r'&amp;', '', text)
    text = re.sub("@[A-Za-z0-9_]+","", text)
    text = re.sub("#[A-Za-z0-9_]+","", text)
    text = re.sub(r'[^\w\s]+', '', text)
    text = re.sub(r'\ng?|\ngt?', ' ', text)
    
    # Tokenize each word
    text = nltk.WordPunctTokenizer().tokenize(text)
    # Lemmatize each word
    text = [nltk.stem.WordNetLemmatizer().lemmatize(token, pos='v') for token in text if len(token)>1]
    return text
def to_string(text):
    # Convert list to string
    text = ' '.join(map(str, text))
    return text

# Add a new column that contains a list of tokens
df_lgbt['clean_tweet_list'] = list(map(text_preprocessing, df_lgbt.text))
# Add a new column 
df_lgbt['clean_tweet'] = list(map(to_string, df_lgbt['clean_tweet_list']))

# Removing stopwords using the stopwords package from nltk
stopwords_list = stopwords.words('english')

# Extending stopwords identified through iterative process
stopwords_list.extend(['lgbt', 'lgbtq','lgbtq+','transgender' 'bisexual', 'gay', 'trans', 'queer', 'lesbian', 'soccer', 'football',
                       'world', 'cup', 'qatar', 'fifa', 'fifaworldcup', '2022', 'sbsworldcup', 'qatars', 'worldcup', 'bi', 'gays', 'qataris',
                      'qatari'])

# Removing the stopwords from the list of tokens and cleaned tweets.
df_lgbt['clean_tweet_list'] = [[word for word in line if word not in stopwords_list] for line in df_lgbt['clean_tweet_list']]
df_lgbt['clean_tweet'] = list(map(to_string, df_lgbt['clean_tweet_list']))

#Check new dataframe
df_lgbt

# Saving as CSV
df.to_csv('final_clean_tweets_lgbt.csv', index=False)

# Create Dictionary
id2word = gensim.corpora.Dictionary(df_lgbt['clean_tweet_list'])

# Create Corpus: Term Document Frequency + bag of words
corpus = [id2word.doc2bow(text) for text in df_lgbt['clean_tweet_list']]


from gensim.models import CoherenceModel
# Compute Coherence Score
number_of_topics = []
coherence_score = []
for i in range(1,5):
  lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus,
                                           id2word=id2word,
                                           iterations=50,
                                           num_topics=i)
  coherence_model_lda = CoherenceModel(model=lda_model, texts=df_lgbt['clean_tweet_list'], dictionary=id2word, coherence='c_v')
  coherence_lda = coherence_model_lda.get_coherence()
  number_of_topics.append(i) #append to the respective list
  coherence_score.append(coherence_lda);

# Returning a list of tuples 
for idx, topic in lda_model.print_topics(-1):
    print("Topic: {} Word: {}".format(idx, topic))
    print("\n")

# Creating the topic modelling visualisation
import pyLDAvis.gensim_models
pyLDAvis.enable_notebook()
vis = pyLDAvis.gensim_models.prepare(lda_model, corpus, dictionary=lda_model.id2word)
vis

# Checking tweet sample in topics 
data_dict = {'dominant_topic':[], 'perc_contribution':[], 'topic_keywords':[]}

# Assigning the dominant topic, its contribution, and keywords to a dictionary 
for i, row in enumerate(lda_model[corpus]):
    #print(i)
    row = sorted(row, key=lambda x: x[1], reverse=True)
    #print(row)
    for j, (topic_num, prop_topic) in enumerate(row):
        wp = lda_model.show_topic(topic_num)
        topic_keywords = ", ".join([word for word, prop in wp])
        data_dict['dominant_topic'].append(int(topic_num))
        data_dict['perc_contribution'].append(round(prop_topic, 3))
        data_dict['topic_keywords'].append(topic_keywords)
        #print(topic_keywords)
        break

df_topics = pd.DataFrame(data_dict)
contents = pd.Series(tweets)
df_topics['text'] = df_lgbt['text']
df_topics

# Repeat above code with the only world cup dataset (world_cup_no_lgbt_tweets.csv)

# CREATING A STYLECLOUD
# Creating a new DataFrame with only the required column
clean_df = pd.DataFrame(df_lgbt['clean_tweet'])

# Exporting the new DataFrame to a CSV file
clean_df.to_csv("clean_lgbt_column.csv", index=False)

# Choosing the colour scheme for the stylecloud
from matplotlib.colors import LinearSegmentedColormap
cmap = LinearSegmentedColormap.from_list("33D7FF", ["#3393FF", "#334FFF", "#163C5A", "#1B71B5", "#9BB6CB"])

# Creating the stylecloud
stylecloud.gen_stylecloud(file_path='clean_lgbt_column.csv',
                          size = 1028,  
                          icon_name = 'fab fa-twitter',
                          output_name = 'stylecloud_lgbt.png',
                          background_color ='white')

# Plotting the stylecloud
from IPython.display import Image
Image(filename='stylecloud_lgbt.png')

# Repeated the above code to create a second stylecloud only including the worldcup dataset


