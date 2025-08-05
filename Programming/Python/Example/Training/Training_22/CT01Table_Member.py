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
		
		oSQL_CreateTable = f"CREATE TABLE IF NOT EXISTS {self.m_oName_Table}(Name TEXT PRIMARY KEY, PNumber TEXT)"
		self.m_oCursor.execute(oSQL_CreateTable)
	
	# 회원을 반환한다
	def getMember(self, a_oName):
		oSQL_Select = f"SELECT * FROM {self.m_oName_Table} WHERE Name = ?"
		self.m_oCursor.execute(oSQL_Select, [a_oName])
		
		oResult = self.m_oCursor.fetchall()
		return list(oResult)[0] if oResult else None
	
	# 모든 회원을 반환한다
	def getMembers_All(self):
		oSQL_Select = f"SELECT * FROM {self.m_oName_Table}"
		self.m_oCursor.execute(oSQL_Select)
		
		return self.m_oCursor.fetchall()
	
	# 회원을 추가한다
	def addMember(self, a_oName, a_oPNumber):
		oSQL_Insert = f"INSERT OR IGNORE INTO {self.m_oName_Table}(Name, PNumber) VALUES(?, ?)"
		self.m_oCursor.execute(oSQL_Insert, [a_oName, a_oPNumber])
	
	# 회원을 제거한다
	def removeMember(self, a_oName):
		oSQL_Delete = f"DELETE FROM {self.m_oName_Table} WHERE Name = ?"
		self.m_oCursor.execute(oSQL_Delete, [a_oName])
		