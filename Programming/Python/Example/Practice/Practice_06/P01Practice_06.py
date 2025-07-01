import os
import sys

"""
Python 과제 6
- 다양한 형태 출력하기
- 라인 수를 입력 받아 해당 라인만큼 다양한 형태를 출력한다

Ex)
라인 수 입력 : 5
*   *
 * *
  *
 * *
*   *

*****
   *
  *
 *
*****

*   *
**  *
* * *
*  **
*   *

    *
   ***
  *****
 *******
*********

*********
 *******
  *****
   ***
    *
"""


# Practice 6
def start(args):
	nNumLines = int(input("라인 수 입력 : "))
	
	for i in range(0, nNumLines):
		for j in range(0, nNumLines):
			bIsStarA = i == j
			bIsStarB = j == (nNumLines - 1) - i
			
			print("{0}".format("*" if bIsStarA or bIsStarB else " "), end = "")
			
		print()
		
	print()
	
	for i in range(0, nNumLines):
		for j in range(0, nNumLines):
			bIsStarA = i == 0
			bIsStarB = i == nNumLines - 1
			bIsStarC = j == (nNumLines - 1) - i
			
			print("{0}".format("*" if bIsStarA or bIsStarB or bIsStarC else " "), end = "")
	
		print()
	
	print()
	
	for i in range(0, nNumLines):
		for j in range(0, nNumLines):
			bIsStarA = j == 0
			bIsStarB = j == nNumLines - 1
			bIsStarC = i == j
			
			print("{0}".format("*" if bIsStarA or bIsStarB or bIsStarC else " "), end = "")
		
		print()
	
	print()
	nWidth_Max = (nNumLines * 2) - 1
	
	for i in range(0, nNumLines):
		nCenter = nWidth_Max // 2
		
		for j in range(0, nWidth_Max):
			bIsStar = j >= nCenter - i and j <= nCenter + i
			print("{0}".format("*" if bIsStar else " "), end = "")
		
		print()
	
	print()
	
	for i in range(0, nNumLines)[::-1]:
		nCenter = nWidth_Max // 2
		
		for j in range(0, nWidth_Max):
			bIsStar = j >= nCenter - i and j <= nCenter + i
			print("{0}".format("*" if bIsStar else " "), end = "")
		
		print()