#include <bits/stdc++.h>

using namespace std;

int main(void) {
    int c;
    cin >> c;
    while(c--) {
        int a, b, c, d;
        int x, y, x1, y1, x2, y2;
        cin >> a >> b >> c >> d;
        cin >> x >> y >> x1 >> y1 >> x2 >> y2;
        
        int calc_x = x + (-a+b), calc_y = y + (-c+d);
        
        if(x2 < calc_x || x1 > calc_x || (x1 == x2 && (a+b) > 0)) { 
            printf("No\n");
            continue;
        }
        if(y2 < calc_y || y1 > calc_y|| (y1 == y2 && (c+d) > 0)) {
            printf("No\n");
            continue;
        }
        
        printf("Yes\n");
        
    }
    
    return 0;
}