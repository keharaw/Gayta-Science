# Exploring the Intersection of Sports and Social Issues: A Textual Analysis of World Cup and LGBTQ+ Tweets

## Obtaining Data

The source for our data is the Twitter API. To make it easier to obtain data, we utilised Tweepy to access the key endpoint for our research (GET /2/tweets/search/recent). Tweepy is a convenient Python library that accessed the API. Since the Twitter API has limits on the number of results that can be returned in a single request, we used a paginator to work around these limits.

Under elevated access, we were able to pull 23637 tweets that matched our criteria for tweets about the LGBTQ+ community within the context of the 2022 FIFA World Cup that was held in Qatar. Restrictions under this level this access includes being only able to pull tweets from the last 7 days. Thus, for our LGBTQ+ dataset, we pulled data from the API on two separate occasions. These datasets were subsequently merged and covers tweets over the period from the 29th of November 2022 to the 15th of December 2022. We then applied a similar process to pull 29889 tweets underpinning the conversation about the world cup outside of the heavily publicised issue of LGBTQ+ rights. The period covered by this dataset covers the 15th of December 2022 only. The reason for this is covered in the next section. For both criteria, we obtained information such as the tweet text, language and the time it was posted. For the full dataset, please see our repository (link). The queries that contain the exact keywords we filtered for are found below:

###### *Query for LGBTQ+ and World Cup tweets*
```
query = "(lgbt OR lgbtq OR lgbtq+ OR transgender OR bisexual OR gay OR trans OR queer OR lesbian) ((soccer OR football OR (world cup)) OR qatar) -is:retweet"
```

###### *Query for World Cup only tweets*
```
query = "-(lgbt OR lgbtq OR lgbtq+ OR transgender OR bisexual OR gay OR trans OR queer OR lesbian) ((soccer OR football OR (world cup)) OR qatar) -is:retweet"
``` 



The keywords were chosen based on the belief that they would best capture the tweets relevant to our analysis. An additional component of our query was to exclude retweets. Whilst retweets can express agreement, it is not a perfect measure. They may potentially introduce bias and skew the results. Retweets can artificially inflate the popularity and visibility of certain tweets and accounts, making it difficult to get an accurate picture of the original content and perspectives being shared on the platform. Furthermore, retweets can introduce duplicate data, which can cause problems when trying to perform numerical analysis or generate visualizations based on the data.


## Describing Our Data

Using a combination of ggplot and matplotlib, we were able to generate visualisations of our datasets.  

![alt text](Images/line_chart_tweet_count_A.png)
###### *Tweets about the LGBTQ+ Community and the World Cup from 29/11/2022 until 15/12/2022*

The graph displayed above showcases the variations in the volume of tweets regarding LGBTQ+ and the World Cup over a specified time period. The fluctuations of tweets seem to coincide with major news events and when matches are played. For example, the spike on the 10th of December is related to the death of American journalist Grant Wahl who was reporting in Qatar. Zero tweets on the  December 7th is not indicative of a lack of tweets but rather a result of the data retrieval method. The data was not obtained exactly a week after the previous pull, which led to a temporary gap in the collected data for that day. Despite this limitation, we still have a substantial sample of tweets from which to carry out a comprehensive analysis.

After our initial project update presentation, we received feedback to include a comparison group of tweets for our analysis. Therefore, we pulled tweets about the World Cup only. Due to timout requests from the Twitter API, we were not able to get all the tweets relevant from the last 7 days. So, we aimed to pull an amount similar to the LGBTQ+ dataset. Owing to the popularity of the World Cup, all 29,889 tweets were posted on the same day. Despite this apparent limitation, we do not anticipate any significant impact on our analysis. Our focus is on comparing the language and topics that emerge in tweets about the LGBTQ+ community and the World Cup, rather than changes over time.

There was also some variation in the number of languages used in these tweets.

![alt text](Images/df_both_language_pie_chart.png) 

![alt text](Images/df_wc_language_pie_chart.png)

In both datasets, there is a wide range of languages represented. The leading languages in the LGBTQ+ dataset are English, French, Spanish, Portuguese, and Italian. For the World Cup only dataset, the top five languages are English, Spanish, French, no linguistic content (such as URLs), and Indonesian. It is evident that English makes up the majority of tweets in both datasets. This is likely due to the fact that the keywords used in our query were in English, thus causing these results to be skewed. The prevalence of European Romance languages in these datasets can be attributed to the popularity of soccer in Europe and South America. These continents are home to many of the world's top football teams and attract a lot of attention from football fans who may fuel the twitter conversation around the world cup and Qatar’s human rights violations.

---