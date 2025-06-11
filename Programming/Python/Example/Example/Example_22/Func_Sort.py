import os
import sys


# 값을 정렬한다
def sortValues_ByBubble(a_oListValues):
	for i in range(0, len(a_oListValues)):
		for j in range(0, len(a_oListValues) - (i + 1)):
			# 정렬이 필요 없을 경우
			if a_oListValues[j] <= a_oListValues[j + 1]:
				continue
				
			nTemp = a_oListValues[j]
			a_oListValues[j] = a_oListValues[j + 1]
			a_oListValues[j + 1] = nTemp


# 값을 정렬한다
def sortValues_BySelection(a_oListValues):
	for i in range(0, len(a_oListValues)):
		nIdx_Compare = i
		
		for j in range(i, len(a_oListValues)):
			nIdx_Compare = j if a_oListValues[j] < a_oListValues[nIdx_Compare] else nIdx_Compare
			
		nTemp = a_oListValues[i]
		a_oListValues[i] = a_oListValues[nIdx_Compare]
		a_oListValues[nIdx_Compare] = nTemp


# 값을 정렬한다
def sortValues_ByInsertion(a_oListValues):
	for i in range(1, len(a_oListValues)):
		nIdx = i - 1
		nVal_Compare = a_oListValues[i]
		
		for j in range(i - 1, -1, -1):
			# 정렬이 필요 없을 경우
			if a_oListValues[j] <= nVal_Compare:
				break
				
			nIdx -= 1
			a_oListValues[j + 1] = a_oListValues[j]
			
		a_oListValues[nIdx + 1] = nVal_Compare
		

# 값을 정렬한다
def sortValues_ByHeap(a_oListValues):
	for i in range(len(a_oListValues) // 2 - 1, -1, -1):
		sortValues_ByHeap_Internal(a_oListValues, i, len(a_oListValues))
		
	for i in range(len(a_oListValues) - 1, -1, -1):
		nTemp = a_oListValues[0]
		a_oListValues[0] = a_oListValues[i]
		a_oListValues[i] = nTemp
		
		sortValues_ByHeap_Internal(a_oListValues, 0, i)


# 값을 정렬한다
def sortValues_ByHeap_Internal(a_oListValues, a_nIdx_Start, a_nNumValues):
	nIdx_Parent = a_nIdx_Start
	
	while nIdx_Parent < a_nNumValues // 2:
		nIdx_Compare = (nIdx_Parent * 2) + 1
		
		# 오른쪽 자식이 존재 할 경우
		if nIdx_Compare + 1 < a_nNumValues:
			nIdx_Compare = nIdx_Compare if a_oListValues[nIdx_Compare] >= a_oListValues[nIdx_Compare + 1] else nIdx_Compare + 1
			
		# 정렬이 필요 없을 경우
		if a_oListValues[nIdx_Parent] >= a_oListValues[nIdx_Compare]:
			break
			
		nTemp = a_oListValues[nIdx_Parent]
		a_oListValues[nIdx_Parent] = a_oListValues[nIdx_Compare]
		a_oListValues[nIdx_Compare] = nTemp
		
		nIdx_Parent = nIdx_Compare
		

# 값을 정렬한다
def sortValues_ByMerge(a_oListValues, a_nLeft, a_nRight):
	oListValues_Buffer = [0] * len(a_oListValues)
	sortValues_ByMerge_Internal(a_oListValues, a_nLeft, a_nRight, oListValues_Buffer)


# 값을 정렬한다
def sortValues_ByMerge_Internal(a_oListValues, a_nLeft, a_nRight, a_oListValues_Buffer):
	# 값 정렬이 불가능 할 경우
	if a_nLeft >= a_nRight:
		return
	
	nMiddle = (a_nLeft + a_nRight) // 2
	
	sortValues_ByMerge_Internal(a_oListValues, a_nLeft, nMiddle, a_oListValues_Buffer)
	sortValues_ByMerge_Internal(a_oListValues, nMiddle + 1, a_nRight, a_oListValues_Buffer)
	
	nIdx_Left = a_nLeft
	nIdx_Right = nMiddle + 1
	
	nNumValues_Buffer = 0
	
	while True:
		while nIdx_Left <= nMiddle and a_oListValues[nIdx_Left] <= a_oListValues[nIdx_Right]:
			a_oListValues_Buffer[nNumValues_Buffer] = a_oListValues[nIdx_Left]
			
			nIdx_Left += 1
			nNumValues_Buffer += 1
			
		while nIdx_Right <= a_nRight and a_oListValues[nIdx_Right] <= a_oListValues[nIdx_Left]:
			a_oListValues_Buffer[nNumValues_Buffer] = a_oListValues[nIdx_Right]
			
			nIdx_Right += 1
			nNumValues_Buffer += 1
			
		# 값 정렬이 불가능 할 경우
		if nIdx_Left > nMiddle or nIdx_Right > a_nRight:
			break
	
	while nIdx_Left <= nMiddle:
		a_oListValues_Buffer[nNumValues_Buffer] = a_oListValues[nIdx_Left]
		
		nIdx_Left += 1
		nNumValues_Buffer += 1
	
	while nIdx_Right <= a_nRight:
		a_oListValues_Buffer[nNumValues_Buffer] = a_oListValues[nIdx_Right]
		
		nIdx_Right += 1
		nNumValues_Buffer += 1
		
	for i in range(0, nNumValues_Buffer):
		a_oListValues[a_nLeft + i] = a_oListValues_Buffer[i]


# 값을 정렬한다
def sortValues_ByQuick(a_oListValues, a_nLeft, a_nRight):
	# 값 정렬이 불가능 할 경우
	if a_nLeft >= a_nRight:
		return
	
	nIdx_Left = a_nLeft + 1
	nIdx_Right = a_nRight
	nIdx_Pivot = a_nLeft
	
	while True:
		while nIdx_Left < nIdx_Right and a_oListValues[nIdx_Left] < a_oListValues[nIdx_Pivot]:
			nIdx_Left += 1
			
		while nIdx_Right >= nIdx_Left and a_oListValues[nIdx_Right] >= a_oListValues[nIdx_Pivot]:
			nIdx_Right -= 1
		
		# 값 정렬이 불가능 할 경우
		if nIdx_Left >= nIdx_Right:
			break
			
		nTemp = a_oListValues[nIdx_Left]
		a_oListValues[nIdx_Left] = a_oListValues[nIdx_Right]
		a_oListValues[nIdx_Right] = nTemp
			
	nTemp = a_oListValues[nIdx_Pivot]
	a_oListValues[nIdx_Pivot] = a_oListValues[nIdx_Right]
	a_oListValues[nIdx_Right] = nTemp
	
	sortValues_ByQuick(a_oListValues, a_nLeft, nIdx_Right - 1)
	sortValues_ByQuick(a_oListValues, nIdx_Right + 1, a_nRight)
	