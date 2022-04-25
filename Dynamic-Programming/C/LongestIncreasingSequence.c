#include <stdio.h>
#include <limits.h>
#define MAX(a, b) (((a) > (b)) ? (a) : (b))

int lengthOfLIS(int *nums, int numsSize)
{
    int d[2501] = {[0] = INT_MIN, [1 ... 2500] = INT_MAX};

    for (int i = 0; i < numsSize; i++)
    {
        int low = 0, high = numsSize;
        while (low < high)
        {
            int mid = (low + high) >> 1;
            if (d[mid] < nums[i])
                low = mid + 1;
            else
                high = mid;
        }
        d[low] = nums[i];
    }
    int output = 0;
    for (int k = 0; k <= numsSize; k++)
    {
        if (d[k] < INT_MAX)
            output = k;
    }
    return output;
}