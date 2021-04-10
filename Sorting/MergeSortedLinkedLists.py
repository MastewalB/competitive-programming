class Node:
    def __init__( self, data ):
        self.data = data
        self.next = None

class LinkedList:
    def __init__( self ):
        self.head = None

    def print_list( self ):
        cur_node = self.head
        while cur_node:
            print( cur_node.data )
            cur_node = cur_node.next
        
    def append( self, data  ):
        new_node = Node( data )

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next= new_node
    
    #merge two sorted linked lists
    def merge_sorted( self, linked_list ):

        p = self.head
        q = linked_list.head
        s = None

        if not p:
            return q
        if not q:
            return p

        if p and q:
            if p.data <= q.data:
                s = p
                p = p.next
            else:
                s = q
                q = s.next

            new_head = s
        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next

        if not p:
            s.next = q
        if not q:
            s.next = p
        #return new_head

ll = LinkedList()
ll.append( 2 )
ll.append( 4 )
ll.append( 6 )
ll.append( 8 )
ll.append( 10 )
ll.append( 12 )
ll.append( 14 )

l = LinkedList()
l.append( 1 )
l.append( 3 )
l.append( 5 )
l.append( 7 )
l.append( 9 )
l.append( 11 )
l.append( 13 )
l.append( 15 )
         
ll.merge_sorted( l )
ll.print_list()
