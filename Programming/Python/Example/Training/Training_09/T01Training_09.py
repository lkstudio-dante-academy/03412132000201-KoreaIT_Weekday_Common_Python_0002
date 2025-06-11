import os
import sys

"""
Python 연습 문제 9
- 연습 문제 5 번을 파일 시스템을 활용해서 구현하기
- 프로그램을 종료하고 다시 실행해도 회원 데이터 유지하기
"""


# Training 9
def start(args):
	oPath_File = "P_T01Training_09_01.txt"
	oDictMembers = {}
	
	# 파일이 존재 할 경우
	if os.path.exists(oPath_File):
		with open(oPath_File, "rt", encoding = "utf8") as oRStream:
			for oStr in oRStream.readlines():
				oTokens = oStr.split(",")
				
				oName = oTokens[0]
				oPNumber = oTokens[1]
				
				oMember = {
					"Name": oName, "PNumber": oPNumber.removesuffix("\n")
				}
				
				oDictMembers[oName] = oMember
	
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
		
		with open(oPath_File, "wt", encoding = "utf8") as oWStream:
			for oKey, oMember in oDictMembers.items():
				oName = oMember["Name"]
				oPNumber = oMember["PNumber"]
				
				oWStream.write(f"{oName},{oPNumber}\n")
	
	print("프로그램을 종료합니다.")
