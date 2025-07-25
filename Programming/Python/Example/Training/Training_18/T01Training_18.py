import os
import sys

import time
import random

from Training.Training_18.CUnit import CPlayer, CMonster, CMonster_Named
from Training.Training_18.CEquip import CEquip

"""
Python 연습 문제 18
- 전투 시뮬레이션 구현하기
- 유닛은 플레이어와 몬스터 구성된다
- 몬스터는 일반 몬스와 네임드 몬스터 구성된다
- 네임드 몬스터는 일정 확률로 크리티컬 대미지를 입힌다
- 프로그램이 시작되면 플레이어의 스탯은 사용자로부터 입력 받는다
- 스탯은 체력, 공격력, 방어력으로 구성된다
- 몬스터는 랜덤하게 생성된다
- 플레이어 스탯을 입력 받고 몬스터가 생성되었으면 서로 번갈아가면서 상대방을 공격한다
- 공격시 피해량은 단순하게 공격력 - 방어력 규칙으로 산출한다
- 피해를 입어서 체력이 0 이하가 되면 공격을 중지하고 승리자를 출력 후 프로그램을 종료한다

Ex)
플레이어 체력 입력 : 100
플레이어 공격력 입력 : 25
플레이어 방어력 입력 : 10

플레이어에게 추가적으로 장비 지급 (+ 지급 된 장비는 기본 스탯에 추가 X)

플레이어 장비 종류
- 무기 (+ 공격력 5 ~ 10)
- 방어구 (+ 방어력 2 ~ 5)

Ex)
공격력 7 무기가 추가적으로 지급 되었습니다.

몬스터의 스탯은 플레이어 각 스탯의 50 % ~ 150 % 범위에서 랜덤하게 설정
(+ Ex. 몬스터의 체력 : 50, 공격력 : 30, 방어력 : 15)

=====> 플레이어 -> 몬스터 공격 후 <=====
플레이어 체력 : 100
몬스터 체력 : 40
"""


# Training 18
def start(args):
	nHp_Player = int(input("플레이어 체력 입력 : "))
	nAtk_Player = int(input("플레이어 공격력 입력 : "))
	nDef_Player = int(input("플레이어 방어력 입력 : "))
	
	oPlayer = CPlayer(nHp_Player, nAtk_Player, nDef_Player)
	oMonster = createMonster(oPlayer)
	
	oEquip = createEquip()
	oPlayer.setEquip(oEquip)
	
	oMsgA = f"{oEquip.getStr_Ability()} {oEquip.m_nVal}"
	oMsgB = f"{oEquip.getStr_Type()} 가 지급되었습니다."
	
	print(f"\n{oMsgA} {oMsgB}\n")
	time.sleep(1.5)
	
	while True:
		oPlayer.attack(oMonster)
		
		print("=====> 플레이어 -> 몬스터 공격 후 <=====")
		print(f"플레이어 체력 : {oPlayer.m_nHp}")
		print(f"몬스터 체력 : {oMonster.m_nHp}\n")
		
		# 몬스터가 사망했을 경우
		if oMonster.m_nHp <= 0:
			break
			
		time.sleep(0.5)
		oMonster.attack(oPlayer)
		
		print("=====> 몬스터 -> 플레이어 공격 후 <=====")
		print(f"플레이어 체력 : {oPlayer.m_nHp}")
		print(f"몬스터 체력 : {oMonster.m_nHp}\n")
		
		# 플레이어가 사망했을 경우
		if oPlayer.m_nHp <= 0:
			break
			
		time.sleep(0.5)
		
	# 플레이어가 승리했을 경우
	if oPlayer.m_nHp > 0:
		print("플레이어가 승리했습니다.")
		
	else:
		print("몬스터가 승리했습니다.")
	
	
# 장비를 생성한다
def createEquip():
	oListInfos_Val = [
		(5, 10), (2, 5)
	]
	
	nType = random.randrange(0, CEquip.TYPE_ARMOR + 1)
	nVal = random.randrange(oListInfos_Val[nType][0], oListInfos_Val[nType][1] + 1)
	
	return CEquip(nType, nVal)

	
# 몬스터를 생성한다
def createMonster(a_oPlayer):
	nHp_Monster = int(a_oPlayer.m_nHp * (random.randrange(50, 151) / 100))
	nAtk_Monster = int(a_oPlayer.m_nAtk * (random.randrange(50, 151) / 100))
	nDef_Monster = int(a_oPlayer.m_nDef * (random.randrange(50, 151) / 100))
	
	return CMonster(nHp_Monster, nAtk_Monster, nDef_Monster) \
		if random.randrange(0, 2) <= 0 else CMonster_Named(nHp_Monster, nAtk_Monster, nDef_Monster)
