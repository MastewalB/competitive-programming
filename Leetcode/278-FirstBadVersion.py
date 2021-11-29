import math


def firstBadVersion(n):
    begin = 0
    end = n
    while (begin < end):
        pivot = begin + (end - begin) // 2
        if (isBadVersion(pivot)):
            end = pivot
        else:
            begin = pivot + 1

    return begin
