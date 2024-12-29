class BST:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(str(root.data) + "->", end = " ")
        inorder(root.right)

def insert(root, data):
    if root is None:
        return BST(data)
    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    return root

def minvaluenode(root):
    current = root
    while current.left is not None:
        current = current.left
    return current

def deleteNode(root, data):
    if root is None:
        return root
    if data < root.data:
        root.left = deleteNode(root.left, data)
    elif data > root.data:
        root.right = deleteNode(root.right, data)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = minvaluenode(root.right)
        root.data = temp.data
        root.right = deleteNode(root.right, temp.data)
    return root

root = BST(50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)

print("In-order Traversal of BST:")
inorder(root)
print() 

value_to_delete = 30
print(f"Deleting {value_to_delete} from the BST...")
root = deleteNode(root, value_to_delete)
print("In-order Traversal after deletion:")
inorder(root)
print()