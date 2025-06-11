import os
import sys

import sqlite3

"""
Python 연습 문제 12
- 연습 문제 5 번을 데이터베이스를 활용해서 구현하기
"""


# Training 12
def start(args):
	with sqlite3.connect("P_T01Training_12_01.db") as oConnection:
		oCursor = oConnection.cursor()
		oCursor.execute("CREATE TABLE IF NOT EXISTS MemberTable(Name TEXT PRIMARY KEY, PNumber TEXT)")
		
		while True:
			printMenu()
			nMenu = int(input("\n선택 : "))
			
			# 종료 메뉴 일 경우
			if nMenu == MENU_EXIT:
				break
			
			# 회원 추가 메뉴 일 경우
			if nMenu == MENU_ADD_MEMBER:
				handleOnMenu_AddMember(oCursor)
			
			# 회원 제거 메뉴 일 경우
			elif nMenu == MENU_REMOVE_MEMBER:
				handleOnMenu_RemoveMember(oCursor)
			
			# 회원 검색 메뉴 일 경우
			elif nMenu == MENU_SEARCH_MEMBER:
				handleOnMenu_SearchMember(oCursor)
			
			# 회원 정보 수정 메뉴 일 경우
			elif nMenu == MENU_UPDATE_MEMBER:
				handleOnMenu_UpdateMember(oCursor)
			
			# 모든 회원 출력 메뉴 일 경우
			elif nMenu == MENU_SHOW_ALL_MEMBERS:
				handleOnMenu_ShowAllMembers(oCursor)
			
			print()
			oConnection.commit()
	
	print("프로그램을 종료합니다.")


# 메뉴
MENU_ADD_MEMBER = 1
MENU_REMOVE_MEMBER = 2
MENU_SEARCH_MEMBER = 3
MENU_UPDATE_MEMBER = 4
MENU_SHOW_ALL_MEMBERS = 5
MENU_EXIT = 6


# 메뉴를 출력한다
def printMenu():
	print("=====> 메뉴 <=====")
	print("1. 회원 추가")
	print("2. 회원 제거")
	print("3. 회원 검색")
	print("4. 회원 정보 수정")
	print("5. 모든 회원 출력")
	print("6. 종료")


# 회원을 탐색한다
def findMember(a_oCursor, a_oName):
	oSQL_Query = "SELECT Name FROM MemberTable WHERE Name = ?"
	a_oCursor.execute(oSQL_Query, [a_oName])
	
	return len(a_oCursor.fetchall()) >= 1


# 회원 추가 메뉴를 처리한다
def handleOnMenu_AddMember(a_oCursor):
	oName = input("이름 입력 : ")
	oPNumber = input("전화 번호 입력 : ")
	
	bIsResult = findMember(a_oCursor, oName)
	
	# 존재하는 회원 일 경우
	if bIsResult:
		print(f"\n{oName} 은(는) 존재하는 회원입니다.")
	
	else:
		oSQL_Insert = "INSERT OR IGNORE INTO MemberTable(Name, PNumber) VALUES(?, ?)"
		a_oCursor.execute(oSQL_Insert, [oName, oPNumber])


# 회원 제거 메뉴를 처리한다
def handleOnMenu_RemoveMember(a_oCursor):
	oName = input("이름 입력 : ")
	bIsResult = findMember(a_oCursor, oName)
	
	# 회원이 존재 할 경우
	if bIsResult:
		oSQL_Query = "DELETE FROM MemberTable WHERE Name = ?"
		a_oCursor.execute(oSQL_Query, [oName])
		
		print(f"\n{oName} 을(를) 제거했습니다.")
	
	else:
		print(f"{oName} 은(는) 존재하지 않습니다.")


# 회원 검색 메뉴를 처리한다
def handleOnMenu_SearchMember(a_oCursor):
	oName = input("이름 입력 : ")
	bIsResult = findMember(a_oCursor, oName)
	
	# 회원이 존재 할 경우
	if bIsResult:
		oSQL_Query = "SELECT * FROM MemberTable WHERE Name = ?"
		a_oCursor.execute(oSQL_Query, [oName])
		
		oListResults = a_oCursor.fetchall()
		
		print("=====> 회원 정보 <=====")
		print(f"이름 : {oListResults[0][0]}")
		print(f"전화 번호 : {oListResults[0][1]}")
	
	else:
		print(f"{oName} 은(는) 존재하지 않습니다.")


# 회원 정보 수정 메뉴를 처리한다
def handleOnMenu_UpdateMember(a_oCursor):
	oName = input("이름 입력 : ")
	bIsResult = findMember(a_oCursor, oName)
	
	# 회원이 존재 할 경우
	if bIsResult:
		oPNumber = input("새로운 전화 번호 입력 : ")
		oSQL_Query = "UPDATE MemberTable SET PNumber = ? WHERE Name = ?"
		
		a_oCursor.execute(oSQL_Query, [oPNumber, oName])
		print(f"{oName} 정보를 수정했습니다.")
	
	else:
		print(f"{oName} 은(는) 존재하지 않습니다.")


# 모든 회원 출력 메뉴를 처리한다
def handleOnMenu_ShowAllMembers(a_oCursor):
	oSQL_Query = "SELECT * FROM MemberTable ORDER BY Name"
	oListResults = a_oCursor.execute(oSQL_Query)
	
	print("=====> 모든 회원 정보 <=====")
	
	for oResult in oListResults:
		print(f"이름 : {oResult[0]}")
		print(f"전화 번호 : {oResult[1]}\n")
		