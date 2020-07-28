class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key


def insert(root, Node):
    if root is None:
        root = Node
    if root.val < Node.val:  # 50<30
        if root.right == None:
            root.right = Node
        else:
            insert(root.right, Node)
    else:
        if root.left == None:
            root.left = Node
        else:
            insert(root.left, Node)


r = Node(5)
insert(r, Node(3))
insert(r, Node(4))
insert(r, Node(6))
insert(r, Node(7))
insert(r, Node(1))
insert(r, Node(8))


def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

def search(root,value):#6
    if root == None:
        print("Not present")
    elif root.val == value:
        return root
    elif root.val < value:
        return search(root.right,value)
    else:
        return search(root.left,value)
print(search(r,9))
