#include <bits/stdc++.h>

using namespace std;
 
int solution(string& S) {
    int init = 0;
    for(int i = 0; i < S.length(); i++) {
        init = i+1;
        if(S[i] == 'A') break;
    }
    
    int max_p = 0, count_p = 0;
    for(int i = init; i < S.length(); i++) {
        if(S[i] == 'P') {
            count_p++;
            max_p = max(max_p, count_p);
        } else {
            count_p = 0;
        }
    }
    
    return max_p;
}
 
int main(void) {
    int test_cases;
    cin >> test_cases;
    for(int i = 0; i < test_cases; i++) {
        int n;
        cin >> n;
        string s;
        s.reserve(n);
        cin >> s;
        cout << solution(s) << endl;
    }
    
    return 0;
}