#include <stdio.h>

int main(void)
{
    int k = 0;
    int n = 3;
    int x = 2;
    int coefficients[] = {0, 1, 2};
    int result = 0;

    while (k < n)
    {
        k++;
        result = result * x + coefficients[n - k];
    }

    printf("%d\n", result);
}