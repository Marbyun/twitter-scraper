# pip install --upgrade git+https://github.com/JustAnotherArchivist/snscrape.git
# incase this code error please use a twitter for developer : signup at "developer.twitter.com"
import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "(#KimSeonHo AND #Scandal) until:2022-09-08 since:2021-01-11"
tweets = []
limits = 100

for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    # print(vars(tweet))
    # break
    if len(tweets) == limits:
        break
    else:
        tweets.append([tweet.date, tweet.user.username, tweet.content])


df = pd.DataFrame(tweets, columns=['Date','User','Tweet'])
df.to_csv('output.csv')
print(df)
