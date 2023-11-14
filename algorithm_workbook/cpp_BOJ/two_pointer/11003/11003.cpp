// A(i-L+1) 부터 A(i)까지 범위에 저장된 값들중 가장작은 수를출력 
#include <iostream>
#include <deque>

using namespace std;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    
    std::deque<pair<int,int>> arr;
    int N, L;
    cin >> N >> L;

    for (int i{0}; i<N; i++){
        int input;
        cin >> input;
        
        pair<int,int> node;  // 원소들을 넣고 비교할 노드
        
        node.first = i;      // 인덱스값을 저장할 first
        node.second = input; // 입력값을 저장할 second
        
        // arr의 맨마지막의 valud가 input보다 작을때까지 pop
        while (arr.size() && arr.back().second > input){
            arr.pop_back();
        }
        arr.push_back(node);  // 노드 삽입
        // 맨앞의 index가 맨뒤 index - L 보다 같거나 작으면 pop
        if(arr.front().first <= arr.back().first - L) arr.pop_front();
        cout << arr.front().second << " ";            
    }
    return 0;
}