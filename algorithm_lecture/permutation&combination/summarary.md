# 순열
- 순서를 따지고, 중복을 허용하지 않는다
- 중복을 검사하기 위한 check 배열을 사용
- depth 를 하나씩 늘려가며, 배열에 하나씩 채우는 방법을 재귀를 수행
```cpp
int pArr[r] = {0, };
bool check[n+1] = {false, };

void permutation(int depth){
    if(depth ==r){
    printArray(pArr);
    return;
    }
    for(int i = 1; i <= n; i++){
        if (!check[i]){
            check[i] = true;
            pArr[depth] = i;
            permutation(depth+1);
            check[i] = false;
        }
    }
}

int main(){
    cout << " 순열 " << endl;
    permutataion(0);
    
    return 0;
```

# 중복순열
- 순서를 따지고 중복을 허용한다
- 중복 검사를 제외하면 순열코드와 진행 양상이 똑같음
```cpp
int dpArr[r] = {0, };

void duplicatePermutation(int depth){
    if(depth == r){
        printArray(dpArr);
        return;
    }
    
    for(int i = 0; i <= n; i++){
        dpArr[depth] = i;
        duplicatePermutation(depth+1);
    }
}

int main(){
    cout << " 중복 순열" << endl;
    duplicatePermutation(0);
    
    return 0;
}    
```

# 순열에서 특수한 경우
- 오름차순으로 출력 해야 할때
- >> 그때는 인덱스를 넣어줘서 인덱스를 늘려가며 이 전 것을 출력하지 않도록 한다
```python
def dfs(depth, index):
    if depth == M:
        print(' '.join(map(str, pArr)))
        return
    for i in range(index, N+1):
        pArr.append(i)
        dfs(depth+1, i)
        pArr.pop()
dfs(0,1)
```  
# 조합
- 순서를 따지지 않고, 중복을 허용하지 않는다
- 반복문을 돌며 모든 경우에 대해 선택하는것
- 반복문 시작값은 이전 값의 + 1만큼 이어야 한다
```cpp
// r은 우리가 구할 배열의 길이
int cArr[r] = { 0, };
// 깊이와 다음을 지시할 지시자
void combination(int depth, int next){
    // 깊이가 구하려는 조합의 길이만큼 늘어났을 때
    if(depth == r){
        printArray(cArr);
        return;
    }
    // for문을 돌릴때 시작값을 1을 넣어줘야 다음꺼부터 확인 가능
    for(int i = next; i <= n; i++){
        cArr[depth] = i;
        combination(depth + 1, i + 1);
    }
}

int main(void){
    cout << " 조합 " <<  endl;
    combination(0,1);
    
    return 0
```

# 비트연산으로 조합 생성
```python
a= [3,6,7,1,5,4]
N = 6
for i in range(1<<N):
    subset1 = []
    for j in range(N):
            if i&(1<<j): # j번 비트가 0이 아니면
                subset1.append(a[j])
    print(*subset1)
```

# 중복 조합
- 순서를 따지지 않고, 중복을 허용한다.
- 조합과 구현이 비슷하나 반복문의 시작 값은 이전에 선택한 값이 된다.
```cpp
int dcArr[r] = { 0, };

void duplicateCombination(int depth, int next){
    if(depth == r){
        printArray(dcArr);
        return;
    }
    
    for(int i = next; i <= n; i++){
        dcArr[depth] = i;
        duplicateCombination(depth + 1, i);
    }
}

int main(void){
    cout << " 중복 조합" << endl;
    duplicateCombination(0,1);
       
    return 0
}
```