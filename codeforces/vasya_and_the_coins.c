#include <stdio.h>

int min_coins(int a, int b);
int main(void)
{
    int test_cases;
    scanf("%d", &test_cases);
    for (int i = 0; i < 2 * test_cases; i += 2)
    {
        int a, b;
        scanf("%d", &a);
        scanf("%d", &b);
        printf("%d\n", min_coins(a, b));
    }
}

int min_coins(int a, int b)
{
    if (a > 0 && b == 0)
    {
        return a + 1;
    }
    if (a == 0 && b > 0)
    {
        return 1;
    }
    return (2 * b) + a + 1;
}