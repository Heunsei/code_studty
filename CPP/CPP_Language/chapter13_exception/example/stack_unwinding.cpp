#include <iostream>
#include <string>

using namespace std;

void func_a(){
    std::cout << "starting func_a" << std::endl;
    func_b();
    std::cout << "ending func_a" << std::endl;  // 출력 x
}

void func_b(){
    std::cout << "starting func_b" << std::endl;
    try{
        func_c();
    }catch(int &ex){
        std::cout << "Caught error in b" << std::endl;
    }
    std::cout << "ending func_b" << std::endl;  // 출력 x
}

void func_c(){
    std::cout << "starting func_c" << std::endl;
    throw 100;
    std::cout << "ending func_c" << std::endl; // 출력 x
}

int main(){
    std::cout << "Starting Main" << std::endl;
    try{
        func_a();
    }
    catch(int &ex){
        std::cout << "Caught error in main" << std::endl;
    }
    std::cout << "Finishing main" << std::endl;
    return 0;
}