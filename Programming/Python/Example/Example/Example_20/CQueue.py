import os
import sys


# 큐
class CQueue:
	# 초기화
	def __init__(self, a_nSize = 5):
		self.m_nFront = 0
		self.m_nRear = 0
		
		self.m_oValues = [0] * a_nSize
	
	# 빈 여부를 검사한다
	def isEmpty(self):
		return self.m_nFront == self.m_nRear
	
	# 값을 추가한다
	def enqueue(self, a_tVal):
		# 공간이 가득 찼을 경우
		if self.getIdx_Next(self.m_nRear) == self.m_nFront:
			self.resize(len(self.m_oValues) * 2)
		
		self.m_oValues[self.m_nRear] = a_tVal
		self.m_nRear = (self.m_nRear + 1) % len(self.m_oValues)
	
	# 값을 제거한다
	def dequeue(self):
		tVal = self.m_oValues[self.m_nFront]
		self.m_nFront = (self.m_nFront + 1) % len(self.m_oValues)
		
		return tVal
	
	# 크기를 변경한다
	def resize(self, a_nSize_New):
		i = 0
		oValues_New = [0] * a_nSize_New
		
		while not self.isEmpty():
			oValues_New[i] = self.dequeue()
			i += 1
		
		self.m_nFront = 0
		self.m_nRear = i
		
		self.m_oValues = oValues_New
	
	# 다음 위치를 반환한다
	def getIdx_Next(self, a_nIdx):
		return (a_nIdx + 1) % len(self.m_oValues)
	