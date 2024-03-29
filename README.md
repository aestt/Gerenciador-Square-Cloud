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
3. E os arquivos do ([Gerenciador](https://github.com/aestt/Gerenciador-Square-Cloud)) baixados 

### Configurando o Gerenciador

1. Abra o arquivo `app.json`, localizado na pasta `config`
2. Insira o `TOKEN` de acordo com seu bot de Discord
3. Insira a `API_SQUARE` de acordo com sua api da square cloud

## 💙 Hospedando sua instância

### Hospedando o bot em sua máquina

1. Instale o [Python](https://www.python.org) 
2. Abra a pasta do Gerenciador (já extraída) no vs code
3. Abra o terminal e execute:
- pip install nextcord
- pip install function-cooldowns
- pip install squarecloud-api
4. Digite o comando py main.py

### Hospedando na Square Cloud

1. Baixe todos os arquivos e compacte eles para .ZIP
2. Acesse o menu inicial da Square ([Square Cloud Dashboard](https://squarecloud.app/dashboard))
3. Clique em adicionar novo ou add new e insira o .ZIP
   
## ➕ Informações adicionais

> 🏁 **`Linguagem`**: Português<br>
> 🤖 **`Linguagem de Programação`**: Python
