import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os
from pymongo import Connection
from datetime import date

myConnection = Connection('127.0.0.1', 27017)
db = myConnection.tweet

#passar como parametro nos objetos
dbTweet = db.tweet

def usage():
	usage = """
	Modo de usar:
	python tsv.py [nome do diretorio] [data]
        python tsv.py [nome do diretorio] [data] [hora_cheia]
	
	Ex:
	python tsv.py joao 2012-03-28
	python tsv.py joao 2012-03-28 14

	"""
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
			content += "%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n" %(myTweet['dateScrap'], myTweet['hourScrap'], myTweet['seguidores'], myTweet['rts'], myTweet['mensagem'], myTweet['teor'], myTweet['obs'], myTweet['url'], myTweet['dateTime'], myTweet['autor'], myTweet['location'], myTweet['statusCount'], myTweet['createdAt'], myTweet['hashTags'], myTweet['entitles'], myTweet['mencoes'], myTweet['autorOriginal'])
	except:
		print 'Nao ha dados'
		

	print "Conteudo: %s\n\n" %(content)
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
