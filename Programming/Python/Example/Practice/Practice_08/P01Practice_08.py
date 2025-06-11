import os
import sys

"""
Python 과제 8
- 파일 복사 프로그램 제작하기
- 사용자로부터 원본 파일 경로와 사본 파일 경로를 입력
- 원본 파일이 존재 할 경우 원본 파일과 동일한 데이터를 지니고 있는 사본 파일 생성

Ex)
원본 파일 경로 입력 : P_P01Practice_08.txt
사본 파일 경로 입력 : P_P01Practice_08_Copy.txt

Case 1. 원본 파일이 존재 할 경우
P_P01Practice_08.txt -> P_P01Practice_08_Copy.txt 파일을 복사했습니다.

Case 2. 원본 파일이 없을 경우
P_P01Practice_08.txt 이(가) 존재하지않습니다.
"""


# Practice 8
def start(args):
	oPath_Origin = input("원본 파일 경로 입력 : ")
	oPath_Copy = input("사본 파일 경로 입력 : ")
	
	bIsValidA = len(oPath_Origin) >= 1
	bIsValidB = len(oPath_Copy) >= 1
	bIsValidC = os.path.exists(oPath_Origin)
	
	# 파일 경로가 유효하지 않을 경우
	if not bIsValidA or not bIsValidB:
		print("원본 or 사본 파일 경로가 유효하지 않습니다.")
		return
	
	# 원본 파일이 존재하지 않을 경우
	if not bIsValidC:
		print("원본 파일이 존재하지 않습니다.")
		return
	
	with open(oPath_Origin, "rb") as oRStream:
		oPath_Dir = os.path.dirname(oPath_Copy)
		
		# 사본 파일 경로에 디렉토리가 없을 경우
		if oPath_Dir and not os.path.exists(oPath_Dir):
			os.makedirs(oPath_Dir)
		
		with open(oPath_Copy, "wb") as oWStream:
			while True:
				oByte = oRStream.read(1)
				
				# 읽어 들 일 데이터가 없을 경우
				if not oByte:
					break
				
				oWStream.write(oByte)
	
	print("파일 복사가 완료 되었습니다.")
	