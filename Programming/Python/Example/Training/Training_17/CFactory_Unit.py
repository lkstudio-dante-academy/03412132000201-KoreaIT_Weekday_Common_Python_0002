import os
import sys

from datetime import datetime
from Training.Training_17.CUnit import CUnitA, CUnitB, CUnitC


# 유닛 팩토리
class CFactory_Unit:
	# 초기화
	def __init__(self):
		self.m_oListClasses_Unit = [CUnitA, CUnitB, CUnitC]
		
		for i in range(0, len(self.m_oListClasses_Unit)):
			self.m_oListClasses_Unit[i].IDX = i
			
	# 유닛 종류 개수를 반환한다
	def getNumKinds_Unit(self):
		return len(self.m_oListClasses_Unit)
	
	# 유닛 클래스를 반환한다
	def getClass_Unit(self, a_nIdx):
		return self.m_oListClasses_Unit[a_nIdx]
	
	# 유닛을 생성한다
	def createUnit(self, a_nIdx):
		oTime = datetime.now()
		oClass_Unit = self.m_oListClasses_Unit[a_nIdx]
		
		return oClass_Unit(oTime)
	