import os
import sys

"""
Python 과제 4
- 디지털 형태로 숫자 출력하기
- 사용자로부터 정수를 입력
- 입력 받은 정수에 해당하는 수를 디지털 형태로 출력

Ex)
정수 입력 : 234
***** ***** *   *
    *     * *   *
***** ***** *****
*         *     *
***** *****     *
"""


# Practice 4
def start(args):
	oListStrings_Digit = [
		"*****     * ***** ***** *   * ***** ***** ***** ***** ***** ",
		"*   *     *     *     * *   * *     *         * *   * *   * ",
		"*   *     * ***** ***** ***** ***** *****     * ***** ***** ",
		"*   *     * *         *     *     * *   *     * *   *     * ",
		"*****     * ***** *****     * ***** *****     * ***** ***** "
	]
	
	oStr_Val = input("정수 입력 : ")
	
	try:
		nVal = int(oStr_Val)
		
		for oStr_Digit in oListStrings_Digit:
			for oVal in oStr_Val:
				nVal = int(oVal)
				nIdx_Start = nVal * 6
				
				for i in range(0, 6):
					print(f"{oStr_Digit[nIdx_Start + i]}", end = "")
			
			print()
			
	except:
		print("숫자를 입력해주세요.")
		