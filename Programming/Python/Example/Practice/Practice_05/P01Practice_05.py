import os
import sys

"""
Python 과제 5
- 다앙한 모양 출력하기
- 라인 수를 입력 받아 라인 수에 맞게 다양한 모양 출력

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
    
    *
   ***
  *****
 *******
*********
"""


# Practice 5
def start(args):
	nNumLines = int(input("라인 수 입력 : "))
	
	for i in range(0, nNumLines):
		for j in range(0, nNumLines):
			bIsStarA = i == j
			bIsStarB = i == nNumLines - (j + 1)
			
			oLetter = "*" if bIsStarA or bIsStarB else " "
			print(f"{oLetter}", end = "")
			
		print()
		
	print()
	
	for i in range(0, nNumLines):
		for j in range(0, nNumLines):
			bIsStarA = i == 0
			bIsStarB = i == nNumLines - 1
			bIsStarC = i == nNumLines - (j + 1)
			
			oLetter = "*" if bIsStarA or bIsStarB or bIsStarC else " "
			print(f"{oLetter}", end = "")
			
		print()
		
	print()
	
	for i in range(0, nNumLines):
		for j in range(0, nNumLines):
			bIsStarA = j == 0
			bIsStarB = j == nNumLines - 1
			bIsStarC = i == j
			
			oLetter = "*" if bIsStarA or bIsStarB or bIsStarC else " "
			print(f"{oLetter}", end = "")
			
		print()
		
	print()
	
	for i in range(0, nNumLines):
		for j in range(0, nNumLines):
			bIsStar = j <= i
			oLetter = "*" if bIsStar else " "
			
			print(f"{oLetter}", end = "")
			
		print()
		
	print()
	
	for i in range(nNumLines - 1, -1, -1):
		for j in range(0, nNumLines):
			bIsStar = j <= i
			oLetter = "*" if bIsStar else " "
			
			print(f"{oLetter}", end = "")
			
		print()
		
	print()
	
	for i in range(0, nNumLines):
		for j in range(nNumLines - 1, -1, -1):
			bIsStar = j <= i
			oLetter = "*" if bIsStar else " "
			
			print(f"{oLetter}", end = "")
			
		print()
		
	print()
	
	for i in range(nNumLines - 1, -1, -1):
		for j in range(nNumLines - 1, -1, -1):
			bIsStar = j <= i
			oLetter = "*" if bIsStar else " "
			
			print(f"{oLetter}", end = "")
			
		print()
		
	print()
	nWidth_Max = (nNumLines * 2) - 1
	
	for i in range(0, nNumLines):
		nCenter = nWidth_Max // 2
		
		for j in range(0, nWidth_Max):
			bIsStar = j >= nCenter - i and j <= nCenter + i
			oLetter = "*" if bIsStar else " "
			
			print(f"{oLetter}", end = "")
			
		print()
		
	print()
	