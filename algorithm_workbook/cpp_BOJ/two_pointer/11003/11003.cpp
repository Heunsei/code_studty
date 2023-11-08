#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    int N, L;
    std::cin >> N >> L;
    vector<int> arr (N, 0);
    vector<int> D (N, 0);

    for (int i{0}; i<N; i++){
        cin >> arr[i];
    }


    for(int i{0}; i<L; i++){
        if (i==0) D[i] = arr[i];
        D[i] = min(D[i-1], arr[i]);
    }


    int j = 0;
    while(j < N){
        int i;
        if(j-L < 0) i = 0;
        else i = j-L;
        

    }

    return 0;
}