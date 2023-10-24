#include <iostream>

class ZeroDivisionError{
};
class NegativeValueError{
};

double calculat_mpg(int miles, int gallons){
    if (gallons == 0) throw ZeroDivisionError();
    if (miles<0 || gallons<0) throw NegativeValueError();
    return static_cast<double> (miles) / gallons;
}

int main(){
    int miles {};
    int gallons {};
    int mile_per_gallon {};
    std::cout << "Enter miles : ";
    std::cin >> miles;
    std::cout << "Enter gallons : ";
    std::cin >> gallons;
    try{
        mile_per_gallon = calculat_mpg(miles,gallons);
        std::cout << "Result : " << mile_per_gallon << std::endl;
    }
    catch(const ZeroDivisionError &ex){
        std::cout << "ZeroDizisionError" << std::endl;
    }catch(const NegativeValueError &ex){
        std::cout << "NegativeValueError" << std::endl;
    }
    std::cout << "Bye" << std::endl;
    return 0;
}