#include <stdio.h>
#include <stdbool.h>

void computerGame();
int main(void)
{
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; i++)
    {
        computerGame();
    }
    return 0;
}
void computerGame()
{
    int n;
    bool output = false;
    scanf("%d", &n);
    char col1[n];
    char col2[n];
    scanf("%s", col1);
    scanf("%s", col2);
    for (int i = 0; i < n; i++)
        output |= (col1[i] == '1' && col2[i] == '1');
    if (output)
        printf("NO\n");
    else
    {
        printf("YES\n");
    }
}