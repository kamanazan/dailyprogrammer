import re
'''
short description:
    1+x=3
    x=2
constraint:
    accepted operations:+,-,x,/
    accepted operands: integer
strategy:
    the expression is a string
    so we must parse it with [parseExp]
    determine wich one is operands and operator
    e.g in the description operands are 1,x,3 and operator is +
    once we figure it all out do a reverse operation
    e.g  to find x we must substract 3 with 1,[parseOP] 
    in other word change '+' to '-'[inverseOP]
    and dont forget to convert the operands to integer except the second
    obviously
    Now...
    you can not just inverse '-' and '/' since a-b != b-a and a/b != b/a
    depends on which operands is missing, check wether inverse operation should
    be done or not
    [case1]if b is missing then there is no inverse operation
    [case2]if a is missing then do an inverse operation
    also consider the order of operands
    So...
    [case3]applying the previous case how to handle missing operand1 for '+' and 'x'
    operation?
'''

def parseExp(exp):
    #returns the missing value
    missing = 0
    matches = re.match('([0-9A-Z]*)([\+-x/])([0-9A-Z])=([0-9]*)',exp) 
    operand1 = matches.group(1)
    operand2 = matches.group(3)
    operand3 = matches.group(4)
    operator = matches.group(2)
    if re.match('[0-9]',operand1):#case3
        if operator == '-' or operator == '/':#case1
            missing = parseOP(operand1,operand3,operator)
        else:
            op = inverseOP(operator)
            missing = parseOP(operand3,operand1,op)
    else:#case2
        op = inverseOP(operator)
        missing = parseOP(operand3,operand2,op)
                

    return missing
def parseOP(a,b,op):
    a = int(a)
    b = int(b)
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == 'x':
        return a * b
    elif op == '/':
        return a / b
def inverseOP(op):
    if op == '+':
        return '-'
    elif op == '-':
        return '+'
    elif op == 'x':
        return '/'
    elif op == '/':
        return 'x'
    

assert parseExp('1+X=3') == 2
assert parseExp('X+2=3') == 1
assert parseExp('2xC=8') == 4
assert parseExp('27/Q=3') == 9
assert parseExp('15-F=8') == 7
assert parseExp('E/6=6') == 36
assert parseExp('W-1=19') == 20
