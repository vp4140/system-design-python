class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []


def remove_nodes(root, target):
    if not root:
        return None

    # If the current node is the target, return None to remove it
    if root.val == target:
        return None

    new_children = []
    for child in root.children:
        result = remove_nodes(child, target)
        if result:
            new_children.append(result)

    root.children = new_children
    return root


def print_tree(root, level=0):
    if root is None:
        return
    print("  " * level + str(root.val))
    for child in root.children:
        print_tree(child, level + 1)


# Example tree structure
root = TreeNode(1)
child1 = TreeNode(2)
child2 = TreeNode(3)
child3 = TreeNode(4)
child4 = TreeNode(5)

root.children = [child1, child2]
child1.children = [child3, child4]

print("Original Tree:")
print_tree(root)

# Remove all nodes under parent 2
root = remove_nodes(root, 2)

print("\nTree after removing nodes under parent 2:")
print_tree(root)
