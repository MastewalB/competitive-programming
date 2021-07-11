#include <stdio.h>
#define MAXN 45

int main(void)
{
}

long binomial_coefficient(n, m)
{
    long bc[MAXN][MAXN];
    int i, j;
    for (i = 0; i <= n; i++)
        bc[i][0] = 1;
    for (j = 0; j <= n; j++)
        bc[j][j] = 1;

    for (i = 0; i <= n; i++)
    {
        for (j = 1; j < i; j++)
        {
            bc[i][j] = bc[i - 1][j - 1] + bc[i - 1][j];
        }
    }
    return bc[n][m];
}