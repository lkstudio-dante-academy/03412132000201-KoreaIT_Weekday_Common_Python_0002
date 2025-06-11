import os
import sys

"""
Python 과제 7
- 회원 관리 프로그램 제작하기
- 연습 문제 5 번을 중첩 리스트를 사용해서 제작하기
"""


# Practice 7
def start(args):
	oListMembers = []
	
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
			
			nIdx = findMember(oListMembers, oName)
			
			# 회원이 존재 할 경우
			if nIdx >= 0:
				print(f"{oName} 은(는) 이미 존재합니다.")
			
			else:
				oMember = [oName, oPNumber]
				oListMembers.append(oMember)
				
				print(f"{oName} 을(를) 추가했습니다.")
		
		#  회원 제거를 선택했을 경우
		elif nMenu == 2:
			oName = input("이름 입력 : ")
			nIdx = findMember(oListMembers, oName)
			
			# 회원이 존재 할 경우
			if nIdx >= 0:
				del oListMembers[nIdx]
				print(f"{oName} 을(를) 제거했습니다.")
			
			else:
				print(f"{oName} 은(는) 회원이 아닙니다.")
		
		# 회원 검색를 선택했을 경우
		elif nMenu == 3:
			oName = input("이름 입력 : ")
			nIdx = findMember(oListMembers, oName)
			
			# 회원이 존재 할 경우
			if nIdx >= 0:
				oMember = oListMembers[nIdx]
				oPNumber = oMember[1]
				
				print("=====> 회원 정보 <======")
				print(f"이름 : {oName}")
				print(f"전화 번호 : {oPNumber}")
			
			else:
				print(f"{oName} 은(는) 회원이 아닙니다.")
		
		# 모든 회원 출력을 선택했을 경우
		elif nMenu == 4:
			print("=====> 모든 회원 정보 <=====")
			
			for oMember in oListMembers:
				printMember(oMember)
				print()
		
		print()
	
	print("프로그램을 종료합니다.")


# 회원을 탐색한다
def findMember(a_oListMembers, a_oName):
	for i in range(0, len(a_oListMembers)):
		# 회원이 존재 할 경우
		if a_oName == a_oListMembers[i][0]:
			return i
	
	return -1


# 회원을 출력한다
def printMember(a_oMember):
	print(f"이름 : {a_oMember[0]}")
	print(f"전화 번호 : {a_oMember[1]}")
