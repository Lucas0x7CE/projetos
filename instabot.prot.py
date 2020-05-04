from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.webdriver import FirefoxProfile
from selenium.webdriver.remote.command import Command
import time

URL = 'https://www.instagram.com/'


class myBot:

    #instanciando configuracoes e iniciando o webdriver
    def __init__(self):
        foxOpt = webdriver.FirefoxOptions()
        # fireFoxOptions.set_headless()

        self.wdriver = webdriver.Firefox(executable_path='geckodriver.exe',firefox_options=foxOpt)

    #funcao abrir URL predefinida
    def abrir(self):
        self.wdriver.get(URL)
        time.sleep(10)

    #ao efetuar o login essa funcao devera ser executada para fechar a notificacao
    def fechar_notf1(self):
        time.sleep(5)
        #o elemento da notificacao pode se alterar a qualquer momento
        #esse loop tentara algumas comninaccoes a fim de acertar a correta
        #criei ela pois notei um certo limite de variacoes, a funcao pode ser readsptada
        for tentativa in range(5):
            try:
                self.wdriver.find_element_by_xpath(f"/html/body/div['{tentativa}']/div/div/div[3]/button[2]").click()
                return True
            except:
                self.wdriver.find_element_by_xpath(f"/html/body/div['{tentativa+1}']/div/div/div[3]/button[2]").click()
                return True
            tentativa += 1

    #funcao de login
    def logar_se(self,usuario,senha):
        
        #selecionar o input user do form de login
        user = self.wdriver.find_element_by_xpath(f"/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input")
        user.send_keys(usuario)#enviando a string q representa o user para o campo de formulario
        
        #selecionar o input passwd do form de login
        pwd = self.wdriver.find_element_by_xpath(f"/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input")
        pwd.send_keys(senha)#enviando a string q representa o passwd para o campo de formulario
        
        #seleciionando e simulando evendo de click no botao de login
        btnLogin = self.wdriver.find_element_by_xpath(f"/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button")
        btnLogin.click()#evento de click(obvio)
        
        #apos clicar, esperar 5s, tempo deve ser suficiente para renderizar a pagina, considere a velocidade de sua internet
        #aumente quando ficar lenta
        time.sleep(5)
        #apos renderizada surgira uma notificacao
        
        """
            creio que a questao da notificacao pode ser resolvida usando cookies ou um perfil existente de um navegador que ja possui login salvo na pagina, importando esses dados provavelmente a notificacao deixara de aparecer
        
        """
        self.fechar_notf1()

    #essa funcao nao funciona
    def curtir_feed(self):
        if self.wdriver.execute(Command.GET_CURRENT_URL) != "https://www.instagram.com/":
            self.wdriver.get("https://www.instagram.com/")
        #area_posts = self.wdriver.find_element_by_xpath(f"/html/body/div[1]/section/main/section/div[1]/div[2]")
        area_posts = self.wdriver.find_element_by_xpath(f"/html/body/div[1]/section/main/section/div[1]/div[3]/div")
        #/html/body/div[1]/section/main/section/div[1]/div[3]/div
        #scrollHeight = self.wdriver.execute(Command.TOUCH_SCROLL)
        
        posts = area_posts.find_elements_by_tag_name("article")

        for post in posts:
            first_div = post.find_element_by_class_name("eo2As")
            btnlike =first_div.find_element_by_tag_name("section").find_element_by_tag_name("span")
            

        for deep in range(5):
            artigo = 0
            timer = 1
            for curtida in range(4):
                if artigo > 3:
                    timer = 2
                btn = self.wdriver.find_element_by_xpath(f"/html/body/div[1]/section/main/section/div[1]/div[2]/div/article['{artigo}']/div[2]/section[1]/span[1]/button")
                #/html/body/div[1]/section/main/section/div[1]/div[3]/div/article[2]/div[2]/section[1]/span[1]
                btn.click()
                time.sleep(timer)
            # /html/body/div[1]/section/main/section/div[1]/div[2]/div
            #botao de curtida
            #/html/body/div[1]/section/main/section/div[1]/div[2]/div/article[2]/div[2]/section[1]/span[1]/button
            #/html/body/div[1]/section/main/section/div[1]/div[2]/div/article[3]/div[2]/section[1]/span[1]/button
            time.sleep(5)
            self.wdriver.execute_script("window.scrollTo(0, 4)")


    #segue todos os perfis na pagina de sugestoes
    def seguir_sugestoes(self):
        url_pag_sugest = f"https://www.instagram.com/explore/people/suggested/"
        #print(self.wdriver.execute(Command.GET_PAGE_SOURCE))
        url_atual = self.wdriver.execute(Command.GET_CURRENT_URL)
        if url_atual != url_pag_sugest:
            self.wdriver.get(url_pag_sugest)

        #selecionando apenas a div q possui os perfis
        cx_sugest = self.wdriver.find_element_by_xpath(f"/html/body/div[1]/section/main/div/div[2]")
        
        #dentro dessa div, eu considero cada botao um perfil
        opts = cx_sugest.find_elements_by_tag_name("button")


        #importante considerar o intervalo entre os eventos
        intervalo = 0.75
        click_Counter = 0
        LIMITE = 4
        razao = 1 / intervalo
        for perfil in opts:
            if click_Counter > LIMITE:
                intervalo = intervalo * 1.5
            perfil.click()
            click_Counter += 1
            time.sleep(intervalo)

    #essa funcao abre o chat
    #o que falta nela é o identificador de usuario para poder iniciar uma conversa
    def direct_chat(self):
    
        url_chat = "https://www.instagram.com/direct/inbox/"
        
        xpath_box_contatos = "/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div"
        xpath_contatos = "/div/div[1]" # 1 < x < qnt_contatos_in_box
        xpath_chat_log = "/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]"
        
        self.wdriver.get(url_chat)
        time.sleep(5)
        div_box_contatos = self.wdriver.find_element_by_xpath(xpath_box_contatos)
        div_contato = div_box_contatos.find_element_by_xpath(xpath_contatos)
        
        div_contato.click()

