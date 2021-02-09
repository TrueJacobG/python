#include <bits/stdc++.h>
#include <iostream>
#include <string>

using namespace std;

string word;
string arr[110];

template <size_t N>
void splitString(string (&arr)[N], string str)
{
    int n = 0;
    istringstream iss(str);
    for (auto it = istream_iterator<string>(iss); it != istream_iterator<string>() && n < N; ++it, ++n)
        arr[n] = *it;
}

int main()
{
    cin >> word;
    string arr[4];

    splitString(arr, word);

    for (int i = 0; i < 4; i++)
        cout << arr[i] << endl;

    return 0;
}