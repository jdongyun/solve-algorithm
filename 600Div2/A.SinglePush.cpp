#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

bool solution(vector<int>& A, vector<int>& B) {
    int size = A.size();
    bool l = false, r = false;
    int k = 0;
    
    for(int i = 0; i < size; i++) {
        if(A[i] != B[i]) {
            if(r) return false; //이미 l, r을 찾았을 경우 무조건 거짓
            if(l) { //l만 찾았으면 k를 체크
                if(A[i] + k != B[i]) return false; 
            }
            if(!l) { //l도 찾지 못했을 때
                k = B[i] - A[i];
                if(k < 1) return false; //k 양수 아니면 거짓
                l = true;
            }
        }
        if(l && !r && A[i] == B[i]) { //r 찾기
            r = true;
        }
    }
    return true;
}

int main(void) {
    int T;
    cin >> T;
    for(int t = 0; t < T; t++) {
        int L;
        cin >> L;
        vector<int> A;
        vector<int> B;
        for(int l = 0; l < L; l++) {
            int temp;
            scanf("%d", &temp);
            A.push_back(temp);
        }
        for(int l = 0; l < L; l++) {
            int temp;
            scanf("%d", &temp);
            B.push_back(temp);
        }
        cout << (solution(A, B) ? "YES" : "NO" ) << endl;
    }
    
    return 0;
}