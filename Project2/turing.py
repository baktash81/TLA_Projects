
# First we convert turing binary code to contorl unit :
turing = dict()
binary_code = input().split('00')

for code in binary_code :
    code = code.split('0')
    if(code[0] not in turing) :
        turing[code[0]] = []
    if(code[2] not in turing) :
        turing[code[2]] = []
    if code[1]=='1' :
        code[1]='#'
    if code[3]=='1' :
        code[3] = '#'
    tup = (code[1],code[3],code[2],code[4])
    turing[code[0]].append(tup)



def check(line,turing,state,head=20) :
    global flag
    if(flag) :
        return
    if(state=='1'*len(turing.keys()) ) :
        print('Accepted')
        flag = True
        return 
    else :
        halt = True
        for trans in turing[state] :
            if(line[head]==trans[0]) :
                line[head] = trans[1]
                if trans[3]=='11' :
                    check(line,turing,trans[2],head+1)
                    if(flag) :
                        return
                elif(trans[3]=='1') :
                    check(line,turing,trans[2],head-1)
                    if(flag) :
                        return
                halt = False
        if(halt) :
            print("Rejected")
            flag = True


count = int(input())
for i in range(count) :
    line = input()
    if line =='' :
        line = '#'
    line = '#0'*20 + line + '0#'*20
    line = line.split('0')
    flag = False
    check(line,turing,'1')

