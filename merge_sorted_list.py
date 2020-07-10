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
llist1.head = insert(llist1.head, 9)
#llist1.head = insert(llist1.head, 10)
#llist1.head = insert(llist1.head, 1)
llist2 = LinkedList()
llist2.head = insert(llist2.head, 3)
llist2.head = insert(llist2.head, 4)
llist2.head = insert(llist2.head, 5)
#llist2.head = insert(llist2.head, 3)
#llist2.head = insert(llist2.head, 4)
#llist2.head = insert(llist2.head, 5)
def view(head):
    temp = head
    while temp:
        print(temp.data)
        temp = temp.next
llist3 = LinkedList()
llist3.head = llist1.head
pointer1 = llist1.head
pointer2 = llist2.head
def merge_list(pointer1,pointer2):
    if pointer1 == None:
        return view(pointer2)
    if pointer2 == None:
        return view(pointer1)
    result = LinkedList()
    temp = None
    if pointer1.data < pointer2.data:
        temp = pointer1
        pointer1 = pointer1.next
    else:
        temp = pointer2
        pointer2 = pointer2.next
    result.head = temp
    while pointer2 and pointer1:
        if pointer1 == None:
            break
        if pointer1.data < pointer2.data:
            temp.next = pointer1
            pointer1 = pointer1.next #9
            temp = temp.next
        else:
            temp.next = pointer2#2,3,4,5
            temp = temp.next
            pointer2 = pointer2.next# 4,5
    while pointer1:
        temp.next = pointer1
        temp = temp.next
        pointer1 = pointer1.next
    while pointer2:
        temp.next = pointer2
        temp = temp.next
        pointer2 = pointer2.next
    view(result.head)
merge_list(pointer1,pointer2)



