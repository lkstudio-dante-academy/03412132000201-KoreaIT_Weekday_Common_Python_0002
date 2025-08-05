import os
import sys

import random

from Example.Example_29.CTree_BSearch import CTree_BSearch
from Example.Example_29.CTable_Hash import CTable_Hash
from Example.Example_29.CGraph_List import CGraph_List

"""
비선형 자료구조 종류
- 트리
- 해시 테이블
- 그래프

트리 (Tree) 란?
- 데이터를 계층적인 구조로 관리하는 자료구조를 의미한다. (+ 즉, 트리에 의해서 관리 되는 데이터는 상/하 관계를
형성 한다는 것을 알 수 있다.)

트리는 노드를 통해 데이터를 관리하며 자식 노드의 개수에 따라 N 차 트리 라고 한다.

프로그래밍에서 주로 활용되는 트리는 자식이 최대 2 개인 이진 트리 (Binary Tree) 이며 이진 트리 구조를 활용하면
데이터를 빠르게 탐색하는 이진 탐색 트리 (Binary Search Tree) 를 구현하는 것이 가능하다.

트리 관련 주요 용어
- 노드				<- 트리의 구성 요소
- 루트 노드			<- 부모 노드가 없는 노드
- 리프 노드			<- 자식 노드가 없는 노드
- 부모 노드			<- 특정 노드의 상위 노드
- 자식 노드			<- 특정 노드의 하위 노드
- 형제 노드			<- 동일한 부모 노드의 다른 자식 노드
- 서브 트리			<- 특정 노드를 루트 노드로 하는 하위 트리
- 레벨				<- 트리의 각 계층

이진 탐색 트리 (Binary Search Tree) 란?
- 이진 탐색을 수행 할 수 있는 트리를 의미한다. (+ 즉, 이진 탐색 트리는 데이터를 빠르게 탐색하는 것이
가능하다.)

이진 탐색 트리는 특정 규칙에 따라 데이터를 추가함으로서 데이터를 빠르게 탐색하는 것이 가능하다.

이진 탐색 트리 데이터 추가 규칙
- 새로운 노드 (데이터) 는 항상 리프 노드에 추가 된다.
- 노드는 데이터의 비교를 통해 작은 데이터는 왼쪽에 위치하고 크거나 같은 데이터는 오른쪽에 위치한다.

위와 같이 이진 탐색 트리는 특정 노드를 기준으로 작은 데이터는 왼쪽에 위치하고 큰 데이터를 오른쪽에
위치 시킴으로서 탐색을 빠르게 수행하는 것이 가능하다. (+ 즉, 이진 탐색 트리에서 특정 노드에 있는 데이터는
항상 왼쪽 서브 트리와 오른쪽 서브 트리의 중간 데이터가 있다는 것을 알 수 있다.)

트리 순회 (Tree Traversal) 란?
- 트리에 존재하는 모든 노드를 방문하는 것을 의미한다. (+ 즉, 순회를 활용하면 트리에 존재하는 모든 노드에
접근하는 것이 가능하다.)

트리 순회 종류
- 전위 순회 (Pre Order Tree Traversal)
- 중위 순회 (In Order Tree Traversal)
- 후위 순회 (Post Order Tree Traversal)
- 레벨 순회 (Level Order Tree Traversal)

전위 순회 (Pre Order Tree Traversal) 란?
- 노드 -> 왼쪽 서브 트리 -> 오른쪽 서브 트리 순서로 트리를 순회하는 방법을 의미한다.

중위 순회 (In Order Tree Traversal) 란?
- 왼쪽 서브 트리 -> 노드 -> 오른쪽 서브 트리 순서로 트리를 순회하는 방법을 의미한다.

후위 순회 (Post Order Tree Traversal) 란?
- 왼쪽 서브 트리 -> 오른쪽 서브 트리 -> 노드 순서로 트리를 순회하는 방법을 의미한다.

레벨 순회 (Level Order Traversal) 란?
- 계층 별로 트리를 순회하는 방법을 의미한다.

해시 테이블 (Hash Table) 이란?
- 해시 값을 기반으로 데이터를 빠르게 탐색하는 자료구조를 의미한다. (+ 즉, 해시 테이블을 활용하면 데이터를
빠르게 탐색하는 것이 가능하다.)

해시 테이블은 이진 탐색 트리와 같이 데이터를 추가 할 때 미리 계산 된 위치에 추가함으로서 데이터를 빠르게
탐색하는 자료구조이다.

해시 테이블은 내부적인 구현 방법에 따라 개방 주소법 (Open Address) 과 체인법 (Chaining) 으로 구분 된다.

해시 테이블 관련 주요 용어
- 충돌				<- 동일한 해시 값이 나오는 현상
- 클러스터			<- 데이터가 특정 부분에 밀집 되어 있는 현상

이진 탐색 트리 (Binary Search Tree) vs 해시 테이블 (Hash Table)
- 이진 탐색 트리는 최선의 경우 든 최악의 경우 든 O(logN) 의 성능을 보장하기 때문에 안정적이라는 장점이
존재한다.

단, 이진 탐색 트리는 균형이 무너졌을 경우 성능이 O(N) 으로 떨어지기 때문에 데이터가 추가 되거나 제거 될 때
균형이 무너지지 않게 추가적인 연산이 필요하다. (+ 즉, 데이터가 빈번하게 추가/제거 될 경우 성능이 떨어진다는 것을
알 수 있다.)

반면 해시 테이블은 최선의 경우 O(1) 로 빠르게 데이터를 탐색하는 것이 가능하다. (+ 즉, 한번이 비교로
데이터의 존재 여부를 파악하는 것이 가능하다.)

단, 해시 테이블은 내부적으로 충돌이 많이 발생하면 탐색 성능이 O(N) 으로 떨어지는 단점이 있기 때문에
충돌을 최소화 시키기 위해서 많은 메모리를 요구한다. (+ 즉, 메모리가 부족한 환경에서는 사용이 불가능하다는 것을
알 수 있다.)

그래프 (Graph) 란?
- 정점과 간선의 집합으로 데이터 간의 관계를 표현하는 자료구조를 의미한다. (+ 즉, 그래프를 활용하면
데이터 간의 복잡한 관계를 표현하는 것이 가능하다.)

그래프는 간선의 방향 유무에 따라 방향성 그래프와 무방향성 그래프가 존재하며 간선의 표현 방식에 따라
인접 행렬 방식 (Adjacency Matrix Graph) 과 인접 리스트 방식 (Adjacency List Graph) 으로 구현이 가능하다.

그래프 탐색 (Graph Search) 란?
- 그래프에 존재하는 모든 정점을 방문하는 것을 의미한다. (+ 즉, 탐색을 활용하면 그래프에 존재하는 모든 정점에
접근하는 것이 가능하다.)

그래프 탐색 종류
- 깊이 우선 탐색 (Depth First Search)
- 너비 우선 탐색 (Breadth First Search)

깊이 우선 탐색 (Depth First Search) 이란?
- 출발 정점에서 인접한 정점 중 하나를 선택해서 탐색을 이어나가는 방법을 의미한다. (+ 즉, 깊이 우선 탐색은
현재 정점에서 인접한 정점 하나를 타고 들어간다는 것을 알 수 있다.)

너비 우선 탐색 (Breadth First Search) 이란?
- 출발 정점에서 인접한 정점으로 탐색 범위를 확장 시켜나가는 탐색 방법을 의미한다. (+ 즉, 너비 우선 탐색은
현재 정점에서 인접한 모든 정점을 탐색 후 다른 정점의 인접한 정점을 탐색한다는 것을 알 수 있다.)

인접 행렬 방식 (Adjacency Matrix Graph) 이란?
- 간선을 행렬로 표현하는 방법을 의미한다. (+ 즉, 인접 행렬 방식은 간선 정보가 하나의 행렬로
모두 표현 된다는 것을 알 수 있다.)

인접 리스트 방식 (Adjacency List Graph) 이란?
- 간선을 연결 리스트로 표현하는 방법을 의미한다. (+ 즉, 인접 리스트 방식은 간선 정보가 각 정점 마다
개별적으로 존재한다는 것을 알 수 있다.)

인접 행렬 방식 (Adjacency Matrix Graph) vs 인접 리스트 방식 (Adjacency List Graph)
- 인접 행렬 방식은 행렬을 통해 간선을 표현하기 때문에 간선의 개수가 적을 경우 메모리가 낭비되는 단점이 존재한다.

반면, 인접 리스트 방식은 연결 리스트를 통해 간선을 표현하기 때문에 간선의 개수가 많을 경우 탐색 성능이
떨어지는 단점이 존재한다.

따라서 간선의 개수가 적을 경우 인접 리스트 방식이 좀 더 유리하며 간선의 개수가 많을 경우 인접 행렬 방식이
좀 더 좋은 선택이라는 것을 알 수 있다.
"""


