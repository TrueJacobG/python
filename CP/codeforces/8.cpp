#include <bits/stdc++.h>

using namespace std;

int tablica[6][6];
int r, c, result;

int main()
{
    for (int i = 1; i < 6; i++)
    {
        for (int j = 1; j < 6; j++)
        {
            cin >> tablica[i][j];
            if (tablica[i][j] == 1)
            {
                r = i;
                c = j;
            }
        }
    }

    /*cout << r << endl
         << c;*/

    result = abs(3 - r) + abs(3 - c);
    cout << result;

    /* abs -> wartość bezwzględna; */

    return 0;
}