import telebot
import requests
import os
from dotenv import load_dotenv

load_dotenv()

chave = os.getenv('TELEGRAM_TOKEN')

if not chave:
    print('ERRO: A chave nao foi encontrada no arquivo .env!')
    exit()

bot = telebot.TeleBot(chave)


@bot.message_handler(commands=['opcao1'])
def jogar_dado(mensagem):
    bot.send_dice(mensagem.chat.id, emoji="🎲")

@bot.message_handler(commands=['opcao2', 'cachorro'])
def mandar_cachorro(mensagem):
    url = "https://dog.ceo/api/breeds/image/random"
    resposta = requests.get(url)
    dados = resposta.json()

    link_da_foto = dados['message']

    bot.send_photo(mensagem.chat.id, link_da_foto, caption='cachorro')

@bot.message_handler(commands=['opcao3'])
def dar_conselho(mensagem):
    response = requests.get("https://api.adviceslip.com/advice")
    dados = response.json()
    frase = dados['slip']['advice']
    bot.reply_to(mensagem, f'Conselho do dia: \n\n{frase}')

def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
Escolha uma ação para o bot(Clique no item):
/opcao1 Dado (rola um dado animado)
/opcao2 Cachorro (busca a imagem de um cachorro aleatorio)
/opcao3 Conselho (pega um conselho aleatorio)
por favor, clique em alguma opção acima, outra coisa não vai funcionar."""
    bot.reply_to(mensagem, texto)


bot.polling()