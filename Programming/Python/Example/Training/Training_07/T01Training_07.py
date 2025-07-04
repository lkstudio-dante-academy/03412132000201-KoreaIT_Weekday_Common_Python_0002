import os
import sys

"""
Python 연습 문제 7
- 삼각형 출력하기
- 라인 수를 입력 받아 해당 라인만큼 삼각형을 출력한다

Ex)
라인 수 입력 : 5
*
**
***
****
*****

*****
****
***
**
*

    *
   **
  ***
 ****
*****

*****
 ****
  ***
   **
    *
"""


# Training 7
def start(args):
	nNumLines = int(input("라인 수 입력 : "))
	
	for i in range(0, nNumLines):
		for j in range(0, nNumLines):
			bIsStar = j <= i
			print("{0}".format("*" if bIsStar else " "), end = "")
		
		print()
	
	print()
	
	"""
	슬라이스 (Slice) 란?
	- 선형 컬렉션 (+ 리스트, 튜플) 과 문자열을 대상으로 특정 구간에 존재하는 데이터를 추출하는 기능을
	의미한다.
	
	Python 슬라이스 사용 방법
	- [시작 인덱스 : 종료 인덱스 : 간격]
	
	Ex)
	oListValues_Origin = [ 1, 2, 3, 4, 5 ]
	
	oListValuesA = oListValues_Origin[0:3]			<- [ 1, 2, 3 ] 추출 및 할당
	oListValuesB = oListValues_Origin[3:5]			<- [ 4, 5 ] 추출 및 할당
	oListValuesC = oListValues_Origin[::-1]			<- [ 5, 4, 3, 2, 1 ] 추출 및 할당
	
	위와 같이 슬라이스를 활용하면 다양한 형태로 데이터를 추출하는 것이 가능하며 종료 인덱스는
	추출 결과에 포함되지 않는다는 특징이 존재한다.
	"""
	for i in range(0, nNumLines)[::-1]:
		for j in range(0, nNumLines):
			bIsStar = j <= i
			print("{0}".format("*" if bIsStar else " "), end = "")
		
		print()
	
	print()
	
	for i in range(0, nNumLines):
		for j in range(0, nNumLines)[::-1]:
			bIsStar = j <= i
			print("{0}".format("*" if bIsStar else " "), end = "")
		
		print()
	
	print()
	
	for i in range(0, nNumLines)[::-1]:
		for j in range(0, nNumLines)[::-1]:
			bIsStar = j <= i
			print("{0}".format("*" if bIsStar else " "), end = "")
		
		print()
