# Exploring the Intersection of Sports and Social Issues: A Textual Analysis of World Cup and LGBTQ+ Tweets

## Describing our data

Using a combination of ggplot and matplotlib, we were able to generate visualisations of our datasets.

![alt text](Images/line_chart_tweet_count_A.png)'Tweets about the LGBTQ+ Community and the World Cup from 29/11/2022 until 15/12/2022'

<div style="text-align:center;">
  <img src="Images/line_chart_tweet_count_A.png" alt="Tweets about the LGBTQ+ Community and the World Cup from 29/11/2022 until 15/12/2022">
  <br>
  <caption style="color: #f2f2f2;">Tweets about the LGBTQ+ Community and the World Cup from 29/11/2022 until 15/12/2022</caption>
</div>



The graph displayed above showcases the variations in the volume of tweets regarding LGBTQ+ and the World Cup over a specified time period. The fluctuations of tweets seem to coincide with major news events and when matches are played. For example, the spike on the 10th of December is related to the death of American journalist Grant Wahl who was reporting in Qatar. Zero tweets on the  December 7th is not indicative of a lack of tweets but rather a result of the data retrieval method. The data was not obtained exactly a week after the previous pull, which led to a temporary gap in the collected data for that day. Despite this limitation, we still have a substantial sample of tweets from which to carry out a comprehensive analysis.

After our initial project update presentation, we received feedback to include a comparison group of tweets for our analysis. Therefore, we pulled tweets about the World Cup only. Due to timout requests from the Twitter API, we were not able to get all the tweets relevant from the last 7 days. So, we aimed to pull an amount similar to the LGBTQ+ dataset. Owing to the popularity of the World Cup, all 29,889 tweets were posted on the same day. Despite this apparent limitation, we do not anticipate any significant impact on our analysis. Our focus is on comparing the language and topics that emerge in tweets about the LGBTQ+ community and the World Cup, rather than changes over time.

There was also some variation in the number of languages used in these tweets.

![alt text](Images/df_both_language_pie_chart.png) 

![alt text](Images/df_wc_language_pie_chart.png)


In both datasets, there is a wide range of languages represented. The leading languages in the LGBTQ+ dataset are English, French, Spanish, Portuguese, and Italian. For the World Cup only dataset, the top five languages are English, Spanish, French, no linguistic content (such as URLs), and Indonesian. It is evident that English makes up the majority of tweets in both datasets. This is likely due to the fact that the keywords used in our query were in English, thus causing these results to be skewed. The prevalence of European Romance languages in these datasets can be attributed to the popularity of soccer in Europe and South America. These continents are home to many of the world's top football teams and attract a lot of attention from football fans who may fuel the twitter conversation around the world cup and Qatar’s human rights violations.

---