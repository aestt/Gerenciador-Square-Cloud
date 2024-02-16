import nextcord
import json

from nextcord.ext import commands

class Ready(commands.Cog):
    def __init__(self, bot, *args, **kwargs):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("-------------------------------------------")
        print(f"Estou logado como: {self.bot.user.name}")
        print("-------------------------------------------")

        with open("./config/app.json") as file:
            data = json.load(file)

        atividade = data['STATUS_DE_ATIVIDADE']
        await self.bot.change_presence(activity=nextcord.Game(name=atividade))

def setup(bot):
    bot.add_cog(Ready(bot))
    print("[+] Evento READY carregado com sucesso.")