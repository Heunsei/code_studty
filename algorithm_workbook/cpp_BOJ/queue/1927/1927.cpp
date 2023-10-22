#include <queue>
#include <iostream>

using namespace std;

int n;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    std::cin >> n;
    priority_queue<int> q;
    for(int i{0}; i<n; i++){
        int x;
        std::cin >> x;
        if(x==0){
            if(q.empty()) std::cout<< '0' << '\n';
            else{
                std::cout << q.top() << '\n';
                q.pop();
            }
        }
        else{
            q.push(x);
        }
    }
    return 0;
}