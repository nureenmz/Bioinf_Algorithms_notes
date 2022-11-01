# Chapter 3.4, stack data type

class Stack:
	def __init__(self):
		self.items = []

	def is_empty(self):
		return self.items == []

	def push(self, item):
		self.items.insert(0, item)

	def pop(self):
		return self.items.pop(0)

	def peek(self):
		return self.items[0]

	def size(self):
		return len(self.items)

s= Stack()
s.push('hello')
s.push('true')
print(s.pop())

# simple balance parentheses
import Stack #as above

# Extended par_checker for: [,{,(,),},]

def par_checker(symbol_string):
	s= Stack()
	balanced = True
	index = 0
	while index < len(symbol_string) and balanced:
		symbol = symbol_string[index]
		if symbol in "([{":
			s.push(symbol)
		else:
			if s.is_empty():
				balanced = False
			else:
				top = s.pop()
				if not matches(top, symbol):
					balanced = False
		index = index+1
	if balanced and s.is_empty():
		return True
	else:
		return False

def matches(open, close):
	opens = "([{"
	closes = ")]}"
	return opens.index(open) == closes.index(close)

print(par_checker('{{([][])}()}'))
print(par_checker('[{()]'))

# Divide by 2 algorithm
# Takes a decimal number argument and repeatedly divides by 2
# Extract remainder, pushes it on the stack
# Construct binary string by popping the stack and appended to right-hand end of string

import Stack # as before
def divide_by_2(dec_number):
	rem_stack = Stack()
	
	while dec_number > 0:
		rem = dec_number % 2
		rem_stack.push(rem)
		dec_number = dec_number // 2

	bin_string = ""
	while not rem_stack.is_empty():
		bin_string = bin_string + str(rem_stack.pop())

	return bin_string

print(divide_by_2(42))

# Modified divideby2 to divide by base to take a decimal number and any base between 2 and 16
# Base 2 to 10 can use the 0-9 digits, but base bigger than 10 need a new sit of digits to represent remainders beyond 9
import Stack
def base_converter(dec_number, base):
	digits = "0123456789ABCDEF"	
	
	rem_stack = Stack()

	while dec_number > 0:
		rem = dec_number % base
		rem_stack.push(rem)
		dec_number = dec_number // base
	
	new_string = ""
	while not rem_stack.is_empty():
		new_string = new_string + digits[rem_stack.pop()]

	return new_string

print(base_converter(25,2))
print(base_converter(25,16))

# Infix to postfix algorithm using a dictionary (prec) to hold the precedence value sfor the operators. Precedence levels is given as integers (3,2,1)
import Stack

def infix_to_postfix(infix_expr):
	prec = {}
	prec["*"] = 3
	prec["/"] = 3
	prec["+"] = 2
	prec["-"] = 2
	prec["("] = 1
	op_stack = Stack()
	postfix_list = []
	token_list = infix_expr.split()
	
	for token in token_list:
		if token in "ABDDEFGHJIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
			postfix_list.append(token)
		elif token == "(":
			op_stack.push(token)
		elif token == ")":
			top_token = op_stack.pop()
			while top_token != '(':
				postfix_list.append(top_token)
				top_token = op_stack.pop()
		else:
			while (not op_stack.is_empty()) and \
			(prec[op_stack.peek()] >= prec[token]):
				postfix_list.append(op_stack.pop())
			op_stack.push(token)

	while not op_stack.is_empty():
		postfix_list.append(op_stack.pop())
	return " ".join(postfix_list)

print(infix_to_postfix("A*B+C*D"))
print(infix_to_postfix("(A+B)*C-(D-E)*(F+G)"))

# Postfix evaluation
# helper function do_math takes two operands and an operator and then perform the proper arithmatic operation
import Stack

def postfix_eval(postfix_expr):
	operand_stack = Stack()
	token_list = postfix_expr.split()

	for token in token_list:
		if token in "0123456789":
			operand_stack.push(int(token))
		else:
			operand2 = operand_stack.pop()
			operand1 = operand_stack.pop()
			result = do_math(token, operand1, operand2)
			operand_stack.push(result)
	return operand_stack.pop()

def do_math(op, op1, op2):
	if op == "*":
		return op1*op2
	elif op == "/":
		return op1/op2
	elif op == "+":
		return op1+op2
	else:
		return op1-op2

print(postfix_eval('78+32+/'))

# TODO: error detection nad reporting in the input expression


