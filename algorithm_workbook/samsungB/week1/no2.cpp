#include <iostream>
#include <stack>

using namespace std;
int main () {
    int TC;
    cin >> TC;
    for (int i{1}; i<=TC; i++){
        int N, M;
        cin >> N >> M;
        int checker = (1<<N) - 1;
        //  그냥 비트연산 때리면 알아서 비교한뒤에 결과 값을 알려준다
        if(checker == (M & checker)){
            cout << '#' << i << " ON" << '\n' ;
        }else{
            cout << '#' << i << " OFF" << '\n' ;
        }
    }
}