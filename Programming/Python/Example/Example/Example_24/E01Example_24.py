import os
import sys

import sqlite3

"""
데이터베이스 (Database) 란?
- 효율적으로 관리 할 수 있도록 구성 된 데이터의 집합을 의미한다. (+ 즉,
데이터베이스는 데이터를 저장 할 수 있는 물리적인 저장소라는 것을 알 수 있다.)

DBMS (Database Management System) 이란?
- 데이터베이스를 제어하기 위한 소프트웨어를 의미한다. (+ 즉,
DBMS 는 데이터베이스에 데이터를 저장하거나 읽어들일 수 있는 다양한 기능을 제공한다.)

주요 DBMS 종류
- 관계형 DBMS (RDBMS)			<- MySQL, SQLite 등등...
- 비관계형 DBMS (NoSQL)			<- MongoDB, Redis 등등...

관계형 DBMS (RDBMS) 란?
- 데이터를 행 (Row) 과 열 (Column) 로 구성 된 테이블 (Table) 형태로 저장하고 테이블 간의 관계를 기반으로
데이터를 관리하는 데이터베이스 시스템을 의미한다. (+ 즉, 데이터를 정형화 된 형식으로 관리 한다는 것을
알 수 있다.)

관계형 DBMS 는 현재 가장 많이 활용되는 데이터베이스 시스템이다.

비관계형 DBMS (NoSQL) 란?
- 테이블 형태가 아닌 유연한 형태 (+ Ex. Json 등등...) 로 데이터를 저장하고 관리하는
데이터베이스 시스템을 의미한다. (+ 즉, 관계형 DBMS 에 비해 관리하는 데이터의 형태가 자유롭다는 것을 알 수 있다.)

SQL (Structured Query Language) 이란?
- 관계형 DBMS 를 대상으로 데이터를 조회, 검색, 제거 등을 지시 할 수 있는 언어를 의미한다. (+ 즉,
SQL 을 활용하면 관계형 DBMS 와 서로 상호 작용하는 것이 가능하다.)

SQL 은 비교적 간단한 문법으로 이루어져 있으며 SQL 을 활용하면 관계형 DBMS 를 대상으로 여러 작업을 처리하는 것이
가능하다.

SQLite 란?
- 관계형 DBMS 중 하나로서 서버 없이 단일 파일을 기반으로 동작하는 데이터베이스 시스템을 의미한다. (+ 즉,
SQLite 를 활용하면 네트워크가 연결 되어있지 않는 환경에서도 데이터베이스를 기반으로 데이터를 관리하는 것이
가능하다.)

SQLite 는 서버가 필요 없기 때문에 클라이언트 단에서 주로 사용 되는 데이터베이스 시스템이며
모바일과 같이 비교적 적은 데이터를 단독으로 다루는 환경에서 적합하다. (+ 즉, SQLite 는
여러 사용자가 공유하는 환경에서는 적합하지 않다는 것을 의미한다.)
"""


# Example 24 (데이터베이스)
def start(args):
	"""
	Connection 이란?
	- Python 으로 제작 된 프로그램과 SQLite 데이터베이스 간에 연결을 제어하는 역할을 수행하는
	클래스를 의미한다. (+ 즉, Connection 를 활용하면 데이터베이스에 데이터를 추가하는 등의 작업을
	처리하는 것이 가능하다.)
	"""
	with sqlite3.connect("P_E01Example_24_01.db") as oConnection:
		oSQL_CreateTable = "CREATE TABLE IF NOT EXISTS MemberTable(Name TEXT PRIMARY KEY, PNumber TEXT)"
		
		"""
		Cursor 란?
		- SQL 명령문을 실행하고 실행 결과를 제어하는 역할을 수행하는 클래스를 의미한다. (+ 즉,
		Python 으로 제작 된 프로그램은 Cursor 객체를 통해 SQL 명령문을 데이터베이스에게 전달하는 것이
		가능하다.)
		"""
		oCursor = oConnection.cursor()
		
		"""
		execute 메서드란?
		- SQL 명령문을 실행하는 역할을 수행하는 메서드를 의미한다. (+ 즉, execute 메서드를 활용하면
		데이터베이스에 테이블을 생성하는 등의 작업을 처리하는 것이 가능하다.)
		"""
		oCursor.execute(oSQL_CreateTable)
		
		oSQL_Insert = "INSERT OR IGNORE INTO MemberTable(Name, PNumber) VALUES(?, ?)"
		
		oCursor.execute(oSQL_Insert, [ "회원 A", "1234" ])
		oCursor.execute(oSQL_Insert, [ "회원 B", "1234" ])
		
		"""
		commit 메서드란?
		- 실행 대기 중인 SQL 명령문을 데이터베이스에 반영하는 역할을 수행하는 클래스를 의미한다. (+ 즉,
		commit 메서드를 호출하지 않으면 SQL 명령문의 실행 결과가 데이터베이스에 반영되지 않을 수 있다는 것을
		알 수 있다.)
		"""
		oConnection.commit()
		
		oSQL_Query = "SELECT * FROM MemberTable"
		oCursor.execute(oSQL_Query)
		
		"""
		fetchall 메서드란?
		- SELECT 명령문에 의해서 데이터베이스로부터 가져 온 데이터를 리스트 자료형으로 반환해주는 역할을
		수행하는 메서드를 의미한다. (+ 즉, fetchall 메서드를 활용하면 데이터베이스로부터 가져온 데이터를
		간단하게 순회하는 것이 가능하다.)
		"""
		oResults = oCursor.fetchall()
		
		print("=====> 모든 회원 정보 <=====")
		
		for oResult in oResults:
			oName = oResult[0]
			oPNumber = oResult[1]
			
			print(f"이름 : {oName}")
			print(f"전화 번호 : {oPNumber}\n")
			