class Erro(object):
    def __init__(self):
        print("Connection timeout.")


# CODIGO
#
#
#
#
#
#
# EXECUCAO

SEGUIRSUGESTOES = 1
CURTIRTUDONOFEED = 0
ABRIRCHAT = 2

#insira login e senha
user = ""
senha = ""

b = myBot()
b.abrir()
b.logar_se(user,senha)
time.sleep(15)



#os comandos a segur sao apenas para fins de testes
opcao = SEGUIRSUGESTOES


#executando a funcao de seguir sugestoes
if opcao == SEGUIRSUGESTOES:
    for i in range(10):
        b.seguir_sugestoes()
        time.sleep(5)

#funcao para curtir postagens
elif opcao == CURTIRTUDONOFEED:

    #tente selecionar a area de postagens, apos falhar na 1 tentativa, sera aguardado 10s para que a pagina renderize 
    #e sera tentado novamente, acessar o msm elemento
    try:
        area_posts = b.wdriver.find_element_by_xpath(f"/html/body/div[1]/section/main/section/div[1]/div[2]")
    except Erro:
        time.sleep(10)
        area_posts = b.wdriver.find_element_by_xpath(f"/html/body/div[1]/section/main/section/div[1]/div[2]")
        
    #os comandos a seguir tratam do scrolling da pagina
    #é necessario um ajuste mais preciso para que possa simular o evento corretamente
    #ele é necessario para que seja carregado os demais elementos
    peso = 1
    while True:
        opcao = int(input("a descer\ns mudar peso "))
        if opcao == 'a':
            b.wdriver.execute_script("window.scrollTo(0,document.body.scrollHeight - {})".format(peso))
        elif opcao == 'b' :
            peso = int(input("peso: "))
        else:
            break
    #b.curtir_feed()
    
#funcao para abrir chat e mandar msg para todos
elif opcao == ABRIRCHAT:
    b.direct_chat()





b.wdriver.quit()