# <img src='https://github.com/josejooj/square-team-bot/assets/76636096/4ca01ab0-4523-4f5a-9f50-5242400845da' style="width: 22px; margin-right: 10px;"> Square Team Bot

Gerenciador Square Cloud serve para você gerenciar suas aplicações através de comandos, pelo próprio Discord.<br><br>
Ele usa a biblioteca de python feita pela própria Square Cloud para fazer as requisições.

## 🤔 Como usar?

- `/apps` -> Gerencie todas suas aplicações. Ligue, desligue, reinicie, solite backup, solicite as logs ou delete!
- `/upload` -> Envie uma aplicação para a sua hospedagem Square Cloud

## 👩‍💻 Obtendo o Gerenciador

### SETUP

Em primeiro lugar, verifique se você tem:

1. O Token do seu bot Discord
2. Sua API da Square Cloud
3. E os arquivos do Gerenciador ([download](https://github.com/aestt/Gerenciador-Square-Cloud)) baixados 

### Configurando o Gerenciador

1. Abra o arquivo `.app.json`, localizado na pasta `config`
2. Insira o `TOKEN` de acordo com seu bot de Discord
3. Insira a `API_SQUARE` de acordo com sua api da square cloud

## 💙 Hospedando sua instância do Square Team Bot

### Hospedando o bot em sua máquina

1. Instale o [python](https://www.python.org) 
2. Abra a pasta do Gerenciador (já extraída) no vs code
3. Abra o terminal e executa:
- pip install nextcord
- pip install function-cooldowns
- pip install squarecloud-api
4. Digite o comando py main.py

### Hospedando na Square Cloud

1. Acesso o menu inicial da Square [Square Cloud Dashboard](https://squarecloud.app/dashboard) e insira o .ZIP do Gerenciador lá

## ➕ Informações adicionais

> 🏁 **`Linguagem`**: Português<br>
> 🤖 **`Linguagem de Programação`**: Python
