import copy

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
final_states = final_states.replace("{","")
final_states = final_states.replace("}","")
final_states = final_states.split(",")
count = int(input())
dFA = dict()
for i in range(len(input_states)):
    dFA[input_states[i]] = dict()
for i in range(count) :
    trans = input().split(",")
    dFA[trans[0]][trans[1]] = trans[2]
#####

def IN_same_group(my_list,s1,s2) :
    for list in my_list :
        if (s1 in list) and (s2 in list) :
            return True
    return False

def check_equality(my_list,s1,s2,dFA,alphabets) :
    count = 0
    for alph in alphabets :
        if dFA[s1][alph]== dFA[s2][alph] or IN_same_group(my_list,dFA[s1][alph],dFA[s2][alph]):
            count+=1
    if count == len(alphabets):
        return True
    return False

def iter(dFA,reach_list,curr = input_states[0]) :
    for state in dFA[curr].values() :
        if state == curr :
            continue
        if state not in reach_list :
            reach_list.append(state)
            iter(dFA,reach_list,state)
    
# remove nonreachable states :
reach_list = list()
reach_list.append(input_states[0])
iter(dFA,reach_list)
dFA_temp = copy.deepcopy(dFA)
for state in dFA_temp.keys() :
    if state not in reach_list :
        del dFA[state]
        input_states.remove(state)
        if state in final_states :
            final_states.remove(state)
# Zero's Equivalence :
my_list = [] ## list of states. will be changed. 
my_list.append(final_states)
unfinal_states = []
for state in input_states :
    if state not in final_states :
        unfinal_states.append(state)
my_list.append(unfinal_states)

while(True) :
    temporary_list = list()
    ##temporary_list.append(final_states)
    mlist = copy.deepcopy(my_list)
    for k in range(len(mlist)) :
        # if(mlist[k] == final_states):
        #     continue
        i=0
        while(i<len(mlist[k])) :
            flag = False
            injected_list = list()
            injected_list.append(mlist[k][i])
            j=i+1
            while(j<len(mlist[k])):
                if check_equality(my_list,mlist[k][i],mlist[k][j],dFA,alphabets):
                    injected_list.append(mlist[k][j])
                    mlist[k].remove(mlist[k][j])
                    flag = True
                else :
                    j+=1
            mlist[k].remove(mlist[k][i])
            temporary_list.append(injected_list)
    if(my_list == temporary_list) :
        break
    my_list = temporary_list
    


print(len(my_list))


