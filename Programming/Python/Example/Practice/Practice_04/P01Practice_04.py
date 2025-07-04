import os
import sys

"""
Python 과제 4
- 모든 조합 출력하기
- 물건이 3 개 있으며 각 물건의 가격은 서로 다르다 (+ Ex. 50 원, 250 원, 500 원)
- 소지 금액을 입력 받은 후 해당 금액을 모두 소비해서 구입 할 수 있는 물건의 조합을 모두 출력한다

Ex)
소지 금액 입력 : 1000

=====> 구입 가능 조합 <=====
물건 A x 0 개, 물건 B x 0 개, 물건 C x 2 개
물건 A x 0 개, 물건 B x 2 개, 물건 C x 1 개
물건 A x 5 개, 물건 B x 1 개, 물건 C x 1 개
...이하 생략
"""


# Practice 4
def start(args):
	PRICE_STUFF_A = 50
	PRICE_STUFF_B = 250
	PRICE_STUFF_C = 500
	
	nAmount = int(input("소지 금액 : "))
	
	print("\n=====> 구입 가능 조합 <=====")
	i = 0
	
	while i <= nAmount:
		j = 0
		
		while j <= nAmount:
			k = 0
			
			while k <= nAmount:
				nPrice = i + j + k
				
				# 금액을 모두 소비했을 경우
				if nPrice == nAmount:
					nNumStuffsA = i // PRICE_STUFF_A
					nNumStuffsB = j // PRICE_STUFF_B
					nNumStuffsC = k // PRICE_STUFF_C
					
					oMsgA = f"물건 A x {nNumStuffsA} 개"
					oMsgB = f"물건 B x {nNumStuffsB} 개"
					oMsgC = f"물건 C x {nNumStuffsC} 개"
					
					print(f"{oMsgA}, {oMsgB}, {oMsgC}")
				
				k += PRICE_STUFF_C
			
			j += PRICE_STUFF_B
		
		i += PRICE_STUFF_A
