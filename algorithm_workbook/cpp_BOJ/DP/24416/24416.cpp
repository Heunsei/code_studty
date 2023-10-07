// 피보나치수 
#include <iostream>

using namespace std;

int memo[41] = {0};
int n;
int c1, c2 = 0;

int fi(int n){
    if(n==1 || n==2){
        c1++;
        return 1;
    }
    else{
        return (fi(n-1) + fi(n-2));
    }
}

int main(){
    std::cin >> n;
    fi(n);

    memo[1] = memo[2] = 1;
    for(int i{3}; i<=n; i++){
        memo[i] = memo[i-1] + memo[i-2];
        c2++;
    }
    std::cout << c1 << " " << c2;
    return 0;
}