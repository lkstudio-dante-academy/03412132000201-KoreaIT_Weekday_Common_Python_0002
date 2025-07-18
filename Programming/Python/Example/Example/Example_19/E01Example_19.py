import os
import sys

from Example.Example_19.CWidget import CWidget

"""
프로퍼티 (Property) 란?
- 접근자 함수를 좀 더 쉽게 사용 할 수 있는 기능으로 프로퍼티를 활용하면 접근자 함수를 변수처럼 제어하는 것이
가능하다. (+ 즉, 변수에 데이터를 할당하거나 변수의 데이터를 읽어들이 듯이 명령문을 작성하는 것이 가능하다.)

Python 에서 접근자는 함수이기 때문에 특정 객체가 지니고 있는 멤버 변수의 값을 변경하거나 읽이들이기 위해서
함수 호출을 해야한다. (+ 즉, 가독성이 떨어진다는 것을 알 수 있다.)

반면 프로퍼티를 활용하면 변수처럼 접근자 함수를 사용하는 것이 가능하기 때문에 가독성이 향상 된다는 장점이
존재한다.

Ex)
class CSomeClass:
	def __init__(self):
		self.m_nVal = 0
		
	@property
	def Val(self):
		return m_nVal
		
	@Val.setter
	def Val(self, a_nVal):
		self.m_nVal = a_nVal
		
oSomeObj = CSomeClass()
oSomeObj.Val = 10

위와 같이 @property 데코레이터와 setter 데코레이터를 활용하면 프로퍼티를 구현하는 것이 가능하다. (+ 즉,
해당 데코레이터로 구현 된 함수는 변수처럼 데이터를 할당하거나 데이터를 가져오는 것이 가능하다.)
"""


# Example 19 (클래스 - 4)
def start(args):
	oWidgetA = CWidget()
	oWidgetB = CWidget()
	
	oWidgetA.Val_Int = 10
	oWidgetA.Val_Real = 3.14
	
	oWidgetB.Val_Int = 20
	oWidgetB.Val_Real = 3.14
	
	print("=====> 위젯 - A <=====")
	oWidgetA.showInfo()
	
	print("\n=====> 위젯 - B <=====")
	oWidgetB.showInfo()
	