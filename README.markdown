# Dependências

* MongoDB 2.0.2
* Python 2.7
* Pymongo
* WebPy 
* TweetStream

# Como funciona
Primeiramente é necessário levantar o servidor mongo, dependendo de seu ambiente o comando `mongod` é o suficiente.

## build.py
Primeiro construa o ambiente movendo o arquivo build.py do diretório /build para o diretório que preferir ter o ambiente de scrapping.
Depois inicie a criação de um novo ambiente:
`python build.py [nome_do_ambiente_ou_do_cliente]`

## scrap.py
Edite o arquivo terms.txt adicionando termos de busca em cada linha do arquivo.
Depois execute o aplicativo de Scrapping:
`python scrap.py`

Ele será responsável por extrair dados do Twitter Streaming API e guardar no banco de dados MongoDB.

## tsv.py
`python tsv.py [nome do diretorio] [data]`                                                                           
`python tsv.py [nome do diretorio] [data] [hora_cheia]`

Salva as informações existentes no banco de dados em arquivos do formato TSV.

##interface.py

Simples Web-Service REST para consulta dos dados no formato XML.

