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
	
	oPage = urlopen(Request("https://namu.wiki", headers = oHeaders))
	oBSoup = BeautifulSoup(oPage.read(), "html.parser")
	
	oListTags = oBSoup.findAll("a")
	print("=====> 태그 <=====")
	
	for oTag in oListTags:
		print(oTag)
		