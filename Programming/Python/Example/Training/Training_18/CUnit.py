import os
import sys

import random
from Training.Training_18.CEquip import CEquip

# 유닛
class CUnit:
	# 초기화
	def __init__(self, a_nHp, a_nAtk, a_nDef):
		self.m_nHp = a_nHp
		self.m_nAtk = a_nAtk
		self.m_nDef = a_nDef
		
	# 공격력을 반환한다
	def getAtk(self):
		return self.m_nAtk
	
	# 방어력을 반환한다
	def getDef(self):
		return self.m_nDef
		
	# 대상 공격한다
	def attack(self, a_oTarget):
		nDamage = self.getAtk() - a_oTarget.getDef()
		nDamage = max(0, nDamage)
		
		a_oTarget.m_nHp -= nDamage
		a_oTarget.m_nHp = max(0, a_oTarget.m_nHp)
		
		
# 플레이어
class CPlayer(CUnit):
	# 초기화
	def __init__(self, a_nHp, a_nAtk, a_nDef):
		super().__init__(a_nHp, a_nAtk, a_nDef)
		self.m_oEquip = None
		
	# 공격력을 반환한다
	def getAtk(self):
		nAtk = super().getAtk()
		
		# 무기 일 경우
		if self.m_oEquip.m_nType == CEquip.TYPE_WEAPON:
			return nAtk + self.m_oEquip.m_nVal
		
		return nAtk
	
	# 방어력을 반환한다
	def getDef(self):
		nDef = super().getDef()
		
		# 방어구 일 경우
		if self.m_oEquip.m_nType == CEquip.TYPE_ARMOR:
			return nDef + self.m_oEquip.m_nVal
		
		return nDef
		
	# 장비를 변경한다
	def setEquip(self, a_oEquip):
		self.m_oEquip = a_oEquip
		
		
# 몬스터
class CMonster(CUnit):
	# 초기화
	def __init__(self, a_nHp, a_nAtk, a_nDef):
		super().__init__(a_nHp, a_nAtk, a_nDef)


# 몬스터
class CMonster_Named(CUnit):
	# 초기화
	def __init__(self, a_nHp, a_nAtk, a_nDef):
		super().__init__(a_nHp, a_nAtk, a_nDef)
		
	# 공격력을 반환한다
	def getAtk(self):
		nAtk = super().getAtk()
		
		# 크리티컬 일 경우
		if random.randrange(0, 100) <= 30:
			nAtk *= 2
			
		return nAtk
		