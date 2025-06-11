import os
import sys

import pickle


# 회원 관리자
class CManager_Member:
	# 초기화
	def __init__(self):
		self.m_oListMembers = []
		
	# 회원을 추가한다
	def addMember(self, a_oMember):
		oMember = self.findMember(a_oMember.m_oName)
		
		# 회원이 존재 할 경우
		if oMember != None:
			return
		
		self.m_oListMembers.append(a_oMember)
		
	# 회원을 제거한다
	def removeMember(self, a_oName):
		oMember = self.findMember(a_oName)
		
		# 회원이 없을 경우
		if oMember == None:
			return
		
		self.m_oListMembers.remove(oMember)
		
	# 회원을 탐색한다
	def findMember(self, a_oName):
		for oMember in self.m_oListMembers:
			# 이름이 동일 할 경우
			if a_oName == oMember.m_oName:
				return oMember
			
		return None
	
	# 모든 회원을 출력한다
	def showMembers_All(self):
		for oMember in self.m_oListMembers:
			oMember.showInfo()
			print()
	
	# 회원을 로드한다
	def loadMembers_All(self):
		# 파일이 없을 경우
		if not os.path.exists("P_T01Training_10_01.bin"):
			return
		
		with open("P_T01Training_10_01.bin", "rb") as oRStream:
			self.m_oListMembers = pickle.load(oRStream)

	# 회원을 저장한다
	def saveMembers_All(self):
		with open("P_T01Training_10_01.bin", "wb") as oWStream:
			pickle.dump(self.m_oListMembers, oWStream)
	