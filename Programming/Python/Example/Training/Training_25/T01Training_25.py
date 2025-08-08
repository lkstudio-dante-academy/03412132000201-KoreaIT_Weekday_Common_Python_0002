import os
import sys

import re
import ssl
import time

from bs4 import BeautifulSoup
from urllib.request import urlopen, Request


# Training 25
def start(args):
	ssl.create_default_https_context = ssl._create_unverified_context
	
	oSetLinks = set()
	getLinks_WebPage("", 0, oSetLinks)
	
	with open("P_T01Training_25_01.txt", "wt") as oWStream:
		for oLink in oSetLinks:
			oWStream.write(f"https://namu.wiki{oLink}\n")
	
	
# 웹 페이지 링크를 반환한다
def getLinks_WebPage(a_oURL, a_nDepth, a_oOutSetLinks):
	# 웹 페이지 탐색이 불가능 할 경우
	if a_nDepth >= 3:
		return
	
	time.sleep(0.25)
	print(f"getLinks_WebPage : {a_oURL}")
	
	try:
		oHeaders = {
			"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"
		}
		
		oPage = urlopen(Request(f"https://namu.wiki{a_oURL}", headers = oHeaders))
		oBSoup = BeautifulSoup(oPage.read(), "html.parser")
		
		oCompile = re.compile(r"^(/w/)")
		oListTags = oBSoup.findAll("a", { "href" : oCompile })
		
		for oTag in oListTags:
			# 웹 페이지 탐색이 불가능 할 경우
			if oTag.attrs["href"] in a_oOutSetLinks:
				continue
				
			a_oOutSetLinks.add(oTag.attrs["href"])
			getLinks_WebPage(oTag.attrs["href"], a_nDepth + 1, a_oOutSetLinks)
	
	except Exception as oException:
		print(f"{oException}")
		