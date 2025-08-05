import os
import sys

import re
import ssl

from bs4 import BeautifulSoup
from urllib.request import urlopen

"""
웹 크롤링 (Web Crawling) 이란?
- 웹 사이트에 존재하는 데이터를 자동으로 수집하는 기술을 의미한다. (+ 즉, 웹 크롤링을 활용하면
인터넷 상에 존재하는 대량의 데이터를 수집해서 활용하는 것이 가능하다.)

웹 사이트는 일반적으로 HTML (Hyper Text Markup Language) 과 CSS (Cascade Style Sheet) 와
JS (Java Script) 명령문으로 구성되어있으며 해당 파일을 브라우저 (+ Ex. 크롬, MS 엣지 등등...) 에서
내려 받아 화면 상에 출력 된다. (+ 즉, 브라우저 내부에는 HTML 과 같은 명령문을 해석하기 위한 파서 등이
내장 되어있다는 것을 알 수 있다.)

HTML + CSS + Java Script 로 구성 된 파일은 주로 웹 페이지라고 불리며 클라이언트에서 간단하게
열어 볼 수 있다는 장점이 존재한다. (+ 즉, 웹 페이지에 존재하는 다양한 정보를 손쉽게 열람하는 것이 가능하다.)

단, 웹 페이지는 정보 뿐만 아니라 HTML 등과 같은 다양한 명령문이 혼재되어있기 때문에 불필요한 정보를 필터링해서
원하는 정보만을 가져오는 라이브러리를 사용하는 것이 일반적이다.

Python 에서는 BeautifulSoup 라 불리는 모듈이 존재하며 해당 모듈을 활용하면 좀 더 수월하게 웹 페이지로부터
원하는 정보를 가져오는 것이 가능하다.

웹 크롤링 (Web Crawling) vs 웹 스크래핑 (Web Scraping)
- 웹 크롤링은 웹 페이지들을 자동으로 탐색하면서 구조를 파악하는 것을 의미한다. (+ 즉, 구조를 분석하는데
중점을 둔다는 것을 알 수 있다.)

일반적으로 웹 서버에 존재하는 웹 페이지는 내부적으로 다른 파일을 참조해가 위한 링크가 걸려있으며
이러한 링크들을 통해 웹 사이트가 형성 된다. (+ 즉, 하나의 화면을 구성하기 위해 여러 웹 페이지가 사용 된다는
것을 알 수 있다.)

따라서 웹 크롤링은 이러한 참조를 재귀적으로 탐색하면서 웹 사이트의 전체 구조를 파악하는 것이 주 된 목적이다.

반면, 웹 스크래핑은 웹 페이지에서 원하는 정보 (데이터) 를 추출하는 것을 의미한다. (+ 즉, 실질적으로 정보를
탐색한다는 것을 의미한다.)

따라서 특정 웹 사이트로부터 원하는 정보를 추출하는 것은 웹 크롤링 + 웹 스크래핑을 같이 수행해야 비로서 원하는
결과를 얻을 수 있다는 것을 알 수 있다.

DOM (Document Object Model) 이란?
- HTML 문서 내부에 존재하는 태그를 계층적인 구조로 표현 한 것을 의미한다. (+ 즉,
DOM 은 트리 구조라는 것을 알 수 있다.)

DOM 은 일반적으로 자바 스크립트에서 HTML 문서를 동적으로 제어하기 위해서 사용 된다. (+ 즉, DOM 을 활용하면
동적으로 동작하는 웹 페이지를 제작하는 것이 가능하다.)
"""

