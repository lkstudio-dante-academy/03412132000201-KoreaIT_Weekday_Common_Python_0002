import os
import sys

"""
Python 연습 문제 2
- 구구단 출력하기
- 2 ~ 9 범위 내의 숫자를 입력 받는다
- 입력 받는 수가 범위를 벗어났을 경우 가이드 메세지 출력 후 프로그램 종료
- 범위 내의 수를 입력했을 경우 입력 한 단부터 9 단까지 구구단 출력
"""


# Training 2
def start(args):
	nVal = int(input("정수 입력 (2 ~ 9) : "))
	
	# 범위 내의 수를 입력했을 경우
	if nVal >= 2 and nVal <= 9:
		while nVal < 10:
			i = 1
			print(f"=====> {nVal} 단 <=====")
			
			# 1 ~ 9 까지 곱셈 결과 출력
			while i < 10:
				print(f"{nVal} * {i} = {nVal * i}")
				i += 1
			
			print()
			nVal += 1
	
	else:
		print("2 ~ 9 범위 내의 수를 입력하세요.")
