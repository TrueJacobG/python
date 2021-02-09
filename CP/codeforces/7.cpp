#include <bits/stdc++.h>

using namespace std;

string string1, string2;

int main()
{
    cin >> string1 >> string2;

    for (int i = 0; i < (string1).size(); i++)
    {
        string1[i] = tolower(string1[i]);
        string2[i] = tolower(string2[i]);
    }

    if (string1 > string2)
    {
        cout << 1;
    }
    else if (string1 < string2)
    {
        cout << -1;
    }
    else
    {
        cout << 0;
    }

    return 0;
}