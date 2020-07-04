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
llist1.head = insert(llist1.head, 5)
llist1.head = insert(llist1.head, 4)
llist1.head = insert(llist1.head, 3)
#llist1.head = insert(llist1.head, 9)
#llist1.head = insert(llist1.head, 1)
llist2 = LinkedList()
llist2.head = insert(llist2.head, 3)
llist2.head = insert(llist2.head, 6)
llist2.head = insert(llist2.head, 9)
def view(head):
    temp = head
    while temp:
        print(temp.data)
        temp = temp.next
def add_list():
    llist3 = LinkedList()
    llist3.head = Node(0)
    temp1 = llist1.head
    temp2 = llist2.head
    carry = 0
    while temp1 and temp2:
        sum = temp1.data + temp2.data
        if sum + carry < 10:
            llist3.head.next = Node(sum + carry)
            print(llist3.head.next.data)
        else:
            llist3.head.next = Node((sum + carry) % 10)
            print(llist3.head.next.data)
            carry = (sum + carry) // 10
        temp1 = temp1.next
        temp2 = temp2.next
    while temp1 is not None: # if some element left in list1
        if carry > 0:
            if temp1.data+carry < 10:
                llist3.head.next = Node(temp1.data+carry)
                carry = (temp1.data+carry)//10
                print(llist3.head.next.data)
            else:
                llist3.head.next = Node((temp1.data + carry)%10)
                carry = (temp1.data + carry) // 10
                print(llist3.head.next.data)

        else:
            llist3.head.next = Node(temp1.data)
            print(llist3.head.next.data)
        temp1 = temp1.next
    while temp2 is not None:# if some element left in list2
        if carry > 0:
            if temp1.data+carry < 10:
                llist3.head.next = Node(temp1.data+carry)
                carry = (temp1.data+carry)//10
                print(llist3.head.next.data)
            else:
                llist3.head.next = Node((temp1.data + carry)%10)
                carry = (temp1.data + carry) // 10
                print(llist3.head.next.data)
        else:
            llist3.head.next = Node(temp1.data)
            print(llist3.head.next.data)
        temp2 = temp2.next
    if carry > 0: # if no element left in either list but carry lefts
       llist3.head.next = Node(carry)
       print(llist3.head.next.data)
add_list()
