// BOJ 11404 플로이드
// n개의 도시, 다른도시에 도착하는 m개의 버스

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

const int inf = 1e9;
int arr[101][101];
int n,m;

int main(){
  std::cin >> n >> m;
  // 크기만큼 배열을 초기화
  for(int i{0}; i<=n; i++){
    for(int j{0}; j<=n; j++){
      arr[i][j] = i==j ? 0 : inf;
    }
  }
  // 정점들을 입력받을때 이전값이랑 비교해서 더 작은길을 넣어줌
  for(int i{0}; i<m; i++){
    int a,b,c;
    std::cin >> a >> b >> c;
    arr[a][b] = min(arr[a][b], c);
  }

  for(int k{1}; k<=n; k++){
    for(int i{1}; i<=n; i++){
      for(int j{1}; j<=n; j++)
        arr[i][j] = min(arr[i][k] + arr[k][j], arr[i][j]);
    }
  }

  for(int i{1}; i<=n; i++){
    for(int j{1}; j<=n; j++){
      if(arr[i][j] == inf) std::cout << "0 " ;
      else std::cout << arr[i][j] << ' ';
    }
    std::cout << std::endl;
  }
  return 0;
}


  
