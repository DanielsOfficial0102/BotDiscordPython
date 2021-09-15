#importações nessesarias
import discord
from discord.ext import commands
import random

#Comando que irá ativar o Bot no discord
client = commands.Bot(command_prefix = ",", case_insensitive = True)

@client.event
async def on_ready():
  print('Entramos como {0.user}' .format(client))

#Aqui é a ação que sera executada pelo usuario e respondida pelo bot em ctx.send
@client.command()
async def ola(ctx):
  await ctx.send(f'Olá, {ctx.author}, Como vai ?')

#insira seu id do bot em Cliente.run
client.run('')

#caso seja da sua vontade, usufrua esse codigo, acrescente mais camadas, funções...
