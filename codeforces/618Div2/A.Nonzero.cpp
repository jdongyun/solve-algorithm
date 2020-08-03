#include <bits/stdc++.h>

using namespace std;
 
int main(void) {
    int c;
    cin >> c;
    while(c--) {
        int n;
        cin >> n;
        int ret = 0, sum = 0;
        for(int i = 0; i < n; i++) {
            int input;
            cin >> input;
            sum += input;
            if(input == 0) {
                ret++;
                sum++;
            }
        }
        if(sum == 0) ret++;
        printf("%d\n", ret);
    }
    
    return 0;
}