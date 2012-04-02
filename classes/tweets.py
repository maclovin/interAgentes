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
