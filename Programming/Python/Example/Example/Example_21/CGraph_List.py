import os
import sys


# 그래프
class CGraph_List:
	# 순서
	DEPTH_FIRST = 1
	BREADTH_FIRST = 2
	
	# 정점
	class CVertex:
		# 초기화
		def __init__(self, a_tKey):
			self.m_tKey = a_tKey
			self.m_oListEdges = []
			
	# 간선
	class CEdge:
		# 초기화
		def __init__(self, a_oVertex_From, a_oVertex_To):
			self.m_oVertex_From = a_oVertex_From
			self.m_oVertex_To = a_oVertex_To
			
	# 초기화
	def __init__(self):
		self.m_oListVertices = []
			
	# 정점을 추가한다
	def addVertex(self, a_tKey):
		oVertex = self.findVertex(a_tKey)
		
		# 정점 추가가 불가능 할 경우
		if oVertex != None:
			return
		
		oVertex = self.createVertex(a_tKey)
		self.m_oListVertices.append(oVertex)

	# 간선을 추가한다
	def addEdge(self, a_tFrom, a_tTo):
		oEdge = self.findEdge(a_tFrom, a_tTo)
		
		# 간선 추가가 불가능 할 경우
		if oEdge != None:
			return
		
		oEdge = self.createEdge(a_tFrom, a_tTo)
		
		oVertex_From = self.findVertex(a_tFrom)
		oVertex_From.m_oListEdges.append(oEdge)
		

	# 정점을 제거한다
	def removeVertex(self, a_tKey):
		oVertex = self.findVertex(a_tKey)
		
		# 정점 제거가 불가능 할 경우
		if oVertex == None:
			return
		
		self.m_oListVertices.remove(oVertex)

	# 간선을 제거한다
	def removeEdge(self, a_tFrom, a_tTo):
		oEdge = self.findEdge(a_tFrom, a_tTo)
		
		# 간선 제거가 불가능 할 경우
		if oEdge == None:
			return
		
		oEdge.m_oVertex_From.m_oListEdges.remove(oEdge)
	
	# 정점을 탐색한다
	def findVertex(self, a_tKey):
		for oVertex in self.m_oListVertices:
			# 정점이 존재 할 경우
			if a_tKey == oVertex.m_tKey:
				return oVertex
			
		return None

	# 간선을 탐색한다
	def findEdge(self, a_tFrom, a_tTo):
		oVertex_From = self.findVertex(a_tFrom)
		
		# 간선 탐색이 불가능 할 경우
		if oVertex_From == None:
			return None
		
		for oEdge in oVertex_From.m_oListEdges:
			# 목적지가 존재 할 경우
			if a_tTo == oEdge.m_oVertex_To.m_tKey:
				return oEdge
			
		return None
	
	# 그래프를 순회한다
	def enumerate(self, a_tKeyStart, a_nOrder, a_oCallback):
		# 깊이 우선 탐색 일 경우
		if a_nOrder == CGraph_List.DEPTH_FIRST:
			self.enumerate_ByDFS(a_tKeyStart, a_oCallback)
			
		# 너비 우선 탐색 일 경우
		elif a_nOrder == CGraph_List.BREADTH_FIRST:
			self.enumerate_ByBFS(a_tKeyStart, a_oCallback)
	
	# 그래프를 순회한다
	def enumerate_ByDFS(self, a_tKey_Start, a_oCallback):
		oListVertices_Visit = []
		self.enumerate_ByDFS_Internal(a_tKey_Start, a_oCallback, oListVertices_Visit)
		
	# 그래프를 순회한다
	def enumerate_ByDFS_Internal(self, a_tKey, a_oCallback, a_oListVertices_Visit):
		a_oCallback(a_tKey)
		a_oListVertices_Visit.append(a_tKey)
		
		oVertex = self.findVertex(a_tKey)
		
		for oEdge in oVertex.m_oListEdges:
			# 순회가 불가능 할 경우
			if oEdge.m_oVertex_To.m_tKey in a_oListVertices_Visit:
				continue
				
			tKey_ToVertex = oEdge.m_oVertex_To.m_tKey
			self.enumerate_ByDFS_Internal(tKey_ToVertex, a_oCallback, a_oListVertices_Visit)
	
	# 그래프를 순회한다
	def enumerate_ByBFS(self, a_tKey_Start, a_oCallback):
		oListVertices = []
		oListVertices_Visit = []
		
		oListVertices.append(a_tKey_Start)
		
		while len(oListVertices) > 0:
			tKey = oListVertices.pop(0)
			
			# 순회가 불가능 할 경우
			if tKey in oListVertices_Visit:
				continue
			
			a_oCallback(tKey)
			oListVertices_Visit.append(tKey)
			
			oVertex = self.findVertex(tKey)
			
			for oEdge in oVertex.m_oListEdges:
				oListVertices.append(oEdge.m_oVertex_To.m_tKey)
		
	# 정점을 생성한다
	def createVertex(self, a_tKey):
		return CGraph_List.CVertex(a_tKey)

	# 간선을 생성한다
	def createEdge(self, a_tFrom, a_tTo):
		oVertex_From = self.findVertex(a_tFrom)
		oVertex_To = self.findVertex(a_tTo)
		
		return CGraph_List.CEdge(oVertex_From, oVertex_To)
