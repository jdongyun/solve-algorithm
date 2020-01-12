#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

void solution(string& s) {
    reverse(s.begin(), s.end());
    if(s.find("op", 0) == 0) {
        cout << "FILIPINO" << endl;
    } else if(s.find("used", 0) == 0 || s.find("usam", 0) == 0) {
        cout << "JAPANESE" << endl;
    } else if(s.find("adinm", 0) == 0) {
        cout << "KOREAN" << endl;
    }
}

int main(void) {
    int N;
    cin >> N;
    for(int i = 0; i < N; i++) {
        string s;
        cin >> s;
        solution(s);
    }
    return 0;
}