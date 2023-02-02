# Exploring the Intersection of Sports and Social Issues: A Textual Analysis of World Cup and LGBTQ+ Tweets

## Introduction

## Motivations

## Data

The source of our data for the analysis was the Twitter API. The API provides real-time data with a large volume of tweets, making it a valuable source for analysis and research. Its user-friendly interface, customizable options, versatility, and reliability make it a powerful tool for social media analysis, sentiment analysis, marketing research, and more.

### Data Retrieval

To facilitate data retrieval, we utilised [Tweepy](https://www.tweepy.org/) to access the [recent tweet endpoint](https://developer.twitter.com/en/docs/twitter-api/tweets/search/api-reference/get-tweets-search-recent). Tweepy is a convenient Python library that makes interacting with the Twitter API very straightforward. 

Under elevated access, we were able to pull 23,637 tweets that matched our criteria for LGBTQ+ related tweets within the context of the 2022 FIFA World Cup in Qatar. Restrictions under this level this access include being only able to pull tweets from the last seven days. Thus, for our LGBTQ+ and World Cup dataset, we pulled data from the API on two separate occasions. These datasets were subsequently merged and covers the period from the 29th of November 2022 to the 15th of December 2022. Due to limits on the number of results that can be returned in a single request, we used a paginator to obtain as many tweets as possible. We then applied a similar process to pull 29,889 tweets underpinning the conversation about the World Cup outside of the heavily publicised issue of LGBTQ+ rights. The period covered by this dataset is the 15th of December 2022 only. The reason for this is explained in the next section. For both datasets, we obtained information such as the tweet text, language and the time it was posted. For the full dataset, please see our [repository](https://github.com/keharaw/Gayta-Science). The queries that contain the exact keywords we filtered for are found below:

###### *Query for LGBTQ+ and World Cup tweets*
```
query = "(lgbt OR lgbtq OR lgbtq+ OR transgender OR bisexual OR gay OR trans OR queer OR lesbian) ((soccer OR football OR (world cup)) OR qatar) -is:retweet"
```

###### *Query for World Cup only tweets*
```
query = "-(lgbt OR lgbtq OR lgbtq+ OR transgender OR bisexual OR gay OR trans OR queer OR lesbian) ((soccer OR football OR (world cup)) OR qatar) -is:retweet"
``` 



The keywords were chosen because they best capture the tweets relevant to our analysis. An additional component of our query was to exclude retweets. Whilst retweets can express agreement, it is not a perfect measure. They may potentially introduce bias and skew the results. Retweets can artificially inflate the popularity and visibility of certain tweets and accounts, making it difficult to get an accurate picture of the original content and perspectives being shared on the platform. Furthermore, retweets can introduce duplicate data, which can cause problems when trying to perform numerical analysis or generate visualisations based on the data.


### Describing Our Data

Using a combination of the ggplot and matplotlib packages, we were able to generate visualisations to understand our data better. In addition to size, how tweets were distributed over time and the language in which they were written shed some light on the kinds of conversations that were taking place.

#### Tweets over time

![alt text](Images/line_chart_tweet_count_A.png)
###### *Tweets about the LGBTQ+ Community and the World Cup from 29/11/2022 until 15/12/2022*

The graph displayed above showcases the variations in the volume of tweets regarding LGBTQ+ and the World Cup over our time period. The fluctuations of tweets seem to coincide with major news events and when matches are played. For example, the spike on the 10th of December is related to the death of American journalist Grant Wahl who was reporting in Qatar. Zero tweets on December 7th is not indicative of a lack of tweets but rather a result of the data retrieval method. The data was not obtained exactly a week after the previous pull, which led to a temporary gap in the collected data for that day. Despite this limitation, we still have a substantial sample of tweets from which to carry out a comprehensive analysis.

After our initial project update presentation, we received feedback to include a comparison group of tweets for our analysis. Therefore, we pulled tweets about the World Cup only. Due to timout requests from the Twitter API, we were not able to get all the tweets relevant from the last 7 days. So, we aimed to pull an amount similar to the LGBTQ+ dataset. Owing to the popularity of the World Cup, all 29,889 tweets were posted on the same day. Despite this apparent limitation, we do not anticipate any significant impact on our analysis. Our focus is on comparing the language and topics that emerge in tweets about the LGBTQ+ community and the World Cup, rather than changes over time.

#### Language

| LGBTQ+ and World Cup | World Cup only |
| --- | --- |
| ![Chart 1](Images/df_both_language_pie_chart.png) | ![Chart 2](Images/df_wc_language_pie_chart.png) |
###### *Breakdown of tweets by language*


In both datasets, there is a wide range of languages represented. The leading languages in the LGBTQ+ dataset are English, French, Spanish, Portuguese, and Italian. For the World Cup only dataset, these are English, Spanish, French, no linguistic content (such as URLs), and Indonesian. It is evident that English makes up the majority of tweets in both datasets. This is likely due to the fact that the keywords used in our query were in English, thus causing these results to be skewed. The prevalence of European Romance languages in these datasets can be attributed to the popularity of football in Europe and South America. These continents are home to many of the world's top football teams and attract a lot of attention from football fans who may fuel the twitter conversation around the World Cup and Qatar’s human rights violations.

---

## Data Analysis

We utilised topic modelling, style clouds, and co-occurrence analysis to analyse tweets because we wanted to gain deeper insights into the underlying themes, sentiments, and language patterns present in the data. These techniques allow us to identify hidden topics, visualise the most frequently used words, and understand the relationships between words used in context. By using these methods, we aimed to uncover valuable insights into the intersection between LGBTQ+ and the World Cup. This information can provide a better understanding of how sports and social issues intersect and how they are perceived by the public.


### Data Cleaning and Pre-processing

Text pre-processing is a crucial step before performing text analysis because it prepares the text data to be in a suitable format for it. Raw text data often contains unwanted characters, numbers, punctuation, and other elements that can interfere with and bias the results of text analysis. For tweets, this could be URLs, mentions, and non-text characters. Pre-processing helps to remove these elements, standardise the format, and normalise the data, resulting in a cleaner and more accurate representation of the text content.

Through running our textual analysis code multiple times and exploring our dataset, we identified a number items that could cloud our analysis. Firstly, there were many spam tweets that offered no substance for analysis. We identified that a common sequence of hashtags that were found in these tweets and used these to remove them. Secondly, tweets marked as possibly sensitive were those that violate Twitter’s user guidelines. Performing a manual check of this, we identified these tweets as sexually explicit and irrelevent to our research question. For the LGBTQ+ and World Cup dataset, there were 412 possibly sensitive tweets. For the World Cup only dataset, there were 292. Finally, we restricted the tweets to English language since this is the language we understand, is supported by the packages we employ, and is the most dominant language in both datasets. 

In our cleaning process, we first converted the text to lower case and expanded contractions if present. We then removed unwanted characters, mentions, hashtags, URLs, and line breaks using regular expressions. The text was tokenized using nltk's WordPunctTokenizer and lemmatized using nltk's WordNetLemmatizer. Two new columns were added to the dataframe, one containing the pre-processed text as a list of tokens and another as a string. Finally, we removed stop words using nltk's stop words package and extended it with additional words and applied thos to both columns. The additional stop words encompassed the keywords we used for our query and their synonyms or related words. For the World Cup only dataset, we also removed the tweets that, as a result of this processing, became empty. This cleaned and prepared text data was then used as the input for generating style clouds, topic modelling, and co-occurrence of words, resulting in improved and more meaningful insights. 

Following this cleaning process, the LGBTQ+ and World Cup dataset contained 17,937 tweets. The World Cup only dataset contained 18,534 tweets.


### Style Clouds

| LGBTQ+ and World Cup | World Cup only |
| --- | --- |
| ![Chart 1](Images/stylecloud_lgbt.png) | ![Chart 2](Images/stylecloud_wc.png) |
###### *Style Clouds showing most frequent words in both samples*


### Topic Modelling

#### LGBTQ+ and World Cup
| Topic 1 | Topic 2|
| --- | --- |
| ![Chart 1](Images/lgbt_1.png) | ![Chart 2](Images/lgbt_2.png) |
| Topic 3 | Topic 4|
| --- | --- |
| ![Chart 3](Images/lgbt_3.png) | ![Chart 4](Images/lgbt_4.png) |
###### *Visualisation of Topic Model for LGBTQ+ and World Cup Tweets*

#### World Cup Only
| Topic 1 | Topic 2|
| --- | --- |
| ![Chart 1](Images/wc_1.png) | ![Chart 2](Images/wc_2.png) |

| Topic 3 |
| --- |
| ![Chart 3](Images/wc_3.png) 
###### *Visualisation of Topic Model for World Cup Only Tweets*

### Co-Occurrence of Words

After conducting topic modeling, examining the co-occurrence of words within the resulting topics can provide deeper insight into the relationships between different terms and their meaning within the context of the data. By analysing the patterns in which words appear together, we can gain a better understanding of how topics are defined and the semantic connections between the terms within each topic. 

To build the network plots below, we began by constructing bigrams to identify co-occuring words. We then selected the top 20 most common bigrams to be visualised in a network plot. We restricted the sample of bigrams to the top 20 for two reasons. Firstly, there is a decline in frequency of bigrams beyond this number so the relative importance of the next few bigrams is lessened. Secondly, for visualisation purposes, the network becomes very difficult to interpret due to overlapping of networks when the sample gets too large.


| LGBTQ+ and World Cup | World Cup only |
| --- | --- |
| ![Chart 1](Images/bigram_lgbtwc.png) | ![Chart 2](Images/bigram_wc.png) |
###### *Networks of co-occuring words*

Looking at the plot on the left, we see five networks. Of these, there are four salient topics: Grant Wahl’s death, migrant workers, support for human rights, and anti-LGBTQ+ policy. It suggests that people were discussing the banning of rainbow flags and the repurcussions people faced for doing so. It also highlights the human rights violations that exist in Qatar that affect not just the LGBTQ+ community, but also migrant workers. What this demonstrates is that discussions surrounding one marginalised group may encourage conversations about others who face similar perils. The frequency of tweets about Grant Wahl is also not unexpected due to the theories that suggested his brother’s homosexuality being the reason for his “killing”.

Looking at the plot on the right, the discussion around the World Cup outside of the LGBTQ+ community seems to be focused solely on football and matches. The prominent topics that emerge from these plots are betting, the World Cup final, platforms for streaming matches and, the drama surrounding Portugal’s coach, Fernando Santos. Given the well-publicised criticism of Qatar for hosting the World Cup, one might have expected other issues besides their treatment of LGBTQ+ to be a prominent topic, such as their treatment of migrant workers or women's rights. Also, as the first Arab country to host the World Cup, one might have expected discussions to celebrate this milestone or to concentrate on the conflict between football and Islamic traditions, particularly regarding the consumption of alcohol.

In summary, these diagrams reveal relationships between words and provide context insight within our tweets. By going beyond topic modelling, these networks have provided context for topics and given a deeper understanding of the relationships between words that make up the topics. Our analysis shows that discussions about the World Cup outside of the LGBTQ+ community tend to focus only on football-related matters such as teams, how to watch it, and who to bet on. But when LGBTQ+ is brought into the picture, not only is there a discussion of their rights being violated, but also those of other marginalised groups. There are limitations to this analysis, mainly due to our sample of tweets, which will be addressed in the limitations section. However, the key conclusion is that the conversation about the World Cup takes a dark turn when Qatar's LGBTQ+ violations are brought into consideration.

---
## Limitations and Future Scope for Research

---

## Conclusion

---

## Footnotes


