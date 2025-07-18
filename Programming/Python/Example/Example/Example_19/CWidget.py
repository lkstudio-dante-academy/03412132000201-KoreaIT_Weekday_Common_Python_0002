import os
import sys


# 위젯
class CWidget:
	# 초기화
	def __init__(self):
		self.m_nVal = 0
		self.m_fVal = 0.0
		
	# 값을 반환한다
	@property
	def Val_Int(self):
		"""
		@property 데코레이터란?
		- Getter 프로퍼티를 구현 할 수 있는 역할을 수행하는 데코레이터를 의미한다. (+ 즉,
		@property 데코레이터가 명시 된 함수는 변수의 데이터를 가져오듯이 명령문을 작성하는 것이 가능하다.)
		"""
		return self.m_nVal
	
	# 값을 반환한다
	@property
	def Val_Real(self):
		return self.m_fVal
	
	# 값을 변경한다
	@Val_Int.setter
	def Val_Int(self, a_nVal):
		"""
		위와 같이 setter 데코레이터를 활용하면 setter 프로퍼티를 구현하는 것이 가능하다. (+ 즉,
		setter 데코레이터가 명시 된 함수는 변수에 데이터를 할당하듯이 명령문을 작성하는 것이 가능하다.)
		"""
		self.m_nVal = a_nVal
		
	# 값을 변경한다
	@Val_Real.setter
	def Val_Real(self, a_fVal):
		self.m_fVal = a_fVal
		
	# 정보를 출력한다
	def showInfo(self):
		print(f"정수 : {self.Val_Int}")
		print(f"실수 : {self.Val_Real}")
		