import requests
import copy
from bs4 import BeautifulSoup
#Criado por Lucas Vieira
#.prettify() retorna string
def a(lista):
    modn = open('modelonoticia.html','r')
    strModn = modn.read()
    modn.close()
    docmdn = BeautifulSoup(strModn,'lxml')
    docmdn.div.h4.string = lista[2]
    docmdn.div.a['href'] = lista[3]
    docmdn.div.h3.string = lista[0]
    docmdn.div.p.string = lista[1]
    #definir id baseado na quantidade de class notice
    groupdiv = docmdn.find('div',class_='group-notices')
    noticia = groupdiv.find('div',class_='notice')
    print(type(noticia.prettify()))
    ## abrir o modelo de pagina
    # selecionar a group-notices
    # copiar as 'notice' de group-notices
    # contar o numero de notice
    # copia + noticia --substitui o conteudo de--> group-notices
    #gnP = modelopagina.find('div',class_='group-notices')
    #gnP.contents = copia + copy.copy(noticia)
    
    return noticia

def b(noticia):        
    modp = open('index.html','r')
    strmodp = modp.read()
    modp.close()
    docmdp = BeautifulSoup(strmodp,'lxml')
    gpdiv = docmdp.find('div',class_='group-notices')
    #listar todas as divs 'notice'
    #se = 0 entao criar
    gpdiv.append(noticia)
    modp = open('index.html','w')
    modp.write(docmdp.prettify())
    modp.close()
    
