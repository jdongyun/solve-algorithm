#include <bits/stdc++.h>

using namespace std;
 
string str(string& A, string& B) {
    string ret = "";
    for(int i = 0; i < A.length(); i++) {
        if(A[i] == B[i]) {
            ret += A[i];
        } else {
            ret += ('S' + 'E' + 'T' - (A[i] + B[i]));
        }
    }
    return ret;
}

int solution(vector<string>& V) {
    map<string, int> m;
    for(int i = 0; i < V.size(); i++) {
        for(int j = i+1; j < V.size(); j++) {
            string s = str(V[i], V[j]);
            if(!m.count(s)) {
                m[s] = 1;
            } else {
                m[s]++;
            }
        }
    }
    int ret = 0;
    for(int i = 0; i < V.size(); i++) {
        ret += m[V[i]];
    }
    return ret / 3;
}
 
int main(void) {
    int n, k;
    cin >> n >> k;
    vector<string> V(n);
    for(int _n = 0; _n < n; _n++) {
        cin >> V[_n];
    }
    cout << solution(V) << endl;
    
    return 0;
}