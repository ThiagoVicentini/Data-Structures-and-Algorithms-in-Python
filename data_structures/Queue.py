from LinkedList import LinkedList

class Queue(object):
    def __init__(self, head=None):
        self.ll = LinkedList(head)

    def enqueue(self, new_element):
        self.ll.append(new_element)

    def peek(self):
        return self.ll.get_position(1)

    def dequeue(self):
        return self.ll.delete_first()

############################################################

class Queue2(object):
    def __init__(self, head=None):
        self.storage = [head]

    def enqueue(self, new_element):
        self.storage.append(new_element)

    def peek(self):
        return self.storage[0]

    def dequeue(self):
        return self.storage.pop(0)

# Test Cases
if __name__ == "__main__":

    # Setup
    queue = Queue2(1)       #1
    queue.enqueue(2)        #2
    queue.enqueue(3)        #3

    # Test peek
    print(queue.peek())     # Should be 1

    # Test dequeue
    print(queue.dequeue())  # Should be 1

    # Test enqueue
    queue.enqueue(4)        # 4
    print(queue.dequeue())  # Should be 2
    print(queue.dequeue())  # Should be 3
    print(queue.dequeue())  # Should be 4
    queue.enqueue(5)        # 5
    print(queue.peek())     # Should be 5