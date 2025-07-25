import os
import sys

import random
from datetime import datetime

from PyQt5 import uic
from PyQt5.QtCore import Qt, QTimer, QPointF
from PyQt5.QtGui import QPainter, QVector2D
from PyQt5.QtWidgets import QMainWindow, QMessageBox

from Example.Example_22.CCircle import CCircle

oCls_MainWnd = uic.loadUiType("P_E01Example_22_01.ui")[0]


# 메인 윈도우
class CWnd_Main(QMainWindow, oCls_MainWnd):
	# 초기화
	def __init__(self):
		super().__init__()
		
		self.setupUi(self)
		self.setWindowTitle("Example 15")
		
		self.m_oTimer = QTimer(self)
		self.m_oTimer.timeout.connect(self.onUpdate)
		
		self.m_oTimer.start(1)
		oPos = QPointF(self.geometry().width() / 2.0, self.geometry().height() / 2.0)
		
		"""
		random 함수란?
		- 0 ~ 1 범위의 실수를 반환하는 함수를 의미한다. (+ 즉, random 함수는 randrange 함수와 달리
		실수 데이터가 반환 된다는 차이점이 존재한다.)
		"""
		oDirection = QVector2D(random.random() * 2.0 - 1.0, random.random() * 2.0 - 1.0)
		
		self.m_oCircle = CCircle(self, oPos, 50.0)
		self.m_oCircle.m_oVelocity = oDirection.normalized() * 450.0
		
		"""
		datetime 클래스란?
		- 시간과 관련 된 다양한 기능을 제공하는 클래스를 의미한다. (+ 즉, datetime 클래스를 활용하면
		이전 프레임과 현재 프레임 간에 흘러 간 시간 등을 계산하는 것이 가능하다.)
		"""
		self.m_oPrevTime = datetime.now()
		self.m_oStartTime = datetime.now()
		
		nHeight = self.frameGeometry().height() - self.geometry().height()
		self.setGeometry(10, 10 + nHeight, self.geometry().width(), self.geometry().height())
		
		self.move(10, 10)
		self.menuBar().setNativeMenuBar(False)
		
		self.setupMenu()
		
	# 상태를 갱신한다
	def onUpdate(self):
		self.update()
		
		fTime_Delta = (datetime.now() - self.m_oPrevTime).total_seconds()
		self.m_oPrevTime = datetime.now()
		
		self.m_oCircle.onUpdate(fTime_Delta)
		
	# 메뉴를 설정한다
	def setupMenu(self):
		self.actionAbout.triggered.connect(self.handleOnTouch_AboutAction)
	
	# 닫기 이벤트를 수신했을 경우
	def closeEvent(self, a_oEvent):
		nResult = QMessageBox.question(self, "알림", "앱을 종료하시겠습니까?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
		a_oEvent.accept() if nResult == QMessageBox.Yes else a_oEvent.ignore()
	
	# 그리기 이벤트를 수신했을 경우
	def paintEvent(self, a_oEvent):
		oPainter = QPainter(self)
		
		try:
			self.m_oCircle.onRender(oPainter)
		
		finally:
			oPainter.end()
	
	# 키 눌림 이벤트를 수신했을 경우
	def keyPressEvent(self, a_oEvent):
		# Esc 키를 눌렀을 경우
		if a_oEvent.key() == Qt.Key_Escape:
			self.close()
		
	# 설명 액션을 터치를 처리한다
	def handleOnTouch_AboutAction(self):
		QMessageBox.aboutQt(self, "알림")
		