import os
import sys


# 회원 없음 예외
class CException_Missing(Exception):
	# 초기화
	def __init__(self, a_oName):
		oMsg = f"{a_oName} 은(는) 존재하지 않습니다."
		super().__init__(oMsg)
		