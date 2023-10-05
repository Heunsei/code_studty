# include <iostream>
# include <string>

using namespace std;

const double pi = 3.141592;

// Function prototype
double cal_area_circle(double);
double cal_vol_cylinder(double, double);
void area_circle();
void vol_cylinder();

int main()
{
  vol_cylinder();
  return 0;
}

double cal_area_circle(double rad){
  return pi * rad * rad;
}

double cal_vol_cylinder(double rad, double height){
  return cal_area_circle(rad) * height;
}

void area_circle(){
  double rad {};
  cout << "\nEnter the rad of the circle: ";
  cin >> rad;
  cout << "The area of a circle with rad" << rad << "is" << cal_area_circle(rad) << endl;
}

void vol_cylinder(){
  double rad {};
  double height {};
  cout << "\nEnter the rad of cylinder: ";
  cin >> rad;
  cout << "\nEnter the height of cylinder: ";
  cin >> height;
  cout << "The vol of cylinder is : " << cal_vol_cylinder(rad, height) << endl;
}