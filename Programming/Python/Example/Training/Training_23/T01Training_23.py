import os
import sys

import re
import ssl

from bs4 import BeautifulSoup
from urllib.request import urlopen

"""
Python 연습 문제 23
- 위키피디아 사이트 크롤링하기 (+ https://en.wikipedia.org/wiki/ + 검색어)
- 사용자로부터 검색어를 입력받아 해당 검색어를 기반으로 위키피디아 사이트를
크롤링한다
- 크롤링 할 내용은 위키피디아 웹 페이지의 링크 태그 정보이다 (+ 즉, a 태크)
- 단, 위키피디아 내부 링크 태그만 크롤링한다 (+ 즉, /wiki/ 로 시작하는 링크)
- 크롤링한 링크는 모두 파일에 기록한다
"""


# Training 23
def start(args):
	ssl._create_default_https_context = ssl._create_unverified_context
	oSearch = input("위키피디아 검색어 입력 : ")
	
	try:
		oPage = urlopen(f"https://en.wikipedia.org/wiki/{oSearch}")
		oBSoup = BeautifulSoup(oPage.read(), "html.parser")
		
		oCompile = re.compile(r"^(/wiki/)")
		oListTags = oBSoup.findAll("a", { "href" : oCompile })
		
		with open("P_T01Training_23_01.txt", "wt") as oWStream:
			oSetLinks = set()
			
			for oTag in oListTags:
				oLink = oTag.attrs["href"]
				oSetLinks.add(oLink)
				
			for oLink in oSetLinks:
				oWStream.write(f"{oLink}\n")
	
	except Exception as oException:
		print(f"{oException}")
