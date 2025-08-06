import os
import sys

import re

"""
Python 연습 문제 24
- 이메일 유효 여부 검사하기 (+ 정규 표현식 활용)
- 사용자로부터 이메일 주소를 입력 받은 후 해당 주소가 유효한지 검사한다
"""


# Training 24
def start(args):
	oEmail = input("이메일 입력 : ")
	bIsResult = isValid_Email(oEmail)
	
	print(f"유효 여부 검사 결과 : {bIsResult}")


# 이메일 유효 여부를 검사한다
def isValid_Email(a_oEmail):
	return bool(re.match(r"^([\w.]+)@[a-z]+\.([a-z]+)$", a_oEmail))
