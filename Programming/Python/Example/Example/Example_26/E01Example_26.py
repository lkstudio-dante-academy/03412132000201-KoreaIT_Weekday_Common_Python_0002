import os
import sys

import re
import ssl

from bs4 import BeautifulSoup
from urllib.request import urlopen

"""
정규 표현식 (Regular Expression) 란?
- 특정 규칙을 지니고 있는 문자열을 탐색하기 위한 수단을 의미한다. (+ 즉, 정규 표현식을 활용하면 문자열 내에
특정 패턴을 지니고 있는 문자열을 탐색하는 것이 가능하다.)

Python 은 re 모듈을 지원하며 해당 묘듈을 통해 정규 표현식을 사용하는 것이 가능하다.

정규 표현식 주요 기호
- * : 바로 앞에 명시 된 문자 or 하위 표현식이 0 번 이상 존재
- + : 바로 앞에 명시 된 문자 or 하위 표현식이 1 번 이상 존재
- | : | 로 구분 된 문자 or 하위 표현식이 존재
- . : 아무 문자가 1 개 존재
- ^ : 바로 뒤에 명시 된 문자 or 하위 표현식이 가장 앞에 존재
- \\ : 특수 문자를 원래 의미대로 사용 (+ Ex. \\., \\|, \\ 등등...)
- $ : 바로 앞에 명시 된 문자 or 하위 표현식이 가장 마지막에 존재
- [] : 대괄호 안에 명시 된 문자 중 하나가 존재
- [^] : 대괄호 안에 명시 된 문자를 제외하고 존재
- {m,n} : 바로 앞에 명시 된 문자 or 하위 표현식이 m 번 이상, n 번 이하 존재
- () : 하위 표현식

정규 표현식 주요 문자 클래스
- \\d or \\D : [0-9] or [^0-9]							<- 숫자
- \\w or \\W : [a-zA-Z_] or [^a-zA-Z_]					<- 문자
- \\s or \\S : [ \r\n\f\t\v] or [^ \r\n\f\t\v]			<- 공백

정규 표현식 연습 사이트 URL
- https://regexr.com/
- https://regexper.com/
"""


# Example 26 (웹 크롤링 - 2)
def start(args):
	ssl._create_default_https_context = ssl._create_unverified_context
	
	oText = \
		"""
		RegExr was created by gskinner.com.
		Edit the Expression & Text to see matches. Roll over matches or the expression for details. PCRE & JavaScript flavors of RegEx are supported. Validate your expression with Tests mode.
		The side bar includes a Cheatsheet, full Reference, and Help. You can also Save & Share with the Community and view patterns you create or favorite in My Patterns.
		Explore results with the Tools below. Replace & List output custom results. Details lists capture groups. Explain describes your expression in plain English.
		"""
	
	oListResults = re.findall(r"Reg", oText)
	print("=====> 정규 표현식 <=====")
	
	for oResult in oListResults:
		print(oResult)
	
	oPage = urlopen("http://www.pythonscraping.com/pages/page3.html")
	oBSoup = BeautifulSoup(oPage.read(), "html.parser")
	
	"""
	아래와 같이 findAll 함수는 정규 표현식을 지원하기 때문에 정규 표현식을 사용해서 규칙을 지니는
	좀 더 복잡한 패턴의 정보를 탐색하는 것이 가능하다.
	
	compile 함수란?
	- 정규 표현식을 미리 분석해서 재사용 가능한 객체를 생성하는 역할을 수행한다. (+ 즉,
	compile 함수를 활용하면 동일한 정규 표현식을 재사용 함으로서 정규 표현식을 분석하는 시간을 줄이는 것이
	가능하다.)
	"""
	oCompile = re.compile(r"\.\./img/gifts/img.*\.jpg")
	oListTags = oBSoup.findAll("img", { "src" : oCompile })
	
	print("\n=====> 웹 크롤링 <=====")
	
	for oTag in oListTags:
		print(f"{oTag}")
		