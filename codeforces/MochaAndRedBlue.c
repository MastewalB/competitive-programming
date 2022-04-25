#include <stdio.h>

int main()
{
    char s[105];
    int t, n, painted;

    scanf("%d", &t);
    while (t--)
    {
        painted = 0;
        scanf("%d", &n);
        scanf("%s", &s);
        for (int i = 0; i < n; i++)
        {
            painted += (s[i] != '?');
        }
        if (!painted)
        {
            s[0] = 'B';
        }
        for (int i = 1; i < n; i++)
        {
            if (s[i] == '?' && s[i - 1] != '?')
            {
                s[i] = s[i - 1] ^ ('B' ^ 'R');
            }
        }
        for (int i = n - 2; i >= 0; i--)
        {
            if (s[i] == '?' && s[i + 1] != '?')
            {
                s[i] = s[i + 1] ^ ('B' ^ 'R');
            }
        }

        printf("%s\n", s);
    }
    return 0;
}