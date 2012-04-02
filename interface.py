import tweetstream
import pymongo
import web
from pymongo import Connection
	
def getTweets(format):
	dbTweet.create_index('id')
	myTweets = dbTweet.find().sort('id', pymongo.DESCENDING)
	
	if format == 'xml':
		response = '<tweets>'
		for myTweet in myTweets:
			response +=	"<user><nick>%s</nick><image>%s</image><content>%s</content><dateScrap>%s</dateScrap></user>" %(myTweet['nick'], myTweet['image'], myTweet['content'], myTweet['dateScrap'])			
		response += '</tweets>'
	elif format == 'tsv':
		for myTweet in myTweets:
			response = "%s\t%s\t%s\n" %(myTweet['nick'], myTweet['image'], myTweet['content'])
			
	return response

class index:
	def GET(self):
		web.header('Content-Type','text/xml; Charset=utf-8', unique=True) 
		response = getTweets('xml')		
		return response


urls = ('/', 'index')
app = web.application(urls, globals())

myConnection = Connection('127.0.0.1', 27017)
db = myConnection.tweet

#passar como parametro nos objetos
dbTweet = db.tweet		

if __name__ == "__main__": app.run()