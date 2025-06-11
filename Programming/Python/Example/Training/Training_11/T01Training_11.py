import os
import sys

import random
from Training.Training_11.CFactory import CFactory

"""
Python 연습 문제 11
- 유닛 생산 프로그램 제작하기
- 유닛은 3 종류 (마린, 파이어벳, 고스트)
- 유닛은 팩토리에서 생산
- 생산 된 유닛들은 공격 가능

Ex)
=====> 메뉴 <=====
1. 마린 생산
2. 파이어 벳 생산
3. 고스트 생산
4. 공격 지시
5. 종료

선택 : 1
마린을 생산했습니다.

선택 : 2
파이어 벳을 생산했습니다.

선택 : 4
총을 발사했습니다.
화염 방사기를 발사했습니다.
"""


# Training 11
def start(args):
	oFactory = CFactory()
	oListUnits = []
	
	while True:
		printMenu()
		nMenu = int(input("선택 : "))
		
		# 종료 일 경우
		if nMenu == MENU_EXIT:
			break
			
		bIsMenu_CreateA = nMenu == MENU_CREATE_MARINE
		bIsMenu_CreateB = nMenu == MENU_CREATE_FIREBET
		bIsMenu_CreateC = nMenu == MENU_CREATE_GHOST
		
		bIsMenu_Create = bIsMenu_CreateA or bIsMenu_CreateB or bIsMenu_CreateC
		
		# 유닛 생산 일 경우
		if bIsMenu_Create:
			oUnit = oFactory.createUnit(nMenu)
			oListUnits.append(oUnit)
			
		# 공격 지시 일 경우
		elif nMenu == MENU_ATTACK:
			nDistance_Target = random.randrange(3, 13)
			print(f"적과의 거리 : {nDistance_Target}\n")
			
			for oUnit in oListUnits:
				oUnit.attack(nDistance_Target)
				
		print()
		
	print("프로그램을 종료합니다.")
	
	
# 메뉴
MENU_CREATE_MARINE = 1
MENU_CREATE_FIREBET = 2
MENU_CREATE_GHOST = 3
MENU_ATTACK = 4
MENU_EXIT = 5


# 메뉴를 출력한다
def printMenu():
	print("=====> 메뉴 <=====")
	print("1. 마린 생산")
	print("2. 파이어 벳 생산")
	print("3. 고스트 생산")
	print("4. 공격 지시")
	print("5. 종료\n")
	