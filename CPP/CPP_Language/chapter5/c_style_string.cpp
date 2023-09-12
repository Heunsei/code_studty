# include <iostream>
# include <cstring>
# include <cctype>

using namespace std;

int main()
{
    char first_name[20] {};
    char last_name[20] {};
    char full_name[50] {};
    char temp[50] {};

    cout << first_name; // 쓰레기값을 출력

    cout << "please enter your first name";
    cin >> first_name;
    cout << "please enter your last name";
    cin >> last_name;

    cout << "-------------------------" << endl;

    cout << "hello," << first_name << "your first name has" << strlen(first_name) << "characters" << endl;
    cout << "and your last name, " << last_name << "has" << strlen(last_name) << "characters" << endl;

    strcpy(full_name, first_name); // 처음 full_name에  first_name 복사
    strcat(full_name, " ");        // space를 한칸 넣어줌
    strcat(full_name, last_name);   // full_name에 last_name를 더해줌

    cout << "my full name is" << full_name << endl;

    cout << "enter your full name" << endl;
    cin.getline(full_name, 50);
    cout << "your full name is " << full_name << endl;
    
    cout << "---------------------" << endl;

    strcpy(temp, full_name); // 같으면 0반환 1이 2보다 작으면 음수반환 아니면 양수반환
    if (strcmp(temp, full_name) == 0)
        cout << temp << "and" << full_name << "are the same" << endl;
    else
        cout << temp << "and" << full_name << "are different" << endl;
    
    cout << "---------------------------------------" << endl;
    
    for (size_t i {0}; i < strlen(full_name); ++i){
        if(isalpha(full_name[i]))
            full_name[i] = toupper(full_name[i]);
    }

    cout << "Your full name is" << full_name << endl;

    cout << "-------------------------" << endl;

    if(strcmp(temp, full_name) == 0){
        cout << temp << "and" << full_name << "is same" << endl;
    }
    else
        cout << temp << "and" << full_name << "is different" << endl;
    
}