
from contextlib import nullcontext
from dataclasses import replace
from msilib.schema import Class

from sympy import false


class State :
    def __init__(self,name,isfinal,isinitial,next):
        self.name = name
        self.isfinal = isfinal
        self.isinitial = isinitial
        self.next = next

states = input().split(',')
states[0].replace('{','')
states[-1].replace('}','')
alphabet = input().split(',')
alphabet[0].replace('{','')
alphabet[-1].replace('}','')
final = input().split(',')
final[0].replace('{','')
final[-1].replace('}','')
NFA = list()
count = int(input())
for i in range(len(states)) :
    s = State(states[i],False,False,nullcontext)
    NFA.append(s)
