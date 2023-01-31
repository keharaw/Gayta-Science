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

# CREATING A STYLECLOUD
# Creating a new DataFrame with only the required column
clean_df = pd.DataFrame(df_lgbt['clean_tweet'])

# Exporting the new DataFrame to a CSV file
clean_df.to_csv("clean_lgbt_column.csv", index=False)

# Creating the stylecloud
from matplotlib.colors import LinearSegmentedColormap
cmap = LinearSegmentedColormap.from_list("33D7FF", ["#3393FF", "#334FFF", "#163C5A", "#1B71B5", "#9BB6CB"])

stylecloud.gen_stylecloud(file_path='clean_lgbt_column.csv',
                          size = 1028,  
                          icon_name = 'fab fa-twitter',
                          output_name = 'stylecloud_lgbt.png',
                          background_color ='white')

# Plotting the stylecloud
from IPython.display import Image
Image(filename='stylecloud_lgbt.png')

# Repeated the above code to create a second stylecloud only including the worldcup dataset
