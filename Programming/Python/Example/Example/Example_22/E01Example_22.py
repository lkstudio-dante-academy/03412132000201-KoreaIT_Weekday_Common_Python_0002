import os
import sys

import random

from Example.Example_22.Func_Find import findVal_ByLinear, findVal_ByBinary
from Example.Example_22.Func_Sort import sortValues_ByBubble, sortValues_BySelection, sortValues_ByInsertion, sortValues_ByHeap, sortValues_ByMerge, sortValues_ByQuick

"""
알고리즘 (Algorithm) 이란?
- 주어진 문제를 해결하기 위한 일련의 단계를 순차적으로 정리한 생각이나 아이디어를 의미한다. (+ 즉,
알고리즘은 문제를 분석하고 해결하기 위한 방법이라는 것을 알 수 있다.)

기본 알고리즘 종류
- 탐색 (Search)
- 정렬 (Sorting)

탐색 알고리즘 종류
- 선형 탐색 (Linear Search)
- 이진 탐색 (Binary Search)
- 해시 탐색 (Hash Search)

정렬 알고리즘 종류
- 버블 정렬 (Bubble Sort)
- 선택 정렬 (Selection Sort)
- 삽입 정렬 (Insertion Sort)
- 힙 정렬 (Heap Sort)
- 병합 정렬 (Merge Sort)
- 퀵 정렬 (Quick Sort)
"""


# Example 22 (알고리즘)
def start(args):
	oListValues = [random.randrange(1, 100) for i in range(0, 10)]
	
	print("=====> 리스트 - 정렬 전 <=====")
	printValues(oListValues)
	
	sortValues_ByBubble(oListValues)
	# sortValues_BySelection(oListValues)
	# sortValues_ByInsertion(oListValues)
	# sortValues_ByHeap(oListValues)
	# sortValues_ByMerge(oListValues, 0, len(oListValues) - 1)
	# sortValues_ByQuick(oListValues, 0, len(oListValues) - 1)
	
	print("\n=====> 리스트 - 정렬 후 <=====")
	printValues(oListValues)
	
	nVal = int(input("\n정수 입력 (탐색) : "))
	
	nResult = findVal_ByLinear(oListValues, nVal)
	# nResult = findVal_ByBinary(oListValues, nVal)
	
	print(f"결과 : {nResult}")


# 값을 출력한다
def printValues(a_oListValues):
	for nVal in a_oListValues:
		print(f"{nVal}, ", end = "")
		
	print()
	