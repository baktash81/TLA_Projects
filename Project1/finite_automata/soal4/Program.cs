using System;
using System.Collections.Generic;
namespace soal4
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
        static void fun(String inn,List<State> NFA,State current,ref bool flag){
            if(inn.Length==0){
                if(current.isFinal){
                    flag = true;
                }
                else{
                    return ;
                }
            }
            if(current.transitions.Count==0){
                return;
            }
            for(int i=0;i<current.transitions.Count;i++){
                if(flag)
                    return;
                if(current.transitions[i][0]=="$"){
                    State next_current = NFA[ssearch(NFA,current.transitions[i][1])];
                    fun(inn,NFA,next_current,ref flag);
                }
                if(current.transitions[i][0]==Convert.ToString(inn[0])){
                    string next_in = inn;
                    next_in = next_in.Remove(0,1);
                    State next_current = NFA[ssearch(NFA,current.transitions[i][1])];
                    fun(next_in,NFA,next_current,ref flag);
                }
            }
        }
        static void Main(string[] args)
        {
            string states,alphabet,final;
            int count;
            states = Console.ReadLine();
            states = states.Remove(0,1);states = states.Remove(states.Length-1,1);
            string[] st= states.Split(',');
            /////
            alphabet = Console.ReadLine();
            ////
            final = Console.ReadLine();
            final = final.Remove(0,1);final = final.Remove(final.Length-1,1);
            string[] fn= final.Split(',');
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
            String inn = Console.ReadLine();
            bool flag = false;
            fun(inn,NFA,current,ref flag);
            if(flag){
                Console.WriteLine("Accepted");
            }
            else{
                Console.WriteLine("Rejected");
            }
        }
    }
}
