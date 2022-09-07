

def sortString(str) :
    str = ''.join(sorted(str))
    return str

def have_lamba(dFA):
    for key,value in dFA.items() :
        for transition in value[0] :
            if(transition[0]=="$"):
                return True 
    return False

def all_visited(dFA) :
    for  isvisited in dFA.values() :
        if(not isvisited[1]) :
            return False
    return True

#inputes : 
input_states = input()
input_states = input_states.replace("{","")
input_states = input_states.replace("}","")
input_states = input_states.split(",")
alphabets = input()
alphabets = alphabets.replace("{","")
alphabets = alphabets.replace("}","")
alphabets = alphabets.split(",")
final_states = input()
count = int(input())
dFA = dict()
dFA_2 = dict()
for i in range(len(input_states)):
    if i==0 :
        dFA[sortString(input_states[i])] = [set(),True]
    else :
        dFA[sortString(input_states[i])] = [set(),False]
for i in range(count) :
    trans = input().split(",")
    dFA[sortString(trans[0])][0].add((sortString(trans[1]),sortString(trans[2])))

def change_trans(s1,s2,name,dFA) :# s1 -> s2
    for key,value in dFA.items() :
        if key==s1 :
            key = name
        for transition in value[0] :
            if transition[1]==s1 :
                value[0].add((transition[0],name))
                value[0].remove(transition)

# concatenate states with lambda transition : 
initial_state = sortString(input_states[0])
while(have_lamba(dFA)) :
    for key,value in dFA.items() :
        state = ""
        flag = False
        for transition in value[0] :
            if transition[0]=="$" :
                state = key + transition[1]
                state = sortString(state)
                new_set = dFA[key][0].union(dFA[transition[1]][0])
                new_set.remove(transition)
                if(value[1] or dFA[transition[1]][1]):
                    dFA[state] = [new_set,True]
                    initial_state = state
                else:
                    dFA[state] = [new_set,False]
                del dFA[key]
                
                change_trans(key,transition[1],state,dFA)
                flag = True
                break
        if flag :
            break

#changing NFA to DFA
have_trap = False
dFA[initial_state][1] = False
dFA_2[initial_state] = dFA[initial_state]
while(not all_visited(dFA_2)) :
    for states,value in dFA_2.items() :
        if(value[1]):
            continue
        value[1] = True
        dFA[states][1]=True
        flag = False
        for alph in alphabets :
            count = 0
            new_set = set()
            new_name =""
            for transition in value[0] :
                if transition[0]==alph :
                    new_name+= transition[1]
                    new_set = new_set.union(dFA[transition[1]][0])
                else:
                    count+=1
            if(count==len(value[0])) :
                have_trap = True
            if(sortString(new_name) not in dFA_2.keys() and new_name!=""):
                dFA[sortString(new_name)] = [new_set,False]
                dFA_2[sortString(new_name)] = [new_set,False]
                flag = True
        if(flag):
            break
if(have_trap) :
    print(len(dFA_2.values())+1)
else:
    print(len(dFA_2.values()))

            







