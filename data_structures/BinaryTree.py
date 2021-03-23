class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#BinarySearchTree
class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_value):
        self.insert_recursive(self.root, new_value)

    def insert_recursive(self, current, new_value):
        if current.value > new_value:
            if current.left:
                self.insert_recursive(current.left, new_value)
            else:
                current.left = Node(new_value)
        else:
            if current.right:
                self.insert_recursive(current.right, new_value)
            else:
                current.right = Node(new_value)

    def remove(self, value):
        pass

    def search(self, value):
        return self.search_recursive(self.root, value)
    
    def search_recursive(self, current, value):
        if current:
            if current.value == value:
                return True
            elif current.value > value:
                return self.preorder_search(current.left, value)
            else:
                return self.preorder_search(current.right, value)
        return False


    def print_tree(self):
        print(self.preorder_print(self.root, "")[:-4])

    def preorder_print(self, start, traversal):  
        if start:
            traversal += str(start.value) + ' ~> ' 
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        
        return traversal

# Test cases
if __name__ == "__main__":

    # Setup
    tree = BST(4)

    # Test insert
    tree.insert(2)
    tree.insert(1)
    tree.insert(3)
    tree.insert(5)

    # Test search
    print(tree.search(4))       # Should be True
    print(tree.search(6))       # Should be False

    # Test print_tree
    tree.print_tree()           # Should be 4-2-1-3-5