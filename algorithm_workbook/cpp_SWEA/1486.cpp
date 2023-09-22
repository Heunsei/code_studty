#include <iostream>
#include <algorithm>
#include <string.h>
#define INF 987654321

using namespace std;

int N, B;
int arr[20];
int res;

void mk_top(int depth, int acc){
  if(depth == N){
    if(acc >= B){
      res = min(res, acc);
    }
    return;
  }
  mk_top(depth+1, acc + arr[depth]);
  mk_top(depth+1, acc);
}


int main(){
  int tc;
  int T;

  cin >> T;

  for(tc=1; tc<=T; tc++){
    N = 0, B = 0;
    memset(arr, 0, sizeof(arr));
    res = INF;

    cin >> N >> B;
    for(int i = 0; i < N; i++){
      cin >> arr[i];
    }

    mk_top(0,0);

    cout << "#" << tc << " " << res - B << "\n";
  }
  return 0;
}
