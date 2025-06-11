import os
import sys

import socket
from concurrent.futures import ThreadPoolExecutor


# 서버
class CServer:
	# 초기화
	def __init__(self):
		self.m_oServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.m_oServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		
		self.m_oServer.bind(("127.0.0.1", 19080))
		self.m_oServer.listen((2 ** 15) - 1)
		
		self.m_oExecutor = ThreadPoolExecutor()
		
	# 서버를 실행 시킨다
	def run(self):
		oClient, oAddress = self.m_oServer.accept()
		print(f"클라이언트 ({oAddress}) 접속")
		
		self.m_oExecutor.submit(self.handleOnConnection_Client, oClient, oAddress)
		
	# 클라이언트 연결을 처리한다
	def handleOnConnection_Client(self, a_oClient, a_oAddress):
		with a_oClient:
			oBytes = a_oClient.recv(1024)
			print(f"서버 수신 메세지 ({a_oAddress} -> 서버) : {oBytes.decode()}")
			
			a_oClient.send(oBytes)
			a_oClient.close()
			