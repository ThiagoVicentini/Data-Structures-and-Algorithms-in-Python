import LinkedList
 
class Stack(object):
    def __init__(self, top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        self.ll.insert_first(new_element)
    
    def pop(self):
        return self.ll.delete_first()