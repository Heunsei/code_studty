int parent[100];

int find_parent(int x){
    if(parent[x] != x)
        return parent[x] = find_parent(parent[x]); 
    return x;     
}
void merge(int a, int b){
    int x = find_parent(a);
    int y = find_parent(b);
 
    if(x != y){
        if(x < y) // 그룹번호가 더 작은 쪽으로 합치기
            parent[y] = x;
        else
            parent[x] = y;
    }    
}