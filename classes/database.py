import pymongo
from pymongo import Connection

class database:
	def __init__(self):
		self.connection = Connection('127.0.0.1', 27017)		
		self.db = self.connection.tweet
		self.dbTweet = self.db.tweet
		
		return 'lol'