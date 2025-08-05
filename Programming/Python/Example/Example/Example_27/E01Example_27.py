import os
import sys

import ssl

from bs4 import BeautifulSoup
from urllib.request import urlopen, Request


# Example 27 (웹 크롤링 - 3)
def start(args):
	ssl._create_default_https_context = ssl._create_unverified_context
	
	oHeaders = {
		"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"
	}
	
	"""
	아래와 같이 headers 매개 변수를 활용하면 헤더 정보를 설정하는 것이 가능하다. (+ 즉, 헤더를 설정함으로서
	봇을 차단하는 웹 사이트에 접속하는 것이 가능하다.)
	"""
	oPage = urlopen(Request("https://namu.wiki", headers = oHeaders))
	oBSoup = BeautifulSoup(oPage.read(), "html.parser")
	
	oListTags = oBSoup.findAll("a")
	print("=====> 태그 <=====")
	
	for oTag in oListTags:
		print(oTag)
		