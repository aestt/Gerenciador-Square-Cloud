import nextcord
import json

from nextcord.ext import commands

class Ready(commands.Cog):
    def __init__(self, bot, *args, **kwargs):
        self.bot = bot

    @commands.Cog.listener() # Cria um evento
    async def on_ready(self): # Indica que o evento é on_ready, ou seja, quando o bot estiver pronto (online) irá acontecer alguma coisa
        print("-------------------------------------------")
        print(f"Estou logado como: {self.bot.user.name}") # Imprime o nome do bot + as mensagens no console
        print("-------------------------------------------")

        with open("./config/app.json") as file: # Abre o arquivo JSON
            data = json.load(file)

        atividade = data['STATUS_DE_ATIVIDADE'] # Pega a váriavel de status de atividade
        await self.bot.change_presence(activity=nextcord.Game(name=atividade)) # Seta o status de atividade de acordo com a variável

def setup(bot):
    bot.add_cog(Ready(bot))
    print("[+] Evento READY carregado com sucesso.")
