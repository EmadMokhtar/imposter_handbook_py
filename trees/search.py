def depth_first_search(root_node):
    stack = [root_node]
    while len(stack) > 0:
        current_node = stack.pop()
        print(current_node)
        if current_node.right is not None:
            stack.append(current_node.right)
        if current_node.left is not None:
            stack.append(current_node.left)


def breadth_first_search(root_node):
    queue = [root_node]
    while len(queue) > 0:
        current_node = queue.pop()
        print(current_node)
        if current_node.right is not None:
            queue.insert(0, current_node.right)
        if current_node.left is not None:
            queue.insert(0, current_node.left)
