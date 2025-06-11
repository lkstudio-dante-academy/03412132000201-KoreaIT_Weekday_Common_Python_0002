import os
import sys


# 카운터
class CCounter:
	# 초기화
	def __init__(self):
		self.m_nCount = 0
		
	# 카운트를 증가 시킨다
	def incrCount(self, a_nCount):
		self.m_nCount += a_nCount
		