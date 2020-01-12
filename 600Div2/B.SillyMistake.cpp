#include <iostream>
#include <vector>
#include <set>

using namespace std;

bool solve(vector<int>& V, vector<int>& ret) {
    int sum = 0;
    set<int> s_day, s_history;
    
    if(V.size() % 2 == 1) return false;
    
    for(int i = 0; i < V.size(); i++) {
        int v = V[i];
        if(v > 0) {
            if(!s_history.insert(v).second || !s_day.insert(v).second) {
                return false;
            }
            s_history.insert(v);
        } else {
            if(s_day.erase(-v) != 1) {
                return false;
            }
            if(s_day.empty()) {
                ret.push_back(i+1);
                s_history.clear();
            }
        }
    }
    
    if(!s_day.empty() || ret.empty()) return false;
    
    return true;
}

int main(void) {
    int N;
    cin >> N;
    vector<int> V;
    int temp;
    for(int i = 0; i < N; i++) {
        cin >> temp;
        V.push_back(temp);
    }
    vector<int> ret;
    bool sol = solve(V, ret);
    if(!sol) {
        cout << "-1";
    } else {
        cout << ret.size() << endl;
        cout << ret[0];
        for(int i = 1; i < ret.size(); i++) {
            cout << " " << (ret[i] - ret[i-1]);
        }
    }
    cout << endl;
    return 0;
}
