// 분할정복 기법중 하나
// 1. 초기상태에 정렬되지 않은 리스트를 제공
// 2. 이 리스트를 두 개의 리스트가 되도록 분할
// 3. 부분리스트를 정렬
// 4. 정렬된 부분 리스트들을 하나의 리스트에 병합
// 메모리 활용이 비효율적

#include <iostream>
#define N 100000

using namespace std;
int sorted[8];


void merge(int arr[], int start, int end){
    int mid = (start+end)/2;
    // k는 sorted 리스트의 위치를 가르킬 변수
    // 왼쪽과 오른쪽을 가리키는 i,j를 비교해서 i가 더 작다면 i의 값을 k번째에 넣고
    // k와 i를 증가시키고 그대로있던 j를 i와 비교. 이 작업을 i가 mid보다 작을때까지, j가 end보다
    // 작을때까지 반복한다
    int i = start;
    int j = mid + 1;
    int k = start;
    // 왼쪽 리스트와 오른쪽리스트의 값을 비교하면서 sorted란 배열에 넣는다
    while(i<=mid && j<=end){
        if(arr[i] < arr[j]){
            sorted[k++] = arr[i++];
        }else{
            sorted[k++] = arr[j++];
        }
    }
    // 왼쪽 정렬이 끝났으니까, 오른쪽을 다 때려박아주는과정
    if(i>mid){
        while(j<=end){
            sorted[k++] = arr[j++];
        }
    }
    // 오른쪽 정렬이 끝났으니, 왼쪽을 전부 때려박는 과정
    if(j>end){
        while(i<=mid){
            sorted[k++] = arr[i++];
        }
    }
    for(int i{0}; i<=end; i++){
        arr[i] = sorted[i];
        std::cout << arr[i]<<' ';
    }
    std::cout << std::endl;
}

// 주어진 정렬을 더 이상 나눌 수 없을 때 까지 쪼갠 후, 크기가 1인 배열들을 순차적으로 합치며 정렬
void mergeSort(int arr[], int start, int end){
    if(start<end){
        int mid = (start+end)/2;
        // 재귀호출을 이용해 가장 작은(크기가 1)크기까지 내려간뒤 merge를 아래서부터 실행
        mergeSort(arr,start,mid);
        mergeSort(arr,mid+1,end);
        merge(arr,start,end);
    }
}

int main(){
    int arr[8] = {15, 147, 11, 46, 78, 32, 1, 17};
    mergeSort(arr,0,7);
}