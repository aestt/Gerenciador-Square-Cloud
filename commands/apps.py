import nextcord
import json
import squarecloud as square
import asyncio
import cooldowns

from cooldowns import CallableOnCooldown
from nextcord.ext import commands, application_checks
from nextcord import slash_command

class Apps(commands.Cog):
    def __init__(self, bot, *args, **kwargs):
        self.bot = bot

    @slash_command(name="apps", description="[🔧] Gerencie suas aplicações")
    @cooldowns.cooldown(1, 30, bucket=cooldowns.SlashBucket.guild)
    async def apps(self, interaction: nextcord.Interaction, id):  
        """
        :param id: ID do BOT
        """ # Coloca uma descrição na propriedade ID

        user = interaction.user

        if interaction.user.guild_permissions.administrator:
            pass
        else:
            await interaction.send(f"❌ **|** {interaction.user.mention} Você não tem **PERMISSÃO** para executar este comando.", ephemeral=True, delete_after=5)
            return
        
        if id == "❌ Você não possui permissão":
            await interaction.send(f"❌ **|** {interaction.user.mention} Você não tem **PERMISSÃO** de executar este comando.", ephemeral=True, delete_after=5)
            return # Verifica se o id retornou que não tem permissão, se sim, da a mensagem
        elif id == "⚠️ API não encontrada":
            await interaction.send(f"⚠️ **|** {interaction.user.mention} Não consegui localizar a **API**! Altere ela e tente novamente.", ephemeral=True, delete_after=3)
            return
        elif id == "Não encontrei nenhum bot hospedado":
            await interaction.send(f"❌ **|** {interaction.user.mention} Não encontrei nenhum bot hospedado.", ephemeral=True, delete_after=3)
            return

        id_selecionado = id.split(" -")[1] # O id retorna assim: Nome do Bot - ID, para verificar as informações na api, é necessário SOMENTE O ID.
                                            # Sendo assim, ele retira o nome e fica somente com o ID
        id_selecionado = id_selecionado.replace(" ", "") # Tira todos os espaços

        nome_selecionado = id.split("- ")[0]
        nome_selecionado = nome_selecionado.replace(" ", "") # Faz a mesma coisa que o de cima, mas pega o NOME
        
        button1 = nextcord.ui.Button(label="Ligar", style=nextcord.ButtonStyle.green) # Cria um botão com a cor verde
        button2 = nextcord.ui.Button(label="Desligar", style=nextcord.ButtonStyle.red) # Cria um botão com a cor Vermelha
        button3 = nextcord.ui.Button(label="Reiniciar", style=nextcord.ButtonStyle.primary) # Cria um botão com a cor Azul
        button4 = nextcord.ui.Button(label="Backup", emoji="💾", style=nextcord.ButtonStyle.secondary) # Cria um botão com a cor cinza
        button5 = nextcord.ui.Button(label="Baixar Logs", emoji="🗃️", style=nextcord.ButtonStyle.secondary) # Cria um botão com a cor cinza
        button6 = nextcord.ui.Button(label="Deletar Aplicação", emoji="🗑️", style=nextcord.ButtonStyle.danger) # Cria um botão com a cor cinza

        with open("./config/app.json") as file:
            data = json.load(file)

        api_square = data["API_SQUARE"] # Pega a API da square

        client = square.Client(api_key=api_square)
        app = await client.app(id_selecionado)

        async def embed_att(valor): # Cria uma função
            status = await app.status() # Pega todos os STATUS do bot selecionado

            squareCpu = status.cpu # Verifica a CPU do bot selecionado
            squareRam = status.ram # Verifica a RAM do bot selecionado
            squareStatus = status.running # Verifica se o bot selecionado está ligado
            squareSSD = status.storage # Verifica o SSD do bot selecionado
            squareRequest = status.requests # Verifica os REQUESTS do bot selecionado
            squareNetwork = status.network # Verifica a NETWORK do bot selecionado

            if squareStatus == True: # Se o bot estiver ligado 
                statusMessage = "Online: Seu bot está LIGADO!" # Retornar essa mensagem
            else: # Se não: Ou seja, se o bot estiver desligado
                statusMessage = "Offline: Seu bot está DESLIGADO!" # Retornar essa mensagem

            if valor == "Embed":
                embed = nextcord.Embed() # Cria uma mensagem
                embed.add_field(name="💾 | CPU", value=f"{squareCpu}")
                embed.add_field(name="💾 | Memoria Ram", value=f"{squareRam}")
                embed.add_field(name="💾 | SSD", value=f"{squareSSD}")
                embed.add_field(name="📥 | Network (Total)", value=f"{squareNetwork['total']}")
                embed.add_field(name="📤 | Network (Now)", value=f"{squareNetwork['now']}")
                embed.add_field(name="📈 | Requests", value=f"{squareRequest}")
                embed.add_field(name="🧮 | Status", value=f"{statusMessage}")
                embed.add_field(name="🆔 | ID", value=f"{id_selecionado}")
                embed.set_author(name=f"{interaction.user.name} | {nome_selecionado}", icon_url=interaction.user.avatar.url if interaction.user.avatar else None)

                return embed
            
            elif valor == "View":
                if squareStatus == True:
                    button1.disabled = True
                    button2.disabled = False
                    button3.disabled = False
                    button4.disabled = False
                    button5.disabled = False
                    button6.disabled = False
                else:
                    button1.disabled = False
                    button2.disabled = True
                    button3.disabled = True
                    button4.disabled = False
                    button5.disabled = True
                    button6.disabled = False

                view = nextcord.ui.View(timeout=None)
                view.add_item(button1)
                view.add_item(button2)
                view.add_item(button3)
                view.add_item(button4)
                view.add_item(button5) # Adiciona o todos os botões em um VIEW, que é basicamente a variavel que vai retornar os botões para o usuário
                view.add_item(button6)

                return view

        async def button1_callback(interaction: nextcord.Interaction): # Callback, ou seja, o que o botão vai fazer
            if interaction.user is user: # Verifica se quem clica no botão é o autor do comando
                pass 
            else:
                return
            
            button1.disabled = True # Desativa o botão
            button2.disabled = True # Desativa o botão
            button3.disabled = True # Desativa o botão
            button4.disabled = True # Desativa o botão
            button5.disabled = True # Desativa o botão
            button6.disabled = True # Desativa o botão

            viewAtt = nextcord.ui.View(timeout=None)
            viewAtt.add_item(button1)
            viewAtt.add_item(button2)
            viewAtt.add_item(button3)
            viewAtt.add_item(button4)
            viewAtt.add_item(button5)
            viewAtt.add_item(button6)

            await interaction.message.edit(view=viewAtt) # Edita a mensagem
            msg = await interaction.send(f"🟩 **|** {interaction.user.mention} Ligando a aplicação...", ephemeral=True) # Manda uma mesnagem
            await app.start() # Liga o bot

            await asyncio.sleep(5) # Bot espera 5 segundos, pra evitar bugs

            await interaction.message.edit(embed=await embed_att("Embed"), view=await embed_att("View")) # Atualiza a mensagem
            await msg.edit(f"✅ **|** {interaction.user.mention} Aplicação ligada com sucesso!", delete_after=3) 

        async def button2_callback(interaction: nextcord.Interaction): # Callback, ou seja, o que o botão vai fazer
            if interaction.user is user: # Verifica se quem clica no botão é o autor do comando
                pass 
            else:
                return
            
            button1.disabled = True # Desativa o botão
            button2.disabled = True # Desativa o botão
            button3.disabled = True # Desativa o botão
            button4.disabled = True # Desativa o botão
            button5.disabled = True # Desativa o botão
            button6.disabled = True # Desativa o botão

            viewAtt = nextcord.ui.View(timeout=None)
            viewAtt.add_item(button1)
            viewAtt.add_item(button2)
            viewAtt.add_item(button3)
            viewAtt.add_item(button4)
            viewAtt.add_item(button5)
            viewAtt.add_item(button6)

            await interaction.message.edit(view=viewAtt) # Edita a mensagem
            msg = await interaction.send(f"🟥 **|** {interaction.user.mention} Desligando a aplicação...", ephemeral=True)
            await app.stop() # Desliga a aplicação

            await asyncio.sleep(5) # Bot espera 5 segundos para evitar bugs

            await interaction.message.edit(embed=await embed_att("Embed"), view=await embed_att("View")) # Atualiza a mensagem 
            await msg.edit(f"✅ **|** {interaction.user.mention} Aplicação desligada com sucesso!", delete_after=3)

        async def button3_callback(interaction: nextcord.Interaction): # Callback, ou seja, o que o botão vai fazer
            if interaction.user is user: # Verifica se quem clica no botão é o autor do comando
                pass 
            else:
                return
            
            button1.disabled = True # Desativa o botão
            button2.disabled = True # Desativa o botão
            button3.disabled = True # Desativa o botão
            button4.disabled = True # Desativa o botão
            button5.disabled = True # Desativa o botão
            button6.disabled = True # Desativa o botão

            viewAtt = nextcord.ui.View(timeout=None)
            viewAtt.add_item(button1)
            viewAtt.add_item(button2)
            viewAtt.add_item(button3)
            viewAtt.add_item(button4)
            viewAtt.add_item(button5)
            viewAtt.add_item(button6)

            await interaction.message.edit(view=viewAtt) # Edita a mensagem
            msg = await interaction.send(f"🟦 **|** {interaction.user.mention} Reiniciando a aplicação...", ephemeral=True)
            await app.restart() # Reinicia o bot

            await asyncio.sleep(5)# Bot espera 5 segundos para evitar bugs

            await interaction.message.edit(embed=await embed_att("Embed"), view=await embed_att("View")) # Atualiza a mensagem 
            await msg.edit(f"✅ **|** {interaction.user.mention} Aplicação ligada com sucesso!", delete_after=3)

        async def button4_callback(interaction: nextcord.Interaction): # Callback, ou seja, o que o botão vai fazer
            if interaction.user is user: # Verifica se quem clica no botão é o autor do comando
                pass 
            else:
                return
            
            msg = await interaction.send(f"🔁 **|** {interaction.user.mention} Carregando link...", ephemeral=True)

            backup = await app.backup() # Pega o backup
            await interaction.user.send(f"🔗 Link para Download da aplicação `{nome_selecionado} - {id_selecionado}`\n{backup.downloadURL}") # Manda pro usuário

            await msg.edit(f"✅ **|** {interaction.user.mention} Link de download foi enviado no seu privado com sucesso.", delete_after=3)

        async def button5_callback(interaction: nextcord.Interaction): # Callback, ou seja, o que o botão vai fazer
            if interaction.user is user: # Verifica se quem clica no botão é o autor do comando
                pass 
            else:
                return
            
            msg = await interaction.send(f"🔁 **|** {interaction.user.mention} Carregando logs...", ephemeral=True)

            try:
                logs = await app.logs() # Pega as logs

                embed = nextcord.Embed(title=f"Logs - {nome_selecionado} | {id_selecionado}", description=f"```{logs.logs}```")

                await interaction.user.send(embed=embed) # Manda pro usuario
                await msg.edit(f"✅ **|** {interaction.user.mention} As logs foram enviadas no seu privado com sucesso.", delete_after=5)
            except Exception as e:
                await msg.edit(f"❌ **|** {interaction.user.mention} Algo deu errado! {e}", delete_after=5)

        async def button6_callback(interaction: nextcord.Interaction):
            if interaction.user is user: # Verifica se quem clica no botão é o autor do comando
                pass 
            else:
                return
            
            form = nextcord.ui.TextInput(label="Digite SIM para continuar", placeholder="SIM", required=True, min_length=1, max_length=3) # Cria o formulario

            async def form_callback(interaction: nextcord.Interaction):
                if form.value == "SIM": # Verifica se o usuário digitou SIM
                    await client.delete_app(id_selecionado)
                    await interaction.message.edit(content=f"✅ **|** {interaction.user.mention} Aplicação deletada com sucesso", delete_after=8, embed=None, view=None)
                else:
                    await interaction.send("❌ **|** {interaction.user.mention} Você não digitou **SIM**, nada aconteceu.", ephemeral=True, delete_after=3)

            modal = nextcord.ui.Modal(title="🗑️ | Deletar aplicação", timeout=None)
            modal.add_item(form)
            modal.callback = form_callback

            await interaction.response.send_modal(modal=modal) # Envie o formulário pro usuário

        button1.callback = button1_callback # Seta o callback no botão
        button2.callback = button2_callback # Seta o callback no botão
        button3.callback = button3_callback # Seta o callback no botão
        button4.callback = button4_callback # Seta o callback no botão
        button5.callback = button5_callback # Seta o callback no botão
        button6.callback = button6_callback # Seta o callback no botão

        await interaction.send(embed=await embed_att("Embed"), view=await embed_att("View")) # Manda a mensagem


    @apps.on_autocomplete("id") # Aqui indica que vai auto completar a propriedade "id"
    async def _(self, interaction: nextcord.Interaction, nome):
        if interaction.user.guild_permissions.administrator: # Verifica se o usuário é um administrador
            pass
        else: # Se ele não for, vai retornar um array indicando que ele não tem permissão
            choices = ["❌ Você não possui permissão"]
            return choices
        
        choices = []
        
        with open("./config/app.json") as file: # Abre nosso arquivo de configuração 
            data = json.load(file)

        try:
            api_square = data["API_SQUARE"] # Pega o valor da api
            client = square.Client(api_key=api_square) # Conecta na api

            appsSquare = await client.all_apps() # Solicita todoso os bots da api 

            for apps in appsSquare:
                choices.append(f"{apps.tag} - {apps.id}")

            for choice in choices:
                if choice == "":
                    choices.append("Não encontrei nenhum bot hospedado")
        except: # Se o código de algum erro, ele vai retornar que a api não foi encontrada
            choices.append("⚠️ API não encontrada")

        return choices
    
    @apps.error
    async def on_command_error(self, interaction: nextcord.Interaction, error):
        error = getattr(error, "original", error)

        if isinstance(error, CallableOnCooldown):
            await interaction.send(f"⚠️ **|** {interaction.user.mention} Aguarde `{int(error.retry_after)}` segundos para executar o comando novamente.", ephemeral=True, delete_after=5)
        

        


def setup(bot):
    bot.add_cog(Apps(bot))
    print("[+] Comando APPS carregado com sucesso.")
