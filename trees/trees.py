class Node:
    def __init__(self, value, right=None, left=None):
        self.value = value
        self.right = right
        self.left = left
    
    def isLeaf(self):
        return self.left is None and self.right is None
    
    def __str__(self):
        return str(self.value)
