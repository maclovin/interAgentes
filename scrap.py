import tweetstream
import pymongo
import time
import sys
from classes.tweets import *
from pymongo import Connection

myConnection = Connection('127.0.0.1', 27017)
db = myConnection.tweet

#passar como parametro nos objetos
dbTweet = db.tweet

words = [sys.argv[1]]
people = [1000]

#instancia o objeto tweets
myTweet = tweets(dbTweet)
	
with tweetstream.FilterStream("neuromancer_br", "q1w2e3r4", track=words, follow=people) as stream:
	for tweet in stream:
		dateToday = time.strftime("%Y-%m-%d")
		hour = time.strftime("%H")

		myTweet.setDateScrap(dateToday)
		myTweet.setHourScrap(hour)
		myTweet.setSeguidores(tweet['user']['followers_count'])
		myTweet.setRts(tweet['retweet_count'])
		myTweet.setMensagem(tweet['text'])
		myTweet.setDateTime(tweet['created_at'])
		myTweet.setAutor(tweet['user']['screen_name'])
		myTweet.setLocation(tweet['user']['location'])
		myTweet.setStatusCount(tweet['user']['statuses_count'])
		myTweet.setCreatedAt(tweet['user']['created_at'])
		myTweet.setHashTags(tweet['entities']['hashtags'])
		myTweet.setEntitles(tweet['entities']['urls'])
		myTweet.setMencoes(tweet['entities']['user_mentions'])
		myTweet.setAutorOriginal(tweet['in_reply_to_screen_name'])
		
		myTweet.save()
		
		print tweet['user']['created_at'], " - "
		print tweet['user']['screen_name'], ":\n"
		print tweet['text'], "\n\n"
		
