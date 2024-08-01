#include <bits/stdc++.h>

using namespace std;

bool comp(const string& a, const string& b) {
  if (a.size() != b.size())
    return a.size() < b.size();
  return a < b;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int n; cin >> n;

  vector<string> words(n);
  for (int i = 0; i < n; i++)
    cin >> words[i];

  sort(words.begin(), words.end(), comp);

  words.erase(unique(words.begin(), words.end()), words.end());

  for (const auto& word : words)
    cout << word << "\n";

  return 0;
}