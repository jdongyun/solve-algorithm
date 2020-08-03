#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <vector>
using namespace std;
 
void solution(vector<int>& V) {
    for(int i = 1; i < V.size(); i++) {
        if(abs(V[i] - V[i-1]) > 1) {
            cout << "YES" << endl;
            cout << i << " " << i+1 << endl;
            return;
        }
    }
    cout << "NO" << endl;
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