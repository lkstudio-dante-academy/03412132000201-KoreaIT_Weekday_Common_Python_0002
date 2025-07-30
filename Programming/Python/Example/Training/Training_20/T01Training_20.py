import os
import sys

"""
Python 연습 문제 20
- 파일 복사 프로그램 제작하기
- 사용자로부터 원본 파일 경로와 사본 파일 경로를 입력받는다
- 원본 파일이 존재 할 경우 원본 파일의 데이터를 기반으로 사본 파일을 생성한다

Ex)
원본 파일 경로 입력 : A/Test.txt
사본 파일 경로 입력 : B/Test_Copy.txt

Case 1. 원본 파일이 존재 할 경우
A/Test.txt -> B/Test_Copy.txt 파일 복사했습니다.

Case 2. 원본 파일이 없을 경우
A/Test.txt 파일은 존재하지 않습니다.
"""


# Training 20
def start(args):
	oPath_Origin = input("원본 파일 경로 : ")
	oPath_Copy = input("사본 파일 경로 : ")
	
	# 원본 파일이 없을 경우
	if not os.path.exists(oPath_Origin):
		print(f"{oPath_Origin} 파일이 존재하지 않습니다.")
		return
	
	oPath_Dir = os.path.dirname(oPath_Copy)
	
	# 디렉토리 경로가 유효 할 경우
	if oPath_Dir:
		os.makedirs(oPath_Dir, exist_ok = True)
		
	with open(oPath_Origin, "rb") as oRStream:
		with open(oPath_Copy, "wb") as oWStream:
			while True:
				oBytes = oRStream.read(1)
				
				# 데이터가 없을 경우
				if not oBytes:
					break
				
				oWStream.write(oBytes)
	
	print(f"{oPath_Origin} -> {oPath_Copy} 파일이 복사되었습니다.")
