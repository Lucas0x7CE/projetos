import requests
from bs4 import BeautifulSoup
import modulogravador
#Criado por Lucas Vieira
r = requests.get('https://olhardigital.com.br/noticias/')

bs = BeautifulSoup(r.text,'lxml')

mainDiv = bs.find('div',class_="blk-items")#contem todos os posts



divsPosts= mainDiv.find_all('div',class_='ite-meta')#conteudo: titulo, subtitulo, data

listaNoticias = []

for post in divsPosts:
    
    noticia = []
    
    titulo = post.h3.string
    subtitulo = post.find('div',class_='ite-nfo nfo-txt').string
    data = post.find('div',class_='ite-nfo nfo-tpo').string
    link = 'https:' + post.parent['href']#tag da variavel post esta contida num <a>
                              #entao utilizando o .parent sera retornado a
                              #propria tag <a>, entao basta acessar o atributo
                              #['href'] para obter o 
                              
    noticia.append(titulo)
    noticia.append(subtitulo)
    noticia.append(data)
    noticia.append(link)
    listaNoticias.append(noticia)
    print('titulo: {}\nSubtitulo: {}\nData: {}\nLink: {}\n#########\n'.format(titulo,subtitulo,data,link))



for noticia in listaNoticias:
    n = modulogravador.a(noticia)
    modulogravador.b(n)