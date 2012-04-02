import sys
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
	fname = '%s/%s_%s.tsv' %(client, date, hour)
	try:
		f = open(fname, 'a')
		f.write(content)
	except:
		os.mkdir(client)
		f = open(fname, 'w')
		f.write(content)
		
	f.close

def search(client, date, hour):
	content = None

	if date and hour:
		myTweets = dbTweet.find({ "hourScrap":hour, "dateScrap":date })
	elif date:
		myTweets = dbTweet.find({ "dateScrap":date })
	
	try: 	
		for myTweet in myTweets:
			content += "%s\t%s\t%s\n" %(myTweet['autor'], myTweet['mensagem'], myTweet['dateTime'])
	except:
		print 'Nao ha dados'

	try:
		toTSV(client, date, hour, content)
	except:
		print 'Impossivel criar TSV'

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
		#toTSV(action,date, hour, '\tlol\n')
