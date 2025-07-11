import os
import sys

"""
Python 연습 문제 15
- 미로 탈출 경로 계산하기
- 정해진 미로를 탈출 할 수 있는 경로를 계산한다
- 탈출 경로는 * 기호로 표기하며 # 기호는 이동 불가, 공백은 이동 가능한 위치를 의미한다

Ex)
=====> 미로 - 탈출 전 <=====
##S##
#   #
# # #
# # #
###E#

=====> 미로 - 탈출 전 <=====
##*##
# **#
# #*#
# #*#
###*#
"""


# Training 15
def start(args):
	oMap = [
		["S", " ", "#", "#", "#"],
		["#", " ", " ", " ", "#"],
		["#", " ", "#", " ", "#"],
		["#", " ", "#", "#", "#"],
		["#", " ", "#", "E", "#"]
	]
	
	print("=====> 미로 - 탈출 전 <=====")
	printMap(oMap)
	
	oPos = findPos(oMap, "S")
	findPath(oMap, oPos[0], oPos[1])
	
	print("\n=====> 미로 - 탈출 후 <=====")
	printMap(oMap)


# 위치를 탐색한다
def findPos(a_oMap, a_oLetter):
	for i in range(0, len(a_oMap)):
		for j in range(0, len(a_oMap[i])):
			# 문자가 존재 할 경우
			if a_oLetter == a_oMap[i][j]:
				return (j, i)
			
	return None


# 경로를 탐색한다
def findPath(a_oMap, a_nPos_X, a_nPos_Y):
	bIsValidA = a_nPos_X >= 0 and a_nPos_X < len(a_oMap)
	bIsValidB = a_nPos_Y >= 0 and a_nPos_Y < len(a_oMap)
	
	# 경로 탐색이 불가능 할 경우
	if not bIsValidA or not bIsValidB:
		return False
	
	oLetter = a_oMap[a_nPos_Y][a_nPos_X]
	
	# 경로 탐색이 불가능 할 경우
	if oLetter == "#" or oLetter == "*":
		return False
	
	a_oMap[a_nPos_Y][a_nPos_X] = "*"
	
	# 목적지 일 경우
	if oLetter == "E":
		return True
	
	oListOffsets = [
		(0, 1), (0, -1), (1, 0), (-1, 0)
	]
	
	for oOffset in oListOffsets:
		nPos_NextX = a_nPos_X + oOffset[0]
		nPos_NextY = a_nPos_Y + oOffset[1]
		
		# 경로 탐색에 성공했을 경우
		if findPath(a_oMap, nPos_NextX, nPos_NextY):
			return True
		
	a_oMap[a_nPos_Y][a_nPos_X] = oLetter
	return False
	

# 맵을 출력한다
def printMap(a_oMap):
	for oList in a_oMap:
		for oLetter in oList:
			print(f"{oLetter} ", end = "")
			
		print()
		