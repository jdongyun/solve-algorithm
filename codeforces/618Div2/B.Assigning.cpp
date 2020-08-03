#include <bits/stdc++.h>

using namespace std;
 
int main(void) {
    int c;
    cin >> c;
    while(c--) {
        int n;
        cin >> n;
        vector<int> V(2*n);
        for(int i = 0; i < 2*n; i++) {
            cin >> V[i];
        }
        sort(V.begin(), V.end());
        printf("%d\n", abs(V[n-1]-V[n]));
    }
    
    return 0;
}