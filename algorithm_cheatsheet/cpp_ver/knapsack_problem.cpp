#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

struct Object{
    int id;             // id값
    int weight;         // 담을 무게
    double value;       // 담을 물건의 가치
    double value_per_unit_weight;

    Object(int i, int w, double v) : id(i), weight(w), value(v),
        value_per_unit_weight(v/w) {}
    
    // std::sort에서 사용할 예정
    inline bool operator< (const Object& obj){
        // 비교연산자 오버로딩
        // 왼쪽에 오는 값이 this 객체임
        return this->value_per_unit_weight < obj.value_per_unit_weight;
    }
    // friend함수는 멤버함수가 아니다.
    friend std::ostream& operator<<(std::ostream& os, const Object& obj);
};

std::ostream& operator<<(std::ostream& os, const Object& obj){
    os << "[" << obj.id << "] 가격" << obj.value << "\t무게: " << obj.weight
    << "kg단위 무게 당 가격 : " << obj.value_per_unit_weight;
    return os;
}

// 담겨진 물건들을 확인하고 빼는 함수
auto fill_kanpsack(std::vector<Object>& objects, int kanpsack_capacity){
    std::vector<Object> knapsack_content;  
    knapsack_content.reserve(objects.size());

    // 물건들을 내림차순으로 정렬
    std::sort(objects.begin(), objects.end());
    std::reverse(objects.begin(), objects.end());

    auto current_object = objects.begin();  // 맨처음에 집어볼 가치가 가장 큰 오브젝트
    int current_total_weight = 0;           // 총 선택한 무게

    // 총 수용량을 넘기지 않으면서  현재 오브젝트가 끝까지 가지 않을때 까지
    while(current_total_weight < kanpsack_capacity && current_object != objects.end()){
        knapsack_content.push_back(*current_object);

        current_total_weight += current_object->weight;
        current_object++;
    }

    int weight_of_last_obj_to_remove = current_total_weight - kanpsack_capacity;
    Object& last_object = knapsack_content.back();
    if(weight_of_last_obj_to_remove > 0){   // 현재 용량이 적재량을 초과한다면 마지막 원소를 빼줄것
        last_object.weight -= weight_of_last_obj_to_remove;
        last_object.value -= last_object.value_per_unit_weight * weight_of_last_obj_to_remove;
    }
    return knapsack_content;
}

int main(int argc, char argv[]){
    std::vector<Object> object;
    object.reserve(7);

    std::vector<int> weights {1, 2, 5, 9, 2, 3, 4};
    std::vector<double> values {10, 7, 15, 10, 12, 11, 5};

    for (auto i{0}; i<7; i++){
        object.push_back(Object(i+1, weights[i], values[i]));
    }

    std::cout << "[사용할 수 있는 물건 정보]" << std::endl;
    for (auto& o : object)
        std::cout << o << std::endl;
    std::cout << std::endl;

    int knapsack_capacity = 7;
    auto solution = fill_kanpsack(object, knapsack_capacity);

    std::cout << "[배낭에 넣을 물건들 ( 최대 용량 = " << knapsack_capacity << ")]" << std::endl;
    for (auto& o : solution){
        std::cout << o << std::endl;
    }
    std::cout << std::endl;
}