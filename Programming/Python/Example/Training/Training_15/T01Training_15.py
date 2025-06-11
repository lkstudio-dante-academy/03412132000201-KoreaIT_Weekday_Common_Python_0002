import os
import sys

import re
import ssl

from bs4 import BeautifulSoup
from urllib.request import urlopen

"""
Python 연습 문제 15
- 위키피디아 사이트 크롤링하기 (+ https://en.wikipedia.org/wiki/ + 검색어 조합)
- 검색어를 입력 받아 위키피디아 사이트를 크롤링한다
- 위키피디아 내부 페이지에 대한 링크를 크롤링한다 (+ 즉, /wiki/ 로 시작하는 링크)
- 크롤링 한 링크는 파일에 모두 기록한다
"""


# Training 15
def start(args):
	ssl._create_default_https_context = ssl._create_unverified_context
	oSearch = input("위키피디아 검색어 입력 : ")
	
	try:
		oPage = urlopen(f"https://en.wikipedia.org/wiki/{oSearch}")
		oBSoup = BeautifulSoup(oPage.read(), "html.parser")
		
		oCompile = re.compile(r"^(/wiki/)")
		oListTags = oBSoup.findAll("a", { "href" : oCompile })
		
		with open("P_T01Training_15_01.txt", "wt") as oWStream:
			oSetLinks = set()
			
			for oTag in oListTags:
				oLink = oTag.attrs["href"]
				oSetLinks.add(f"https://en.wikipedia.org{oLink}")
			
			for oLink in oSetLinks:
				oWStream.write(f"{oLink}\n")
	
	except:
		print(f"{oSearch} 검색어에 대한 페이지가 존재하지 않습니다.")
		