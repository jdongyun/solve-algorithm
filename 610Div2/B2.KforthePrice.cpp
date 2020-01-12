#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int solution(vector<int>& a, int n, int p, int k) {
    sort(a.begin(), a.end());
    vector<int> cache(n+1);
    cache[0] = 0;
    for(int i = 1; i < k; i++) {
        cache[i] = cache[i-1] + a[i-1];
    }
    for(int i = k; i <= n; i++) {
        cache[i] = cache[i-k] + a[i-1];
    }
    int ret = 0;
    for(int i = 1; i <= n; i++) {
        if(cache[i] <= p) {
            ret = i;
        }
    }
    return ret;
    
}

int main(void) {
    int T;
    cin >> T;
    for(int i = 0; i < T; i++) {
        int n, p, k;
        scanf("%d %d %d", &n, &p, &k);
        vector<int> a(n);
        for(int j = 0; j < n; j++) {
            cin >> a[j];
        }
        cout << solution(a, n, p, k) << endl;
    }
    
    return 0;
}