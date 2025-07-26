import os
import sys

from Training.Training_16.CMember import CMember


# 회원 관리자
class CManager_Member:
	# 초기화
	def __init__(self):
		self.m_oListMembers = []
	
	# 회원을 추가한다
	def addMember(self, a_oName:str, a_oPNumber:str):
		"""
		위와 같이 변수에 자료형을 명시 할 경우 에디터의 인텔리센스의 도움을 받는 것이 가능하다. (+ 즉,
		에디터에게 해당 변수에 어떤 자료형의 데이터가 전달 될 지 명시함으로서 자동 완성 등의 기능을
		사용하는 것이 가능하다.)
		"""
		
		oMember = CMember(a_oName, a_oPNumber)
		self.m_oListMembers.append(oMember)
	
	# 회원을 제거한다
	def removeMember(self, a_oName):
		nResult = self.findMember(a_oName)
		del self.m_oListMembers[nResult]
	
	# 회원 정보를 출력한다
	def showMember(self, a_oName):
		nResult = self.findMember(a_oName)
		self.m_oListMembers[nResult].showInfo()
	
	# 모든 회원 정보를 출력한다
	def showMembers_All(self):
		for oMember in self.m_oListMembers:
			oMember.showInfo()
			print()
	
	# 회원을 탐색한다
	def findMember(self, a_oName):
		for i in range(0, len(self.m_oListMembers)):
			# 회원이 존재 할 경우
			if a_oName == self.m_oListMembers[i].m_oName:
				return i
		
		return -1
	