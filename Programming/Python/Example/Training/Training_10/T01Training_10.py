import os
import sys

from Training.Training_10.CMember import CMember
from Training.Training_10.CManager_Member import CManager_Member

"""
Python 연습 문제 10
- 연습 문제 5 번을 클래스로 활용해서 구현하기
- 회원 클래스 정의하기
- 회원 관리자 클래스 정의하기
"""


# Training 10
def start(args):
	oManager = CManager_Member()
	oManager.loadMembers_All()
	
	while True:
		printMenu()
		nMenu = int(input("\n선택 : "))
		
		# 종료 메뉴 일 경우
		if nMenu == MENU_EXIT:
			break
		
		# 회원 추가 메뉴 일 경우
		if nMenu == MENU_ADD_MEMBER:
			handleOnMenu_AddMember(oManager)
			
		# 회원 제거 메뉴 일 경우
		elif nMenu == MENU_REMOVE_MEMBER:
			handleOnMenu_RemoveMember(oManager)
			
		# 회원 검색 메뉴 일 경우
		elif nMenu == MENU_SEARCH_MEMBER:
			handleOnMenu_SearchMember(oManager)
			
		# 모든 회원 출력 메뉴 일 경우
		elif nMenu == MENU_SHOW_ALL_MEMBERS:
			handleOnMenu_ShowAllMembers(oManager)
			
		print()
		
	oManager.saveMembers_All()
	print("\n프로그램을 종료합니다.")


# 메뉴
MENU_ADD_MEMBER = 1
MENU_REMOVE_MEMBER = 2
MENU_SEARCH_MEMBER = 3
MENU_SHOW_ALL_MEMBERS = 4
MENU_EXIT = 5

# 메뉴를 출력한다
def printMenu():
	print("=====> 메뉴 <=====")
	print("1. 회원 추가")
	print("2. 회원 제거")
	print("3. 회원 검색")
	print("4. 모든 회원 출력")
	print("5. 종료")
	
	
# 회원 추가 메뉴를 처리한다
def handleOnMenu_AddMember(a_oManager):
	oName = input("이름 입력 : ")
	oPNumber = input("전화 번호 입력 : ")
	
	oMember = a_oManager.findMember(oName)
	
	# 회원이 존재 할 경우
	if oMember != None:
		print(f"{oName} 은(는) 존재하는 회원입니다.")
	
	else:
		oMember = CMember()
		oMember.m_oName = oName
		oMember.m_oPNumber = oPNumber
		
		a_oManager.addMember(oMember)
		print(f"{oName} 을(를) 추가했습니다.")
	
	
# 회원 제거 메뉴를 처리한다
def handleOnMenu_RemoveMember(a_oManager):
	oName = input("이름 입력 : ")
	oMember = a_oManager.findMember(oName)
	
	# 회원이 존재 할 경우
	if oMember != None:
		a_oManager.removeMember(oName)
		print(f"{oName} 을(를) 제거했습니다.")
	
	else:
		print(f"{oName} 은(는) 존재하지않습니다.")


# 회원 검색 메뉴를 처리한다
def handleOnMenu_SearchMember(a_oManager):
	oName = input("이름 입력 : ")
	oMember = a_oManager.findMember(oName)
	
	# 회원이 존재 할 경우
	if oMember != None:
		print("=====> 회원 정보 <=====")
		oMember.showInfo()
		
	else:
		print(f"{oName} 은(는) 존재하지않습니다.")


# 모든 회원 출력 메뉴를 처리한다
def handleOnMenu_ShowAllMembers(a_oManager):
	print("=====> 모든 회원 정보 <=====")
	a_oManager.showMembers_All()
