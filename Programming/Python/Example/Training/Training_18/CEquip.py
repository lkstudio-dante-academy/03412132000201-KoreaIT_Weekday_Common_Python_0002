import os
import sys


# 장비
class CEquip:
	TYPE_WEAPON = 0
	TYPE_ARMOR = 1
	
	# 초기화
	def __init__(self, a_nType, a_nVal):
		self.m_nType = a_nType
		self.m_nVal = a_nVal
		
	# 타입을 반환한다
	def getStr_Type(self):
		oListStrings = [
			"무기", "방어구"
		]
		
		return oListStrings[self.m_nType]
	
	# 능력치를 반환한다
	def getStr_Ability(self):
		oListStrings = [
			"공격력", "방어력"
		]
		
		return oListStrings[self.m_nType]
		