#include <cstddef>
#include <iterator>
#include <algorithm>
#include <string_view>
#include <vector>
#include <iostream>
#include <format>

using namespace std;

int main()
{
    using namespace std::literals; // ""sv 연산자 사용

    constexpr auto str = "whatever"sv;
    ostreambuf_iterator<char> o(cout);
    // ostream_iterator<char> o(cout); // 내부에서 << 연산자 사용

    cout << format("{}\n", 1); // 런타임 때 format_string이 결정되는 경우 vformat 사용
    format_to(o, "{}\n", 2);

    vector<int> numbers;
    size_t n;

    cin >> n;
    numbers.reserve(n);

    istream_iterator<int> in(cin);
    copy_n(in, n, back_inserter(numbers)); // cin으로부터 n개의 int를 numbers에 입력

    ostream_iterator<int> out(cout, " ");
    copy(begin(numbers), end(numbers), out); // n1 n2 n3 n4

    return 0;
}
