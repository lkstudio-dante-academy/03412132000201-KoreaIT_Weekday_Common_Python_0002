import os
import sys

import sqlite3


# 회원 테이블
class CTable_Member:
	# 초기화
	def __init__(self, a_oPath_DB):
		self.m_oName_Table = "MemberTable"
		
		self.m_oConnection = sqlite3.connect(a_oPath_DB)
		self.m_oCursor = self.m_oConnection.cursor()
		
		oSQL_CreateTable = "CREATE TABLE IF NOT EXISTS MemberTable(Name TEXT PRIMARY KEY, PNumber TEXT)"
		self.m_oCursor.execute(oSQL_CreateTable)
	
	# 모든 회원을 반환한다
	def getMembers_All(self):
		oSQL_Select = "SELECT * FROM MemberTable"
		self.m_oCursor.execute(oSQL_Select)
		
		return self.m_oCursor.fetchall()
	
	# 회원을 추가한다
	def addMember(self, a_oName, a_oPNumber):
		oSQL_Insert = "INSERT OR IGNORE INTO MemberTable(Name, PNumber) VALUES(?, ?)"
		self.m_oCursor.execute(oSQL_Insert, [a_oName, a_oPNumber])
	