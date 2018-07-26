def depth_first_search(root_node):
    stack = [root_node]
    while stack:
        current_node = stack.pop()
        print(current_node)
        if current_node.right:
            stack.append(current_node.right)
        if current_node.left:
            stack.append(current_node.left)


def breadth_first_search(root_node):
    queue = [root_node]
    while queue:
        current_node = queue.pop()
        print(current_node)
        if current_node.right:
            queue.insert(0, current_node.right)
        if current_node.left:
            queue.insert(0, current_node.left)
