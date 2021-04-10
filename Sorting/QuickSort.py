import random

def QuickSort( A, low, high ):
    if low < high:
        pivot = Partition( A, low, high )
        QuickSort( A, low, pivot - 1 )
        QuickSort( A, pivot + 1, high )

def Partition( A, low, high ):
    pivot = low

    swap( A, low, high )
    for i in range( low, high ):
        if A[ i ] <= A[ high ]:
            swap( A, i, low )
            low += 1
    swap( A, low, high )
    return low

def swap( A, x, y ):
    '''Takes an array A and swaps elements A[x] and A[y]'''
    temp = A[ x ]
    A[ x ] = A[ y ]
    A[ y ] = temp

A = [ 5, 4, 3, 7, 2, 9 ]
QuickSort( A, 0, len( A ) - 1 )
print( A )
