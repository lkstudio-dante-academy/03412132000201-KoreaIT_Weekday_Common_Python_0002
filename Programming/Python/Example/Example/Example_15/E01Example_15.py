import os
import sys

from PyQt5.QtWidgets import QApplication
from Example.Example_15.CWnd_Main import CWnd_Main

"""
패키지 (Package) 란?
- 모듈의 집합을 의미한다. (+ 즉, 패키지를 활용하면 다양한 기능을 특정 그룹으로 분류 시켜서 관리하는 것이
가능하다.)

Python 에서 패키지는 디렉토리를 의미하기 때문에 디렉토리 내부에는 Python 명령문이 작성 된
다양한 파일을 추가해서 관리하는 것이 가능하다. (+ 즉, Python 의 다양한 모듈도 패키지 형태로
관리 된다는 것을 알 수 있다.)

__init__.py 파일이란?
- Python 3.2 이하 버전에서 주로 사용 된 파일로서 __init__.py 파일이 있어야 디렉토리가 패키지로 인식 되었다.
(+ 즉, 현재는 대부분 Python 3.3 이상 버전을 사용하기 때문에 __init__.py 파일이 없어도 된다.)

__init__.py 파일은 디렉토리를 패키지로 인식 시키는 역할 이외에도 패키지 안에 존재하는 모듈을 명시하는 역할도
수행한다. (+ 즉, __init__.py 파일을 활용하면 특정 패키지 안에 있는 모듈을 모두 가져올 수 있는
* (와일드 카드) 를 사용하는 것이 가능하다.)
"""


# Example 15 (패키지)
def start(args):
	oApp = QApplication(args)
	oCanvas = CWnd_Main()
	
	oCanvas.show()
	sys.exit(oApp.exec_())
