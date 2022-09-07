#include <bits/stdc++.h>

using namespace std;

bool flag =false;
class State{
public:
    string name;
    bool isFinal = false;
    bool isInitial = false;
    vector<array<string,2>>transitions;
};

int ssearch(vector<State> states,string name){
    for(int i=0;i<states.size();i++){
        if(states[i].name == name){
            return i;
        }
    }
}
void split(vector<string> &splited,string s){
    string str = "";
    if(s[0]=='{'){
        s.erase(s.begin());
    }
    if(s[s.length()-1]=='}'){
        s.erase(s.length()-1);
    }
    str.push_back(s[0]);
    for(int i=1;i<s.size();i++){
        if(s[i]==','){
            splited.push_back(str);
            str = "";
        }
        else{
            str.push_back(s[i]);
        }
    }
    splited.push_back(str);
    return;

}

void fun(string in,vector<State> NFA,State current){
    if(in.size()==0){
        if(current.isFinal){
            flag = true;
        }
        else{
            return ;
        }
    }
    if(current.transitions.size()==0){
        return;
    }
    string alph(in[0],1);
    for(int i=0;i<current.transitions.size();i++){
        if(flag)
            return;
        if(current.transitions[i][0]=="$"){
            State next_current = NFA[ssearch(NFA,current.transitions[i][1])];
            fun(in,NFA,next_current);
        }
        if(current.transitions[i][0]==alph){
            string next_in = in;
            next_in.erase(next_in.begin());
            State next_current = NFA[ssearch(NFA,current.transitions[i][1])];
            fun(next_in,NFA,next_current);
        }
    }
}

int main(){
    string states,alphabet,final;
    string count;
    cin>>states;
    cin>>alphabet;
    cin>>final;
    cin>>count;
    vector <string> st;// all states 
    vector <string> fn;
    split(fn,final);
    vector <State> NFA;
    split(st,states);
    for(int i=0;i<st.size();i++){
        State v;
        v.name = st[i];
        NFA.push_back(v);
    }
    for(int i=0;i<fn.size();i++){
        NFA[ssearch(NFA,fn[i])].isFinal=true;
    }
    
    
    State current;
	for(int i=0;i<count[0]-48;i++){        
		string trans;
		cin>>trans;
		vector <string> trns;
		split(trns,trans);
        if(i==0){
            current = NFA[ssearch(NFA,trns[0])];
        }
        array<string,2> next;// 0 : alphabet 1: next state 
        next[0] = trns[1];
        next[1] = trns[2];
		NFA[ssearch(NFA,trns[0])].transitions.push_back(next);

	}

    // cin the string and start the transitions with recursive function :
    string in;
    cin>>in;
    fun(in,NFA,current);
    cout<<flag?"Accepted":"Rejected";
    return 1;
}