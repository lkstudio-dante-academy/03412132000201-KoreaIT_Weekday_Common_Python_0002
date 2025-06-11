import os
import sys

"""
Python 연습 문제 1
- 세부 학점 계산하기
- 점수를 입력 받아 해당 점수에 해당하는 학점 출력

학점 범위
- A : 90 이상
- B : 80 이상
- C : 70 이상
- D : 60 이상
- F : 60 미만

세부 학점 범위
- + : 7 ~ 9
- 0 : 4 ~ 6
- - : 0 ~ 3

Ex)
점수 입력 : 85
학점 : B0
"""


# Training 1
def start(args):
	nScore = int(input("점수 입력 : "))
	nScore_Detail = nScore % 10
	
	oGrade = ""
	oGrade_Detail = ""
	
	# F 학점 일 경우
	if nScore < 60:
		oGrade = "F"
	
	else:
		# A 학점 일 경우
		if nScore >= 90:
			oGrade = "A"
		
		# B 학점 일 경우
		elif nScore >= 80:
			oGrade = "B"
		
		# C 학점 일 경우
		elif nScore >= 70:
			oGrade = "C"
		
		else:
			oGrade = "D"
		
		# + 학점 일 경우
		if nScore >= 100 or nScore_Detail >= 7:
			oGrade_Detail = "+"
		
		else:
			oGrade_Detail = "-" if nScore_Detail <= 3 else "0"
	
	print(f"학점 : {oGrade}{oGrade_Detail}")
