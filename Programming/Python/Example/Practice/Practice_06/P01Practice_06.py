import os
import sys

import random

"""
Python 과제 6
- 행맨 게임 제작하기
- 미리 정해 진 여러 단어 중 정답에 해당하는 단어 1 개를 램덤하게 선택
- 정답 단어 중 일부만 공개 후 사용자로부터 문자를 입력받는다
- 입력 받은 문자가 정답 단어에 포함 되어있을 경우 해당 문자 공개 (+ 단, 대/소문자 구분 X)
- 모든 문자를 맞췄을 경우 게임 종료

Ex)
정답 : Microsoft

_ i _ _ _ s _ _ t
문자 입력 : m

M i _ _ _ s _ _ t
문자 입력 : o

M i _ _ o s o _ t
...이하 생략

M i c _ o s o f t
문자 입력 : r

M i c r o s o f t
프로그램을 종료합니다.
"""


# Practice 6
def start(args):
	oAnswer = getAnswer()
	print(f"정답 : {oAnswer}\n")
	
	oListLetters = []
	setupWord(oAnswer, oListLetters)
	
	while True:
		printWord(oListLetters)
		oLetter = input("문자 입력 : ")
		
		for i in range(0, len(oAnswer)):
			# 문자가 존재 할 경우
			if oLetter.upper() == oAnswer[i].upper():
				oListLetters[i] = oAnswer[i]
		
		print()
		
		# 정답 일 경우
		if "_" not in oListLetters:
			break
		
	printWord(oListLetters)
	print("프로그램을 종료합니다.")
	
	
# 정답을 반환한다
def getAnswer():
	oListAnswers = [
		"Apple",
		"Google",
		"Samsung",
		"Microsoft"
	]
	
	nIdx = random.randrange(0, len(oListAnswers))
	return oListAnswers[nIdx]


# 단어를 설정한다
def setupWord(a_oAnswer, a_oOutListLetters):
	for i in range(0, len(a_oAnswer)):
		a_oOutListLetters.append("_")
		
	nNumLetters = int(len(a_oAnswer) * 0.3)
	
	for i in range(0, nNumLetters):
		nIdx = random.randrange(0, len(a_oAnswer))
		a_oOutListLetters[nIdx] = a_oAnswer[nIdx]
		
		
# 단어를 출력한다
def printWord(a_oListLetters):
	for oLetter in a_oListLetters:
		print(f"{oLetter} ", end = "")
		
	print()
	