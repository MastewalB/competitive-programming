class Queue:

    def __init__( self ):
        self.queue = []

    def enqueue( self, data ):
        self.queue.append( data )

    def dequeue( self ):
        answer = self.queue[ 0 ]

        self.queue.pop( 0 )
        return answer

    def peek( self ):

        if self.isEmpty():
            return "Empty"
        else:
            print( self.queue[ 0 ] )

    def size( self ):
        return len( self.queue )

    def isEmpty( self ):
        return self.size() == 0

    def clear( self ):

        self.queue = []


class Stack:

    def __init__( self ):

        self.queueOne = Queue()
        self.queueTwo = Queue()

    def push( self, element ):

        self.queueTwo.enqueue( element )
        
        while not self.queueOne.isEmpty():
            self.queueTwo.enqueue( self.queueOne.dequeue() )

        self.queueOne = self.queueTwo
        self.queueTwo.clear()

    def pop( self ):
        
        return self.queueOne.dequeue()


a = Stack()
a.push( 5 )
a.pop()


