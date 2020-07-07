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
    if pointer1.data < pointer2.data:    
        while pointer2:
            if pointer1 == None:
                break
            if pointer1.data < pointer2.data:
                print(pointer1.data)
                prev = pointer1
                pointer1 = pointer1.next
            else:
                temp1 = pointer2.next
                prev.next = pointer2
                print(prev.next.data)
                prev.next.next = pointer1
                #print(prev.next.next.data)
                pointer2 = temp1
    else:
        while pointer1:
            if pointer2 == None:
                break
            if pointer2.data < pointer1.data:
                print(pointer2.data)
                prev = pointer2
                pointer2 = pointer2.next
            else:
                temp1 = pointer1.next
                prev.next = pointer1
                print(prev.next.data)
                prev.next.next = pointer2
                pointer1 = temp1         
    while pointer1:
        print(pointer1.data)
        pointer1 = pointer1.next
