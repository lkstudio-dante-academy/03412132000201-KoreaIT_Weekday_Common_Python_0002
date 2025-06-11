import os
import sys

import re

"""
Python 연습 문제 16
- 이메일 형식 유효 여부 검사하기
- 이메일을 입력 받아 올바른 형식인지 검사한다 (+ 단, 정규 표현식 사용)
"""


# Training 16
def start(args):
	oEmail = input("이메일 입력 : ")
	print(isValid_Email(oEmail))
	
	
# 이메일 유효 여부를 검사한다
def isValid_Email(a_oEmail):
	return bool(re.match(r"^([\d\w.+-]+)@[a-z]+\.([a-z]+)$", a_oEmail))
	