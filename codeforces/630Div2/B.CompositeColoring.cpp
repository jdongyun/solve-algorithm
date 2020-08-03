#include <bits/stdc++.h>

using namespace std;

int main(void) {
    int c;
    cin >> c;
    while(c--) {
        int n;
        cin >> n;
        vector<int> v(n), color(n);
        int primes[] = { 2,3,5,7,11,13,17,19,23,29,31};
        
        for(int i = 0; i < n; i++) { //입력받은 합성수를 소인수분해한 소수 중 최솟값으로 체크
            cin >> v[i];
            for(int j = 0; j < 11; j++) {
                if(v[i] % primes[j] == 0) {
                    color[i] = j;
                    break;
                }
            }
        }
        
        bool used[11] = { false }; //배열 압축
        int cnt = 1;
        int ret[11] = {0};
        for(int i = 0; i < n; i++) {
            used[color[i]] = true;
        }
        
        for(int i = 0; i < 11; i++) {
            if(used[i]) {
                ret[i] = cnt;
                cnt++;
            }
        }
        cout << (cnt-1) << "\n";
        for(int i = 0; i < n; i++) {
            cout << ret[color[i]] << " ";
        }
        cout << "\n";
    }
    return 0;
}
