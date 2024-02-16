import nextcord
import json
import squarecloud as square
import cooldowns

from cooldowns import CallableOnCooldown
from nextcord.ext import commands
from nextcord import slash_command

class Upload(commands.Cog):
    def __init__(self, bot, *args, **kwargs):
        self.bot = bot

    @slash_command(name="upload", description="[➕] Envie uma aplicação")
    @cooldowns.cooldown(1, 30, bucket=cooldowns.SlashBucket.guild) # Seta tempo de 30 segundos por uso de comando na GUILD
    async def upload(self, interaction: nextcord.Interaction, arquivo: nextcord.Attachment):
        if interaction.user.guild_permissions.administrator: # Verifica se o usuário que executou o comando é um administrador
            pass
        else:
            await interaction.send(f"❌ **|** {interaction.user.mention} Você não tem **PERMISSÃO** para executar este comando.", ephemeral=True, delete_after=5) # Se ele não for, retorna essa mensagem
            return
        
        with open("./config/app.json") as file: # Abre o arquivo JSON
            data = json.load(file)

        msg = await interaction.send("🔁 | Enviando aplicação...", ephemeral=True)

        try:
            local_path = f"./temp/{arquivo.filename}" # Indica o local aonde o ARQUIVO inserido será salvo
            await arquivo.save(local_path) # Salva o arquivo no caminho acima

            api_square = data["API_SQUARE"] # Pega a API_SQUARE no arquivo JSON
            client = square.Client(api_square) 
            
            file = square.File(local_path) # Indica um arquivo pra biblioteca da square
            await client.upload_app(file) # Manda o arquivo de acordo com a API

            await msg.edit(f"✅ **|** {interaction.user.mention} Aplicação enviada com sucesso! Utilize `/apps` para gerenciar.", delete_after=5) # Executa uma mensagem de sucesso

        except Exception as e: # Se der algum erro
            if str(e).startswith("1"):
                await msg.edit(f"✅ **|** {interaction.user.mention} Aplicação enviada com sucesso! Utilize `/apps` para gerenciar.", delete_after=5)
            else:
                await msg.edit(f"❌ **|** {interaction.user.mention} Algo deu errado! {e}") # Vai retornar essa mensagem

    @upload.error
    async def on_command_error(self, interaction: nextcord.Interaction, error): # Indica que se o @commands.cooldown estiver LIGADO
        error = getattr(error, "original", error)

        if isinstance(error, CallableOnCooldown):
            await interaction.send(f"⚠️ **|** {interaction.user.mention} Aguarde `{int(error.retry_after)}` segundos para executar o comando novamente.", ephemeral=True, delete_after=5) # Vai mandar uma mensagem pedindo para o usuário esperar


def setup(bot):
    bot.add_cog(Upload(bot))
    print("[+] Comando UPLOAD carregado com sucesso.")
