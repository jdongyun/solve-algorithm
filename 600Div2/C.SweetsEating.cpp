#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<long long> solve(int M, vector<int>& V) {
    vector<long long> ret;
    sort(V.begin(), V.end());

    vector<long long> S;
    long long sum = 0;
    
    for(int i = 0; i < V.size(); i++) {
        sum += V[i];
        S.push_back(sum);
        //cout << sum << endl;
    }
    
    vector<long long> D;
    
    for(int i = 0; i < M; i++) {
        D.push_back(S[i]);
    }
    
    for(int i = M; i < V.size(); i++) {
        D.push_back(S[i] + D[i - M]);
    }
    
    return D;
}

int main(void) {
    int N, M;
    cin >> N >> M;
    
    vector<int> V;
    
    for(int i = 0; i < N; i++) {
        int temp;
        scanf("%d", &temp);
        V.push_back(temp);
    }
    
    vector<long long> sol = solve(M, V);
    
    for(int i = 0; i < sol.size(); i++) {
        cout << sol[i] << " ";
    }
    
    return 0;
}