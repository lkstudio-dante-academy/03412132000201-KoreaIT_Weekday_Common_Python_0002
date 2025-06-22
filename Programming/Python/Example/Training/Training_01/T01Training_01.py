import os
import sys

"""
Python 연습 문제 1
- 다양한 방법으로 ABC 출력하기
- 최소 4 가지 이상의 방법으로 ABC 출력하기
"""


# Training 1
def start(args):
	print("ABC")
	print("{0}".format("ABC"))
	print("{0}{1}{2}".format("A", "B", "C"))
	print("{0:X}{1:X}{2:X}".format(10, 11, 12))
	