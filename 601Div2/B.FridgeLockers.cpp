#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void solution(int N, int M, vector<int>& V) {
    if(N != M || N < 3) { //N = 2면 무조건 불가능, N이 M과 다르면 무조건 불가능
        printf("-1\n");
        return;
    }
    
    int S = 0;
    for(int i = 0; i < V.size(); i++) {
        S += V[i];
    }
    
    printf("%d\n", S * 2); //필요한 Cost는 Sum * 2
    for(int i = 1; i < N; i++) {
        printf("%d %d\n", i, i+1); //1 ~ N-1 까지 출력
    }
    printf("%d %d\n", 1, N); //첫 점과 마지막 점 출력
    
}

int main(void) {
    int T;
    cin >> T;
    
    for(int t = 0; t < T; t++) {
        int N, M;
        cin >> N >> M;
        vector<int> V;
        for(int n = 0; n < N; n++) {
            int temp;
            scanf("%d", &temp);
            V.push_back(temp);
        }
        solution(N, M, V);
    }
    
    return 0;
}