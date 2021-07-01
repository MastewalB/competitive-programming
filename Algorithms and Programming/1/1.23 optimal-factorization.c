#include <stdio.h>

int main(void)
{
    int k = 15;
    int t = 2;

    while (k != 1)
    {
        if (k % t == 0)
        {
            k /= t;
            printf("%d", t);
        }
        else
        {
            if (t * t > k)
            {
                t = k;
            }
            else
            {
                t += 1;
            }
        }
    }
}
