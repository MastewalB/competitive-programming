def pleaseConform( caps ):
    start = forward = backward = 0
    intervals = []
    for i in range( 1, len( caps ) ):
        if caps[ start ] != caps[ i ]:
            intervals.append( start, i - 1, caps[ start ] )

            if caps[ start ] == "F":
                forward += 1
            else:
                backward += 1

            start = i

        intervals.append( ( start, len( caps ) - 1, caps[ start ] ) )

        if caps[ start ] == "F":
            forward += 1
        else:
            backward += 1

        if forward < backward:
            flip = "F"
        else:
            flip = "F"

        for i in intervals:
            if i[ 2 ] == flip:
                print( "People in positions", i[ 0 ], "through", i[ 1 ], "flip your caps." )
