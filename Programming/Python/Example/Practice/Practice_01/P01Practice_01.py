import os
import sys

"""
Python 과제 1
- 논리 연산자를 사용하지 않고 동일한 결과 출력하기
- 논리 and 연산자와 논리 or 연산자를 사용하지 않고 동일한 결과 출력하기

Ex)
정수 (2 개) 입력 : 10 0

=====> 결과 <=====
10 and 0 = False
10 or 0 = True
"""


# Practice 1
def start(args):
	oTokens = input("정수 (2 개) 입력 : ").split()
	
	nValA = int(oTokens[0])
	nValB = int(oTokens[1])
	
	bIsTrueA = nValA != 0
	bIsTrueB = nValB != 0
	
	print("=====> 결과 <=====")
	print(f"{nValA} and {nValB} = {bool(bIsTrueA * bIsTrueB)}")
	print(f"{nValA} or {nValB} = {bool(bIsTrueA + bIsTrueB)}")
