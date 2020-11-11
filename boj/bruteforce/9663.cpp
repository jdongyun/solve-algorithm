#include <iostream>
using namespace std;
int n;
int count = 0;
bool arr[15][15];

bool check(int x, int y) {
    for (int i = 0; i < x; i++) {
        if (arr[i][y]) {
            return false;
        }
    }
    
    for (int i = x-1, j = y-1; i >= 0 && j >= 0; i--, j--) {
        if (arr[i][j]) {
            return false;
        }
    }
    
    for (int i = x-1, j = y+1; i >= 0 && j < n; i--, j++) {
        if (arr[i][j]) {
            return false;
        }
    }
    return true;
    
}

void dfs(int x) {
    if (x == n) {
        count++;
        return;
    }
    for (int y = 0; y < n; y++) {
        if (!arr[x][y] && check(x, y)) {
            arr[x][y] = true;
            dfs(x + 1);
            arr[x][y] = false;
        }
    }
}

int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            arr[i][j] = false;
        }
    }
    
    dfs(0);
    printf("%d\n", count);
    
    return 0;
}