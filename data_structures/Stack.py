from LinkedList import LinkedList, Element
 
class Stack(object):
    def __init__(self, top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        self.ll.insert_first(new_element)
    
    def pop(self):
        return self.ll.delete_first()

# Test cases
if __name__ == "__main__":
    
    # Setting up Elements
    e1 = Element(1)
    e2 = Element(2)
    e3 = Element(3)
    e4 = Element(4)
    e5 = Element(5)

    # Setup
    stack = Stack(e1)           #1

    # Test stack functionality
    stack.push(e2)              #2
    stack.push(e3)              #3
    print(stack.pop().value)    # Should be 3
    print(stack.pop().value)    # Should be 2
    stack.push(e4)              # 4
    print(stack.pop().value)    # Should be 4
    stack.push(e5)              # 5
    print(stack.pop().value)    # Should be 5
    print(stack.pop().value)    # Should be 1