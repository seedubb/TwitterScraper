#the twitter API being used
from twython import Twython, TwythonError
#to print the time
import time
from datetime import datetime
from dateutil.parser import parse
#sentiment analysis
from textblob import TextBlob

#time.strftime('%X \t %x \t %Z')

APP_KEY = 'JFSas8y72R38gIAgb3C5eQ'
APP_SECRET = '5YmtyQqCmYc76rLTgMc0jTgA8CCOvj2LDwg7cwyaBI'
OAUTH_TOKEN = '1927007174-b8UmDKtQuKXQhqCqqUiwoQDMltbfmWyt8XIZGto'
OAUTH_TOKEN_SECRET = 'dCjIlspSTqR2BxV5O8dP5qdu9JExFYaZJNUxvtdaM'

twitter = Twython(APP_KEY, APP_SECRET,
                 OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
tweets = []

f = open('trump_tweet_data.txt', 'w')
# Requires Authentication as of Twitter API v1.1

screen_name = '@realDonaldTrump'
f.write('ScreenName,Time,Date,TimeZone,Tweet,InReplyToUserID,FavoriteCount,RetweetCount,SentimentAverage\n')

try:
    user_timeline = twitter.get_user_timeline(screen_name='@realDonaldTrump',count=100)
except TwythonError as e:
    print e
#print len(user_timeline)
for tweet in user_timeline:
    # Add whatever you want from the tweet, here we just add the text
    tweets.append(tweet['text'])
    #Tue Jan 12 21:15:07 +0000 2016
    timestamp = parse(tweet['created_at'])
    print timestamp.strftime('%X \t %x \t %Z')
    tweet_text = tweet['text'].replace('\n', ' ').replace('\r', '')
    tweet_text = tweet_text.replace('"', "")
    print tweet_text
    blob = TextBlob(tweet['text'])
    sentiment = []
    for sentence in blob.sentences:
        sentiment.append(sentence.sentiment.polarity)
        #print(sentence.sentiment.polarity)
    sentiment_avg = sum(sentiment) / float(len(sentiment))
    print sentiment_avg
    print tweet['in_reply_to_user_id_str']
    #print tweet['entities']
    print tweet['coordinates']
    print tweet['favorite_count']
    print tweet['retweet_count']
    print '\n'
    f.write(screen_name+','+timestamp.strftime('%X,%x,%Z')+',"'+tweet_text.encode('utf-8')+'",'+str(tweet['in_reply_to_user_id_str'])+','+str(tweet['favorite_count'])+','+str(tweet['retweet_count'])+','+str(sentiment_avg)+'\n') 
# Count could be less than 200, see:
# https://dev.twitter.com/discussions/7513
while len(user_timeline) != 0: 
    try:
        user_timeline = twitter.get_user_timeline(screen_name='@realDonaldTrump',count=100,max_id=user_timeline[len(user_timeline)-1]['id']-1)
    except TwythonError as e:
        print e
    #print len(user_timeline)
    for tweet in user_timeline:
        # Add whatever you want from the tweet, here we just add the text
        timestamp = parse(tweet['created_at'])
        print timestamp.strftime('%X \t %x \t %Z')
        tweet_text = tweet['text'].replace('\n', ' ').replace('\r', '')
        tweet_text = tweet_text.replace('"', "")
        print tweet_text
        blob = TextBlob(tweet['text'])
        for sentence in blob.sentences:
            print(sentence.sentiment.polarity)
        print tweet['in_reply_to_user_id_str']
        print tweet['entities']
        print tweet['coordinates']
        print tweet['favorite_count']
        print tweet['retweet_count']
        print '\n'
        f.write(screen_name+','+timestamp.strftime('%X,%x,%Z')+',"'+tweet_text.encode('utf-8')+'",'+str(tweet['in_reply_to_user_id_str'])+','+str(tweet['favorite_count'])+','+str(tweet['retweet_count'])+','+str(sentiment_avg)+'\n') 
    #time.sleep(300)
# Number of tweets the user has made
print len(tweets)
#print tweets

