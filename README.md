# 🤖 Bot Multifuncional Telegram

Este projeto é um Chatbot para Telegram desenvolvido em Python. Ele integra múltiplas APIs para fornecer funcionalidades de entretenimento, utilitários e consumo de dados externos em tempo real.

## 🚀 Funcionalidades

- **🎲 Jogos Nativos:** Integração com animações nativas do Telegram (Dados).
- **🐶 API Visual:** Consumo da *DogCEO API* para envio de imagens aleatórias.
- **🔮 API de Texto:** Consumo da *AdviceSlip API* para conselhos e frases de sabedoria.
- **📌 API de Endereço** Consumo da *ViaCEP* para buscar endereços.
- **☁️ API de Clima**   Consumo da *Open-Meteo* para buscar o clima.
- **🛡️ Segurança:** Utilização de variáveis de ambiente (.env) para proteção de credenciais sensíveis.

## 🛠️ Tecnologias Utilizadas

- **Python 3.12+**
- **PyTelegramBotAPI** (Manipulação do Bot)
- **Requests** (Consumo de APIs REST)
- **Python-Dotenv** (Gerenciamento de variáveis de ambiente)

## 📦 Como rodar este projeto

### Pré-requisitos
Você precisará ter o [Python](https://www.python.org/) instalado em sua máquina.

### Passo a passo

1. **Clone o repositório**
   ```bash
   git clone [https://github.com/Renanmrqs/telegram-bot-python.git](https://github.com/Renanmrqs/telegram-bot-python.git)
   cd telegram-bot-python

2. **Crie um ambiente virtual (Opcional, mas recomendado)**

    ```Bash
    python -m venv venv
# No Windows:
venv\Scripts\activate
# No Linux/Mac:
source venv/bin/activate

3. *Instale as dependências*

pip install -r requirements.txt

4. *Configuração de Segurança (.env) Crie um arquivo chamado .env na raiz do projeto e adicione seu token:*

TELEGRAM_TOKEN=seu_token_aqui_pego_no_botfather

5. *Execute o Bot*

**Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.**

---