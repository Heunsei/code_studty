// N-queen
#include <iostream>
# define MAX 15
using namespace std;

int col[MAX];
int N, total = 0;
bool check(int level)
{
    for(int i = 0; i < level; i++)
        if(col[i] == col[level] || abs(col[i] - col[level]) == level - i)
            return false;
    return true;
}
void nqueen(int x)
{
    if(x == N)
        // N 까지 닿으면 배치할수 있는 가지수를 출력
        total++;
    else
    {
        for(int i = 0; i < N; i++)
        {
            col[x] = i;
            if(check(x))
                nqueen(x+1);
        }
    }
}

int main(){
    cin >> N;
    nqueen(0);
    cout << total;
}