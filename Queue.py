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