# Dependências

* MongoDB 2.0.2
* Python 2.7
* Pymongo
* WebPy 
* TweetStream

# Como funciona

## scrap.py
`python scrap.py [termo de busca]`

Responsável por extrair dados do Twitter Streaming API e guardar no banco de dados MongoDB.

## tsv.py
`python tsv.py [nome do diretorio] [data]`                                                                           
`python tsv.py [nome do diretorio] [data] [hora_cheia]`

Salva as informações existentes no banco de dados em arquivos do formato TSV.

##interface.py

Simples Web-Service REST para consulta dos dados no formato XML.

