import os
import sys


# 스택
class CStack:
	# 초기화
	def __init__(self):
		self.m_nTop = 0
		self.m_oListValues = []
	
	# 빈 여부를 검사한다
	def isEmpty(self):
		return self.m_nTop <= 0
	
	# 값을 추가한다
	def push(self, a_tVal):
		self.m_oListValues.append(a_tVal)
		self.m_nTop += 1
	
	# 값을 제거한다
	def pop(self):
		tVal = self.m_oListValues[self.m_nTop - 1]
		del self.m_oListValues[self.m_nTop - 1]
		
		self.m_nTop -= 1
		return tVal
	