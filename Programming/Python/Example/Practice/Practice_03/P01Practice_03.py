import os
import sys

"""
Python 과제 3
- 구구단 출력하기
- 2 ~ 9 범위 내의 숫자 중 2 개를 입력 받는다
- 입력 받는 수가 범위를 벗어 났을경우 가이드 메세지 출력 후 프로그램을 종료한다
- 범위 내의 수를 입력했을 경우 작은 수부터 큰 수까지 구구단 출력한다

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


# Practice 3
def start(args):
	oTokens = input("정수 2 개 입력 (2 ~ 9) : ").split()
	
	nValA = int(oTokens[0])
	nValB = int(oTokens[1])
	
	# 값 보정이 필요 할 경우
	if nValA > nValB:
		nValA, nValB = nValB, nValA
	
	for i in range(nValA, nValB + 1):
		print(f"=====> {i} 단 <=====")
		
		for j in range(1, 10):
			nVal = i * j
			print(f"{i} * {j} = {nVal}")
		
		print()
