import os
import sys

"""
Python 과제 2
- 비트 연산자 활용하기
- 정수와 위치를 입력 받아 해당 위치의 비트를 변경하기 (+ 즉, 0 -> 1, 1 -> 으로 변경)
- 위치는 가장 오른쪽에 있는 비트가 0 이며 왼쪽으로 갈수록 1 씩 증가

Ex)
정수 입력 : 10
위치 입력 : 1

=====> 결과 <=====
변경 전 : 0b1010
변경 후 : 0b1000
"""


# Practice 2
def start(args):
	nVal = int(input("정수 입력 : "))
	nPos = int(input("위치 입력 : "))
	
	nVal_Replace = nVal ^ (1 << nPos)
	
	print("=====> 결과 <=====")
	print(f"변경 전 : {nVal:#b}")
	print(f"변경 후 : {nVal_Replace:#b}")
	