# Example 25 (웹 크롤링 - 1)
def start(args):
	"""
	SSL (Security Socket Layer) 이란?
	- 웹 브라우저와 웹 서버 간에 주고 받는 데이터를 암호화하는 프로토콜을 의미한다. (+ 즉,
	SSL 은 보안을 위한 프로토콜이라는 것을 알 수 있다.)
	
	현재는 TLS (Transport Layer Security) 로 대체 되었지만 관행적으로 계속 사용되고 있다. (+ 즉,
	현재 SSL 이라고 지칭하는 것은 TLS 라는 것을 의미한다.)
	"""
	ssl._create_default_https_context = ssl._create_unverified_context
	
	"""
	urlopen 함수란?
	- 웹 서버에 접속해서 파일을 읽어오는 역할을 수행하는 함수를 의미한다. (+ 즉, urlopen 함수를 활용하면
	간단하게 웹 페이지를 가져와서 제어하는 것이 가능하다.)
	
	urlopen 함수는 웹 페이지 뿐만 아니라 이미지 등과 같은 파일도 읽어들이는 것이 가능하다. (+ 즉, 범용성이
	뛰어나다는 것을 알 수 있다.)
	"""
	oPage = urlopen("http://www.pythonscraping.com/pages/page3.html")
	
	"""
	html.parser 란?
	- Python 에 내장 된 HTML 파일을 해석하기 위한 해석기를 의미한다. (+ 즉, BeautifulSoup 는
	HTML 파일을 해석하기 위한 해석기를 입력으로 전달 받음으로서 HTML 파일의 구조를
	파악 한다는 것을 알 수 있다.)
	"""
	oBSoup = BeautifulSoup(oPage.read(), "html.parser")
	
	print("=====> 제목 <=====")
	
	"""
	아래와 같이 BeautifulSoup 는 웹 페이지 구조를 분석해서 계층적인 형태로 태그를 관리하기 때문에
	. (멤버 지정 연산자) 를 통해 하위에 존재하는 태그에 접근하는 것이 가능하다.
	
	단, 동일한 계층에 동일한 태그가 여러 개 존재 할 경우 가장 앞에 있는 태그에만 접근하기 때문에
	. (멤버 지정 연산자) 를 통한 접근 방식은 많은 제약이 있다는 것을 알 수 있다.
	"""
	print(f"{oBSoup.body.h1}")
	
	"""
	findAll 함수란?
	- 웹 페이지에 존재하는 모든 태그를 탐색하는 역할을 수행하는 함수를 의미한다. (+ 즉,
	findAll 함수를 활용하면 HTML 파일 내부에 존재하는 특정 태그를 모두 가져오는 것이 가능하다.)
	
	HTML 태그는 속성 (Attribute) 이라는 것이 존재하며 findAll 함수는 태그 뿐만 아니라 속성을 비교해서
	원하는 태그만을 가져오는 기능도 제공한다.
	
	Ex)
	<div id = "ID_01">
	<div id = "ID_02">
	
	oListElements = oBSoup.findAll("div", { "id" : "ID_01" })
	
	위와 같이 탐색 할 태그와 함께 속성을 딕셔너리 형태로 findAll 함수의 입력으로 전달하면 태그와 속성을
	모두 비교해서 일치하는 태그를 반환한다는 것을 알 수 있다.
	"""
	oListTagsA = oBSoup.findAll("img", { "src" : "../img/gifts/logo.jpg" })
	
	print("\n=====> 태그 - A <=====")
	
	for oTag in oListTagsA:
		print(f"{oTag}")
	
	"""
	아래와 같이 함수를 활용하면 태그와 속성을 직접 탐색하는 것도 가능하다. (+ 즉,
	태그 탐색에 대한 조건이 복잡 할 경우 직접 태그를 검사하는 것도 하나의 방법이라는 것을 의미한다.)
	"""
	oListTagsB = oBSoup.findAll(compareTag)
	
	print("\n=====> 태그 - B <=====")
	
	for oTag in oListTagsB:
		print(f"{oTag}")


# 태그를 비교한다
def compareTag(a_oTag):
	# 이미지 태그가 아닐 경우
	if a_oTag.name != "img":
		return False
	
	# src 속성이 없을 경우
	if "src" not in a_oTag.attrs:
		return False
	
	return re.match(r"\.\./img/gifts/img.*\.jpg", a_oTag.attrs["src"])