# Example 29 (이진 탐색 트리)
def start(args):
	oTree_BSearch = CTree_BSearch()
	
	for i in range(0, 10):
		nVal = random.randrange(1, 100)
		oTree_BSearch.addVal(nVal)
	
	print("=====> 이진 탐색 트리 - 전위 순회 <=====")
	oTree_BSearch.enumerate(CTree_BSearch.PRE_ORDER, printVal_BSearchTree)
	
	print("\n\n=====> 이진 탐색 트리 - 중위 순회 <=====")
	oTree_BSearch.enumerate(CTree_BSearch.IN_ORDER, printVal_BSearchTree)
	
	print("\n\n=====> 이진 탐색 트리 - 후위 순회 <=====")
	oTree_BSearch.enumerate(CTree_BSearch.POST_ORDER, printVal_BSearchTree)
	
	nVal_Remove = int(input("\n\n정수 입력 (제거) : "))
	oTree_BSearch.removeVal(nVal_Remove)
	
	print("\n=====> 이진 탐색 트리 - 전위 순회 (제거 후) <=====")
	oTree_BSearch.enumerate(CTree_BSearch.PRE_ORDER, printVal_BSearchTree)
	
	print("\n\n=====> 이진 탐색 트리 - 중위 순회 (제거 후) <=====")
	oTree_BSearch.enumerate(CTree_BSearch.IN_ORDER, printVal_BSearchTree)
	
	print("\n\n=====> 이진 탐색 트리 - 후위 순회 (제거 후) <=====")
	oTree_BSearch.enumerate(CTree_BSearch.POST_ORDER, printVal_BSearchTree)
	
	oTable_Hash = CTable_Hash()
	
	for i in range(0, 10):
		nVal = random.randrange(1, 100)
		oTable_Hash.addVal(nVal)
	
	print("\n\n=====> 해시 테이블 <=====")
	oTable_Hash.enumerate(printVal_HashTable)
	
	oGraph_List = CGraph_List()
	oGraph_List.addVertex("A")
	oGraph_List.addVertex("B")
	oGraph_List.addVertex("C")
	oGraph_List.addVertex("D")
	oGraph_List.addVertex("E")
	oGraph_List.addVertex("F")
	
	oGraph_List.addEdge("A", "B")
	oGraph_List.addEdge("A", "C")
	oGraph_List.addEdge("A", "D")
	
	oGraph_List.addEdge("B", "E")
	oGraph_List.addEdge("B", "F")
	oGraph_List.addEdge("B", "A")
	
	oGraph_List.addEdge("C", "B")
	oGraph_List.addEdge("C", "D")
	oGraph_List.addEdge("C", "E")
	
	oGraph_List.addEdge("D", "F")
	oGraph_List.addEdge("D", "A")
	oGraph_List.addEdge("D", "B")
	
	oGraph_List.addEdge("E", "C")
	oGraph_List.addEdge("E", "D")
	oGraph_List.addEdge("E", "F")
	
	oGraph_List.addEdge("F", "A")
	oGraph_List.addEdge("F", "B")
	oGraph_List.addEdge("F", "C")
	
	print("\n\n=====> 그래프 - 깊이 우선 탐색 <=====")
	oGraph_List.enumerate("A", CGraph_List.DEPTH_FIRST, printVal_Graph)
	
	print("\n\n=====> 그래프 - 너비 우선 탐색 <=====")
	oGraph_List.enumerate("A", CGraph_List.BREADTH_FIRST, printVal_Graph)
	
	print()


# 값을 출력한다
def printVal_HashTable(a_nIdx, a_nVal):
	print(f"{a_nIdx}:{a_nVal}, ", end = "")


# 값을 출력한다
def printVal_BSearchTree(a_nVal):
	print(f"{a_nVal}, ", end = "")


# 값을 출력한다
def printVal_Graph(a_oKey):
	print(f"{a_oKey}, ", end = "")
	