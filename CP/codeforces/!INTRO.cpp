#include <bits/stdc++.h>

using namespace std;
ios::sync_with_stdio(0);
cin.tie(0);

int n, k, score = 0;
int s[100];

/*getline(cin, u)    zapisuje całą linie do zmiennej u*/

int main()
{
    cin >> n >> k;

    for (int i = 1; i <= n; i++)
    {
        cin >> s[i];
    }

    for (int i = 1; i <= n; i++)
    {
        if (s[i] >= s[k] && s[i] > 0)
        {
            score++;
        }
    }

    printf("%d", score);
}