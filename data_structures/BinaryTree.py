class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, value):
        return self.preorder_search(self.root, value)
    
    def preorder_search(self, start, value):
        if start:
            if start.value == value:
                return True
            else:
                return self.preorder_search(start.left, value) or self.preorder_search(start.right, value)
        return False


    def print_tree(self):
        print(self.preorder_print(self.root, "")[:-4])

    def preorder_print(self, start, traversal):  
        if start:
            traversal += str(start.value) + ' ~> ' 
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        
        return traversal