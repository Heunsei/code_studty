// BOJ : 12891 DNA 비밀번호
#include <iostream>
#include <string>

using namespace std;

int pwd_count[4] = {0, };
int compare[4] = {0, };

// 지금까지 나온 임시비밀번호의 문자열 갯수를 저장
void add(char c){
    switch(c){
        case 'A':
            pwd_count[0] ++;
            break;
        case 'C':
            pwd_count[1] ++;
            break;
        case 'G':
            pwd_count[2] ++;
            break;
        case 'T':
            pwd_count[3] ++;
            break;
    }   
}

// 문자열 갯수를 보고 빼기
void sub(char c){
    switch(c){
        case 'A':
            pwd_count[0] --;
            break;
        case 'C':
            pwd_count[1] --;
            break;
        case 'G':
            pwd_count[2] --;
            break;
        case 'T':
            pwd_count[3] --;
            break;
    }   
}

bool check(){
    bool pass = true;
    for(int i{0}; i<4; i++){
        if (pwd_count[i] < compare[i])
            pass = false;
    }
    return pass;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    // 임의의 문자열 길이 S, 부분비밀번호 P자리
    int S, P;
    cin >> S >> P;
    // 비밀번호를 찾을 문자열
    string passward;
    cin >> passward;
    // 최소입력값 받아오기
    for(int i{0}; i<4; i++){
        cin >> compare[i];
    }

    int i = 0;   // 시작 
    int j = i + P - 1; // 끝지점
    int result = 0;

    for(int i{0}; i<=j; i++){   // 초기 첫 P글자 확인
        add(passward[i]);   
    }

    while (j < S){
        if (check()) result++;
        // cout << i << " " << j << " count : " << result <<'\n';
        sub(passward[i]);
        i+=1; j+=1;     // 비밀번호 길이는 일정하니 1칸씩 오른쪽으로
        add(passward[j]);
    }
    cout << result << '\n';
    return 0;
}