array = [ 5, 2, 4, 6, 1, 3 ]

for i in range( 1, len( array ) ):

    temp = array[ i ]
    k = i

    while ( k > 0 ) and ( temp < array[ k - 1 ] ) :
        array[ k ] = array[ k - 1 ]
        k -= 1
    array[ k ] = temp

print( array )


for i in range( 1, len( array ) ):

    temp = array[ i ]
    k = i

    while ( k > 0 ) and ( temp > array[ k - 1 ] ):
        array[ k ] = array[ k - 1 ]
        k -= 1
    array[ k ] = temp

print(array)
