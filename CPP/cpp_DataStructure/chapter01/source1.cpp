// 동적 크기 배열 구하기

#include<iostream>
#include<sstream>
#include<algorithm>
#include<string>

template <typename T>
class dynamic_array
{
    T* data;
    size_t n;

    public:
        // 생성자
        dynamic_array(int n)
        {
            this->n = n;
            data = new T[n];
        }
        // 복사 생성자
        dynamic_array(const dynamic_array<T>& other)
        {
            n = other.n;
            data = new T[n];

            for(int i =0; i < n ; i++)
                data[i] = other[i];
        }

    // 접근을 위한 []연산자와 at()함수 작정
    T& operator[](int index)
    {
        return data[index];
    }
    const T& operator[](int index) const
    {
        return data[index];
    }
    T& at(int index)
    {
        if(index<n)
            return data[index];
        throw "index out of range";
    }
    // size 함수 생성
    size_t size() const
    {
        return n;
    }
    // 소멸자
    ~dynamic_array()
    {
        delete[] data;
    }
    // 반복자 관련 함수
    T* begin() {return data;}
    const T* begin() {return data;}
    T* end() {return data + n;}
    const T* end() {return data + n;}
    // + 연산
    friend dynamic_array<T> opreator+(const dynamic_array<T> arr1,
                                        const dynamic_array<T> arr2)
    {
            dynamic_array<T> result(arr1.size() + arr2.size());
            std::copy(arr1.begin(), arr1.end(), result.begin());
            std::copy(arr2.begin(), arr2.end(), result.begin()+arr1.size());
            return result;
    }
    // 구분을 위한 sep를 인자로 받으며 기본값을 쉼표로 지정
    std::string to_string(const std::string& sep = ", ")
    {
        if(n == 0)
            return "";
            
        std::ostringstream os;
            os << data[0];

        for(int i = 1; i < n; i++)
        {
            os << sep << data[i];
        }

        return os.str();
    }
    
};

struct student
{
    std::string name;
    int standard;
};

std::ostream& operator<<(std::ostream& os, const student& s)
{
    return (os <<"[" << s.name << ", " << s.standard << "]");
}

int main()
{
    int nStudents;
    std::cout << "1반 학생 수를 입력하세요 : ";
    std::cin >> nStudents;

    dynamic_array<student> class1(nStudents);

    for(int i = 0; i < nStudents; i++)
    {
        std::string name;
        int standard;
        std::cout << i + 1 << "번째 학생 이름과 나이를 입력 하십시오";
        std::cin >> name >> standard;
        class1[i] = student{name, standard};
    }

    // 깊은 복사
    auto class2 = class1;
    std::cout << "1반을 복사해서 2반생성 : " ;

    return 0;
}