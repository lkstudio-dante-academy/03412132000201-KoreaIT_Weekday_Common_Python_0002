import os
import sys

"""
Python 연습 문제 4
- 합계/평균 계산하기
- 사용자로부터 정수를 입력 받은 후 해당 정수를 리스트에 추가
- 사용자가 입력한 수가 0 이 아닐 경우 정수 입력 반복
- 사용자가 0 을 입력 할 경우 정수 입력을 종료하고 그동안
입력한 정수와 해당 정수들의 합계 및 평균을 출력

Ex)
1 번째 정수 입력 : 10
2 번째 정수 입력 : 5
3 번째 정수 입력 : 0

=====> 입력 받은 수 <=====
10, 5

합계 : 15
평균 : 7.5
"""


# Training 4
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
	
	for nVal in oListValues:
		print(f"{nVal}, ", end = "")
	
	nVal_Sum = 0
	fVal_Average = 0.0
	
	# 합계 계산
	for nVal in oListValues:
		nVal_Sum += nVal
	
	# 평균 계산
	fVal_Average = nVal_Sum / len(oListValues)
	
	# 결과 출력
	print(f"\n\n합계 : {nVal_Sum}")
	print(f"평균 : {fVal_Average}")
