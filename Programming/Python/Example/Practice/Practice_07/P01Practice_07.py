import os
import sys

"""
Python 과제 7
- 디지털 숫자 출력하기
- 정수를 입력 받아 디지털 형태로 숫자 출력하기

Ex)
정수 입력 : 123
    * ***** *****
    *     *     *
    * ***** *****
    * *         *
    * ***** *****
"""


# Practice 7
def start(args):
	oListStrings = [
		"*****     * ***** ***** *   * ***** *     ***** ***** ***** ",
		"*   *     *     *     * *   * *     *         * *   * *   * ",
		"*   *     * ***** ***** ***** ***** *****     * ***** ***** ",
		"*   *     * *         *     *     * *   *     * *   *     * ",
		"*****     * ***** *****     * ***** *****     * *****     * "
	]
	
	oStr_Val = input("정수 입력 : ")
	
	for i in range(0, len(oListStrings)):
		for j in range(0, len(oStr_Val)):
			nVal = int(oStr_Val[j])
			
			for k in range(0, 6):
				nIdx = (nVal * 5) + nVal + k
				print(f"{oListStrings[i][nIdx]}", end = "")
				
		print()
