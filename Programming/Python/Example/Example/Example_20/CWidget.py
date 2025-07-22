import os
import sys


# 위젯
class CWidget:
	# 초기화
	def __init__(self):
		self.m_nVal = 0
		
	# 정보를 반환한다
	def __str__(self):
		return f"정수 : {self.m_nVal}"
	