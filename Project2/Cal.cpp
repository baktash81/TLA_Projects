#include <iostream>
#include <bits/stdc++.h>
using namespace std;

vector<string> operators = {"(",")","+","-","*","/","^","sqrt","sin","cos","tan","abs","exp","ln"};
vector<string> operators2 = {"+","-","*","/","^","sqrt","sin","cos","tan","abs","exp","ln"};
vector<string> operators3 = {"+","-","*","/","^"};


int priority(string value)
{
    if(value=="sin" || value=="cos" || value=="tan" || value=="exp" || value=="abs" || value=="ln" || value=="sqrt"){
        return 4;
    }
    else if(value == "^"){
        return 3;
    }
    else if(value == "/" || value == "*"){
        return 2;
    }
    else if(value == "+" || value == "-"){
        return 1;
    }

    else{
        return -1;
    }
}


bool isoperand(string value){
    try{
    if (count(operators.begin(), operators.end(), value)==0) {
        return true;
    }
    return false;
    }catch (const std::exception& e){
        cout<<"INVALID";
    }
}
bool isoperator(string value){
    try{
    if (count(operators2.begin(), operators2.end(), value)) {
        return true;
    }
    return false;
    }catch (const std::exception& e){
        cout<<"INVALID";
    }
}



int main(){
    try{
        stack<string> st;
        vector<string> output;
        vector<string> line;
        string c;
        getline(cin,c);
        // First we add space in some position like sin( --> sin (  
        for(int i=0;i<c.length();i++){
            if(i==c.length()-1){
                if(c[i]==')' and c[i-1]!=' '){
                    c.insert(i," ");
                    break;
                }
            }
            else{
                if(c[i]=='(' || c[i]==')'){
                    if(c[i-1]!=' ' && i!=0){
                        c.insert(i," ");
                        i--;
                        continue;
                    }
                    if(c[i+1]!=' ' && i!=c.length()-1){
                        c.insert(i+1," ");
                        i--;
                        continue;
                    }
                }
            }
        }
        

        string ind =  "";
        for(int i=0;i<c.length();i++){
            if(c[i]!=' '){
                ind.push_back(c[i]);
                if(i==c.length()-1){
                    line.push_back(ind);
                }
            }
            else{
                line.push_back(ind);
                ind = "";
            }
        }
        // handeling some invalid input :
        for(int i=0;i<line.size()-1;i++){
            if(line[i].find("..") != string::npos){
                throw  invalid_argument( "invalid input" );
            }
            if(isoperand(line[i]) && isoperand(line[i+1])){
                throw  invalid_argument( "invalid input" );
            }
            if((i==0 || i==line.size()-1) && count(operators3.begin(), operators3.end(), line[i])){
                throw  invalid_argument( "invalid input" );
            }
            if(isoperator(line[i]) and isoperator(line[i+1])){
                throw  invalid_argument( "invalid input" );
            }
            if(line[i]==")" && isoperand(line[i+1]) && stod(line[i+1])<0){
                line[i+1] = to_string(abs(stod(line[i+1])));
                line.insert(line.begin()+i+1,"-");
            }
        }
        // start to convert infix to postfix 
        vector<string> st_temp;
        for(int i=0;i<line.size();i++){
            if(isoperand(line[i])){
                output.push_back(line[i]);
            }
            else if(line[i]=="("){
                st.push(line[i]);
                st_temp.push_back(line[i]);
            }
            else if(line[i]==")"){
                if(count(st_temp.begin(),st_temp.end(),"(")==0){
                    cout<<"INVALID";
                    return 1;
                }
                while(!st.empty() && st.top()!="("){
                    string ch = st.top();
                    st.pop();
                    st_temp.pop_back();
                    output.push_back(ch);
                }
                st.pop();
                st_temp.pop_back();
            }
            else{
                while(!st.empty() && priority(line[i])<= priority(st.top())){
                    string ch = st.top();
                    st.pop();
                    st_temp.pop_back();
                    output.push_back(ch);
                }
                st.push(line[i]);
                st_temp.push_back(line[i]);
            }
        }
        while(! st.empty()){
            string ch = st.top();
            st.pop();
            if(ch=="("){
                cout<<"INVALID";
                return 1 ;
            }
            output.push_back(ch);
        }
        stack<string> st2;
        // calculating postfix expression using stack
        for(int i=0;i<output.size();i++){
            if(isoperand(output[i])){
                double temp = stod(output[i]);
                st2.push(output[i]);
            }
            else{
                if(output[i]=="sin"){
                    string a = st2.top();
                    st2.pop();
                    double result = stod(a);
                    result = sin(result);
                    st2.push(to_string(result));
                }
                else if(output[i]=="cos"){
                    string a = st2.top();
                    st2.pop();
                    double result = stod(a);
                    result = cos(result);
                    st2.push(to_string(result));
                }
                else if(output[i]=="tan"){
                    string a = st2.top();
                    st2.pop();
                    double result = stod(a);
                    result = tan(result);
                    st2.push(to_string(result));
                }
                else if(output[i]=="abs"){
                    string a = st2.top();
                    st2.pop();
                    double result = stod(a);
                    result = abs(result);
                    st2.push(to_string(result));
                }
                else if(output[i]=="exp"){
                    string a = st2.top();
                    st2.pop();
                    double result = stod(a);
                    result = exp(result);
                    st2.push(to_string(result));
                }
                else if(output[i]=="ln"){
                    string a = st2.top();
                    st2.pop();
                    double result = stod(a);
                    if(result<0){
                        throw invalid_argument( "received negative value" );
                    }
                    result = log(result);
                    st2.push(to_string(result));
                }
                else{
                    string result = st2.top();
                    st2.pop();
                    double a = stod(result);
                    result = st2.top();
                    st2.pop();
                    double b = stod(result);
                    if(output[i]=="+"){
                        double final = b + a;
                        st2.push(to_string(final));
                    }
                    else if(output[i]=="-"){
                        double final = b - a;
                        st2.push(to_string(final));
                    }
                    else if(output[i]=="/"){
                        double final = b / a;
                        st2.push(to_string(final));
                    }
                    else if(output[i]=="*"){
                        double final = b * a;
                        st2.push(to_string(final));
                    }
                    else if(output[i]=="^"){
                        double final = pow(b,a);
                        st2.push(to_string(final));
                    }
                    else{
                        throw  invalid_argument( "invalid input" );
                    }
                }
            }
        }

        string fresult = st2.top();
        int count = 0;
        bool flag = false;
        for(int i=0;i<fresult.length();i++){
            if(fresult[i]=='.'){
                flag = true;
                cout<<fresult[i];
                continue;
            }
            if(count==2){
                break;
            }
            if(flag==true){
                count++;
                cout<<fresult[i];
                continue;
            }
            
            cout<<fresult[i];
        }
    }
    catch (const std::exception& e){
        cout<<"INVALID";
    }
}