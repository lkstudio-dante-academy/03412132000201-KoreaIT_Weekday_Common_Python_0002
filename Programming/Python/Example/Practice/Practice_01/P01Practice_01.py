import os
import sys

"""
Python 과제 1
- 구구단 출력하기
- 2 ~ 9 범위 내의 숫자 중 2 개를 입력 받는다
- 입력 받는 수가 범위를 벗어났을 경우 가이드 메세지 출력 후 프로그램 종료
- 범위 내의 수를 입력했을 경우 작은 수부터 큰 수까지 구구단 출력

Ex)
정수 2 개 입력 (2 ~ 9) : 4 2
=====> 2 단 <=====
2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
...이하 생략

=====> 3 단 <=====
3 * 1 = 3
3 * 2 = 6
3 * 3 = 9
...이하 생략

=====> 4 단 <=====
4 * 1 = 4
4 * 2 = 8
4 * 3 = 12
...이하 생략
"""


# Practice 1
def start(args):
	oTokens = input("정수 (2 개) 입력 (2 ~ 9) : ").split()
	
	nVal_Min = int(oTokens[0])
	nVal_Max = int(oTokens[1])
	
	# 보정이 필요 할 경우
	if nVal_Min > nVal_Max:
		nVal_Min, nVal_Max = nVal_Max, nVal_Min
	
	bIsValidA = nVal_Min >= 2 and nVal_Min <= 9
	bIsValidB = nVal_Max >= 2 and nVal_Max <= 9
	
	# 범위 내의 수를 입력했을 경우
	if bIsValidA and bIsValidB:
		for i in range(nVal_Min, nVal_Max + 1):
			print(f"=====> {i} 단 <=====")
			
			for j in range(1, 10):
				print(f"{i} * {j} = {i * j}")
			
			print()
	
	else:
		print("2 ~ 9 범위 내의 수를 입력하세요.")
