import os
import sys

from Training.Training_11.CUnit import CMarine, CFirebet, CGhost


# 팩토리
class CFactory:
	# 유닛 타입
	TYPE_MARINE_UNIT = 1
	TYPE_FIREBET_UNIT = 2
	TYPE_GHOST_UNIT = 3
	
	# 유닛을 생성한다
	def createUnit(self, a_nType_Unit):
		# 마린 일 경우
		if a_nType_Unit == CFactory.TYPE_MARINE_UNIT:
			return CMarine(10)
		
		# 파이어 벳 일 경우
		elif a_nType_Unit == CFactory.TYPE_FIREBET_UNIT:
			return CFirebet(5)
		
		# 고스트 일 경우
		elif a_nType_Unit == CFactory.TYPE_GHOST_UNIT:
			return CGhost(12)
		
		return None
	