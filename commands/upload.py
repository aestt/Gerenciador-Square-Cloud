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
    @cooldowns.cooldown(1, 30, bucket=cooldowns.SlashBucket.guild)
    async def upload(self, interaction: nextcord.Interaction, arquivo: nextcord.Attachment):
        if interaction.user.guild_permissions.administrator:
            pass
        else:
            await interaction.send(f"❌ **|** {interaction.user.mention} Você não tem **PERMISSÃO** para executar este comando.", ephemeral=True, delete_after=5)
            return
        
        with open("./config/app.json") as file:
            data = json.load(file)

        msg = await interaction.send("🔁 | Enviando aplicação...", ephemeral=True)

        try:
            local_path = f"./temp/{arquivo.filename}"
            await arquivo.save(local_path)

            api_square = data["API_SQUARE"]
            client = square.Client(api_square)
            
            file = square.File(local_path)
            await client.upload_app(file)

            await msg.edit(f"✅ **|** {interaction.user.mention} Aplicação enviada com sucesso! Utilize `/apps` para gerenciar.", delete_after=5)

        except Exception as e:
            if str(e).startswith("1"):
                await msg.edit(f"✅ **|** {interaction.user.mention} Aplicação enviada com sucesso! Utilize `/apps` para gerenciar.", delete_after=5)
            else:
                await msg.edit(f"❌ **|** {interaction.user.mention} Algo deu errado! {e}")

    @upload.error
    async def on_command_error(self, interaction: nextcord.Interaction, error):
        error = getattr(error, "original", error)

        if isinstance(error, CallableOnCooldown):
            await interaction.send(f"⚠️ **|** {interaction.user.mention} Aguarde `{int(error.retry_after)}` segundos para executar o comando novamente.", ephemeral=True, delete_after=5)


def setup(bot):
    bot.add_cog(Upload(bot))
    print("[+] Comando UPLOAD carregado com sucesso.")