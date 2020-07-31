class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def insert(root, Node):
    if root == None:
        root = Node
    if root.val < Node.val:
        if root.right is None:
            root.right = Node
        else:
            insert(root.right, Node)

    if root.val > Node.val:
        if root.left is None:
            root.left = Node
        else:
            insert(root.left, Node)


r = Node(3)
insert(r, Node(1))
insert(r, Node(4))
insert(r, Node(2))


# insert(r, Node(99))
# insert(r, Node(97))


def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)


def kth_larger_node(root, k, count):
    if root is None or count == k:
        return
    # count += 1
    kth_larger_node(root.right, k, count)
    count[0] += 1
    if count[0] == k:
        print(root.val)
    kth_larger_node(root.left, k, count)


# kth_larger_node(r,6,[0])

# method 2
def kth_greatest_node(root, k):
    arr = []

    def inorder(root, arr):
        if root:
            inorder(root.left, arr)
            arr.append(root.val)
            inorder(root.right, arr)

    inorder(r, arr)
    print(arr[len(arr) - k])


kth_greatest_node(r, 2)
