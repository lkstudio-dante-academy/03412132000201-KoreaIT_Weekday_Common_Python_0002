import os
import sys

from Example.Example_20.CWidget import CWidget

"""
Object 클래스란?
- Python 에서 정의 한 모든 클래스를 직접 or 간접적으로 상속하는 최상단 클래스를 의미한다. (+ 즉,
Python 의 모든 클래스는 Object 클래스가 지니고 있는 멤버를 사용하는 것이 가능하다.)

Object 클래스는 __init__ 함수를 비롯한 다양한 함수를 지원하며 해당 함수를 자식 클래스에서
재정의 함으로서 자식 클래스만에 명령문을 작성하는 것이 가능하다.

Ex)
class CSomeClass:
	def __str__(self):
		return "Some Class 정보"
		
oSomeObj = CSomeClass()
print(oSomeObj)

위와 같이 Object 클래스는 __str__ 함수를 지원하며 해당 함수를 자식 클래스에서 재정의하면
print 와 같은 함수를 사용해서 객체의 정보를 출력하는 것이 가능하다.
"""


# Example 20 (클래스 - 5)
def start(args):
	oWidget = CWidget()
	
	"""
	issubclass 함수란?
	- 클래스가 특정 클래스를 상속하고 있는 검사하는 역할을 수행하는 함수를 의미한다. (+ 즉,
	issubclass 함수를 활용하면 부모 클래스를 검사해서 제어하는 것이 가능하다.)
	
	isinstance 함수란?
	- 특정 클래스로부터 생성 된 객체인지 검사하는 역할을 수행하는 함수를 의미한다. (+ 즉,
	해당 함수를 활용하면 안전한 다운 캐스팅이 가능하다.)
	"""
	print("=====> 캐스팅 결과 <=====")
	print(issubclass(CWidget, object))
	print(isinstance(oWidget, object))
	print(isinstance(oWidget, CWidget))
	
	print("\n=====> Object 정보 <=====")
	print(dir(object))
	
	print("\n=====> 위젯 정보 <=====")
	print(oWidget)
