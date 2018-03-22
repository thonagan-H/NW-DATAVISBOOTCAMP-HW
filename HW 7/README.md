

```python
# Dependencies
import tweepy
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from datetime import datetime

# Import and Initialize Sentiment Analyzer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

# Twitter API Keys
consumer_key = "Ed4RNulN1lp7NbOooHa9STCoU"
consumer_secret = "P7cUJlmJpq0VaCY0Jg7COliwQqzK0qYEyUF9Y0idx4ujb3ZlW5"
access_token = "839621358724198402-dzdOsx2WWHrSuBwyNUiqXEnTivHozAZ"
access_token_secret = "dCZ80uNRbFDjxdU2EckmNiSckdoATach6Q8zb7YYYE5EW"

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


```


```python
# Target Search Term
target_term = ["@BBC","@CBS","@CNN","@FoxNews","@nytimes"]

# Lists to hold sentiments
sentiment =[]
compound_list = []
positive_list = []
negative_list = []
neutral_list = []
handle = []
counter = 1

# Grab 25 tweets
for i in target_term:
    public_tweets = api.user_timeline(i, count=100)

    # Loop through all tweets
    for tweet in public_tweets:

        # Run Vader Analysis on each tweet
        compound = analyzer.polarity_scores(tweet["text"])["compound"]
        pos = analyzer.polarity_scores(tweet["text"])["pos"]
        neu = analyzer.polarity_scores(tweet["text"])["neu"]
        neg = analyzer.polarity_scores(tweet["text"])["neg"]

        # Add each value to the appropriate array
        compound_list.append(compound)
        positive_list.append(pos)
        negative_list.append(neg)
        neutral_list.append(neu)
        handle.append(i)

        # Store the Average Sentiments
        sentiment.append({"Date": tweet["created_at"],
                          "Handle":i,
                          "Compound": np.mean(compound_list),
                          "Positive": np.mean(positive_list),
                          "Neutral": np.mean(negative_list),
                          "Negative": np.mean(neutral_list),
                          "Tweets Ago": counter})
        
        counter = counter + 1
     
            
            
    
```


