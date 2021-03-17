class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        if self.head == None:       #Empty List
            self.head = new_element
        else:
            current = self.head
            while current.next:    
                current = current.next
            current.next = new_element

    def get_position(self, position):
        current = self.head
        counter = 1
        if position < 1:    # Undefined position
            return None
        while current and counter < position:
            current = current.next
            counter += 1
        if counter == position:
            return current
        else:
            return None
    
    def insert(self, new_element, position):
        if position == 1:   # Insert at the start of the list
            new_element.next = self.head
            self.head = new_element
        elif position > 1:  
            counter = 1
            current = self.head
            previous = None
            while current and counter < position:
                previous = current
                current = current.next
                counter += 1
            if counter == position:    
                new_element.next = current
                previous.next = new_element
    
    def delete(self, value):
        if self.head == None:           # Empty list
            pass
        elif self.head.value == value:  # Delete first item
            self.head = self.head.next
        else:
            current = self.head
            prev = None
            while current.next and current.value != value:
                prev = current
                current = current.next
            prev.next = current.next
            current.next = None 