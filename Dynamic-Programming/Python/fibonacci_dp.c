#include <stdio.h>
#define MAXN 45


int main(void){

}

long fib_dp(int n){
    int i;
    long f[MAXN+1];

    f[0] = 0;
    f[1] = 1;
    for(i = 2; i <= n; i++){
        f[i] = f[i-1] + f[i-2];
    }

    return f[n];
}