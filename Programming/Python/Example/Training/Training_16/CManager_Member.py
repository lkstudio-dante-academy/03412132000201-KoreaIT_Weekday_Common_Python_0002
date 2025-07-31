import os
import sys

import pickle
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
		
	# 회원을 검색한다
	def searchMember(self, a_oName):
		self.showMember(a_oName)
		
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
	
	# 회원을 로드한다
	def loadMembers_FromFile(self, a_oPath_File):
		# 로드가 불가능 할 경우
		if not os.path.exists(a_oPath_File):
			return
		
		with open(a_oPath_File, "rt", encoding = "utf-8") as oRStream:
			oListInfos_Member = oRStream.readlines()
			
			for oInfo_Member in oListInfos_Member:
				oTokens = oInfo_Member.split(",")
				oMember = CMember(oTokens[0], oTokens[1])
				
				self.m_oListMembers.append(oMember)
	
	# 회원을 저장한다
	def saveMembers_ToFile(self, a_oPath_File):
		oPath_Dir = os.path.dirname(a_oPath_File)
		
		# 디렉토리 생성이 필요 할 경우
		if oPath_Dir:
			os.makedirs(oPath_Dir, exist_ok = True)
			
		with open(a_oPath_File, "wt", encoding = "utf-8") as oWStream:
			for oMember in self.m_oListMembers:
				oName = oMember.m_oName
				oPNumber = oMember.m_oPNumber
				
				oInfo_Member = f"{oName},{oPNumber}"
				
				oWStream.write(oInfo_Member)
				oWStream.write("\n")
	
	# 회원을 로드한다
	def deserializeMembers_FromFile(self, a_oPath_File):
		# 로드가 불가능 할 경우
		if not os.path.exists(a_oPath_File):
			return
		
		with open(a_oPath_File, "rb") as oRStream:
			self.m_oListMembers = pickle.load(oRStream)
	
	# 회원을 저장한다
	def serializeMembers_ToFile(self, a_oPath_File):
		oPath_Dir = os.path.dirname(a_oPath_File)
		
		# 디렉토리 생성이 필요 할 경우
		if oPath_Dir:
			os.makedirs(oPath_Dir, exist_ok = True)
	
		with open(a_oPath_File, "wb") as oWStream:
			pickle.dump(self.m_oListMembers, oWStream)
			