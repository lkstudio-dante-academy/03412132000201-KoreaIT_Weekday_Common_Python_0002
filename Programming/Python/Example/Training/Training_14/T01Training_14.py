import os
import sys

"""
Python 연습 문제 14
- 중위 표기법 -> 후위 표기법 으로 변환하기
- 중위 표기법으로 된 수식을 후위 표기법으로 변환하기

중위 표기법 -> 후위 표기법 변환 규칙
- 중위 표기법으로 된 수식을 왼쪽 -> 오른쪽 방향으로 토큰을 읽어들인다

- 토큰이 피연산자 일 경우 그대로 수식에 출력한다.

- 토큰이 연산자 일 경우 스택에 보관한다. (+ 단, 스택에 이미 연산자가 존재 할 경우 우선 순위를 비교해서
우선 순위가 가장 높은 연산자가 스택의 Top 위치에 저장 되도록 한다.)

- 더이상 읽어들일 토큰이 없을 경우 스택에 남아 있는 모든 연산자를 가져와서 수식에 출력한다.

후위 표기법 계산 방법
- 후위 표기법으로 된 수식을 왼쪽 -> 오른쪽 방향으로 토큰을 읽어들인다

- 토큰이 피연산자 일 경우 스택에 보관한다.

- 토큰이 연산자 일 경우 스택에서 피연산자 2 개를 꺼낸 후 연산자에 맞게 연산한다.
이후 연산이 완료 된 결과는 다시 스택에 보관한다.

- 더이상 읽어들일 토큰이 없을  경우 스택에 남이 있는 피연산자가 최종 계산 결과이다.
"""


# Training 14
def start(args):
	oExpression = input("수식 입력 : ")
	oExpression_Postfix = infixToPostfix(oExpression)
	
	print(f"후위 표기법 : {oExpression_Postfix}")
	
	fResult = getResult(oExpression_Postfix)
	print(f"\n결과 : {fResult}")


# 연산자 여부를 검사한다
def isOperator(a_oToken):
	oOperators = "+-*/()"
	return a_oToken in oOperators


# 피연산자 여부를 검사한다
def isOperand(a_oToken):
	oOperands = "0123456789."
	return a_oToken in oOperands


# 우선 순위를 반환한다
def getPriority(a_oOperator, a_bIsPush):
	# +, - 연산자 일 경우
	if a_oOperator == "+" or a_oOperator == "-":
		return 2
	
	# *, / 연산자 일 경우
	if a_oOperator == "*" or a_oOperator == "/":
		return 1
	
	# ( 연산자 일 경우
	if a_oOperator == "(":
		return 0 if a_bIsPush else 4
	
	return 3


# 토큰을 반환한다
def getToken(a_oExpression, a_nIdx_Start):
	i = a_nIdx_Start
	oToken = ""
	
	while i < len(a_oExpression):
		oToken += a_oExpression[i]
		
		bIsOperand = i + 1 < len(a_oExpression)
		bIsOperand = bIsOperand and isOperand(a_oExpression[i])
		bIsOperand = bIsOperand and isOperand(a_oExpression[i + 1])
		
		# 피연산자가 아닐 경우
		if not bIsOperand:
			break
		
		i += 1
	
	return oToken


# 결과를 반환한다
def getResult(a_oExpression_Postfix):
	i = 0
	oListOperands = []
	
	while i < len(a_oExpression_Postfix):
		oToken = getToken(a_oExpression_Postfix, i)
		i += len(oToken)
		
		# 공백 일 경우
		if oToken.isspace():
			continue
		
		# 피연산자 일 경우
		if isOperand(oToken[0]):
			oListOperands.append(float(oToken))
		
		# 연산자 일 경우
		else:
			fRhs = oListOperands.pop()
			fLhs = oListOperands.pop()
			
			fResult = 0
			
			# + 연산자 일 경우
			if oToken == "+":
				fResult = fLhs + fRhs
			
			# - 연산자 일 경우
			elif oToken == "-":
				fResult = fLhs - fRhs
			
			# * 연산자 일 경우
			elif oToken == "*":
				fResult = fLhs * fRhs
			
			# / 연산자 일 경우
			elif oToken == "/":
				fResult = fLhs / fRhs
			
			oListOperands.append(fResult)
	
	return oListOperands.pop()


# 중위 -> 후위 표기법으로 변경한다
def infixToPostfix(a_oExpression_Infix):
	oListOperators = []
	oExpression_Postfix = ""
	
	i = 0
	
	while i < len(a_oExpression_Infix):
		oToken = getToken(a_oExpression_Infix, i)
		i += len(oToken)
		
		# 공백 일 경우
		if oToken.isspace():
			continue
		
		# 피연산자 일 경우
		if isOperand(oToken[0]):
			oExpression_Postfix += f"{oToken} "
		
		# ) 연산자 일 경우
		elif oToken[0] == ")":
			while len(oListOperators) > 0:
				oOperator = oListOperators.pop()
				
				# ( 연산자 일 경우
				if oOperator == "(":
					break
				
				oExpression_Postfix += oOperator
		
		else:
			while len(oListOperators) > 0:
				oOperator = oListOperators.pop()
				
				nPriority_Token = getPriority(oToken, True)
				nPriority_Operator = getPriority(oOperator, False)
				
				# 토큰의 우선 순위가 높을 경우
				if nPriority_Token < nPriority_Operator:
					oListOperators.append(oOperator)
					break
				
				oExpression_Postfix += oOperator
			
			oListOperators.append(oToken)
	
	while len(oListOperators) > 0:
		oExpression_Postfix += oListOperators.pop()
	
	return oExpression_Postfix
