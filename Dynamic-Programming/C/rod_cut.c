#include <stdio.h>
#include <limits.h>

int bottomUPCutRod(int *prices, int lenPrices, int n);
int main(void)
{
    int prices[] = {0, 1, 5, 8, 9, 10};
    printf("%d\n", bottomUPCutRod(prices, 6, 5));
    return 0;
}

int bottomUPCutRod(int *prices, int lenPrices, int n)
{
    int priceDp[11];
    int cuts[11];
    priceDp[0] = 0;

    for (int i = 0; i < lenPrices; i++)
    {
        int res = INT_MIN;
        for (int j = 0; j <= i; j++)
        {
            if (res < (prices[j] + prices[i - j]))
            {
                res = prices[j] + prices[i - j];
                cuts[i] = j;
            }
            priceDp[i] = res;
        }
    }

    return priceDp[lenPrices - 1];
}