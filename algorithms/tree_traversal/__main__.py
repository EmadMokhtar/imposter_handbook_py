from trees import Node
from search import (depth_first_search, breadth_first_search,
                    recursion_tree_traverse)

# Setup Tree
root = Node(0)
root.left = Node(1)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)

print('Depth First Search')
depth_first_search(root)
print('=' * 25)
print('Breadth First Search')
breadth_first_search(root)
print('Recursion Tree Traversal')
recursion_tree_traverse(root)
