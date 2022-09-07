import copy
from random import randint
# make a data structure for saving grammar
num  = int(input())
grammar = {}
start = ''
for i in range(num) : 
    line = input().split(' -> ')
    products = line[1].split(' | ')
    line[0] = line[0].replace('<','')
    line[0] = line[0].replace('>','')
    grammar[line[0]] = []
    if(i==0) :
        start = line[0]
    for prod in products :
        grammar[line[0]].append(prod)


#remove unit value:
def unit(grammar) :
    for key,value in grammar.items() :
        for item in value :
            if(key==item) :
                value.remove(item)
            elif len(item)==3 and item[0] == '<' and item[-1] == '>' :
                string = item.replace('<','')
                string = string.replace('>','')
                value.remove(item)
                for item2 in grammar[string] :
                    if(item2 not in grammar[key]) :
                        grammar[key].append(item2)


# remove null value :
def null(grammar) :
    for key,value in grammar.items() :
        for item in value :
            if item == "#" :
                value.remove(item)
                string = '<' + key + '>'
                for key2,value2 in grammar.items() :
                    for item2 in value2 :
                        if string in item2 :
                            if(item2.replace(string,'') not in value2) :
                                value2.append(item2.replace(string,''))

## change the form :

#print(grammar)
flag = True
while(flag) :
    flag = False
    for value in grammar.values() :
        if '#' in value :   
            null(grammar)
            flag = True
            break

flag = True
while(flag) :
    flag = False
    for value in grammar.values() :
        for item in value :
                if len(item)==3 and item[0] == '<' and item[-1] == '>' :    
                    unit(grammar)
                    flag = True
                    break
        if flag : 
            break


# in first step put variable for every terminal :
flag = True
while(flag) :
    flag = False
    for key,value in grammar.items() :
        for j in range(len(value)) :
            if(len(value[j])==1):
                continue
            count_3 = 0
            flag_t = False
            for i in range(len(value[j])) :
                if(count_3==3) :
                    count_3 = 0
                    if(flag_t) :
                        flag_t = False
                        continue
                if(count_3>0) :
                    count_3+=1
                    continue
                elif(value[j][i]=='<') :
                    if(value[j][i+1]=='8'):
                        flag_t = True
                    count_3+=1
                    continue
                else :
                    string = '8' + value[j][i]
                    if(string not in grammar.keys()) :
                        grammar[string] = []
                        if(value[j][i] not in grammar[string]) :
                            grammar[string].append(value[j][i])
                    value[j] = value[j].replace(value[j][i],'<'+string+'>')
                    flag = True
                    break
            if(flag) :
                break
        if(flag) :
            break

# {'S': ['<Ta><S><Tb>', '<Ta><A>', '<Tb><B>', 'a', 'b'], 'A': ['<Ta><A>', 'a'], 'B': ['<Tb><B>', 'b'], 'Ta': ['a'], 'Tb': ['b']}

# in next step partitioning these variables :
flag = True
while(flag) :
    flag = False
    for key,value in grammar.items() :
        for i in range(len(value)) :
            if(len(value[i])==1 or value[i].count('<')==2 or value[i].count('<')==1) :
                continue
            for j in range(len(value[i])-6):
                if(value[i][j]=='<' and value[i][j+1]!='8' and value[i][j+4]!='8') :
                    string = '<' +  value[i][j+1] + '>'+'<'+value[i][j+4]+'>'
                    #string2 =   'V' + chr(ord(value[i][j+1]) + ord(value[i][j+4]))
                    string2 =    chr((ord(value[i][j+1]) + ord(value[i][j+5]))%64+192)
                    #string2 =   'V' + chr(randint(33,126))
                    value[i] = value[i].replace(string,'<'+string2+'>')
                    if(string2 not in grammar.keys()) :
                        grammar[string2] = []
                        if string not in grammar[string2] :
                            grammar[string2].append(string)
                    flag = True
                    break
                elif(value[i][j]=='<' and value[i][j+1]=='8' and value[i][j+5]!='8') :
                    string = '<' + '8' + value[i][j+2] + '>'+'<'+value[i][j+5]+'>'
                    #string2 =  'F' + chr(ord(value[i][j+2]) + ord(value[i][j+5]))
                    string2 =   chr((ord(value[i][j+1]) + ord(value[i][j+5]))%64+192)
                    #string2 =   'F' + chr(randint(33,126))
                    value[i] = value[i].replace(string,'<'+string2+'>')
                    if(string2 not in grammar.keys()) :
                        grammar[string2] = []
                        if string not in grammar[string2] :
                            grammar[string2].append(string)
                    flag = True
                    break
                elif(value[i][j]=='<' and value[i][j+1]!='8' and value[i][j+4]=='8') :
                    string = '<' +  value[i][j+1] + '>'+'<'+'8'+value[i][j+5]+'>'
                    string2 =  chr((ord(value[i][j+1]) + ord(value[i][j+5]))%64+192)
                    #string2 = 'K' + chr(ord(value[i][j+1]) + ord(value[i][j+5]))
                    #string2 =   'K' + chr(randint(33,126))
                    value[i] = value[i].replace(string,'<'+string2+'>')
                    if(string2 not in grammar.keys()) :
                        grammar[string2] = []
                        if string not in grammar[string2] :
                            grammar[string2].append(string)
                    flag = True
                    break
                elif(j+9<len(value[i])) :
                    if(value[i][j]=='<' and value[i][j+1]=='8' and value[i][j+5]=='8') and value[i][j+9]=='8' :
                        string = '<' +  '8'+value[i][j+2] + '>'+'<'+'8'+value[i][j+6]+'>'
                        string2 =   chr((ord(value[i][j+1]) + ord(value[i][j+5]))%64+192)
                        #string2 =  'L' + chr(ord(value[i][j+2]) + ord(value[i][j+6]))
                        #string2 =   'L' + chr(randint(33,126))
                        value[i] = value[i].replace(string,'<'+string2+'>')
                        if(string2 not in grammar.keys()) :
                            grammar[string2] = []
                            if string not in grammar[string2] :
                                grammar[string2].append(string)
                        flag = True
                        break
            if(flag) :
                break
        if(flag) :
            break

for key,value in grammar.items() :
    if '' in value :
        value.remove('')

# finish converting to CNF


#applying CYK algorithm :
input = input()
dp = [[set() for i in range(len(input))] for j in range(len(input))]

for i in range(len(input)) :
    for key,value in grammar.items() :
        for rule in value :
            if(len(rule)==1 and rule==input[i]) :
                dp[i][i].add(key)

for l in range(2,len(input)+1) :
    for i in range(len(input)-l+1) :
        j = i+l-1
        for k in range(i,j) :
            for key,value in grammar.items() :
                for rule in value :
                    if(len(rule)==1):
                        continue
                    string1 = ''
                    string2 = ''
                    if(rule[1] in ('8')) :
                        string1 = rule[1] + rule[2]
                        if(rule[5] in ('8')) :
                            string2 = rule[5] + rule[6]
                        else :
                            string2 = rule[5] 
                    else :
                        string1 = rule[1]
                        if(rule[4] in ('8')) :
                            string2 = rule[4] + rule[5]
                        else :
                            string2 = rule[4] 
                    if(string1 in dp[i][k] and string2 in dp[k+1][j]) :
                        dp[i][j].add(key)

# for i in range(len(input)) :
#     for j in range(len(input)) :
#         print(dp[i][j],end=" ")
#     print()

if(start in dp[0][len(input)-1]) :
    print("Accepted")
else :
    print("Rejected")


