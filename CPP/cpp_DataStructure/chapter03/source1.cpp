#include <vector>
#include <iostream>

using namespace std;

using unit = unsigned int;

class hash_map{
    std::vector<int> data;
public:
    hash_map(size_t n){ // 생성자 작성
        data = std::vector<int> (n, -1);
    }
    
    void insert(unit value){
        int n = data.size();
        data[value%n] = value;  // 값을 확인하지 않고 그냥 덮어씌움
        cout << value << "를 삽입" << std::endl;    
    }

    bool find(unit value){
        int n = data.size();
        return (data[value%n] == value);
    }

    void erase(unit value){
        int n = data.size();
        if (data[value%n] == value){
            data[value%n] = -1;
            std::cout << value << "를 삭제했습니다" << std::enld;
        }
    }
};

int main(){
    hash_map map(7);
    auto print = [&](int value){
        if(map.find(value)) std:: cout << "해시맵에서 " << value << "를 찾았습니다";
        else std::cout << "해시맵에서 " << value << "를 찾지 못했습니다";
        std::cout << std::endl;
    }
}