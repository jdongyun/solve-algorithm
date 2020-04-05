#include <bits/stdc++.h>

using namespace std;
 
int main(void) {
    int c;
    cin >> c;
    while(c--) {
        int x, y, a, b;
        cin >> x >> y >> a >> b;
        if( (y - x) % (a+b) != 0) {
            cout << "-1" << endl;
            continue;
        }
        cout << ((y-x)/(a+b)) << endl;
    }
    
    return 0;
}