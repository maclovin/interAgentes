import tweetstream
import pymongo
import time
import sys
import os
import string
from classes.tweets import *
from pymongo import Connection

#inicia conexao com MongoDB (host e porta)
myConnection = Connection('127.0.0.1', 27017)
db = myConnection.tweet

#passar como parametro nos objetos
dbTweet = db.tweet
#instancia o objeto tweets
myTweet = tweets(dbTweet)

#le arquivo externo de termos a serem utilizados nas buscas
f = open('terms.txt', 'r')
lines = string.split(f.read(), '\n')
f.close
myTerms = []
for line in lines:
	if not line == '':
		myTerms.append(line)
people = [1000]

with tweetstream.FilterStream("neuromancer_br", "q1w2e3r4", track=myTerms, follow=people) as stream:
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