import os
import sys

import random

"""
Python 과제 2
- 숫자 야구 게임 제작하기
- 1 ~ 9 범위의 수 중 정답에 해당하는 중복되지 않는 수 4 개 추출
- 사용자로부터 4 개의 수를 입력 받아 결과 판정
- 사용자가 입력 한 숫자가 정답에 포함되어있고 위치가 일치 할 경우 스트라이크 판정
- 사용자가 입력 한 숫자가 정답에 포함되어있지만 위치가 다를 경우 볼 판정
- 4 스트라이크가 되면 게임 종료

Ex)
정답 : 1 5 2 9

정수 (4 개) 입력 : 1 2 9 5
결과 : 2 Strike, 2 Ball

정수 (4 개) 입력 : 1 5 2 9
결과 : 4 Strike, 0 Ball

프로그램을 종료합니다.
"""


# Practice 2
def start(args):
	oAnswer = []
	
	while len(oAnswer) < 4:
		nVal = random.randrange(1, 10)
		
		# 숫자가 존재 할 경우
		if nVal in oAnswer:
			continue
		
		oAnswer.append(nVal)
	
	print("정답 : ")
	
	for nVal in oAnswer:
		print(f"{nVal}, ", end = "")
	
	print("\n")
	
	while True:
		oTokens = input("정수 (4 개) 입력 : ").split()
		
		nNumStrikes = 0
		nNumBalls = 0
		
		for i in range(0, len(oTokens)):
			nVal = int(oTokens[i])
			
			# 숫자가 정답에 없을 경우
			if nVal not in oAnswer:
				continue
			
			"""
			index 함수란?
			- 리스트가 관리하는 데이터의 인덱스 번호를 가져오는 역할을 수행하는 함수를 의미한다. (+ 즉,
			index 함수를 활용하면 데이터의 인덱스 번호를 손쉽게 가져오는 것이 가능하다.)
			
			단, 리스트에 존재하지 않는 데이터를 index 함수의 입력으로 전달 할 경우 내부적으로 예외가
			발생하기 때문에 주의가 필요하다.
			"""
			nIdx = oAnswer.index(nVal)
			
			# 위치가 동일 할 경우
			if i == nIdx:
				nNumStrikes += 1
			
			else:
				nNumBalls += 1
		
		print(f"결과 : {nNumStrikes} Strike, {nNumBalls} Ball\n")
		
		# 4 스트라이크 일 경우
		if nNumStrikes >= len(oAnswer):
			break
	
	print("프로그램을 종료합니다.")
