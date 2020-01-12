#include <iostream>
#include <algorithm>

using namespace std;

int solution(int a, int b, int c, int r) {
    return min(b-a, max(0, c-r-a) + max(0, b-(c+r)));
}

int main(void) {
    int T;
    cin >> T;
    for(int i = 0; i < T; i++) {
        int a, b, c, r;
        scanf("%d %d %d %d", &a, &b, &c, &r);
        if(a > b) 
            printf("%d\n", solution(b, a, c, r));
        else
            printf("%d\n", solution(a, b, c, r));
    }
    return 0;
}