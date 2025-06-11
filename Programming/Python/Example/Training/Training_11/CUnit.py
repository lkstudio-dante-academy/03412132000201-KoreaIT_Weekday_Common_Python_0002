import os
import sys


# 유닛
class CUnit:
	# 초기화
	def __init__(self, a_nRange_Atk):
		self.m_nRange_Atk = a_nRange_Atk
		
	# 공격 가능 여부를 검사한다
	def isEnable_Attack(self, a_nDistance_Target):
		return a_nDistance_Target <= self.m_nRange_Atk
	
	# 공격한다
	def attack(self, a_nDistance_Target):
		# 공격이 가능 할 경우
		if self.isEnable_Attack(a_nDistance_Target):
			self.attack_Internal()
		
		else:
			print("공격이 불가능합니다.")
	
	# 공격한다
	def attack_Internal(self):
		pass
	
	
# 마린
class CMarine(CUnit):
	# 공격한다
	def attack_Internal(self):
		print("총을 발사했습니다.")


# 파이어 벳
class CFirebet(CUnit):
	# 공격한다
	def attack_Internal(self):
		print("화염 방사기를 발사했습니다.")


# 고스트
class CGhost(CUnit):
	# 공격한다
	def attack_Internal(self):
		print("장총을 발사했습니다.")
		