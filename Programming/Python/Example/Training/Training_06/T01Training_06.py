import os
import sys

"""
Python 연습 문제 6
- 연습 문제 4 번을 함수를 활용해서 구현하기
- 합계를 반환하는 함수 구현
- 평균을 반환하는 함수 구현
- 입력 받은 수를 출력하는 함수 구현
"""


# Training 6
def start(args):
	oListValues = []
	
	# 정수 입력
	while True:
		nNumValues = len(oListValues)
		nVal = int(input(f"{nNumValues + 1} 번째 정수 입력 : "))
		
		# 0 을 입력했을 경우
		if nVal == 0:
			break
		
		oListValues.append(nVal)
	
	# 입력 받은 수 출력
	print("\n=====> 입력 받은 수 <=====")
	printValues(oListValues)
	
	nVal_Sum = getVal_Sum(oListValues)
	fVal_Average = getVal_Average(nVal_Sum, len(oListValues))
	
	print(f"\n합계 : {nVal_Sum}")
	print(f"평균 : {fVal_Average}")


# 합계를 반환한다
def getVal_Sum(a_oListValues):
	nVal_Sum = 0
	
	for nVal in a_oListValues:
		nVal_Sum += nVal
	
	return nVal_Sum


# 평균을 반환한다
def getVal_Average(a_nVal_Sum, a_nNumValues):
	return a_nVal_Sum / a_nNumValues


# 값을 출력한다
def printValues(a_oListValues):
	for nVal in a_oListValues:
		print(f"{nVal}, ", end = "")
	
	print()
