class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


def insert(head, value):
    node = Node(value)
    if head is None:
        head = node
        return head
    temp = head
    while temp.next:
        temp = temp.next
    temp.next = node
    return head


llist1 = LinkedList()
llist1.head = insert(llist1.head, 1)
llist1.head = insert(llist1.head, 2)
llist1.head = insert(llist1.head, 3)
llist1.head = insert(llist1.head, 4)
#llist1.head = insert(llist1.head, 5)
#llist1.head = insert(llist1.head, 6)



def view(head):
    temp = head
    temp2 = temp
    while temp:
        print(temp.data)
        temp = temp.next
def reverse(llist):
    temp = llist
    if temp == None:
        print("No element")
    prev = None
    while temp:
        next = temp.next
        temp.next = prev
        prev = temp
        temp = next
    answer = LinkedList()
    answer.head = prev
    view(answer.head)





reverse(llist1.head)
