#include <list>
#include <iostream>
#include <vector>
#include <algorithm>

using unit = unsigned int;
// 중복을 허용하는 해쉬맵
class hash_map{
    std::vector<std::list<int>> data;
public: 
    hash_map(size_t n){
        data.resize(n);
    }

    void insert(unit value){
        int n = data.size();            // vector의 크기
        data[value % n].push_back(n);
        std::cout << value << " 를 삽입했습니다" << std::endl;
    }

    bool find(unit value){
        int n = data.size();
        auto &entries = data[value%n];
        return std::find(entries.begin(), entries.end(), value) != entries.end();
    }

    void erase(unit value){
        int n = data.size();
        auto& entries = data[value%n];
        auto iter = std::find(entries.begin(), entries.end(), value);
        if (iter != entries.end()){
            entries.erase(iter);
            std::cout << value << "를 삭제했습니다." << std::endl;
        }
    }
};

int main(){
    hash_map map(7);
    auto print = [&](int value){
        if (map.find(value)){
            std::cout << value << "발견!";
        }else{
            std::cout << value << "를 찾지 못했습니다";
        }
        std::cout << std::endl;
    };
}