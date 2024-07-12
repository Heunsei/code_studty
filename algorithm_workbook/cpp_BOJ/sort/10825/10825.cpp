#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

struct STUDENT {
    string name;
    int kor, eng, math; 
};

bool cmp(STUDENT A, STUDENT B){
    if(A.kor == B.kor && A.eng == B.eng && A.math == B.math) return A.name < B.name;
    if(A.kor == B.kor && A.eng == B.eng ) return A.math > B.math;
    if(A.kor == B.kor) return A.eng < B.eng;
    return A.kor > B.kor;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int N;
    cin >> N;
    vector<STUDENT> v(N);

    for (int i{0}; i<N;i++){
        cin >> v[i].name >> v[i].kor >> v[i].eng >> v[i].math;
    }

    sort(v.begin(), v.end(), cmp);
    
    for(auto i : v){
        cout << i.name << '\n';
    }
}