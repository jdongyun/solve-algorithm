#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main(void) {
    int test_cases;
    cin >> test_cases;
    for(int i = 0; i < test_cases; i++) {
        int n, a, b;
        scanf("%d %d %d", &n, &a, &b);
        bool ret = false;
        for(int i = 0; i < n; i++) {
            int temp;
            scanf("%d", &temp);
            if(temp == n) {
                if(i < a) ret = true;
            }
        }
        cout << (ret ? "YES" : "NO") << endl;
    }
    
    return 0;
}