```python
sentiments_pd = pd.DataFrame.from_dict(sentiment)
sentiments_pd.to_csv("Dataframe.csv")
sentiments_pd
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Compound</th>
      <th>Date</th>
      <th>Handle</th>
      <th>Negative</th>
      <th>Neutral</th>
      <th>Positive</th>
      <th>Tweets Ago</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.000000</td>
      <td>Tue Mar 20 19:48:04 +0000 2018</td>
      <td>@BBC</td>
      <td>1.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.000000</td>
      <td>Tue Mar 20 19:03:04 +0000 2018</td>
      <td>@BBC</td>
      <td>1.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-0.128633</td>
      <td>Tue Mar 20 18:33:01 +0000 2018</td>
      <td>@BBC</td>
      <td>0.922667</td>
      <td>0.053333</td>
      <td>0.023667</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>-0.011475</td>
      <td>Tue Mar 20 17:33:03 +0000 2018</td>
      <td>@BBC</td>
      <td>0.876500</td>
      <td>0.065500</td>
      <td>0.057750</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>-0.009180</td>
      <td>Tue Mar 20 17:03:01 +0000 2018</td>
      <td>@BBC</td>
      <td>0.901200</td>
      <td>0.052400</td>
      <td>0.046200</td>
      <td>5</td>
    </tr>
    <tr>
      <th>5</th>
      <td>-0.007650</td>
      <td>Tue Mar 20 16:05:04 +0000 2018</td>
      <td>@BBC</td>
      <td>0.917667</td>
      <td>0.043667</td>
      <td>0.038500</td>
      <td>6</td>
    </tr>
    <tr>
      <th>6</th>
      <td>-0.006557</td>
      <td>Tue Mar 20 15:33:03 +0000 2018</td>
      <td>@BBC</td>
      <td>0.929429</td>
      <td>0.037429</td>
      <td>0.033000</td>
      <td>7</td>
    </tr>
    <tr>
      <th>7</th>
      <td>0.045312</td>
      <td>Tue Mar 20 15:03:02 +0000 2018</td>
      <td>@BBC</td>
      <td>0.921750</td>
      <td>0.032750</td>
      <td>0.045375</td>
      <td>8</td>
    </tr>
    <tr>
      <th>8</th>
      <td>0.111044</td>
      <td>Tue Mar 20 14:24:06 +0000 2018</td>
      <td>@BBC</td>
      <td>0.901667</td>
      <td>0.029111</td>
      <td>0.069111</td>
      <td>9</td>
    </tr>
    <tr>
      <th>9</th>
      <td>0.099940</td>
      <td>Tue Mar 20 14:03:04 +0000 2018</td>
      <td>@BBC</td>
      <td>0.911500</td>
      <td>0.026200</td>
      <td>0.062200</td>
      <td>10</td>
    </tr>
    <tr>
      <th>10</th>
      <td>0.111173</td>
      <td>Tue Mar 20 13:16:25 +0000 2018</td>
      <td>@BBC</td>
      <td>0.908727</td>
      <td>0.023818</td>
      <td>0.067364</td>
      <td>11</td>
    </tr>
    <tr>
      <th>11</th>
      <td>0.068383</td>
      <td>Tue Mar 20 13:02:01 +0000 2018</td>
      <td>@BBC</td>
      <td>0.902833</td>
      <td>0.035333</td>
      <td>0.061750</td>
      <td>12</td>
    </tr>
    <tr>
      <th>12</th>
      <td>0.110154</td>
      <td>Tue Mar 20 11:03:23 +0000 2018</td>
      <td>@BBC</td>
      <td>0.896308</td>
      <td>0.032615</td>
      <td>0.071000</td>
      <td>13</td>
    </tr>
    <tr>
      <th>13</th>
      <td>0.056793</td>
      <td>Tue Mar 20 10:30:04 +0000 2018</td>
      <td>@BBC</td>
      <td>0.877714</td>
      <td>0.049643</td>
      <td>0.072571</td>
      <td>14</td>
    </tr>
    <tr>
      <th>14</th>
      <td>0.077287</td>
      <td>Tue Mar 20 10:04:02 +0000 2018</td>
      <td>@BBC</td>
      <td>0.874333</td>
      <td>0.046333</td>
      <td>0.079267</td>
      <td>15</td>
    </tr>
    <tr>
      <th>15</th>
      <td>0.072456</td>
      <td>Tue Mar 20 09:49:33 +0000 2018</td>
      <td>@BBC</td>
      <td>0.882188</td>
      <td>0.043438</td>
      <td>0.074313</td>
      <td>16</td>
    </tr>
    <tr>
      <th>16</th>
      <td>0.049476</td>
      <td>Tue Mar 20 09:49:23 +0000 2018</td>
      <td>@BBC</td>
      <td>0.870471</td>
      <td>0.052059</td>
      <td>0.077412</td>
      <td>17</td>
    </tr>
    <tr>
      <th>17</th>
      <td>0.060617</td>
      <td>Tue Mar 20 09:49:10 +0000 2018</td>
      <td>@BBC</td>
      <td>0.865444</td>
      <td>0.054000</td>
      <td>0.080500</td>
      <td>18</td>
    </tr>
    <tr>
      <th>18</th>
      <td>0.057426</td>
      <td>Tue Mar 20 09:49:02 +0000 2018</td>
      <td>@BBC</td>
      <td>0.872526</td>
      <td>0.051158</td>
      <td>0.076263</td>
      <td>19</td>
    </tr>
    <tr>
      <th>19</th>
      <td>0.079250</td>
      <td>Tue Mar 20 09:32:02 +0000 2018</td>
      <td>@BBC</td>
      <td>0.869600</td>
      <td>0.048600</td>
      <td>0.081750</td>
      <td>20</td>
    </tr>
    <tr>
      <th>20</th>
      <td>0.075476</td>
      <td>Tue Mar 20 09:03:04 +0000 2018</td>
      <td>@BBC</td>
      <td>0.875810</td>
      <td>0.046286</td>
      <td>0.077857</td>
      <td>21</td>
    </tr>
    <tr>
      <th>21</th>
      <td>0.072045</td>
      <td>Tue Mar 20 08:25:06 +0000 2018</td>
      <td>@BBC</td>
      <td>0.881455</td>
      <td>0.044182</td>
      <td>0.074318</td>
      <td>22</td>
    </tr>
    <tr>
      <th>22</th>
      <td>0.068913</td>
      <td>Tue Mar 20 08:03:03 +0000 2018</td>
      <td>@BBC</td>
      <td>0.886609</td>
      <td>0.042261</td>
      <td>0.071087</td>
      <td>23</td>
    </tr>
    <tr>
      <th>23</th>
      <td>0.050133</td>
      <td>Mon Mar 19 19:33:04 +0000 2018</td>
      <td>@BBC</td>
      <td>0.886750</td>
      <td>0.045083</td>
      <td>0.068125</td>
      <td>24</td>
    </tr>
    <tr>
      <th>24</th>
      <td>0.054252</td>
      <td>Mon Mar 19 18:33:05 +0000 2018</td>
      <td>@BBC</td>
      <td>0.879640</td>
      <td>0.047920</td>
      <td>0.072400</td>
      <td>25</td>
    </tr>
    <tr>
      <th>25</th>
      <td>0.048215</td>
      <td>Mon Mar 19 18:03:01 +0000 2018</td>
      <td>@BBC</td>
      <td>0.881192</td>
      <td>0.049154</td>
      <td>0.069615</td>
      <td>26</td>
    </tr>
    <tr>
      <th>26</th>
      <td>0.046430</td>
      <td>Mon Mar 19 17:30:08 +0000 2018</td>
      <td>@BBC</td>
      <td>0.885593</td>
      <td>0.047333</td>
      <td>0.067037</td>
      <td>27</td>
    </tr>
    <tr>
      <th>27</th>
      <td>0.019429</td>
      <td>Mon Mar 19 17:00:05 +0000 2018</td>
      <td>@BBC</td>
      <td>0.869750</td>
      <td>0.060429</td>
      <td>0.069786</td>
      <td>28</td>
    </tr>
    <tr>
      <th>28</th>
      <td>0.018759</td>
      <td>Mon Mar 19 16:33:29 +0000 2018</td>
      <td>@BBC</td>
      <td>0.874241</td>
      <td>0.058345</td>
      <td>0.067379</td>
      <td>29</td>
    </tr>
    <tr>
      <th>29</th>
      <td>0.018133</td>
      <td>Mon Mar 19 15:02:02 +0000 2018</td>
      <td>@BBC</td>
      <td>0.878433</td>
      <td>0.056400</td>
      <td>0.065133</td>
      <td>30</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>470</th>
      <td>0.070662</td>
      <td>Tue Mar 20 13:00:11 +0000 2018</td>
      <td>@nytimes</td>
      <td>0.861911</td>
      <td>0.055985</td>
      <td>0.082091</td>
      <td>471</td>
    </tr>
    <tr>
      <th>471</th>
      <td>0.070033</td>
      <td>Tue Mar 20 12:45:04 +0000 2018</td>
      <td>@nytimes</td>
      <td>0.861801</td>
      <td>0.056106</td>
      <td>0.082081</td>
      <td>472</td>
    </tr>
    <tr>
      <th>472</th>
      <td>0.069885</td>
      <td>Tue Mar 20 12:28:03 +0000 2018</td>
      <td>@nytimes</td>
      <td>0.862093</td>
      <td>0.055987</td>
      <td>0.081907</td>
      <td>473</td>
    </tr>
    <tr>
      <th>473</th>
      <td>0.069738</td>
      <td>Tue Mar 20 12:15:08 +0000 2018</td>
      <td>@nytimes</td>
      <td>0.862384</td>
      <td>0.055869</td>
      <td>0.081734</td>
      <td>474</td>
    </tr>
    <tr>
      <th>474</th>
      <td>0.069591</td>
      <td>Tue Mar 20 12:00:06 +0000 2018</td>
      <td>@nytimes</td>
      <td>0.862674</td>
      <td>0.055752</td>
      <td>0.081562</td>
      <td>475</td>
    </tr>
    <tr>
      <th>475</th>
      <td>0.069970</td>
      <td>Tue Mar 20 11:50:08 +0000 2018</td>
      <td>@nytimes</td>
      <td>0.862729</td>
      <td>0.055634</td>
      <td>0.081624</td>
      <td>476</td>
    </tr>
    <tr>
      <th>476</th>
      <td>0.070127</td>
      <td>Tue Mar 20 11:39:04 +0000 2018</td>
      <td>@nytimes</td>
      <td>0.862524</td>
      <td>0.055738</td>
      <td>0.081725</td>
      <td>477</td>
    </tr>
    <tr>
      <th>477</th>
      <td>0.071196</td>
      <td>Tue Mar 20 11:30:07 +0000 2018</td>
      <td>@nytimes</td>
      <td>0.862186</td>
      <td>0.055772</td>
      <td>0.082029</td>
      <td>478</td>
    </tr>
    <tr>
      <th>478</th>
      <td>0.072040</td>
      <td>Tue Mar 20 11:20:08 +0000 2018</td>
      <td>@nytimes</td>
      <td>0.862073</td>
      <td>0.055656</td>
      <td>0.082259</td>
      <td>479</td>
    </tr>
    <tr>
      <th>479</th>
      <td>0.072506</td>
      <td>Tue Mar 20 11:11:05 +0000 2018</td>
      <td>@nytimes</td>
      <td>0.862108</td>
      <td>0.055540</td>
      <td>0.082340</td>
      <td>480</td>
    </tr>
    <tr>
      <th>480</th>
      <td>0.073149</td>
      <td>Tue Mar 20 11:00:04 +0000 2018</td>
      <td>@nytimes</td>
      <td>0.862156</td>
      <td>0.055424</td>
      <td>0.082407</td>
      <td>481</td>
    </tr>
    <tr>
      <th>481</th>
      <td>0.073872</td>
      <td>Tue Mar 20 10:44:03 +0000 2018</td>
      <td>@nytimes</td>
      <td>0.862187</td>
      <td>0.055309</td>
      <td>0.082492</td>
      <td>482</td>
    </tr>
    <tr>
      <th>482</th>
      <td>0.073719</td>
      <td>Tue Mar 20 10:36:06 +0000 2018</td>
      <td>@nytimes</td>
      <td>0.862472</td>
      <td>0.055195</td>
      <td>0.082321</td>
      <td>483</td>
    </tr>
    <tr>
      <th>483</th>
      <td>0.073567</td>
      <td>Tue Mar 20 10:14:01 +0000 2018</td>
      <td>@nytimes</td>
      <td>0.862756</td>
      <td>0.055081</td>
      <td>0.082151</td>
      <td>484</td>
    </tr>
    <tr>
      <th>484</th>
      <td>0.072207</td>
      <td>Tue Mar 20 10:00:07 +0000 2018</td>
      <td>@nytimes</td>
      <td>0.862662</td>
      <td>0.055344</td>
      <td>0.081981</td>
      <td>485</td>
    </tr>
    <tr>
      <th>485</th>
      <td>0.072058</td>
      <td>Tue Mar 20 09:45:09 +0000 2018</td>
      <td>@nytimes</td>
      <td>0.862944</td>
      <td>0.055230</td>
      <td>0.081813</td>
      <td>486</td>
    </tr>
    <tr>
      <th>486</th>
      <td>0.070896</td>
      <td>Tue Mar 20 09:30:14 +0000 2018</td>
      <td>@nytimes</td>
      <td>0.862930</td>
      <td>0.055413</td>
      <td>0.081645</td>
      <td>487</td>
    </tr>
    <tr>
      <th>487</th>
      <td>0.071311</td>
      <td>Tue Mar 20 09:15:06 +0000 2018</td>
      <td>@nytimes</td>
      <td>0.862906</td>
      <td>0.055299</td>
      <td>0.081783</td>
      <td>488</td>
    </tr>
    <tr>
      <th>488</th>
      <td>0.071165</td>
      <td>Tue Mar 20 09:00:18 +0000 2018</td>
      <td>@nytimes</td>
      <td>0.863186</td>
      <td>0.055186</td>
      <td>0.081616</td>
      <td>489</td>
    </tr>
    <tr>
      <th>489</th>
      <td>0.071433</td>
      <td>Tue Mar 20 08:45:06 +0000 2018</td>
      <td>@nytimes</td>
      <td>0.863047</td>
      <td>0.055073</td>
      <td>0.081867</td>
      <td>490</td>
    </tr>
    <tr>
      <th>490</th>
      <td>0.071287</td>
      <td>Tue Mar 20 08:30:12 +0000 2018</td>
      <td>@nytimes</td>
      <td>0.863326</td>
      <td>0.054961</td>
      <td>0.081701</td>
      <td>491</td>
    </tr>
    <tr>
      <th>491</th>
      <td>0.072146</td>
      <td>Tue Mar 20 08:15:04 +0000 2018</td>
      <td>@nytimes</td>
      <td>0.863181</td>
      <td>0.054850</td>
      <td>0.081957</td>
      <td>492</td>
    </tr>
    <tr>
      <th>492</th>
      <td>0.070784</td>
      <td>Tue Mar 20 08:02:02 +0000 2018</td>
      <td>@nytimes</td>
      <td>0.863043</td>
      <td>0.055154</td>
      <td>0.081791</td>
      <td>493</td>
    </tr>
    <tr>
      <th>493</th>
      <td>0.069787</td>
      <td>Tue Mar 20 07:47:03 +0000 2018</td>
      <td>@nytimes</td>
      <td>0.863081</td>
      <td>0.055281</td>
      <td>0.081626</td>
      <td>494</td>
    </tr>
    <tr>
      <th>494</th>
      <td>0.069646</td>
      <td>Tue Mar 20 07:32:03 +0000 2018</td>
      <td>@nytimes</td>
      <td>0.863358</td>
      <td>0.055170</td>
      <td>0.081461</td>
      <td>495</td>
    </tr>
    <tr>
      <th>495</th>
      <td>0.070630</td>
      <td>Tue Mar 20 07:17:04 +0000 2018</td>
      <td>@nytimes</td>
      <td>0.863204</td>
      <td>0.055058</td>
      <td>0.081726</td>
      <td>496</td>
    </tr>
    <tr>
      <th>496</th>
      <td>0.071720</td>
      <td>Tue Mar 20 07:07:42 +0000 2018</td>
      <td>@nytimes</td>
      <td>0.862704</td>
      <td>0.054948</td>
      <td>0.082336</td>
      <td>497</td>
    </tr>
    <tr>
      <th>497</th>
      <td>0.071576</td>
      <td>Tue Mar 20 07:02:05 +0000 2018</td>
      <td>@nytimes</td>
      <td>0.862980</td>
      <td>0.054837</td>
      <td>0.082171</td>
      <td>498</td>
    </tr>
    <tr>
      <th>498</th>
      <td>0.071432</td>
      <td>Tue Mar 20 06:33:04 +0000 2018</td>
      <td>@nytimes</td>
      <td>0.863255</td>
      <td>0.054727</td>
      <td>0.082006</td>
      <td>499</td>
    </tr>
    <tr>
      <th>499</th>
      <td>0.070409</td>
      <td>Tue Mar 20 06:18:45 +0000 2018</td>
      <td>@nytimes</td>
      <td>0.863040</td>
      <td>0.055106</td>
      <td>0.081842</td>
      <td>500</td>
    </tr>
  </tbody>
</table>
<p>500 rows × 7 columns</p>
</div>




```python
for user in target_term:
    dataframe = sentiments_pd.loc[sentiments_pd["Handle"] == user]
    plt.scatter(dataframe["Tweets Ago"],dataframe["Compound"],label = user)

plt.legend(bbox_to_anchor = (1,1))
plt.grid()
#plt.xlim(1,-1)
plt.savefig('Analysis_1.png')
plt.show()
```


![png](output_3_0.png)



```python
sentiments_pd.groupby('Handle')["Compound"].sum()
```




    Handle
    @BBC         6.493245
    @CBS        19.286886
    @CNN        16.263189
    @FoxNews    12.138717
    @nytimes     8.059501
    Name: Compound, dtype: float64




```python

sentiments_pd.groupby('Handle')["Compound"].sum().plot.bar(x='Tweets Ago', 
                                                           y='Compound',width = 1.0, title="title")

plt.title("Overall Sentiment of Media Tweets (11/5/2017)")
plt.xlabel("News Organizations")
plt.ylabel("Tweet Polarity")
plt.savefig("Overall Sentiment of Media Tweets")
plt.ylim(-20,20)
plt.savefig("Analysis_2.png")
plt.show()

```


![png](output_5_0.png)

