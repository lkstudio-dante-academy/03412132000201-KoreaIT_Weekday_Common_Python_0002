import os
import sys


# 해시 테이블
class CTable_Hash:
	# 초기화
	def __init__(self, a_nSize = 32):
		self.m_oContainerList = [None] * a_nSize
		
		for i in range(0, len(self.m_oContainerList)):
			self.m_oContainerList[i] = []
		
	# 값을 추가한다
	def addVal(self, a_tVal):
		nKey = self.makeKey(a_tVal)
		self.m_oContainerList[nKey].append(a_tVal)
		
	# 값을 제거한다
	def removeVal(self, a_tVal):
		nKey = self.makeKey(a_tVal)
		
		# 값 제거가 불가능 할 경우
		if a_tVal not in self.m_oContainerList[nKey]:
			return
		
		self.m_oContainerList[nKey].remove(a_tVal)
		
	# 해시 테이블을 순회한다
	def enumerate(self, a_oCallback):
		for i in range(0, len(self.m_oContainerList)):
			for nVal in self.m_oContainerList[i]:
				a_oCallback(i, nVal)
		
	# 키를 생성한다
	def makeKey(self, a_tVal):
		return hash(a_tVal) % len(self.m_oContainerList)
