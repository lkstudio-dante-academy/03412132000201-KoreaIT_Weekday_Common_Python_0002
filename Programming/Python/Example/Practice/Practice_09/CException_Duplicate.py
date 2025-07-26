import os
import sys


# 회원 중복 예외
class CException_Duplicate(Exception):
	# 초기화
	def __init__(self, a_oName):
		super().__init__(f"{a_oName} 은(는) 이미 존재하는 회원입니다.")
		