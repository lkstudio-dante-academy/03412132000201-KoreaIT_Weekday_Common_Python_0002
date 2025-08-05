import os
import sys


# 이진 탐색 트리
class CTree_BSearch:
	# 순서
	PRE_ORDER = 1
	IN_ORDER = 2
	POST_ORDER = 3
	
	# 노드
	class CNode:
		# 초기화
		def __init__(self, a_tVal):
			self.m_tVal = a_tVal
			
			self.m_oNode_LChild = None
			self.m_oNode_RChild = None
	
	# 초기화
	def __init__(self):
		self.m_oNode_Root = None
	
	# 값을 추가한다
	def addVal(self, a_tVal):
		# 루트 노드가 없을 경우
		if not self.m_oNode_Root:
			self.m_oNode_Root = self.createNode(a_tVal)
			return
		
		oNode = self.m_oNode_Root
		oNode_Parent = None
		
		while oNode != None:
			oNode_Parent = oNode
			
			# 왼쪽 자식으로 이동해야 될 경우
			if a_tVal < oNode.m_tVal:
				oNode = oNode.m_oNode_LChild
			
			else:
				oNode = oNode.m_oNode_RChild
		
		# 왼쪽 자식으로 추가 해야 될 경우
		if a_tVal < oNode_Parent.m_tVal:
			oNode_Parent.m_oNode_LChild = self.createNode(a_tVal)
		
		else:
			oNode_Parent.m_oNode_RChild = self.createNode(a_tVal)
	
	# 값을 제거한다
	def removeVal(self, a_tVal):
		oNode_Remove, oNode_Parent = self.findNode(a_tVal)
		
		# 값 제거가 불가능 할 경우
		if oNode_Remove == None:
			return
		
		# 자식 노드가 모두 존재 할 경우
		if oNode_Remove.m_oNode_LChild != None and oNode_Remove.m_oNode_RChild != None:
			oNode_Parent = oNode_Remove
			oNode_Descendant = oNode_Remove.m_oNode_RChild
			
			while oNode_Descendant.m_oNode_LChild != None:
				oNode_Parent = oNode_Descendant
				oNode_Descendant = oNode_Descendant.m_oNode_LChild
			
			oNode_Remove.m_tVal = oNode_Descendant.m_tVal
			oNode_Remove = oNode_Descendant
		
		# 루트 노드를 제거 할 경우
		if oNode_Remove == self.m_oNode_Root:
			# 제거 할 노드의 왼쪽 자식이 존재 할 경우
			if oNode_Remove.m_oNode_LChild != None:
				self.m_oNode_Root = oNode_Remove.m_oNode_LChild
			
			else:
				self.m_oNode_Root = oNode_Remove.m_oNode_RChild
			
			return
		
		# 왼쪽 자식이 존재 할 경우
		if oNode_Remove.m_oNode_LChild != None:
			# 제거 할 노드가 부모의 왼쪽 자식 일 경우
			if oNode_Remove == oNode_Parent.m_oNode_LChild:
				oNode_Parent.m_oNode_LChild = oNode_Remove.m_oNode_LChild
			
			else:
				oNode_Parent.m_oNode_RChild = oNode_Remove.m_oNode_LChild
		
		else:
			# 제거 할 노드가 부모의 왼쪽 자식 일 경우
			if oNode_Remove == oNode_Parent.m_oNode_LChild:
				oNode_Parent.m_oNode_LChild = oNode_Remove.m_oNode_RChild
			
			else:
				oNode_Parent.m_oNode_RChild = oNode_Remove.m_oNode_RChild
	
	# 값을 탐색한다
	def findVal(self, a_tVal):
		oNode, oNode_Parent = self.findNode(a_tVal)
		return oNode != None
	
	# 노드를 탐색한다
	def findNode(self, a_tVal):
		oNode = self.m_oNode_Root
		oNode_Parent = None
		
		while oNode != None and a_tVal != oNode.m_tVal:
			oNode_Parent = oNode
			
			# 왼쪽 자식으로 이동해야 될 경우
			if a_tVal < oNode.m_tVal:
				oNode = oNode.m_oNode_LChild
			
			else:
				oNode = oNode.m_oNode_RChild
		
		return oNode, oNode_Parent
	
	# 트리를 순회한다
	def enumerate(self, a_nOrder, a_oCallback):
		# 전위 순회 일 경우
		if a_nOrder == CTree_BSearch.PRE_ORDER:
			self.enumerate_ByPreOrder(self.m_oNode_Root, a_oCallback)
		
		# 중위 순회 일 경우
		elif a_nOrder == CTree_BSearch.IN_ORDER:
			self.enumerate_ByInOrder(self.m_oNode_Root, a_oCallback)
		
		# 후위 순회 일 경우
		elif a_nOrder == CTree_BSearch.POST_ORDER:
			self.enumerate_ByPostOrder(self.m_oNode_Root, a_oCallback)
	
	# 트리를 전위 순회한다
	def enumerate_ByPreOrder(self, a_oNode, a_oCallback):
		# 순회가 불가능 할 경우
		if a_oNode == None:
			return
		
		a_oCallback(a_oNode.m_tVal)
		
		self.enumerate_ByPreOrder(a_oNode.m_oNode_LChild, a_oCallback)
		self.enumerate_ByPreOrder(a_oNode.m_oNode_RChild, a_oCallback)
	
	# 트리를 중위 순회한다
	def enumerate_ByInOrder(self, a_oNode, a_oCallback):
		# 순회가 불가능 할 경우
		if a_oNode == None:
			return
		
		self.enumerate_ByInOrder(a_oNode.m_oNode_LChild, a_oCallback)
		a_oCallback(a_oNode.m_tVal)
		
		self.enumerate_ByInOrder(a_oNode.m_oNode_RChild, a_oCallback)
	
	# 트리를 후위 순회한다
	def enumerate_ByPostOrder(self, a_oNode, a_oCallback):
		# 순회가 불가능 할 경우
		if a_oNode == None:
			return
		
		self.enumerate_ByPostOrder(a_oNode.m_oNode_LChild, a_oCallback)
		self.enumerate_ByPostOrder(a_oNode.m_oNode_RChild, a_oCallback)
		
		a_oCallback(a_oNode.m_tVal)
	
	# 노드를 생성한다
	def createNode(self, a_tVal):
		return CTree_BSearch.CNode(a_tVal)
