import os
import sys


# 회원
class CMember:
	# 초기화
	def __init__(self):
		self.m_oName = ""
		self.m_oPNumber = ""
		
	# 정보를 출력한다
	def showInfo(self):
		print(f"이름 : {self.m_oName}")
		print(f"전화 번호 : {self.m_oPNumber}")
		