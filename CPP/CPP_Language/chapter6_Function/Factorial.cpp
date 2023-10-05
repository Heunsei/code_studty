// make factorial
using namespace std;

unsigned long long factorial(unsigned long long n){
  if (n == 0)
    return 1;
  return n * factorial(n-1);
}

unsigned long long fibo(unsigned long long n){
  if (n<=1)
    return n;
  return fibo(n-1) + fibo(n-2);
}


int main(){
  cout << factorial(8) << endl;
  return 0;
}