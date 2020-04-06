#Papago API Reference : https://developers.naver.com/docs/nmt/reference/

import os
import sys
import urllib.request
from urllib.request import urlopen,quote,Request
import json


'''
조합 가능한 번역
ko : 한국어
en : 영어
zh-CN : 중국어 간체
zh-TW : 중국어 번체
es : 스페인어
fr : 프랑스어
vi : 베트남어
th : 태국어
id : 인도네시아어
ko<->en, ko<->zh-CN, ko<->zh-TW, ko<->es, ko<->fr, ko<->vi, ko<->th, ko<->id, en<->ja, en<->fr
'''


#You can get id and secret key with registering in naver
client_id = ""
client_secret = ""

#Text to translate
entData = quote()

dataParmas = "source=ko&target=en&text=" + entData
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
    api_callResult = json.loads(stringConvertJSON)
    translatedText = api_callResult['message']['result']["translatedText"]
else:
    print("Error Code : " + responsedCode)
