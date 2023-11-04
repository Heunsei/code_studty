#include <iostream>
#include <array>


using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    int N, M;
    std::cin >> N >> M;
    std::array<int, 100'000> acc;

    for(int i{1}; i<N+1; i++){
        int tmp;
        cin >> tmp;
        acc[i] = acc[i-1] + tmp;
    }
    
    // for(int i{0}; i<N; i++){
    //     cout << acc[i] <<endl;
    // }

    for(int i{0}; i<M; i++){
        int a, b;
        cin >> a >> b;
        cout << acc[b] - acc[a-1] << '\n';
    }
    return 0;
}