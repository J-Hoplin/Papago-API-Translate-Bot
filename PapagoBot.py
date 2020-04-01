#This code and description is written by Hoplin
#This code is written with API version 1.0.0(Rewirte-V)
#No matter to use it as non-commercial.
#Papago API Reference : https://developers.naver.com/docs/nmt/reference/

import discord
import asyncio
import os
from discord.ext import commands
import urllib
from urllib.request import URLError
from urllib.request import HTTPError
from urllib.request import urlopen
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from urllib.parse import quote
import re # Regex for youtube link
import warnings
import requests
import unicodedata
import json

#discord bot tokken
token = ''
#Naver Open API application ID
client_id = ""
#Naver Open API application token
client_secret = ""

client = discord.Client()
@client.event # Use these decorator to register an event.
async def on_ready(): # on_ready() event : when the bot has finised logging in and setting things up
    await client.change_presence(status=discord.Status.online, activity=discord.Game("Type !help or !도움말 for help"))
    print("New log in as {0.user}".format(client))

@client.event
async def on_message(message): # on_message() event : when the bot has recieved a message
    #To user who sent message
    # await message.author.send(msg)
    print(message.content)
    if message.author == client.user:
        return

    '''
    #You can get id and secret key with registering in naver
    client_id = ""
    client_secret = ""

    #Text to translate
    entData = quote("")

    dataParmas = "source=en&target=id&text=" + entData
    baseurl = "https://openapi.naver.com/v1/papago/n2mt"

    #Make a Request Instance
    request = Request(baseurl)

    #add header to packet
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urlopen(request,data=dataParmas.encode("utf-8"))

    responsedCode = response.getcode()
    if(responsedCode==200):
        response_body = response.read()
        #response_body -> byte string : decode to utf-8
        api_callResult = response_body.decode('utf-8')

        #JSON Type data will be printed. So need to make it back to type JSON(like dictionary)
        stringConvertJSON = api_callResult.replace("'","\"")
        api_callResult = json.loads(stringConvertJSON)
        translatedText = api_callResult['message']['result']["translatedText"]
        print(translatedText)
    else:
        print("Error Code : " + responsedCode)
    '''

    if message.content.startswith("!한영번역"):
        baseurl = "https://openapi.naver.com/v1/papago/n2mt"
        #띄어쓰기 : split처리후 [1:]을 for문으로 붙인다.
        trsText = message.content.split(" ")
        try:
            if len(trsText) == 1:
                await message.channel.send("단어 혹은 문장이 입력되지 않았어요. 다시한번 확인해주세요.")
            else:
                trsText = trsText[1:]
                combineword = ""
                for word in trsText:
                    combineword += " " + word
                # if entered value is sentence, assemble again and strip blank at both side
                savedCombineword = combineword.strip()
                combineword = quote(savedCombineword)
                print(combineword)
                # Make Query String.
                dataParmas = "source=ko&target=en&text=" + combineword
                # Make a Request Instance
                request = Request(baseurl)
                # add header to packet
                request.add_header("X-Naver-Client-Id", client_id)
                request.add_header("X-Naver-Client-Secret", client_secret)
                response = urlopen(request, data=dataParmas.encode("utf-8"))

                responsedCode = response.getcode()
                if (responsedCode == 200):
                    response_body = response.read()
                    # response_body -> byte string : decode to utf-8
                    api_callResult = response_body.decode('utf-8')
                    # JSON data will be printed as string type. So need to make it back to type JSON(like dictionary)
                    api_callResult = json.loads(api_callResult)
                    # Final Result
                    translatedText = api_callResult['message']['result']["translatedText"]
                    embed = discord.Embed(title="Translate | Korean -> English", description="", color=0x5CD1E5)
                    embed.add_field(name="Korean to translate", value=savedCombineword, inline=False)
                    embed.add_field(name="Translated English", value=translatedText, inline=False)
                    embed.set_thumbnail(url="https://papago.naver.com/static/img/papago_og.png")
                    embed.set_footer(text="Service provided by Hoplin. API provided by Naver Open API",
                                     icon_url='https://avatars2.githubusercontent.com/u/45956041?s=460&u=1caf3b112111cbd9849a2b95a88c3a8f3a15ecfa&v=4')
                    await message.channel.send("Translate complete", embed=embed)
                else:
                    await message.channel.send("Error Code : " + responsedCode)
        except HTTPError as e:
            await message.channel.send("Translate Failed. HTTPError Occured.")


    if message.content.startswith("!영한번역"):
        baseurl = "https://openapi.naver.com/v1/papago/n2mt"
        # 띄어쓰기 : split처리후 [1:]을 for문으로 붙인다.
        trsText = message.content.split(" ")
        try:
            if len(trsText) == 1:
                await message.channel.send("단어 혹은 문장이 입력되지 않았어요. 다시한번 확인해주세요.")
            else:
                trsText = trsText[1:]
                combineword = ""
                for word in trsText:
                    combineword += " " + word
                # if entered value is sentence, assemble again and strip blank at both side
                savedCombineword = combineword.strip()
                combineword = quote(savedCombineword)
                # Make Query String.
                dataParmas = "source=en&target=ko&text=" + combineword
                # Make a Request Instance
                request = Request(baseurl)
                # add header to packet
                request.add_header("X-Naver-Client-Id", client_id)
                request.add_header("X-Naver-Client-Secret", client_secret)
                response = urlopen(request, data=dataParmas.encode("utf-8"))

                responsedCode = response.getcode()
                if (responsedCode == 200):
                    response_body = response.read()
                    # response_body -> byte string : decode to utf-8
                    api_callResult = response_body.decode('utf-8')

                    # JSON data will be printed as string type. So need to make it back to type JSON(like dictionary)
                    api_callResult = json.loads(api_callResult)
                    # Final Result
                    translatedText = api_callResult['message']['result']["translatedText"]
                    embed = discord.Embed(title="Translate | English -> Korean", description="", color=0x5CD1E5)
                    embed.add_field(name="English to translate", value=savedCombineword, inline=False)
                    embed.add_field(name="Translated Korean", value=translatedText, inline=False)
                    embed.set_thumbnail(url="https://papago.naver.com/static/img/papago_og.png")
                    embed.set_footer(text="Service provided by Hoplin. API provided by Naver Open API",
                                     icon_url='https://avatars2.githubusercontent.com/u/45956041?s=460&u=1caf3b112111cbd9849a2b95a88c3a8f3a15ecfa&v=4')
                    await message.channel.send("Translate complete", embed=embed)
                else:
                    await message.channel.send("Error Code : " + responsedCode)
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
                trsText = trsText[1:]
                combineword = ""
                for word in trsText:
                    combineword += " " + word
                # if entered value is sentence, assemble again and strip blank at both side
                savedCombineword = combineword.strip()
                combineword = quote(savedCombineword)
                # Make Query String.
                dataParmas = "source=ko&target=ja&text=" + combineword
                # Make a Request Instance
                request = Request(baseurl)
                # add header to packet
                request.add_header("X-Naver-Client-Id", client_id)
                request.add_header("X-Naver-Client-Secret", client_secret)
                response = urlopen(request, data=dataParmas.encode("utf-8"))

                responsedCode = response.getcode()
                if (responsedCode == 200):
                    response_body = response.read()
                    # response_body -> byte string : decode to utf-8
                    api_callResult = response_body.decode('utf-8')

                    # JSON data will be printed as string type. So need to make it back to type JSON(like dictionary)
                    api_callResult = json.loads(api_callResult)
                    # Final Result
                    translatedText = api_callResult['message']['result']["translatedText"]
                    embed = discord.Embed(title="Translate | Korean -> Japanese", description="", color=0x5CD1E5)
                    embed.add_field(name="Korean to translate", value=savedCombineword, inline=False)
                    embed.add_field(name="Translated Japanese", value=translatedText, inline=False)
                    embed.set_thumbnail(url="https://papago.naver.com/static/img/papago_og.png")
                    embed.set_footer(text="Service provided by Hoplin. API provided by Naver Open API",
                                     icon_url='https://avatars2.githubusercontent.com/u/45956041?s=460&u=1caf3b112111cbd9849a2b95a88c3a8f3a15ecfa&v=4')
                    await message.channel.send("Translate complete", embed=embed)
                else:
                    await message.channel.send("Error Code : " + responsedCode)
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
                trsText = trsText[1:]
                combineword = ""
                for word in trsText:
                    combineword += " " + word
                # if entered value is sentence, assemble again and strip blank at both side
                savedCombineword = combineword.strip()
                combineword = quote(savedCombineword)
                # Make Query String.
                dataParmas = "source=ja&target=ko&text=" + combineword
                # Make a Request Instance
                request = Request(baseurl)
                # add header to packet
                request.add_header("X-Naver-Client-Id", client_id)
                request.add_header("X-Naver-Client-Secret", client_secret)
                response = urlopen(request, data=dataParmas.encode("utf-8"))

                responsedCode = response.getcode()
                if (responsedCode == 200):
                    response_body = response.read()
                    # response_body -> byte string : decode to utf-8
                    api_callResult = response_body.decode('utf-8')

                    # JSON data will be printed as string type. So need to make it back to type JSON(like dictionary)
                    api_callResult = json.loads(api_callResult)
                    # Final Result
                    translatedText = api_callResult['message']['result']["translatedText"]
                    embed = discord.Embed(title="Translate | Japanese -> Korean", description="", color=0x5CD1E5)
                    embed.add_field(name="Japanese to translate", value=savedCombineword, inline=False)
                    embed.add_field(name="Translated Korean", value=translatedText, inline=False)
                    embed.set_thumbnail(url="https://papago.naver.com/static/img/papago_og.png")
                    embed.set_footer(text="Service provided by Hoplin. API provided by Naver Open API",
                                     icon_url='https://avatars2.githubusercontent.com/u/45956041?s=460&u=1caf3b112111cbd9849a2b95a88c3a8f3a15ecfa&v=4')
                    await message.channel.send("Translate complete", embed=embed)
                else:
                    await message.channel.send("Error Code : " + responsedCode)
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
                trsText = trsText[1:]
                combineword = ""
                for word in trsText:
                    combineword += " " + word
                # if entered value is sentence, assemble again and strip blank at both side
                savedCombineword = combineword.strip()
                combineword = quote(savedCombineword)
                # Make Query String.

                #Simplified Chinese
                dataParmas = "source=ko&target=zh-CN&text=" + combineword

                # Make a Request Instance
                request = Request(baseurl)
                # add header to packet
                request.add_header("X-Naver-Client-Id", client_id)
                request.add_header("X-Naver-Client-Secret", client_secret)
                response = urlopen(request, data=dataParmas.encode("utf-8"))

                responsedCode = response.getcode()
                if (responsedCode == 200):
                    response_body = response.read()
                    # response_body -> byte string : decode to utf-8
                    api_callResult = response_body.decode('utf-8')
                    # JSON data will be printed as string type. So need to make it back to type JSON(like dictionary)
                    api_callResult = json.loads(api_callResult)
                    # Final Result
                    translatedText = api_callResult['message']['result']["translatedText"]
                    embed = discord.Embed(title="Translate | Korean -> Chinese(Simplified Chinese)", description="", color=0x5CD1E5)
                    embed.add_field(name="Korean to translate", value=savedCombineword, inline=False)
                    embed.add_field(name="Translated Chinese(Simplified)", value=translatedText, inline=False)
                    embed.set_thumbnail(url="https://papago.naver.com/static/img/papago_og.png")
                    embed.set_footer(text="Service provided by Hoplin. API provided by Naver Open API",
                                     icon_url='https://avatars2.githubusercontent.com/u/45956041?s=460&u=1caf3b112111cbd9849a2b95a88c3a8f3a15ecfa&v=4')
                    await message.channel.send("Translate complete", embed=embed)
                else:
                    await message.channel.send("Error Code : " + responsedCode)
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
                trsText = trsText[1:]
                combineword = ""
                for word in trsText:
                    combineword += " " + word
                # if entered value is sentence, assemble again and strip blank at both side
                savedCombineword = combineword.strip()
                combineword = quote(savedCombineword)
                # Make Query String.
                # Simplified Chinese
                dataParmas = "source=zh-CN&target=ko&text=" + combineword


                # Make a Request Instance
                request = Request(baseurl)
                # add header to packet
                request.add_header("X-Naver-Client-Id", client_id)
                request.add_header("X-Naver-Client-Secret", client_secret)
                response = urlopen(request, data=dataParmas.encode("utf-8"))

                responsedCode = response.getcode()
                if (responsedCode == 200):
                    response_body = response.read()
                    # response_body -> byte string : decode to utf-8
                    api_callResult = response_body.decode('utf-8')
                    # JSON data will be printed as string type. So need to make it back to type JSON(like dictionary)
                    api_callResult = json.loads(api_callResult)
                    # Final Result
                    translatedText = api_callResult['message']['result']["translatedText"]
                    embed = discord.Embed(title="Translate | Chinese -> Korean", description="", color=0x5CD1E5)
                    embed.add_field(name="Chinese to translate", value=savedCombineword, inline=False)
                    embed.add_field(name="Translated Korean", value=translatedText, inline=False)
                    embed.set_thumbnail(url="https://papago.naver.com/static/img/papago_og.png")
                    embed.set_footer(text="Service provided by Hoplin. API provided by Naver Open API",
                                     icon_url='https://avatars2.githubusercontent.com/u/45956041?s=460&u=1caf3b112111cbd9849a2b95a88c3a8f3a15ecfa&v=4')
                    await message.channel.send("Translate complete", embed=embed)
                else:
                    await message.channel.send("Error Code : " + responsedCode)
        except HTTPError as e:
            await message.channel.send("Translate Failed. HTTPError Occured.")
client.run(token)


