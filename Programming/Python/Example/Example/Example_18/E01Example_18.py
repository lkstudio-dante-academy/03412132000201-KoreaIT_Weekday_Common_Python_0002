import os
import sys

import socket
import threading

from Example.Example_18.CServer import CServer

"""
소켓 (Socket) 이란?
- 네트워크로 연결 된 호스트 간에 데이터를 주고 받을 수 있는 수단을 의미한다. (+ 즉, 소켓을 활용하면
네트워크를 통해 다른 호스트에 데이터를 전송하는 것이 가능하다.)

호스트 간에 네트워크를 통해 데이터를 주고 받기 위해서는 정해진 규약 (Protocol) 이 필요하며
현재 가장 많이 활용되는 규약은 TCP (Transmission Control Protocol) 와
UDP (User Datagram Protocol) 이다.

또한 호스트 간에 데이터를 주고 받기 위해서는 호스트를 식별하기 위한 정보가 필요하며 이를
IP 주소 (Internet Protocol Address) 와 포트 번호 (Port Number) 라고 한다.

IP 주소는 호스트를 식별하기 위한 주소를 의미하며 포트 번호는 호스트에서 실행 중인 프로그램이 생성 한 소켓을
식별하기 위한 번호이다. (+ 즉, IP 주소는 네트워크 상에서 중복되지 않는 식별자를 의미하며 포트 번호는
프로그램 상에서 중복되지 않는 식별자를 의미한다.)

Python TCP 서버 소켓 생성 및 동작 과정
- 소켓 생성 및 주소 (+ IP 주소 및 포트 번호) 할당
- 리스닝 소켓 설정
- 클라이언트 접속 대기
- 클라이언트 연결 및 데이터 송/수신

Python TCP 클라이언트 소켓 생성 과정
- 소켓 생성 및 주소 할당 (+ 단, 주소 할당은 생략 가능)
- 서버 접속 요청
- 서버 연결 및 데이터 송/수신

서버 소켓 (Server Socket) 이란?
- 클라이언트의 접속을 제어하는 소켓을 의미한다. (+ 즉, TCP 는 연결 된 소켓 간에 데이터를 송/수신하는
프로토콜이기 때문에 데이터를 송/수신하기 전에 연결 과정이 필요하며 이를 제어하는 소켓이 서버 소켓이다.)

단, 서버 소켓은 접속만을 제어하기 때문에 클라이언트와 연결 되면 해당 클라이언트와 데이터를 송/수신하기 위한
소켓이 별도로 생성 된다.
"""


# Example 18 (소켓)
def start(args):
	oServer = CServer()
	
	oThread_Server = threading.Thread(target = oServer.run)
	oThread_Client = threading.Thread(target = main_Client)
	
	oThread_Server.daemon = True
	oThread_Client.daemon = True
	
	oThread_Server.start()
	oThread_Client.start()
	
	oThread_Server.join()
	oThread_Client.join()
	
	
# 클라이언트 쓰레드 진입 함수
def main_Client():
	"""
	아래와 같이 socket 함수를 활용하면 데이터를 송/수신 하기 위한 소켓을 생성하는 것이 가능하며
	소켓을 생성하기 위해서는 주소 체계와 프로토콜을 지정 해 줄 필요가 있다. (+ 즉, 아래의 경우는
	IP 버전 4 기반의 TCP 로 데이터를 송/수신하는 소켓을 생성하고 있다.)
	"""
	oSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	"""
	connect 함수란?
	- 서버 소켓에게 연결 요청을 송신하는 역할을 수행하는 함수를 의미한다. (+ 즉, connect 함수를 활용하면
	서버 소켓에게 연결 요청을 전송하는 것이 가능하다.)
	"""
	oSocket.connect(("127.0.0.1", 19080))
	
	oMsg = input("\n메세지 입력 : ")
	oSocket.send(oMsg.encode())
	
	"""
	getsockname 함수란?
	- 로컬 호스트의 주소를 가져오는 역할을 수행하는 함수를 의미한다. (+ 즉, getsockname 함수를 활용하면
	특정 클라이언트 소켓의 주소를 가져오는 것이 가능하다.)
	"""
	oAddress = oSocket.getsockname()
	
	oBytes = oSocket.recv(1024)
	print(f"클라이언트 수신 메세지 (서버 -> {oAddress}) : {oBytes.decode()}")
	