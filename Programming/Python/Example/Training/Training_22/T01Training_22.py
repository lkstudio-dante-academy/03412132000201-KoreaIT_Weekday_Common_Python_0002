import os
import sys

from Training.Training_19.CException_Duplicate import CException_Duplicate
from Training.Training_19.CException_Missing import CException_Missing

from Training.Training_22.CT01Table_Member import CTable_Member


# Training 22
def start(args):
	MENU_ADD_MEMBER = 1
	MENU_REMOVE_MEMBER = 2
	MENU_SEARCH_MEMBER = 3
	MENU_SHOW_MEMBERS_ALL = 4
	MENU_EXIT = 5
	
	oPath_DB = "P_T01Training_22_01.db"
	oTable = CTable_Member(oPath_DB)
	
	while True:
		printMenu()
		nMenu = int(input("\n선택 : "))
		
		# 종료 일 경우
		if nMenu == MENU_EXIT:
			break
		
		try:
			# 회원 추가 일 경우
			if nMenu == MENU_ADD_MEMBER:
				addMember(oTable)
			
			# 회원 제거 일 경우
			elif nMenu == MENU_REMOVE_MEMBER:
				removeMember(oTable)
			
			# 회원 검색 일 경우
			elif nMenu == MENU_SEARCH_MEMBER:
				searchMember(oTable)
			
			# 모든 회원 출력 일 경우
			elif nMenu == MENU_SHOW_MEMBERS_ALL:
				printMembers_All(oTable)
		
		except Exception as oException:
			print(f"{oException}")
		
		print()
	
	oTable.m_oCursor.close()
	oTable.m_oConnection.commit()
	
	print("프로그램을 종료합니다.")


# 메뉴를 출력한다
def printMenu():
	print("=====> 메뉴 <=====")
	print("1. 회원 추가")
	print("2. 회원 제거")
	print("3. 회원 검색")
	print("4. 모든 회원 출력")
	print("5. 종료")


# 회원을 추가한다
def addMember(a_oTable):
	oName = input("이름 입력 : ")
	oPNumber = input("전화 번호 입력 : ")
	
	oMember = a_oTable.getMember(oName)
	
	# 회원 정보가 존재 할 경우
	if oMember != None:
		raise CException_Duplicate(oName)
	
	a_oTable.addMember(oName, oPNumber)
	print(f"{oName} 을(를) 추가했습니다.")


# 회원을 제거한다
def removeMember(a_oTable):
	oName = input("이름 입력 : ")
	oMember = a_oTable.getMember(oName)
	
	# 회원이 없을 경우
	if oMember == None:
		raise CException_Missing(oName)
	
	a_oTable.removeMember(oName)
	print(f"{oName} 을(를) 제거했습니다.")
	

# 회원을 검색한다
def searchMember(a_oTable):
	oName = input("이름 입력 : ")
	oMember = a_oTable.getMember(oName)
	
	# 회원이 없을 경우
	if oMember == None:
		raise CException_Missing(oName)
	
	print("=====> 회원 정보 <=====")
	print(f"이름 : {oMember[0]}")
	print(f"전화 번호 : {oMember[1]}")
	

# 모든 회원을 출력한다
def printMembers_All(a_oTable):
	oListMembers = a_oTable.getMembers_All()
	print("=====> 모든 회원 정보 <=====")
	
	for oMember in oListMembers:
		oName = oMember[0]
		oPNumber = oMember[1]
		
		print(f"이름 : {oName}")
		print(f"전화 번호 : {oPNumber}\n")
		