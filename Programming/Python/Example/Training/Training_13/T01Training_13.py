import os
import sys

import random

from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from multiprocessing import Pool

"""
Python 연습 문제 13
- 쓰레드 및 프로세스를 활용해서 합계 계산하기
"""


# Training 13
def start(args):
	"""
	리스트 컴프리헨션 (List Comprehension) 이란?
	- 반복문을 이용해 리스트를 생성 할 수 있는 기능을 의미한다. (+ 즉, 리스트 컴프리헨션을 활용하면
	리스트를 생성과 동시에 데이터를 추가하는 것이 가능하다.)
	
	Ex)
	oListValues = [i for i in range(0, 10)]			<- [ 0, 1, 2, ..., 9 ] 리스트 생성 및 할당
	
	위와 같이 리스트 컴프리헨션을 활용하면 리스트를 생성과 동시에 데이터를 추가함으로서 빠르게 리스트를
	생생하는 것이 가능하다. (+ 즉, 리스트를 생성 후 데이터를 추가하는 것 보다 속도가 빠르다는 것을 의미한다.)
	"""
	oListValues = [random.randrange(1, 100) for i in range(0, 1000000)]
	
	nNumValues = len(oListValues) // (os.cpu_count() * 2)
	
	nNumThreads = os.cpu_count() * 2
	nNumThreads += 1 if nNumValues * nNumThreads < len(oListValues) else 0
	
	nVal_Sum = 0
	oTime_Start = datetime.now()
	
	for nVal in oListValues:
		nVal_Sum += nVal
	
	fTime_Delta = (datetime.now() - oTime_Start).total_seconds()
	
	print("=====> 메인 쓰레드 <=====")
	print(f"합계 : {nVal_Sum} ({fTime_Delta} sec)")
	
	"""
	슬라이스 (Slice) 란?
	- 선형 컬렉션 (+ 리스트, 튜플) 과 문자열을 대상으로 특정 구간에 존재하는 데이터를 추출하는 기능을
	의미한다.
	
	Python 슬라이스 사용 방법
	- [시작 인덱스 : 종료 인덱스 : 간격]
	
	Ex)
	oListValues_Origin = [ 1, 2, 3, 4, 5 ]
	
	oListValuesA = oListValues_Origin[0:3]			<- [ 1, 2, 3 ] 추출 및 할당
	oListValuesB = oListValues_Origin[3:5]			<- [ 4, 5 ] 추출 및 할당
	oListValuesC = oListValues_Origin[::-1]			<- [ 5, 4, 3, 2, 1 ] 추출 및 할당
	
	위와 같이 슬라이스를 활용하면 다양한 형태로 데이터를 추출하는 것이 가능하며 종료 인덱스는 추출 결과에
	포함되지 않는다는 특징이 존재한다.
	"""
	oContainerListValues = [oListValues[nNumValues * i:nNumValues * (i + 1)] for i in range(0, nNumThreads)]
	
	oTime_Start = datetime.now()
	nVal_Sum = 0
	
	with ThreadPoolExecutor(nNumThreads) as oExecutor:
		oListResults = oExecutor.map(getVal_Sum, oContainerListValues)
		
		for nVal in oListResults:
			nVal_Sum += nVal
	
	fTime_Delta = (datetime.now() - oTime_Start).total_seconds()
	
	print("\n=====> 멀티 쓰레드 <=====")
	print(f"합계 : {nVal_Sum} ({fTime_Delta} sec)")
	
	nVal_Sum = 0
	oTime_Start = datetime.now()
	
	with Pool(nNumThreads) as oPool:
		oListResults = oPool.map(getVal_Sum, oContainerListValues)
		
		for nVal in oListResults:
			nVal_Sum += nVal
	
	fTime_Delta = (datetime.now() - oTime_Start).total_seconds()
	
	print("\n=====> 멀티 프로세스 <=====")
	print(f"합계 : {nVal_Sum} ({fTime_Delta} sec)")


# 합계를 반환한다
def getVal_Sum(a_oListValues):
	nVal_Sum = 0
	
	for nVal in a_oListValues:
		nVal_Sum += nVal
	
	return nVal_Sum
