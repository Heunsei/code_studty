# include <iostream>
# include <string>
# include <iomanip>

using namespace std;

int main(){
  string s0;
  string s1 {"Apple"};
  string s2 {"Banana"};
  string s3 {"Kiwi"};
  string s4 {"apple"};
  string s5 {s1};  // Apple
  string s6 {s1, 0, 3}; // App
  string s7 (10,'X'); // XXXXXXXXXX

  cout << s0 << endl;
  cout << s0.length() << endl; 

  // cout << "----------Init----------" << endl;
  // cout << "s1 is init to" << s1 << endl;
  // cout << "s2 is init to" << s2 << endl;
  // cout << "s3 is init to" << s3 << endl;
  // cout << "s4 is init to" << s4 << endl;
  // cout << "s5 is init to" << s5 << endl;
  // cout << "s6 is init to" << s6 << endl;
  // cout << "s7 is init to" << s7 << endl;

  // compariosn
  // cout << s1 << "==" << s5 << " : " << (s1 == s5) << endl;
  // cout << s1 << "==" << s2 << " : " << (s1 == s2) << endl;
  // cout << s1 << "!=" << s5 << " : " << (s1 != s2) << endl;
  // cout << s1 << "<" << s2 << ":" << (s1 < s2) << endl;
  // cout << s2 << ">" << s1 << ":" << (s2 > s1) << endl;
  // cout << s4 << "<" << s5 << ":" << (s4 < s5) << endl;
  // cout << s1 << "==" << "Apple" << ":" (s1 == "Apple") << endl;

  // assignment
  // string t1 {};
  // string t2 {};
  // cout << "assignment" << endl;
  // t1 = "Watermelon";
  // cout << "t1 is now" << s1 << endl;
  // s2 = s1;
  // cout << "s2 is now" << s2 << endl;

  // string t3 {"Frank"};
  // cout << "s3 is now" << s3 <<endl;
  // s3[0] = 'C'; 
  // cout << "s3 change first letter to C" << endl; 
  // s3.at(0) = 'P';
  // cout << "s3 change first letter to : P" << s3 << endl;

  // councatenation
  // s3 = "Watermelon";
  // cout << "\nConcatenation" << "\n--------------------" << endl;  
  // s3 = s5 + " and" + s2 + " juice";
  // cout << "s3 is now" << s3 << endl;

  // s3 = "nice" + "cold" + s5 + " juice"; // compiler error 
  // c-style 문자열에서는 + 연산자를 지원을 하지 않음
  
  // looping
  // cout << "--------looping--------"
  // s1 = "Apple";
  // for (size_t i {0}; i < s1.length(); ++i)
  //   cout << s1.at(i);
  // cout << endl;

  // for (char c: s1)
  //   cout << c;
  // cout << endl;

  // Find
  // cout << "----------Find---------"
  // s1 = "The secret word is Boo";
  // string word {} ;
  
  // cout << "enter the word to find";
  // cin >> word;

  // size_t position = s1.find(word);
  // if (position != string::npos)
  //   cout << "Found" << word << "at position" << position << endl;
  // else
  //   cout << "sorry" << word << "not found" << endl;
  // cout << endl;
  return 0;
}