#include <bits/stdc++.h>

using namespace std;

int n, k, score = 0;
int s[100];

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