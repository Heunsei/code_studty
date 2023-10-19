// 최소 스패닝 트리
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int vertex, e, answer;
int parent[10'001];
vector<pair<int, pair<int,int>>> tree;

int Find(int x){
    if(parent[x] == x) return x;
    return parent[x] = Find(parent[x]);
}

void Union(int x, int y){
    x = Find(x);
    y = Find(y);

    if(x!=y) parent[y] = x;
}

bool SameParent(int x, int y){
    x = Find(x);
    y = Find(y);

    if (x==y) return true;
    else return false;
}


int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    std::cin >> vertex >> e;
    for(int i{0}; i<e; i++){
        int from, to, cost;
        std::cin >> from >> to >> cost;
        tree.push_back({cost,{from,to}});
    }
    sort(tree.begin(), tree.end());

    for(int i=0; i<vertex; i++){
        parent[i] = i;
    }
    
    for(int i=0; i<e; i++){
        if(SameParent(tree[i].second.first, tree[i].second.second) == false){
                Union(tree[i].second.first, tree[i].second.second);
                answer = answer + tree[i].first;
        }
    }
    cout << answer;
    return 0;
}