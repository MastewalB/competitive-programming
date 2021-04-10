
A = [ 85, 24, 63, 45, 17, 31, 96, 50, 67 ]

def quick_sort( A, low, high ):
    if low >= high: return
    pivot = A[ high ]

    left = low
    right = high - 1

    while left <= right:
        while left <= right and A[ left ] < pivot :
            left += 1
        while left <= right and A[ right ] > pivot:
            right -= 1

        if left <= right:
            A[ left ], A[ right ] = A[ right ], A[ left ]
            left, right = left + 1, right - 1

    A[ left ], A[ high ] = A[ high ], A[ left ]

    
    quick_sort( A, low, left - 1 )
    quick_sort( A, left + 1, high )
            

quick_sort( A, 0, len( A )- 1 )
print( A )


def quicksort( array ):
    if len( array ) < 2:
        return array
    else:
        pivot = array[ 0 ]

        less = [ i for i in array[ 1: ] if i <= pivot ]
        greater = [ i for i in array[ 1: ] if i > pivot ]

    return quicksort(less) + pivot + quicksort(greater)


















