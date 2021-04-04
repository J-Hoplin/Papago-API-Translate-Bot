#This code and description is written by Hoplin
#This code is written with API version 1.0.0(Rewirte-V)
#No matter to use it as non-commercial.
#Papago API Reference : https://developers.naver.com/docs/nmt/reference/

import discord
import asyncio
import os
from discord.ext import commands
from urllib.request import URLError
from urllib.request import HTTPError
from urllib.request import urlopen
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from typing import Any, MutableSequence
from urllib.parse import quote_plus,quote,unquote
import re # Regex for youtube link
import warnings
import requests
import unicodedata
import json,time
from typing import Any, MutableSequence


DataDictionary = {
    "!한영번역" : ["ko","Korean","en","English"],
    "!영한번역" : ["en", "English","ko","Korean"],
    "!한일번역" : ["ko","Korean","ja","Japanese"],
    "!일한번역" : ["ja","Japanese", "ko","Korean"],
    "!한중번역" : ["ko","Korean","zh-CN","Chinese"],
    "!중한번역" : ["zh-CN","Korean","ko","Korean"]
}

class dataProcessStream(object):
    def __init__(self):
        self.baseurl = "https://openapi.naver.com/v1/papago/n2mt"
        self.translateDict = dict()
        self.InitiateData()

    def InitiateData(self) -> None:
        for y in list(DataDictionary.keys()):
            self.translateDict[y] = {
                "ntl" : {
                    "queryParam" : DataDictionary[y][0],
                    "languageName" : DataDictionary[y][1]
                },
                "tl" : {
                    "queryParam" : DataDictionary[y][2],
                    "languageName" : DataDictionary[y][3]
                }
            }

    def returnQuery(self, message) -> MutableSequence:
        translateType = message[0]
        needTranslate = self.remakeText(message)
        basicQuery = f"source={self.translateDict[translateType]['ntl']['queryParam']}&target={self.translateDict[translateType]['tl']['queryParam']}&text={quote_plus(needTranslate)}"
        return self.buildRequestInstane(basicQuery,needTranslate,self.translateDict[translateType]['ntl']['languageName'],self.translateDict[translateType]['tl']['languageName'])

    def buildRequestInstane(self,Query,needTranslate,ntl,tl) -> MutableSequence:
        req = Request(self.baseurl)
        req.add_header("X-Naver-Client-Id", client_id)
        req.add_header("X-Naver-Client-Secret", client_secret)
        response = urlopen(req,data=Query.encode("utf-8"))
        return self.checkResponseReturnDataBox(response,needTranslate,ntl,tl)


    def checkResponseReturnDataBox(self,response,needTranslate,ntl,tl) -> MutableSequence:
        dataBox = {
            "status" : {
                "code" : None
            },
            "data" : {
                "ntl" : {
                    "text" : needTranslate,
                    "name" : ntl
                },
                "tl" : {
                    "text" : None,
                    "name" : tl
                }
            }
        }
        if response.getcode() < 300:
            dataBox["status"]["code"] = response.getcode()
            response = response.read()
            apiResult = response.decode('utf-8')
            apiResult = json.loads(apiResult)
            translated = apiResult['message']['result']["translatedText"]
            dataBox["data"]["tl"]["text"] = translated
            return dataBox
        else:
            dataBox["status"]["code"] = response.getcode()
            return dataBox


    def remakeText(self,message) -> str:
        translateText = message[1:]
        translateText = " ".join(translateText)
        return translateText

#discord bot tokken
token = ''
#Naver Open API application ID
client_id = ""
#Naver Open API application token
client_secret = ""

# stream Instane
streamInstance = dataProcessStream()
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
    if message.content.startswith("!한영번역"):
        #띄어쓰기 : split처리후 [1:]을 for문으로 붙인다.
        trsText = message.content.split(" ")
        try:
            if len(trsText) == 1:
                await message.channel.send("단어 혹은 문장이 입력되지 않았어요. 다시한번 확인해주세요.")
            else:
                resultPackage = streamInstance.returnQuery(trsText)
                embedInstance = sendmsg(resultPackage)
                await message.channel.send("Translate complete", embed=embedInstance)
        except HTTPError as e:
            await message.channel.send(f"Translate Failed. HTTPError Occured : {e}")

    if message.content.startswith("!영한번역"):
        baseurl = "https://openapi.naver.com/v1/papago/n2mt"
        # 띄어쓰기 : split처리후 [1:]을 for문으로 붙인다.
        trsText = message.content.split(" ")
        try:
            if len(trsText) == 1:
                await message.channel.send("단어 혹은 문장이 입력되지 않았어요. 다시한번 확인해주세요.")
            else:
                resultPackage = streamInstance.returnQuery(trsText)
                embedInstance = sendmsg(resultPackage)
                await message.channel.send("Translate complete", embed=embedInstance)
        except HTTPError as e:
            await message.channel.send("Translate Failed. HTTPError Occured.")

    if message.content.startswith("!한일번역"):
        baseurl = "https://openapi.naver.com/v1/papago/n2mt"
        # 띄어쓰기 : split처리후 [1:]을 for문으로 붙인다.
        trsText = message.content.split(" ")
        try:
            if len(trsText) == 1:
                await message.channel.send("단어 혹은 문장이 입력되지 않았어요. 다시한번 확인해주세요.")
            else:
                resultPackage = streamInstance.returnQuery(trsText)
                embedInstance = sendmsg(resultPackage)
                await message.channel.send("Translate complete", embed=embedInstance)
        except HTTPError as e:
            await message.channel.send("Translate Failed. HTTPError Occured.")

    if message.content.startswith("!일한번역"):
        baseurl = "https://openapi.naver.com/v1/papago/n2mt"
        # 띄어쓰기 : split처리후 [1:]을 for문으로 붙인다.
        trsText = message.content.split(" ")
        try:
            if len(trsText) == 1:
                await message.channel.send("단어 혹은 문장이 입력되지 않았어요. 다시한번 확인해주세요.")
            else:
                resultPackage = streamInstance.returnQuery(trsText)
                embedInstance = sendmsg(resultPackage)
                await message.channel.send("Translate complete", embed=embedInstance)
        except HTTPError as e:
            await message.channel.send("Translate Failed. HTTPError Occured.")

    if message.content.startswith("!한중번역"):
        baseurl = "https://openapi.naver.com/v1/papago/n2mt"
        # 띄어쓰기 : split처리후 [1:]을 for문으로 붙인다.
        trsText = message.content.split(" ")
        try:
            if len(trsText) == 1:
                await message.channel.send("단어 혹은 문장이 입력되지 않았어요. 다시한번 확인해주세요.")
            else:
                resultPackage = streamInstance.returnQuery(trsText)
                embedInstance = sendmsg(resultPackage)
                await message.channel.send("Translate complete", embed=embedInstance)
        except HTTPError as e:
            await message.channel.send("Translate Failed. HTTPError Occured.")

    if message.content.startswith("!중한번역"):
        baseurl = "https://openapi.naver.com/v1/papago/n2mt"
        # 띄어쓰기 : split처리후 [1:]을 for문으로 붙인다.
        trsText = message.content.split(" ")
        try:
            if len(trsText) == 1:
                await message.channel.send("단어 혹은 문장이 입력되지 않았어요. 다시한번 확인해주세요.")
            else:
                resultPackage = streamInstance.returnQuery(trsText)
                embedInstance = sendmsg(resultPackage)
                await message.channel.send("Translate complete", embed=embedInstance)
        except HTTPError as e:
            await message.channel.send("Translate Failed. HTTPError Occured.")
client.run(token)
