#Papago API Reference : https://developers.naver.com/docs/nmt/reference/

import os
import sys
import urllib.request
from urllib.request import urlopen,quote,Request
import json



'''
PapagoAPIBasicUsage.py 를 사용하실때에는 번역하실 문장을 quote안에 입력해 주시고 실행해 주시기 바랍니다.
'''

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
entData = quote("안녕하세요 디스코드 파파고 API를 이용한 자동 번역 봇입니다. 이것은 테스트 문장입니다.")

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

     #JSON Type data will be printed. So need to make it back to type JSON(like dictionary)
    api_callResult = json.loads(api_callResult)
    translatedText = api_callResult['message']['result']["translatedText"]
    print(translatedText)
else:
    print("Error Code : " + responsedCode)
