# include <vector>
# include <iostream>

using namespace std;

void display_menu();
char get_selection();

void handle_display(const vector<int> &v);
void handle_add(vector<int> &v);
void handle_mean(const vector<int> &v);
void handle_smallest(const vector<int> &v);
void handle_largest(const vector<int> &v);
void handle_find(const vector<int> &v);
void handle_quit();
void handle_unknown();

void display_list(const vector<int> &v);
double calculate_mean(const vector<int> &v);
int get_smallest(const vector<int> &v);
int get_largest(const vector<int> &v);
bool find(const vector<int> &v, int target);

int main(){
  vector<int> numbers;
  char selection {};

  do{
    display_menu();
    selection = get_selection();
    switch (selection)
    {
    case 'P':
      handle_display(numbers);
      break;
    case 'A':
      handle_add(numbers);
      break;
    case 'M':
      handle_mean(numbers);
      break;
    case 'S':
      handle_smallest(numbers);
      break;
    case 'L':
      handle_largest(numbers);
      break;
    case 'F':
      handle_find(numbers);
      break;
    case 'Q':
      handle_quit();
      break;
    default:
      handle_unknown();
    }
  }while(selection != 'Q');
  cout << endl;
  return 0;
}

void display_menu(){
  cout << "\nP - print numbers" <<endl;
  cout << "A - Add a number" <<endl;
  cout << "M - Display mean of the number" <<endl;
  cout << "S - Display smallest number" <<endl;
  cout << "L - Display largest number" <<endl;
  cout << "F - Find a number" <<endl;
  cout << "Q - Quit" <<endl;
  cout << "\nEnter your choice:";
}

void handle_display(const vector<int> &v){
  if (v.size() == 0)
    cout << "the list is empty" << endl;
  else
    display_list(v);
}

void handle_add(vector<int> &v){
  int num_to_add {};
  cout << "enter integer to add to the list";
  cin >> num_to_add;
  v.push_back(num_to_add);
  cout << num_to_add << "added" << endl;
}

void handle_mean(const vector<int> &v){
  if (v.size() == 0)
    cout << "empty!" << endl;
  else
    cout << "mean is " << calculate_mean(v) << endl;
}

void handle_largest(const vector<int> &v){

}

void handle_smallest(const vector<int> &v){

}

void handle_find(const vector<int> &v){
  int target {};
  cout << "Enter the number to find : ";
  cin >> target;
  if (find(v, target))
    cout << target << " was found" << endl;
  else
    cout << target << " was not found" << endl;
}

double calculate_mean(const vector<int> &v){
  int temp {};
  for (auto num:v)
    temp += num;
  return static_cast<double>(temp)/v.size();
}

void handle_quit(){
  cout << "Good bye" << endl;
}

void handle_unknown(){
  cout << "unknown" << endl;
}

void display_list(const vector<int> &v){
  cout << "[";
  for (auto num:v)
    cout << num << " ";
  cout << "]" << endl;
}

int get_smallest(const vector<int> &v){
  int smallest = v.at(0);
  for (auto num:v)
    if (num < smallest)
      smallest = num;
  return smallest;
}

bool find(const vector<int> &v, int target){
  for (auto num:v)
    if (num == target)
      return true;
  return false;
}