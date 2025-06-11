import os
import sys

import re
import ssl
import time

from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

"""
Python 연습 문제 17
- 나무위키 크롤링하기 (+ https://namu.wiki/)
- 나무위키 메인 사이트부터 모든 링크를 타고 들어가면서 크롤링한다
- 단, 내부 링크만 타고 들어간다 (+ 즉, /w/ 로 시작하는 링크)
- 링크의 깊이가 너무 깊어질 경우를 고려해서 3 깊이까지만 탐색 시도
- 크롤링 된 링크는 모두 파일에 기록한다
"""


# Training 17
def start(args):
	ssl._create_default_https_context = ssl._create_unverified_context
	
	oSetLinks = set()
	getLinks_WebPage("", 0, oSetLinks)
	
	with open("P_T01Training_17_01.txt", "wt", encoding = "utf8") as oWStream:
		for oLink in oSetLinks:
			oLink_URL = f"https://namu.wiki{oLink}\n"
			oWStream.write(oLink_URL)


# 링크를 반환한다
def getLinks_WebPage(a_oURL, a_nDepth, a_oOutSetLinks):
	# 페이지 탐색이 불가능 할 경우
	if a_nDepth >= 3:
		return
	
	time.sleep(0.25)
	print(f"getLinks_WebPage : {a_oURL}")
	
	try:
		oHeaders = {
			"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"
		}
		
		oURL = f"https://namu.wiki{a_oURL}"
		oPage = urlopen(Request(oURL, headers = oHeaders))
		oBSoup = BeautifulSoup(oPage.read(), "html.parser")
		
		oCompile = re.compile(r"^(/w/)")
		oListTags = oBSoup.findAll("a", { "href" : oCompile })
		
		for oTag in oListTags:
			# 페이지 탐색이 불가능 할 경우
			if oTag.attrs["href"] in a_oOutSetLinks:
				continue
				
			a_oOutSetLinks.add(oTag.attrs["href"])
			getLinks_WebPage(oTag.attrs["href"], a_nDepth + 1, a_oOutSetLinks)
	
	except:
		print(f"getLinks_WebPage Exception : {a_oURL}")
		