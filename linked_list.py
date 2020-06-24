class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
if __name__ == '__main__':
    llist = LinkedList()
    print(llist)
    print(llist.head)
    
    node1 = Node(1)
    llist.head = node1
    print(llist)
    #print(node1.data)

    node2 = Node(2)
    node1.next = node2
    print(llist)
    #print(node2.data)

    node2.next = Node(3)
    print(llist)
    #print(node2.next.data)

    temp = node1
    while temp:
        print(temp.data)
        temp = temp.next
    # print in reverse order
    stack = []
    temp = node1
    while temp:
        stack.append(temp.data)
        temp = temp.next
    while stack:
        data = stack.pop()
        print(data)
