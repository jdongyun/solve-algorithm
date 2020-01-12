#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

void solution(string& s, string& c) {
    string s2 = s;
    for(int i = s.size() - 2; i >= 0; i--) { //[i, s.size()) 사이에서 최소값을 s2[i]에 넣음
        s2[i] = min(s2[i], s2[i+1]);
    }
    for(int i = 0; i < s.size(); i++) {
        if(s[i] != s2[i]) {
            int j;
            for(j = i; j < s.size()-1; j++) {
                if(s2[j] != s2[j+1]) break;
            }
            
            //swap
            char temp = s[j];
            s[j] = s[i];
            s[i] = temp;
            break;
        }
    }
    if(s.compare(c) < 0) { //사전 순으로 앞에 있으면 출력
        cout << s << endl;
    } else {
        cout << "---" << endl;
    }
}

int main(void) {
    int N;
    cin >> N;
    for(int i = 0; i < N; i++) {
        string s, c;
        cin >> s >> c;
        solution(s, c);
    }
}