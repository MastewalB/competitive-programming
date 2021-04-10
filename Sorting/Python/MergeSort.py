def merge( listOne, listTwo, lst ):

    i = j = 0
    while i + j < len( lst ):
        if j == len( listTwo ) or ( i < len( listOne ) and listOne[ i ] < listTwo[ j ] ):
            lst[ i + j ] = listOne[ i ]
            i += 1
        else:
            lst[ i + j ] = listTwo[ j ]
            j += 1
    return lst

def mergeSort( lst ):

    n = len( lst )
    if n < 2:
        return
    mid = n // 2
    listOne = lst[ 0 : mid ]
    listTwo = lst[ mid : n ]

    mergeSort( listOne )
    mergeSort( listTwo )

    merge( listOne, listTwo, lst )
    return lst





def merger( a, b ):

    c = []
    i = 0
    j = 0
    
    while i < len( a ) and j < len( b ):
        if a[ i ] > b[ j ]:
            c.append( b[ j ] )
            j += 1
        else:
            c.append( a[ i ] )
            i += 1

    if i < len( a ):
        c.extend( a[ i: ] )

    if j < len( b ):
        c.extend( b[ j: ] )
    return c

##a = [ 1, 2, 3 ]
##b = [ 2, 4 ]
##print( merger( a, b ) )


#merging two sorted queue instances

def merge( queueOne, queueTwo, final ):

    while not queueOne.is_empty() and not queueTwo.is_empty():
        if queueOne.first() < queueTwo.first():
            final.enqueue( queueOne.dequeue() )
        else:
            final.enqueue( queueTwo.dequeue() )
    while not queueOne.isempty():
        final.enqueue( queueTwo.dequeue() )
    
    while not queueTwo.isempty():
        final.enqueue( queueOne.dequeue() )


def merge_sort( queue ):

    n = len( queue )
    if n < 2:
        return
    queueOne = LinkedQueue()
    queueTwo = LinkedQueue()

    while len( queueOne ) < n // 2:
        queueOne.enqueue( queue.dequeue() )
    while not queue.is_empty():
        queueTwo.enqueue( queue.dequeue() )

    merge_sort( queueOne )
    merge_sort( queueTwo )

    merge( queueOne, queueTwo, queue )
    


























