import os
import sys

"""
Python 연습 문제 7
- 2 진수 출력하기
- 사용자로부터 10 진수에 해당하는 수를 입력 받아 2 진수로 변환
- 10 진수 -> 2 진수 변환에 재귀 호출 활용

Ex)
정수 입력 : 13
결과 : 1101
"""


# Training 7
def start(args):
	nVal = int(input("정수 입력 : "))
	oBinary = getBinary(nVal)
	
	print(f"결과 : {oBinary}")


# 2 진수를 반환한다
def getBinary(a_nVal):
	# 0 이하 일 경우
	if a_nVal <= 0:
		return ""
	
	oBinary = getBinary(a_nVal // 2)
	return oBinary + f"{a_nVal % 2}"
