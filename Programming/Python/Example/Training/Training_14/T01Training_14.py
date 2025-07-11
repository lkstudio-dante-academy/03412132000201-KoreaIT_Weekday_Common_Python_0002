import os
import sys

"""
Python 연습 문제 14
- 하노이 탑 시뮬레이션 제작하기
- 원반 개수를 입력받아 해당 개수의 원반을 목적지로 이동시킨다

Ex)
원반 개수 입력 : 3
1 번 원반 : A -> C 이동
2 번 원반 : A -> B 이동
1 번 원반 : C -> B 이동
3 번 원반 : A -> C 이동
1 번 원반 : B -> A 이동
2 번 원반 : B -> C 이동
1 번 원반 : A -> C 이동
"""


# Training 14
def start(args):
	nNum = int(input("원반 개수 입력 : "))
	printResult_HanoiTower(nNum, "A", "C", "B")


# 하노이 탑 결과를 출력한다
def printResult_HanoiTower(a_nNum, a_oFrom, a_oTo, a_oBuffer):
	# 결과 출력이 불가능 할 경우
	if a_nNum <= 0:
		return
	
	printResult_HanoiTower(a_nNum - 1, a_oFrom, a_oBuffer, a_oTo)
	print(f"{a_nNum} 원반 : {a_oFrom} -> {a_oTo} 이동")
	
	printResult_HanoiTower(a_nNum - 1, a_oBuffer, a_oTo, a_oFrom)
	