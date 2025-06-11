import os
import sys

"""
Python 연습 문제 8
- 하노이 탑 시뮬레이션 제작하기
- 사용자로부터 숫자를 입력 받아 해당 숫자에 맞는 하노이 탑 시뮬레이션 출력

Ex)
원반 번호 입력 : 3
1 번 원반 : A -> C 이동
2 번 원반 : A -> B 이동
1 번 원반 : C -> B 이동
3 번 원반 : A -> C 이동
1 번 원반 : B -> A 이동
2 번 원반 : B -> C 이동
1 번 원반 : A -> C 이동
"""


# Training 8
def start(args):
	nNumDisc = int(input("원반 번호 입력 : "))
	printResult_HanoiTower(nNumDisc, "A", "C", "B")


# 하노이 탑 결과를 출력한다
def printResult_HanoiTower(a_nNumDisc, a_oFrom, a_oTo, a_oBuffer):
	# 결과 출력이 불가능 할 경우
	if a_nNumDisc <= 0:
		return
	
	printResult_HanoiTower(a_nNumDisc - 1, a_oFrom, a_oBuffer, a_oTo)
	print(f"{a_nNumDisc} 번 원반 : {a_oFrom} -> {a_oTo} 이동")
	
	printResult_HanoiTower(a_nNumDisc - 1, a_oBuffer, a_oTo, a_oFrom)
