

# Convert infix to postfix :

from cmath import cos, exp, sin, tan
import math

from sympy import ln


def isempty(head) :
    if head[0]==-1 :
        return True
    return False

def peek(stack) :
    return stack[-1]

def pop(head,stack) :
    
    if not isempty(head) :
        head[0]-=1
        return stack.pop()
    else :
        return '#'

def push(head,stack,value) :
    head[0]+=1
    stack.append(value)

def isoperand(char) :
    if char not in operators :
        return True
    return False

def notgreater(character,stack,i) :
    try :
        a = character[i]
        b = character[peek(stack)]
        if(a<=b) : return True
        else : return False
    except  :
        return False


operators = ['(',')','+','-','*','/',
'^','sqrt','sin','cos','tan','abs','exp','ln']
line = input()
flag = True
while(flag):
    flag = False
    for i in range(len(line)) :
        if(i==0 and (line[i]=='(' or line[i]==')')) :
            if line[i+1]!=' ' :
                line = line[:i+1] + ' ' + line[i+1:]
                flag = True
        elif(i==len(line)-1 and (line[i]=='(' or line[i]==')')) :
            if line[i-1]!=' ' :
                line = line[:i] + ' ' + line[i:]
                flag = True
        elif (line[i]=='(' or line[i]==')') :
            if(line[i-1]!=' ' and line[i+1]!=' '):
                line = line[:i] + ' ' + line[i] + ' ' + line[i+1:]
                flag = True
            elif(line[i+1]!=' ') :
                line = line[:i+1] + ' ' + line[i+1:]
                flag = True
            elif(line[i-1]!=' ') :
                line = line[:i] + ' ' + line[i:]
                flag = True
            if(flag) :
                break
line = line.split()

head = [-1]
stack = []
output = []

character = {'+' : 1, '-' : 1, '*' :2, '/' : 2, '^' :3}
# if (line[0] in ('+','-','/','*')) or (line[-1] in ('+','-','/','*')) :
#     print("INVALID")
#     quit()
for value in line :
    if value not in operators  :
        output.append(value)
    elif value == '(' :
        push(head,stack,value)
    elif value==')' :
        if('(' not in stack) :
            print('INVALID')
            quit()
        while(not isempty(head)) and peek(stack)!='(' :
            ch = pop(head,stack)
            output.append(ch)
        pop(head,stack)
    else :
        while(not isempty(head) and notgreater(character,stack,value)) :
            output.append(pop(head,stack))
        push(head,stack,value)

if('(' in stack) :
    print('INVALID')
    quit()
while(not isempty(head)) :
    output.append(pop(head,stack))


#now calculate the expression from postfix :

head = [-1]
stack = []
try :
    for value in output :
        if value not in operators :
            push(head,stack,value)
        else :
            if(value == 'sin') :
                a = pop(head,stack)
                push(head,stack,str(math.sin(float(a))))
            elif(value == 'cos') :
                a = pop(head,stack)
                push(head,stack,str(math.cos(float(a))))
            elif(value == 'tan') :
                a = pop(head,stack)
                push(head,stack,str(math.tan(float(a))))
            elif(value == 'abs') :
                a = pop(head,stack)
                push(head,stack,str(abs(float(a))))
            elif(value == 'exp') :
                a = pop(head,stack)
                push(head,stack,str(math.exp(float(a))))
            elif(value == 'ln') :
                a = pop(head,stack)
                push(head,stack,str(ln(float(a))))
            else :
                a = pop(head,stack)
                b = pop(head,stack)
                if(value == '+') :
                    push(head,stack,str(float(b)+float(a)))
                elif(value == '-') :
                    push(head,stack,str(float(b)-float(a)))
                elif(value == '*') :
                    push(head,stack,str(float(b)*float(a)))
                elif(value == '^') :
                    push(head,stack,str(float(b)**float(a)))
                elif(value == '/') :
                    if(a==0) :
                        print('INVALID')
                        quit()
                    push(head,stack,str(float(b)/float(a)))

    result = "{:.2f}".format(float(pop(head,stack)))

    print(result)
except :
    print("INVALID")