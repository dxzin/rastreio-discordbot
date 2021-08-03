import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup

client = commands.Bot(command_prefix='!', case_insensitive=True)


@client.event
async def on_ready():
    print("Entramos como {0.user}".format(client))


@client.command()
async def r(ctx, codigo):
    variavel = str(codigo)
    resposta = requests.post(url='https://www2.correios.com.br/sistemas/rastreamento/ctrl/ctrlRastreamento.cfm?',
                             data={'objetos': codigo})
    soup = BeautifulSoup(resposta.text, 'html.parser')
    texto = soup.find(id='UltimoEvento').strong.text
    data = soup.find(id='UltimoEvento').text.split()[-1]
    print(texto, data)
    await ctx.send(f'{variavel} {texto} {data}')


client.run('token')