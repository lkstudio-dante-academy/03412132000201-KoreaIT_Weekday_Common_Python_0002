import os
import sys

"""
Python 연습 문제 5
- 회원 관리 프로그램 제작하기
- 회원 정보는 이름과 전화 번호로 구성
- 메뉴는 회원 추가, 제거, 검색으로 구성
- 회원 추가는 이름 중복 허용 X
- 제거, 검색은 회원 이름을 기준으로 진행

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

Case 1. 동일한 이름의 회원이 없을 경우
회원 A 을(를) 추가했습니다.

Case 2. 동일한 이름의 회원이 존재 할 경우
회원 A 은(는) 이미 존재하는 회원입니다.

선택 : 2
이름 입력 : 회원 A

Case 1. 회원이 아닐 경우
회원 A 은(는) 회원이 아닙니다.

Case 2. 회원 일 경우
회원 A 을(를) 제거했습니다.

선택 : 3
이름 입력 : 회원 A

Case 1. 회원이 아닐 경우
회원 A 은(는) 회원이 아닙니다.

Case 2. 회원 일 경우
=====> 회원 정보 <=====
이름 : 회원 A
전화 번호 : 1234

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


# Training 5
def start(args):
	oDictMembers = {}
	
	while True:
		print("=====> 메뉴 <=====")
		print("1. 회원 추가")
		print("2. 회원 제거")
		print("3. 회원 검색")
		print("4. 모든 회원 출력")
		print("5. 종료")
		
		nMenu = int(input("\n선택 : "))
		
		# 종료를 선택했을 경우
		if nMenu == 5:
			break
		
		# 회원 추가를 선택했을 경우
		if nMenu == 1:
			oName = input("이름 입력 : ")
			oPNumber = input("전화 번호 입력 : ")
			
			# 회원이 존재 할 경우
			if oName in oDictMembers:
				print(f"{oName} 은(는) 이미 존재합니다.")
			
			else:
				oMember = {
					"Name": oName, "PNumber": oPNumber
				}
				
				oDictMembers[oName] = oMember
				print(f"{oName} 을(를) 추가했습니다.")
		
		#  회원 제거를 선택했을 경우
		elif nMenu == 2:
			oName = input("이름 입력 : ")
			
			# 회원이 존재 할 경우
			if oName in oDictMembers:
				del oDictMembers[oName]
				print(f"{oName} 을(를) 제거했습니다.")
			
			else:
				print(f"{oName} 은(는) 회원이 아닙니다.")
		
		# 회원 검색를 선택했을 경우
		elif nMenu == 3:
			oName = input("이름 입력 : ")
			
			# 회원이 존재 할 경우
			if oName in oDictMembers:
				oMember = oDictMembers[oName]
				oPNumber = oMember["PNumber"]
				
				print("=====> 회원 정보 <======")
				print(f"이름 : {oName}")
				print(f"전화 번호 : {oPNumber}")
			
			else:
				print(f"{oName} 은(는) 회원이 아닙니다.")
		
		# 모든 회원 출력을 선택했을 경우
		elif nMenu == 4:
			print("=====> 모든 회원 정보 <=====")
			
			for oKey, oVal in oDictMembers.items():
				oName = oVal["Name"]
				oPNumber = oVal["PNumber"]
				
				print(f"이름 : {oName}")
				print(f"전화 번호 : {oPNumber}\n")
		
		print()
	
	print("프로그램을 종료합니다.")
