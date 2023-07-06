#This code and description is written by Hoplin
#This code is written with API version 1.0.0(Rewirte-V)
#No matter to use it as non-commercial.
#Papago API Reference : https://developers.naver.com/docs/nmt/reference/

import discord
import yaml
from asyncio import *
from discord.ext import commands
from urllib.error import HTTPError, URLError
from papagoRequestClass import dataProcessStream

with open('config.yml') as f:
    keys = yaml.load(f, Loader=yaml.FullLoader)

###############################################################
#discord bot tokken
token = keys['Keys']['discordAPIToken']
#Naver Open API application ID
client_id = keys['Keys']['client_id']
#Naver Open API application token
client_secret = keys['Keys']['client_secret']
# stream Instane
streamInstance = dataProcessStream(client_id,client_secret)
###############################################################

client = discord.Client()
@client.event # Use these decorator to register an event.
async def on_ready(): # on_ready() event : when the bot has finised logging in and setting things up
    await client.change_presence(status=discord.Status.online, activity=discord.Game("Type !help or !도움말 for help"))
    print("New log in as {0.user}".format(client))

@client.event
async def on_message(message): # on_message() event : when the bot has recieved a message
    def sendmsg(resultPackage) -> discord.Embed:
        if resultPackage['status']["code"] < 300:
            embed = discord.Embed(title=f"Translate | {resultPackage['data']['ntl']['name']} -> {resultPackage['data']['tl']['name']}",description="", color=0x5CD1E5)
            embed.add_field(name=f"{resultPackage['data']['ntl']['name']} to translate", value=resultPackage['data']['ntl']['text'],inline=False)
            embed.add_field(name=f"Translated {resultPackage['data']['tl']['name']}", value=resultPackage['data']['tl']['text'],inline=False)
            embed.set_thumbnail(url="https://papago.naver.com/static/img/papago_og.png")
            embed.set_footer(text="Service provided by Hoplin. API provided by Naver Open API",icon_url='https://avatars2.githubusercontent.com/u/45956041?s=460&u=1caf3b112111cbd9849a2b95a88c3a8f3a15ecfa&v=4')
            return embed
        else:
            embed = discord.Embed(title="Error Code", description=resultPackage['status']['code'],color=0x5CD1E5)
            return embed

    #To user who sent message
    # await message.author.send(msg)
    print(message.content)
    if message.author == client.user:
        return
    if message.content.startswith("!韓翻英"):
        #띄어쓰기 : split처리후 [1:]을 for문으로 붙인다.
        trsText = message.content.split(" ")
        try:
            if len(trsText) == 1:
                await message.channel.send("並沒有輸入單字或句子，請確認後再試一次。")
            else:
                resultPackage = streamInstance.returnQuery(trsText)
                embedInstance = sendmsg(resultPackage)
                await message.channel.send("Translate complete", embed=embedInstance)
        except HTTPError as e:
            await message.channel.send(f"Translate Failed. HTTPError Occured : {e}")

    if message.content.startswith("!英翻韓"):
        baseurl = "https://openapi.naver.com/v1/papago/n2mt"
        # 띄어쓰기 : split처리후 [1:]을 for문으로 붙인다.
        trsText = message.content.split(" ")
        try:
            if len(trsText) == 1:
                await message.channel.send("並沒有輸入單字或句子，請確認後再試一次。")
            else:
                resultPackage = streamInstance.returnQuery(trsText)
                embedInstance = sendmsg(resultPackage)
                await message.channel.send("Translate complete", embed=embedInstance)
        except HTTPError as e:
            await message.channel.send("Translate Failed. HTTPError Occured.")

    if message.content.startswith("!韓翻日"):
        baseurl = "https://openapi.naver.com/v1/papago/n2mt"
        # 띄어쓰기 : split처리후 [1:]을 for문으로 붙인다.
        trsText = message.content.split(" ")
        try:
            if len(trsText) == 1:
                await message.channel.send("並沒有輸入單字或句子，請確認後再試一次。")
            else:
                resultPackage = streamInstance.returnQuery(trsText)
                embedInstance = sendmsg(resultPackage)
                await message.channel.send("Translate complete", embed=embedInstance)
        except HTTPError as e:
            await message.channel.send("Translate Failed. HTTPError Occured.")

    if message.content.startswith("!日翻韓"):
        baseurl = "https://openapi.naver.com/v1/papago/n2mt"
        # 띄어쓰기 : split처리후 [1:]을 for문으로 붙인다.
        trsText = message.content.split(" ")
        try:
            if len(trsText) == 1:
                await message.channel.send("並沒有輸入單字或句子，請確認後再試一次。")
            else:
                resultPackage = streamInstance.returnQuery(trsText)
                embedInstance = sendmsg(resultPackage)
                await message.channel.send("Translate complete", embed=embedInstance)
        except HTTPError as e:
            await message.channel.send("Translate Failed. HTTPError Occured.")

    if message.content.startswith("!韓翻中"):
        baseurl = "https://openapi.naver.com/v1/papago/n2mt"
        # 띄어쓰기 : split처리후 [1:]을 for문으로 붙인다.
        trsText = message.content.split(" ")
        try:
            if len(trsText) == 1:
                await message.channel.send("並沒有輸入單字或句子，請確認後再試一次。")
            else:
                resultPackage = streamInstance.returnQuery(trsText)
                embedInstance = sendmsg(resultPackage)
                await message.channel.send("Translate complete", embed=embedInstance)
        except HTTPError as e:
            await message.channel.send("Translate Failed. HTTPError Occured.")

    if message.content.startswith("!中翻韓"):
        baseurl = "https://openapi.naver.com/v1/papago/n2mt"
        # 띄어쓰기 : split처리후 [1:]을 for문으로 붙인다.
        trsText = message.content.split(" ")
        try:
            if len(trsText) == 1:
                await message.channel.send("並沒有輸入單字或句子，請確認後再試一次。")
            else:
                resultPackage = streamInstance.returnQuery(trsText)
                embedInstance = sendmsg(resultPackage)
                await message.channel.send("Translate complete", embed=embedInstance)
        except HTTPError as e:
            await message.channel.send("Translate Failed. HTTPError Occured.")
client.run(token)
