#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N, M;
vector<pair<int,int>> reagents; // 화학물질 a,b가 들어있음

bool compare(pair<int,int> a, pair<int,int> b){
    if (a.first > b.first) return true;
    else return false;
}

void input(){
    cin >> N;
    for(int i{0}; i<N; i++){
        int a, b;
        cin >> a >> b;
        reagents.push_back({a,b});
    }
    cin >> M;
}

void solve(){
    int start_a = reagents[0].first;
    int start_b = reagents[0].second;
    // i는 넣어볼 용액의 양, 0부터 M까지 전부 넣어볼 것
    for(int i{0}; i<M+1; i++){
        bool okay = true;
        int acc = i;    // 누적값 M보다 커지면 break
        int spawn_gas = start_a * i + start_b;   // 생성된 가스의 양
        for(int j{1}; j<N; j++){
            int selected_a = reagents[j].first;  // j번째로 생성된 가스의 a와 b
            int selected_b = reagents[j].second;
            // spawn_gas와 값을 맞추기위한 필요 req의 양
            double req_solution = (spawn_gas-selected_b) / (double)selected_a;
            if (req_solution - int(req_solution) != 0){  // 만약 소수점이 있다면 그만
                okay=false;
                break;
            }    
            if (acc + req_solution > M) {
                okay=false; 
                break;
            }
            else{
                acc += req_solution;
            }
        }

        if (acc==M && okay){
            cout << spawn_gas;
            return;
        } 
        else continue;   
    }
    cout << 0;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    input();
    sort(reagents.begin(), reagents.end(), compare);
    solve();

    return 0;
}