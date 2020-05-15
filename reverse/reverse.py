class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
     
        #RECURSIVE method
        #check if it's empty
        if self.head is None:
            return None
        #check if it's the tail
        if node.next_node is None:
           self.head = node # make it the head
        else: 
           nex = node.next_node #store the next node in nex
           #pass it as the current
           #pass prev as the node (last current)
           self.reverse_list(nex, node) 
        #next is prev
        node.next_node = prev
    
        
        """ #Iterative method
        node = self.head  #mark node given as the head
  
        while node: 
           nex = node.next_node
           node.next_node = prev
           prev = node
           node = nex     

        self.head = prev  """
       