#include <iostream>

using namespace std;

int main(){
    int miles {};
    int gallons {};
    double mile_to_gallon {};

    std::cout << "Enter the miles : ";
    std::cin >> miles;
    std::cout << "Enter the gallons : ";
    std::cin >> gallons;

    try{
        if (gallons==0)
            throw 0;
        mile_to_gallon = static_cast<double>(miles) / gallons;
        std::cout << "Result" << mile_to_gallon << std::endl;
    }catch (int &ex){
        std::cerr << "Sorry, can't divide by zero" << std::endl;
    }
    std::cout << "Bye" << std::endl;
}