#include <iostream>
#include <vector>


using namespace std;

void solution(vector<int>& V) {
    if(V.size() < 10) {
        printf("0 0 0\n");
        return;
    }
    
    int m = V.size() / 2;
    while(m > 0) {
        if(V[m] < V[m-1])
            break;
        m--;
    }
    
    int g = 1;
    while(g < m) {
        if(V[g] < V[g-1]) break;
        g++;
    }
    
    int s = g+g+1;
    while(s < m) {
        if(V[s] < V[s-1]) break;
        s++;
    }
    s -= g;
    
    int b = m - g - s;
    if(g < s && g < b)
       printf("%d %d %d\n", g, s, b);
    else printf("0 0 0\n");
    
}

int main(void) {
    int T;
    cin >> T;
    for(int t = 0; t < T; t++) {
        int L;
        cin >> L;
        vector<int> V;
        V.reserve(L);
        for(int l = 0; l < L; l++) {
            int t;
            scanf("%d", &t);
            V.push_back(t);
        }
        solution(V);
    }
}