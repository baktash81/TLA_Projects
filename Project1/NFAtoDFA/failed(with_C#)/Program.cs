using System;
using System.Collections.Generic;
namespace NFAtoDFA
{
    class State{
        public string name;
        public bool isFinal = false;
        public bool isInitial = false;
        public List<string[]> transitions = new List<string[]>();
    };

    class Program
    {
        static int ssearch(List<State> states,string name){
            for(int i=0;i<states.Count;i++){
                if(states[i].name == name){
                    return i;
                }
            }
            return -1;
        }

        static  int Dsearch(List<List<State>> DFA,string name){
            for(int i=0;i<DFA.Count;i++){
                for(int j=0;j<DFA[i].Count;j++){
                    if(DFA[i][j].name==name){
                        return i;
                    }
                }
            }
            return -1;
        }
        
        static bool check(List<State>DFA,State ii){
            for(int i=0;i<DFA.Count;i++){
                if(DFA[i].name==ii.name){
                    return true;
                }
            }
            return false;
        }
        static  bool check_state(List<State> s1,List<State> s2){
            if(s1.Count!=s2.Count){
                return false;
            }
            else{
                for(int i=0;i<s1.Count;i++){
                    if(!check(s2,s1[i])){
                        return false;
                    }
                }
                return true;
            }
        }
        static bool check_big(List<List<State>> DFA,List<State> sDFA){
            for(int i=0;i<DFA.Count;i++){
                if(check_state(sDFA,DFA[i])){
                    return true;
                }
                
            }
            return false;
        }
        static  bool check_trap(List<List<State>> DFA){
            for(int i=0;i<DFA.Count;i++){
                for(int j=0;j<DFA[i].Count;j++){
                    if(DFA[i][j].name == "trap"){
                        return true;
                    }
                }
            }
            return false;
        }
        static void Main(string[] args)
        {
            string states,alphabet,final;
            int count;
            ////
            states = Console.ReadLine();
            states = states.Remove(0,1);states = states.Remove(states.Length-1,1);
            string[] st= states.Split(',');
            /////
            alphabet = Console.ReadLine();
            alphabet = alphabet.Remove(0,1);alphabet = alphabet.Remove(alphabet.Length-1,1);
            string[] alph = alphabet.Split(',');
            ////
            final = Console.ReadLine();
            final = final.Remove(0,1);final = final.Remove(final.Length-1,1);
            string[] fn= final.Split(',');
            ////
            count = Convert.ToInt32(Console.ReadLine());
            List<State> NFA = new List<State>();
            for(int i=0;i<st.Length;i++){
                State v = new State();
                v.name = st[i];
                NFA.Add(v);
            }
            for(int i=0;i<fn.Length;i++){
                NFA[ssearch(NFA,fn[i])].isFinal=true;
            }
            State current = new State();
            for(int i=0;i<count;i++){        
                string trans = Console.ReadLine();
                String[]trns = trans.Split(',');
                if(i==0){
                    NFA[ssearch(NFA,trns[0])].isInitial = true;
                    current = NFA[ssearch(NFA,trns[0])];
                    
                }
                String[] next = new String [2];// 0 : alphabet 1: next state 
                next[0] = trns[1];
                next[1] = trns[2];
                NFA[ssearch(NFA,trns[0])].transitions.Add(next);
            }

            List<List<State>> DFA = new List<List<State>>();
            List<State>nw = new List<State>();
            nw.Add(current);
            DFA.Add(nw);
            for(int i=0;i<DFA.Count;i++){//tamam state ha ra check mikonim
                bool landa_flag = false;
                for(int j=0;j<alph.Length;j++){//check kardan alphabet ha baraye har state
                    List<State> ne = new List<State>();
                    for(int k=0;k<DFA[i].Count;k++){//har state ro check mikonim
                        int countt = 0; 
                        for(int l=0;l<DFA[i][k].transitions.Count;l++){//check kardan input har state
                            if(DFA[i][k].transitions[l][0]=="$"){
                                List<State>ne2 = new List<State>();
                                // pak kardn transitioni ke daraye landa ast dar har 2 state
                                string name = DFA[i][k].transitions[l][1];
                                
                                DFA[i][k].transitions.Remove(DFA[i][k].transitions[l]);
                                //
                                for(int g=0;g<DFA[i].Count;g++){
                                    ne2.Add(NFA[ssearch(NFA,DFA[i][g].name)]);
                                }
                                for(int g=0;g<DFA[Dsearch(DFA,name)].Count;g++){
                                    if(!check(ne2,DFA[Dsearch(DFA,name)][g])){
                                        ne2.Add(DFA[Dsearch(DFA,name)][g]);
                                    }
                                }
                                ne2.Add(NFA[ssearch(NFA,name)]);
                                if(!check_big(DFA,ne2)){
                                    DFA.Add(ne2);
                                    DFA.Remove(DFA[i]);
                                    DFA.Remove(DFA[Dsearch(DFA,name)]);
                                    landa_flag = true;
                                    break;
                                }
                            }
                            if(DFA[i][k].transitions[l][0]==alph[j]){
                                if(!check(ne,NFA[ssearch(NFA,DFA[i][k].transitions[l][1])])){
                                    ne.Add(NFA[ssearch(NFA,DFA[i][k].transitions[l][1])]);
                                }
                            }
                            else if(DFA[i].Count==1){
                                countt++;
                            }
                        }
                        if(landa_flag){
                            break;
                        }
                        if(countt==DFA[i][k].transitions.Count){
                            List<State> trap = new List<State>();
                            State trap_state = new State();
                            trap_state.name = "trap";
                            trap.Add(trap_state);
                            if(!check_trap(DFA)){
                                DFA.Add(trap);
                            }
                        }
                    }
                    if(landa_flag){
                        i--;
                        break;
                    }
                    if(ne.Count!=0 && !check_big(DFA,ne)){
                        DFA.Add(ne);
                    }
                }
                
            }
            Console.WriteLine(DFA.Count);
        }
    }   
}
