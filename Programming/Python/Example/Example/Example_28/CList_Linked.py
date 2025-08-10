import os
import sys


# 연결 리스트
class CList_Linked:
	# 노드
	class CNode:
		# 초기화
		def __init__(self, a_tVal):
			self.m_tVal = a_tVal
			self.m_oNode_Next = None
	
	# 초기화
	def __init__(self):
		self.m_nNumValues = 0
		self.m_oNode_Head = self.createNode(None)
	
	# 값을 반환한다
	def getVal(self, a_nIdx):
		oNode = self.findNode_At(a_nIdx)
		return oNode.m_tVal
	
	# 값을 추가한다
	def addVal(self, a_tVal):
		oNode_Tail = self.m_oNode_Head
		
		while oNode_Tail.m_oNode_Next != None:
			oNode_Tail = oNode_Tail.m_oNode_Next
		
		oNode_Tail.m_oNode_Next = self.createNode(a_tVal)
		self.m_nNumValues += 1
	
	# 값을 추가한다
	def insertVal(self, a_nIdx, a_tVal):
		oNode_New = self.createNode(a_tVal)
		oNode_Prev = self.findNode_AtPrev(a_nIdx)
		
		oNode_New.m_oNode_Next = oNode_Prev.m_oNode_Next
		oNode_Prev.m_oNode_Next = oNode_New
		
		self.m_nNumValues += 1
	
	# 값을 제거한다
	def removeVal(self, a_tVal):
		oNode_Prev = self.m_oNode_Head
		
		while oNode_Prev.m_oNode_Next != None and oNode_Prev.m_oNode_Next.m_tVal != a_tVal:
			oNode_Prev = oNode_Prev.m_oNode_Next
		
		oNode_Remove = oNode_Prev.m_oNode_Next
		
		# 값 제거가 불가능 할 경우
		if oNode_Remove == None:
			return
		
		oNode_Prev.m_oNode_Next = oNode_Remove.m_oNode_Next
		self.m_nNumValues -= 1
	
	# 노드를 탐색한다
	def findNode_At(self, a_nIdx):
		oNode = self.findNode_AtPrev(a_nIdx)
		return oNode.m_oNode_Next
	
	# 노드를 탐색한다
	def findNode_AtPrev(self, a_nIdx):
		oNode = self.m_oNode_Head
		
		for i in range(0, a_nIdx):
			oNode = oNode.m_oNode_Next
		
		return oNode
	
	# 노드를 생성한다
	def createNode(self, a_tVal):
		return CList_Linked.CNode(a_tVal)
