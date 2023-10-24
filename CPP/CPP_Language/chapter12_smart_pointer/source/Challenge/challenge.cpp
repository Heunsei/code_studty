#include <memory>
#include <iostream>
#include <vector>

using namespace std;

class Test{
private:
    int data;
public:
    Test() : data{0} {std::cout << "\tTest constructor (" << data << ")" << std::endl; }
    Test(int data) : data{data} {std::cout << "\tTest constructor (" << data << ")" << std::endl;}
    int get_data() const { return data; }
    ~Test() {std::cout << "\tDestructor (" << data << ")" << std::endl;} 
};

auto make();
void fill(std::vector<std::shared_ptr<Test>> &vec, int num);
void display(const std::vector<shared_ptr<Test>> & vec);

// 무엇을 반환하는지 정확히 아니까 auto로 가능
auto make(){
    // shared_ptr을 지니는 vector를 가리키는 포인터 생성
    return std::make_unique<std::vector<std::shared_ptr<Test>>>();
}

void fill(std::vector<std::shared_ptr<Test>> &vec, int num){
    int temp;
    for(int i{1}; i<=num; i++){
        std::cout << "Enter data Point [" << i << "] : " ;
        std::cin >> temp;
        // std::shared_ptr<Test> ptr = std::make_shared<Test>(temp);
        // vec.push_back(ptr);
        vec.push_back(std::make_shared<Test>(temp));
    }
}

void display(const std::vector<std::shared_ptr<Test>> &vec){
    std::cout << "\nDisplaying vector data" << std::endl;
    std::cout << "=========================" << std::endl;
    for(const auto &ptr : vec)
        std::cout << ptr ->get_data() << std::endl;
    std::cout << "======================="<< std::endl;
}

int main(){
    // 아직 아무곳도 가리키지 않는 ptr생성
    std::unique_ptr<std::vector<std::shared_ptr<Test>>> vec_ptr;
    // vec_ptr이 어디를 가리킬지 알려줌
    vec_ptr = make();
    std::cout << "How many data points do yo want to enter : ";
    int num;
    std::cin >> num;
    fill(*vec_ptr, num);
    display(*vec_ptr);
    return 0;
}