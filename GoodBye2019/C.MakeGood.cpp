#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <vector>
using namespace std;
 
void solution(vector<int>& V) {
    unsigned long long sum = 0, xr = 0;
    for(int i = 0; i < V.size(); i++) {
        sum = sum + (unsigned long long) V[i];
        xr = xr ^ V[i];
    }
    if(sum == 2 * xr) {
        printf("0\n\n");
    } else if(sum < 2 * xr && sum % 2 == 0) {
        printf("2\n");
        printf("%llu %llu\n", (2*xr - sum)/2, (2*xr - sum)/2);
    } else {
        printf("2\n");
        printf("%llu %llu\n", xr, xr+sum);
    }
}
 
int main(void) {
    int test_cases;
    cin >> test_cases;
    for(int i = 0; i < test_cases; i++) {
        int n;
        cin >> n;
        vector<int> v(n);
        for(int j = 0; j < n; j++) {
            cin >> v[j];
        }
        solution(v);
    }
    
    return 0;
}