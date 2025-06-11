import os
import sys

import random

"""
Python 과제 3
- 바위 가위 보 게임 제작하기
- 사용자로부터 바위/가위/보 선택지를 입력
- 컴퓨터는 바위/가위/보 중 랜덤하게 선택
- 사용자가 승리했거나 비겼을 경우 게임 다시 진행
- 사용자가 패배했을 경우 전적 출력 후 게임 종료
- 사용자의 선택과 컴퓨터의 선택을 입력 받아 승패 여부를 반환하는 함수 구현

Ex)
선택 (1. 바위, 2. 가위, 3. 보) : 2
결과 : 승리 (나 - 가위, 컴퓨터 - 보)

선택 (1. 바위, 2. 가위, 3. 보) : 1
결과 : 무승부 (나 - 바위, 컴퓨터 - 바위)

선택 (1. 바위, 2. 가위, 3. 보) : 3
결과 : 패배 (나 - 보, 컴퓨터 - 가위)

전적 : 1 승 1 무 1 패
프로그램을 종료합니다.
"""

# 결과
RESULT_WIN = 1
RESULT_LOSE = 2
RESULT_DRAW = 3


# Practice 3
def start(args):
	nCount_Win = 0
	nCount_Draw = 0
	
	oStrings_Select = [
		"", "바위", "가위", "보"
	]
	
	oStrings_Result = [
		"", "승리", "패배", "무승부"
	]
	
	while True:
		nSelect = int(input("선택 (1. 바위, 2. 가위, 3. 보) : "))
		nSelect_Computer = random.randrange(1, 4)
		
		nResult = getResult(nSelect, nSelect_Computer)
		
		nCount_Win += 1 if nResult == RESULT_WIN else 0
		nCount_Draw += 1 if nResult == RESULT_DRAW else 0
		
		oStr_Select = oStrings_Select[nSelect]
		oStr_ComputerSelect = oStrings_Select[nSelect_Computer]
		
		oStr_Result = oStrings_Result[nResult]
		print(f"결과 : {oStr_Result} (나 - {oStr_Select}, 컴퓨터 - {oStr_ComputerSelect})\n")
		
		# 패배했을 경우
		if nResult == RESULT_LOSE:
			break
	
	print(f"전적 : {nCount_Win} 승 {nCount_Draw} 무 1 패")
	print("프로그램을 종료합니다.")


# 결과를 반환한다
def getResult(a_nSelect, a_nSelect_Computer):
	# 비겼을 경우
	if a_nSelect == a_nSelect_Computer:
		return RESULT_DRAW
	
	nSelect_Next = (a_nSelect % 3) + 1
	return RESULT_WIN if nSelect_Next == a_nSelect_Computer else RESULT_LOSE
