import os
import sys

from Training.Training_17.CFactory_Unit import CFactory_Unit

"""
Python 연습 문제 17
- 유닛 생산 시뮬레이션 제작하기
- 서로 다른 가격의 유닛이 존재한다
- 사용자로부터 메뉴를 입력 받아 유닛을 생산한다
- 단, 소지 금액이 부족 할 경우 유닛 생산 불가

Ex)
소지 금액 입력 : 1000

=====> 메뉴 <=====
1. 유닛 A 생산 (가격 : 250)
2. 유닛 B 생산 (가격 : 500)
3. 유닛 C 생산 (가격 : 750)
4. 생산 된 유닛 정보 출력
5. 종료

선택 (소지 금액 : 1000) : 1
유닛 A 을(를) 생산했습니다.

선택 (소지 금액 : 750) : 2
유닛 B 을(를) 생산했습니다.

선택 (소지 금액 : 250) : 4
유닛 A 를 {시간} 에 생산했습니다.
유닛 B 를 {시간} 에 생산했습니다.

선택 (소지 금액 : 250) : 5
프로그램을 종료합니다.
"""


# Training 17
def start(args):
	nAmount = int(input("소지 금액 입력 : "))
	oFactory = CFactory_Unit()
	
	oListUnits = []
	
	while True:
		printMenu(oFactory)
		nMenu = int(input(f"\n선택 (소지 금액 : {nAmount}) : "))
		
		# 종료 일 경우
		if nMenu == MENU_EXIT:
			break
			
		# 유닛 생산 일 경우
		if nMenu != MENU_SHOW_INFOS_ALL_UNIT:
			oClass_Unit = oFactory.getClass_Unit(nMenu - 1)
			
			# 금액 부족 할 경우
			if nAmount < oClass_Unit.PRICE:
				print("금액이 부족합니다.\n")
				continue
				
			oUnit = oFactory.createUnit(nMenu - 1)
			oListUnits.append(oUnit)
			
			nAmount -= oClass_Unit.PRICE
			print(f"{oClass_Unit.NAME} 을(를) 생산했습니다.")
		
		else:
			print("=====> 생산 된 유닛 정보 <=====")
			
			for oUnit in oListUnits:
				oName_Unit = type(oUnit).NAME
				oTime_Unit = oUnit.m_oTime
				
				print(f"{oName_Unit} 을(를) {oTime_Unit} 에 생산했습니다.")
		
		print()
		
	print("프로그램을 종료합니다.")
	

MENU_SHOW_INFOS_ALL_UNIT = 0
MENU_EXIT = 0

# 메뉴를 출력한다
def printMenu(a_oFactory):
	print("=====> 메뉴 <=====")
	
	for i in range(0, a_oFactory.getNumKinds_Unit()):
		nMenu = i + 1
		oName_Unit = a_oFactory.getClass_Unit(i).NAME
		nPrice_Unit = a_oFactory.getClass_Unit(i).PRICE
		
		print(f"{nMenu}. {oName_Unit} 생산 (가격 : {nPrice_Unit})")
	
	global MENU_SHOW_INFOS_ALL_UNIT
	global MENU_EXIT
	
	MENU_SHOW_INFOS_ALL_UNIT = a_oFactory.getNumKinds_Unit() + 1
	MENU_EXIT = a_oFactory.getNumKinds_Unit() + 2
	
	print(f"{MENU_SHOW_INFOS_ALL_UNIT}. 생산 된 유닛 정보 출력")
	print(f"{MENU_EXIT}. 종료")
	