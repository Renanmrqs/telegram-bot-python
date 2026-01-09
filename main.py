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

@bot.message_handler(commands=['opcao4'])
def buscar_cep(mensagem):
    try:
        cep_bruto = mensagem.text.split()[1]
    except IndexError:
        bot.reply_to(mensagem, "Ops! Digite o CEP junto. Ex: /opcao4 88010000")
        return
    cep_validado = cep_bruto.replace('-', '').replace('.', '').replace(' ', '')
    if len(cep_validado) == 8 and cep_validado.isdigit():
        resposta = requests.get(f'https://viacep.com.br/ws/{cep_validado}/json/')
        dados_cep = resposta.json()
        if "erro" in dados_cep:
            bot.reply_to(mensagem, 'cep inexistente!')
            return
        rua_usuario = dados_cep['logradouro']
        bairro_usuario = dados_cep['bairro']
        cidade_usuario = dados_cep['localidade']
        estado_usuario = dados_cep['uf']
        bot.reply_to(mensagem, f'{rua_usuario}, {bairro_usuario}, {cidade_usuario}-{estado_usuario}')
    else:
        bot.reply_to(mensagem, f'DIGITE APENAS 8 CARECTERES')

@bot.message_handler(commands=['opcao5', 'clima'])
def buscar_clima(mensagem):
    resposta = requests.get('https://api.open-meteo.com/v1/forecast?latitude=-27.59&longitude=-48.54&current_weather=true')
    clima = resposta.json()
    calor = clima['current_weather']['temperature']
    bot.reply_to(mensagem, f'A temperatura de florianopolis agora é: {calor}°C')



def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
Escolha uma ação para o bot(Clique no item):
/opcao1 Dado (rola um dado animado)
/opcao2 Cachorro (busca a imagem de um cachorro aleatorio)
/opcao3 Conselho (pega um conselho aleatorio)
/opcao4 Cep (Busca seu cep)
/opcao5 Clima (busca o clima de florianopolis)
por favor, clique em alguma opção acima, outra coisa não vai funcionar."""
    bot.reply_to(mensagem, texto)


bot.polling()

