import os
import sys

from PyQt5.QtCore import QPointF
from PyQt5.QtGui import QVector2D


# 원
class CCircle:
	# 초기화
	def __init__(self, a_oWnd_Main, a_oPos, a_fRadius):
		self.m_oPos = a_oPos
		self.m_oVelocity = QVector2D(0.0, 0.0)
		
		self.m_fRadius = a_fRadius
		self.m_oWnd_Main = a_oWnd_Main
		
	# 상태를 갱신한다
	def onUpdate(self, a_fTime_Delta):
		self.m_oPos += self.m_oVelocity.toPointF() * a_fTime_Delta
		fHeight_MenuBar = self.m_oWnd_Main.menuBar().geometry().height()
		
		fPos_X = min(self.m_oPos.x(), self.m_oWnd_Main.geometry().width() - self.m_fRadius)
		fPos_X = max(fPos_X, self.m_fRadius)
		
		fPos_Y = min(self.m_oPos.y(), self.m_oWnd_Main.geometry().height() - self.m_fRadius)
		fPos_Y = max(fPos_Y, self.m_fRadius + fHeight_MenuBar)
		
		self.m_oPos = QPointF(fPos_X, fPos_Y)
		
		# 왼쪽 or 오른쪽에 부딛쳤을 경우
		if fPos_X <= self.m_fRadius or fPos_X >= self.m_oWnd_Main.geometry().width() - self.m_fRadius:
			self.m_oVelocity = QVector2D(self.m_oVelocity.x() * -1.0, self.m_oVelocity.y())
			
		# 위쪽 or 아래쪽에 부딛쳤을 경우
		if fPos_Y <= self.m_fRadius + fHeight_MenuBar or fPos_Y >= self.m_oWnd_Main.geometry().height() - self.m_fRadius:
			self.m_oVelocity = QVector2D(self.m_oVelocity.x(), self.m_oVelocity.y() * -1.0)
	

	# 물체를 그린다
	def onRender(self, a_oPainter):
		a_oPainter.drawEllipse(self.m_oPos, self.m_fRadius, self.m_fRadius)
		