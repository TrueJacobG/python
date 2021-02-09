#include <bits/stdc++.h>

using namespace std;

int n, result = 0;
string x;

int main()
{
    cin >> n;

    while (n)
    {
        cin >> x;
        if (x == "X++" || x == "++X")
        {
            result++;
        }
        else if (x == "X--" || x == "--X")
        {
            result--;
        }

        n--;
    }

    cout << result;

    return 0;
}