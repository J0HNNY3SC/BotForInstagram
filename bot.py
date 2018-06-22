import telepot, time
import sendemails
 
def handle(msg):
    userName = msg['from']['first_name']+" "+msg['from']['last_name']   
    content_type, chat_type, chat_id = telepot.glance(msg)

    i = 1
     
    if(content_type == 'text'):
        command = msg['text']
        print (userName + ' says: %s' % command)
     
    if 'Ola' in command:
        ola(msg)
        ##bot.sendMessage(chat_id, "Ola "+userName+", como voce esta?")
    if 'Bem' in command:
        bot.sendMessage(chat_id, "Legal\nquer conversar sobre algum assunto?")
    if 'Sim' in command:
        ##bot.sendMessage(chat_id, "1 Filmes\n2 Jogos\n3 Comida")
        bot.sendMessage(chat_id, "==============================\n===== 1 - FILMES =====\n===== 2 - JOGOS   =====\n===== 3 - COMIDA =====\n==============================")
    if 'Nao' in command:
        bot.sendMessage(chat_id, "Tudo bem entao :(")       
    if '1' in command:
     bot.sendMessage(chat_id, "qual seu filme favorito?")
    if '2' in command:
     bot.sendMessage(chat_id, "qual seu jogo favorito?")
    if '3' in command:
     bot.sendMessage(chat_id, "qual sua comida favorita?")
    if 'Email' in command:
        send(msg)
        while i != 0 :
            if i == 1:
                sendto(msg, i)
            if i == 2:
                subt(msg, i)
                bot.sendMessage(chat_id, "escreva ""Texto:"" mais seu texto que deseja enviar")
                i = 3
            if i == 3 and command.find('Texto:')  == 0:
                t = command
                bot.sendMessage(chat_id, "escreva ""Send"" para enviar")
                i = 4
            if i == 4 and 'Send' in command:
                envio(msg, st, sub, t)
                i = 0
            time.sleep(30)
##    if command.find('@') >0 and command.find('.com') >0:
##        st = command
##        sendto(st)
##        bot.sendMessage(chat_id, "escreva ""Sub:"" mais seu assunto")
##    if command.find('Sub:')  == 0:
##        sub = command
##        subt(sub)
##        bot.sendMessage(chat_id, "escreva ""Texto:"" mais seu texto que deseja enviar")
##    if  command.find('Texto:')  == 0:
##        t = command
##        te(t)
##        bot.sendMessage(chat_id, "escreva ""Send"" para enviar")
##    if  'Send' in command:
##        em = sendto(e)
##        envio(msg, st, sub, t)
##        print st
##        print sub
##        print t
def ola(msg):
     userName = msg['from']['first_name']+" "+msg['from']['last_name']   
     content_type, chat_type, chat_id = telepot.glance(msg)
     bot.sendMessage(chat_id, "Ola "+userName+", como voce esta?")

def send(msg):
    userName = msg['from']['first_name']+" "+msg['from']['last_name']   
    content_type, chat_type, chat_id = telepot.glance(msg)
    bot.sendMessage(chat_id, "pra quem deseja enviar email?")
    
def envio(msg, st, sub, t):
    send_from = 'JohnnyescBot@arris.com'
    password  = ''
    send_to   = [st]
    subject   = sub
    text      = t
    sendemails.send_mail(send_from, send_to, subject, text)

    userName = msg['from']['first_name']+" "+msg['from']['last_name']   
    content_type, chat_type, chat_id = telepot.glance(msg)
    bot.sendMessage(chat_id, "email enviado")

def sendto (st, i):
    userName = msg['from']['first_name']+" "+msg['from']['last_name']   
    content_type, chat_type, chat_id = telepot.glance(msg)
    if(content_type == 'text'):
        txt = msg['text']
        if txt.find('@') >0 and txt.find('.com') >0:
            st = txt
            bot.sendMessage(chat_id, "escreva ""Sub:"" mais seu assunto")
            i = 2
        else:
            bot.sendMessage(chat_id, "email invalido")
    return st, i       
    
def subt (sub):
    s = sub

def te (t):
    te = t
# Cria um bot com a API key disponibilizada pelo BotFather
bot = telepot.Bot('494674167:AAFJRaME65c9QqKmNIIlsRFUCoeInftCuPs')
 
# Adiciona a funcao handle para ser chamada sempre que uma nova mensagem for recebida
bot.message_loop(handle)
 
# Aguarda por novas mensagens
while 1:
 time.sleep(20)
