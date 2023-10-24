#include <iostream>

double calculate_mpg(int miles, int gallons){
    if (gallons==0)
        throw 0;
    return static_cast<double>(miles) / gallons;
}

int main(){
    double mile_to_gallon {};
    int miles {};
    std::cout << "Enter the miles : "; 
    std::cin >> miles;
    int gallons {};
    std::cout << "Enter the gallons : "; 
    std::cin >> gallons;
    try{
        mile_to_gallon = calculate_mpg(miles, gallons);
        std::cout << "Resutl : " << mile_to_gallon << std::endl;
    }catch(int &ex){
        std::cout << "zero division error"<< std::endl;
    }
    std::cout << "Bye" << std::endl;
}
