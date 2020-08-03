#include <bits/stdc++.h>

using namespace std;
 
int main(void) {
    int c;
    cin >> c;
    vector<int> V(c);
    for(int i = 0; i < c; i++) {
        cin >> V[i];
    }
    
    vector<int> l(c); //l[i]=~V[0]&...&~V[i-1]
    vector<int> r(c); //r[i]=~V[n-1]&...&~V[i+1]
    l[0]=r[c-1]=(1<<31)>>31;
    
    for(int i = 1; i < c; i++) {
        l[i] = l[i-1] & ~V[i-1];
    }
    for(int i = c-2; i >= 0; i--) {
        r[i] = r[i+1] & ~V[i+1];
    }
    
    int m = -1, sum = -1;
    for(int i = 0; i < c; i++) {
        if(sum < (l[i] & r[i] & V[i])) {
            sum = l[i] & r[i] & V[i];
            m = i;
        }
    }
    
    printf("%d ", V[m]);
    for(int i = 0; i < c; i++){
        if(i == m) continue;
        printf("%d ", V[i]);
    }
    
    return 0;
}