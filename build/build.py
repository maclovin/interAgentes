#!/usr/bin/python
import os,sys

def makedir(diretorio):
	print 'Criando diretorio %s' %(diretorio)
	
	if not os.path.isdir(diretorio):
		os.mkdir(diretorio)

def makefile(local,conteudo):
	f = open(local, 'w')
	f.write(conteudo)
	f.close
	print 'Criando arquivo %s' %(local)

def usage():
	usage = """
	Modo de usar:
	python build.py [nome_do_ambiente_ou_banco_de_dados]

	Ex:
	python build.py clienteX

	"""
	return usage


def generate(client):
	scrapPy = """
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
	db = myConnection."""+client+"""

	#passar como parametro nos objetos
	dbTweet = db."""+client+"""
	#instancia o objeto tweets
	myTweet = tweets(dbTweet)

	#le arquivo externo de termos a serem utilizados nas buscas
	f = open('terms.txt', 'r')
	lines = string.split(f.read(), '\\n')
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
			print tweet['user']['screen_name'], ":\\n"
			print tweet['text'], "\\n\\n"
	"""
	tsvPy = """
	import sys
	reload(sys)
	sys.setdefaultencoding("utf-8")

	import os
	from pymongo import Connection
	from datetime import date

	myConnection = Connection('127.0.0.1', 27017)
	db = myConnection."""+client+"""

	#passar como parametro nos objetos
	dbTweet = db."""+client+"""

	def usage():
		usage = \"\"\"
		Modo de usar:
		python tsv.py [nome do diretorio] [data]
	        python tsv.py [nome do diretorio] [data] [hora_cheia]
	
		Ex:
		python tsv.py joao 2012-03-28
		python tsv.py joao 2012-03-28 14

		\"\"\"
		return usage
	
	def toTSV(client, date, hour, content):
		if hour == None:
			fname = '%s/%s.tsv' %(client, date)
		else:
			fname = '%s/%s_%s.tsv' %(client, date, hour)
		
		try:
			f = open(fname, 'w')
			f.write(content)
			f.close
		except:
			if not os.path.isdir(client):
				os.mkdir(client)

			f = open(fname, 'w')
			f.write(content)
			f.close

	def search(client, date, hour):
		content = ''

		if not date == None and not hour == None:
			myTweets = dbTweet.find({ "hourScrap":hour, "dateScrap":date })
		elif not date == None:
			myTweets = dbTweet.find({ "dateScrap":date })
	
		try: 	
			for myTweet in myTweets:
				content += "%s\\t%s\\t%s\\t%s\\t%s\\t%s\\t%s\\t%s\\t%s\\t%s\\t%s\\t%s\\t%s\\t%s\\t%s\\t%s\\t%s\\n" %(myTweet['dateScrap'], myTweet['hourScrap'], myTweet['seguidores'], myTweet['rts'], myTweet['mensagem'], myTweet['teor'], myTweet['obs'], myTweet['url'], myTweet['dateTime'], myTweet['autor'], myTweet['location'], myTweet['statusCount'], myTweet['createdAt'], myTweet['hashTags'], myTweet['entitles'], myTweet['mencoes'], myTweet['autorOriginal'])
		except:
			print 'Nao ha dados'
		

		print "Conteudo: %s\\n\\n" %(content)
		toTSV(client, date, hour, content)

	if __name__ == "__main__":
		action = None
		date = None
		hour = None
	
		try:
			action = sys.argv[1]
			date = sys.argv[2]			
		except:
			print usage()
	
		try:
			hour = sys.argv[3]
		except:
			hour = None
	
	 	if not action == None and not date == None:
			search(action,date,hour)
	"""

	databasePy = """
	import pymongo
	from pymongo import Connection

	class database:
		def __init__(self):
			self.connection = Connection('127.0.0.1', 27017)		
			self.db = self.connection."""+client+"""
			self.dbTweet = self.db."""+client+"""
		
			return 'lol'
	"""
	tweetsPy = """
	import pymongo
	from pymongo import Connection

	class tweets():
		def __init__(self,db):
			"Classe para Streamming API do Twitter"
			self.dbTweet = db
			self.dateScrap = ''
			self.hourScrap = ''
			self.seguidores = ''
			self.rts = ''
			self.mensagem = ''
			self.teor = ''
			self.obs = ''
			self.url = ''
			self.dateTime = ''
			self.autor = ''
			self.location = ''
			self.statusCount = ''
			self.createdAt = ''
			self.hashTags = ''
			self.entitles = ''
			self.mencoes = ''
			self.autorOriginal = ''
			
		def setDateScrap(self, dateScrap):
			self.dateScrap = dateScrap
	
		def setHourScrap(self, hourScrap):
			self.hourScrap = hourScrap
	
		def setSeguidores(self, seguidores):
			self.seguidores = seguidores	
	
		def setRts(self, rts):
			self.rts = rts;
	
		def setMensagem(self, mensagem):
			self.mensagem = mensagem
		
		def setTeor(self, teor):
			self.teor = teor
		
		def setObs(self, obs):
			self.obs = obs	
	
		def setUrl(self, url):
			self.url = url	
	
		def setDateTime(self, dateTime):
			self.dateTime = dateTime
		
		def setAutor(self, autor):
			self.autor = autor	
	
		def setLocation(self, location):
			self.location = location
		
		def setStatusCount(self, statusCount):
			self.statusCount = statusCount
		
		def	setCreatedAt(self, createdAt):
			self.createdAt = createdAt
	
		def setHashTags(self, hashTags):
			self.hashTags = hashTags
	
		def setEntitles(self, entitles):
			self.entitles = entitles
	
		def setMencoes(self, mencoes):
			self.mencoes = mencoes
	
		def setAutorOriginal(self, autorOriginal):
			self.autorOriginal = autorOriginal
		
	
		def save(self):
			self.dbTweet.insert({"dateScrap":self.dateScrap, "hourScrap":self.hourScrap, "seguidores":self.seguidores, "rts":self.rts, "mensagem":self.mensagem, "teor":self.teor, "obs":self.obs, "url":self.url, "dateTime":self.dateTime, "autor":self.autor, "location":self.location, "statusCount":self.statusCount, "createdAt":self.createdAt, "hashTags":self.hashTags, "entitles":self.entitles, "mencoes":self.mencoes, "autorOriginal":self.autorOriginal })

	"""

	makefile('scrap.py',scrapPy)
	makefile('terms.txt','')
	makefile('tsv.py',tsvPy)
	makedir('classes')
	makefile('classes/__init__.py','')
	makefile('classes/database.py',databasePy)
	makefile('classes/tweets.py',tweetsPy)

if __name__ == "__main__":
	client = None

	try:
		client = sys.argv[1]
		generate(client)
	except:
		print usage()
	