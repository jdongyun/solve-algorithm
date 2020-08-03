#include <iostream>

using namespace std;

void solution(int data[]) {
    
    if((data[0] > 0 && data[3] > data[2]) ||
       (data[2] > 0 && data[0] > data[1]) ||
       data[1] + data[3] < data[0] + data[2] - 1 ||
       data[1] + data[3] > data[0] + data[2] + 1) { 
        cout << "NO" << endl;
        return;
    }

    int length = data[0] + data[1] + data[2] + data[3];
    
    int r[100000] = {0};
    
    int first = 0;
    if(data[1] + data[3] > data[0] + data[2]) { //1이 먼저냐 0이 먼저냐
            //1이 먼저다
            first = 1;
    }
    
    for(int i = 0; i < length; i++) {
        if(i % 2 == 0) {
            if(data[first] > 0) {
                r[i] = first;
                data[first]--;
            }
            else r[i] = first + 2;
        } else {
            if(data[(first + 1) % 2] > 0) {
                r[i] = (first + 1) % 2;
                data[(first + 1) % 2]--;
            }
            else r[i] = ((first + 1) % 2) + 2;
        }
    }
    cout << "YES" << endl;
    for(int i = 0; i < length; i++) {
        cout << r[i] << " ";
    }
    
}

int main(void) {
    int input[4];
    cin >> input[0] >> input[1] >> input[2] >> input[3];
    solution(input);
    return 0;
}