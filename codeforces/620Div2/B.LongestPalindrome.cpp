#include <bits/stdc++.h>

using namespace std;

int main(void) {
    int n, m;
    cin >> n >> m;
    vector<string> s(n);
    unordered_set<string> set;
    string left = "", middle = "", right = "";
    
    for(int i = 0; i < n; i++) {
        cin >> s[i];
        set.insert(s[i]);
    }
    
    for(int i = 0; i < n; i++) {
        string rev = s[i];
        reverse(rev.begin(), rev.end());
        if(s[i].compare(rev) == 0) { //이미 palindrome일 때
            if(middle.length() < s[i].length()) middle = s[i]; //중간은 제일 긴 것으로
            set.erase(s[i]);
            continue;
        }
        
        if(set.find(rev) != set.end()) { //reverse가 set에 있으면 사용이 가능함
            left += s[i]; //left는 제일 끝에 붙이고
            right = rev + right; //right는 제일 앞에 붙인다
            set.erase(s[i]); //rev를 다시 한 번 시도하지 못하게 함
            set.erase(rev); //위와 같음
        }
    }
    string ret = left + middle + right;
    cout << ret.length() << endl << ret << endl;
    
    return 0;
}