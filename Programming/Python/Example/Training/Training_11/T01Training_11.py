import os
import sys

"""
Python 연습 문제 11
- 회원 관리 프로그램 제작하기 (+ 선형 컬렉션 활용)
- 회원 정보는 이름, 전화 번호로 이루어져있다
- 메뉴를 출력 후 사용자의 선택에 따라 회원 추가, 회원 제거 등이 가능하다
- 회원 추가 시 동일한 이름의 회원이 존재 할 경우 추가 불가 (+ 즉, 모든 회원의 이름은 중복 되지 않는다)

Ex)
=====> 메뉴 <=====
1. 회원 추가
2. 회원 제거
3. 회원 검색
4. 모든 회원 출력
5. 종료

선택 : 1
이름 입력 : 회원 A
전화 번호 입력 : 1234

Case 1. 신규 회원 일 경우
회원 A 을(를) 추가했습니다.

Case 2. 동일한 이름의 회원이 존재 할 경우
회원 A 을(를) 이미 존재하는 회원입니다.

선택 : 2
이름 입력 : 회원 B

Case 1. 회원이 존재 할 경우
회원 B 을(를) 제거했습니다.

Case 2. 회원이 없을 경우
회원 B 은(는) 존재하지 않는 회원입니다.

선택 : 3
이름 입력 : 회원 A

Case 1. 회원이 존재 할 경우
=====> 회원 정보 <=====
이름 : 회원 A
전화 번호 : 1234

Case 2. 회원이 없을 경우
회원 A 은(는) 존재하지 않는 회원입니다.

선택 : 4
=====> 모든 회원 정보 <=====
이름 : 회원 A
전화 번호 : 1234

이름 : 회원 B
전화 번호 : 1234

...이하 생략

선택 : 5
프로그램을 종료합니다.
"""


# Training 11
def start(args):
	MENU_ADD_MEMBER = 1
	MENU_REMOVE_MEMBER = 2
	MENU_SEARCH_MEMBER = 3
	MENU_SHOW_ALL_MEMBERS = 4
	MENU_EXIT = 5
	
	nMenu = 0
	oListMembers = []
	
	while nMenu != MENU_EXIT:
		print("=====> 메뉴 <=====")
		print("1. 회원 추가")
		print("2. 회원 제거")
		print("3. 회원 검색")
		print("4. 모든 회원 출력")
		print("5. 종료")
		
		nMenu = int(input("\n선택 : "))
		
		# 회원 추가 일 경우
		if nMenu == MENU_ADD_MEMBER:
			oName = input("이름 입력 : ")
			oPNumber = input("전화 번호 입력 : ")
			
			oMember_Find = None
			
			for oMember in oListMembers:
				# 회원이 존재 할 경우
				if oName in oMember:
					oMember_Find = oMember
					break
			
			# 회원이 존재 할 경우
			if oMember_Find != None:
				print(f"{oName} 은(는) 이미 존재하는 회원입니다.")
			
			else:
				oListMembers.append((oName, oPNumber))
				print(f"{oName} 을(를) 추가했습니다.")
		
		# 회원 제거 일 경우
		elif nMenu == MENU_REMOVE_MEMBER:
			oName = input("이름 입력 : ")
			oMember_Find = None
			
			for oMember in oListMembers:
				# 회원이 존재 할 경우
				if oName in oMember:
					oMember_Find = oMember
					break
			
			# 회원이 존재 할 경우
			if oMember_Find != None:
				oListMembers.remove(oMember_Find)
				print(f"{oName} 을(를) 제거했습니다.")
			
			else:
				print(f"{oName} 은(는) 존재하지 않는 회원입니다.")
		
		# 회원 검색 일 경우
		elif nMenu == MENU_SEARCH_MEMBER:
			oName = input("이름 입력 : ")
			oMember_Find = None
			
			for oMember in oListMembers:
				# 회원이 존재 할 경우
				if oName in oMember:
					oMember_Find = oMember
					break
			
			# 회원이 존재 할 경우
			if oMember_Find != None:
				print("=====> 회원 정보 <=====")
				print(f"이름 : {oMember_Find[0]}")
				print(f"전화 번호 : {oMember_Find[1]}")
			
			else:
				print(f"{oName} 은(는) 존재하지 않는 회원입니다.")
		
		# 모든 회원 출력 일 경우
		elif nMenu == MENU_SHOW_ALL_MEMBERS:
			print("=====> 모든 회원 정보 <======")
			
			for oMember in oListMembers:
				print(f"이름 : {oMember[0]}")
				print(f"전화 번호 : {oMember[1]}\n")
		
		print()
	
	print("프로그램을 종료합니다.")
