import nextcord
import json
import os

from nextcord.ext import commands

with open("./config/app.json") as file:
    data = json.load(file)

token = data["TOKEN"]
intents = nextcord.Intents.all()

client = commands.Bot(command_prefix="!", intents=intents)
client.remove_command("help") # Remove o comando padrão de help

for filename in os.listdir('./events'): # Utilizado para que os eventos sejam lidos e adicionados
    if filename.endswith('.py'):
        client.load_extension(f'events.{filename[:-3]}')

for filename in os.listdir('./commands'): # Utilizado para que os comandos sejam lidos e adicionados
    if filename.endswith('.py'):
        client.load_extension(f'commands.{filename[:-3]}')

client.run(token)