#include <iostream>
#include <queue>

using namespace std;

struct compare{
    bool operator()(int a, int b){
        int first = abs(a);
        int second = abs(b);

        if(first == second){
            // true를 리턴하면 앞에 위치한 값이 남음.
            return a > b;
        }
        else {
            return first > second;
        }
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N;
    cin >> N;
    priority_queue<int, vector<int>, compare> pq;

    for (int i{0}; i<N; i++){
        int req;
        cin >> req;
        if (req == 0){
            if(pq.empty()){
                cout << "0\n";
            }
            else {
                cout << pq.top() << '\n';
                pq.pop();
            }
        } else {
            pq.push(req);
        }
    }
    return 0;
}