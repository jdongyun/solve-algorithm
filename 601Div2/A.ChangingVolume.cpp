#include <iostream>
#include <algorithm>

using namespace std;

int solution(int A, int B) {
    if(A == B) return 0;
    if(A < B) swap(A, B); //A가 B보다 크도록
    
    int ret = (A - B) / 5; //무조건 -5를 누르는 게 이득
    int mod = (A - B) % 5; //0부터 4의 남은 음량 카운트
    ret += (mod + 1) / 2;
    
    return ret;
}

int main(void) {
    int T;
    cin >> T;
    
    for(int i = 0; i < T; i++) {
        int A, B;
        scanf("%d %d", &A, &B);
        printf("%d\n", solution(A, B));
    }
    
    return 0;
}