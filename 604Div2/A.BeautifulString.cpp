#include <iostream>
#include <cstring>

using namespace std;

void solution(string& s) {
    for(int i = 1; i < s.length() - 2; i++) {
        if(s[i] == s[i+1] && s[i] != '?') {
            cout << "-1" << endl;
            return;
        }
    }
    
    for(int i = 1; i < s.length() - 1; i++) {
        if(s[i] == '?') {
            if(s[i+1] == '?' || s[i-1] == s[i+1]) {
                s[i] = s[i-1] + 1;
                if (s[i] > 'c') s[i] = 'a';
            } else {
                s[i] = 'a' + 'b' + 'c' - (s[i-1] + s[i+1]);
                if(s[i] < 'a') s[i] = 'a';
            }
        }
    }
    for(int i = 1; i < s.length() - 1; i++) {
        printf("%c", s[i]);
        if(i == s.length() - 2) printf("\n");
    }
}

int main(void) {
    int T;
    cin >> T;
    for(int i = 0; i < T; i++) {
        string s, t;
        cin >> t;
        s += "c";
        s += t;
        s += "c";
        solution(s);
    }
    return 0;
}