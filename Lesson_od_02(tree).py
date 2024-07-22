class Node():
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.value < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)

    return root

root = Node(10)

root = insert(root, 8)
root = insert(root, 12)
root = insert(root, 6)
root = insert(root, 14)
