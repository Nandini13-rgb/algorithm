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
    temp1 = llist1.head
    temp2 = llist2.head
    llist3 = LinkedList()
    sum = temp1.data + temp2.data
    if sum < 10:
        node1 = Node(sum)
        carry = 0
    else:
        node1 = Node(sum%10)
        carry = sum//10
    llist3.head = node1
    result = node1
    temp1 = temp1.next
    temp2 = temp2.next
    while temp1 and temp2:
        sum = temp1.data + temp2.data
        if sum + carry < 10:
            # node1 = Node(sum)
            result.next = Node(sum + carry)
            result = result.next
        else:
            result.next = Node((sum + carry) % 10)
            result = result.next
            carry = (sum + carry) // 10
        temp1 = temp1.next
        temp2 = temp2.next
    while temp1 is not None:
        if carry > 0:
            if temp1.data+carry < 10:
                result.next = Node(temp1.data+carry)
                carry = (temp1.data+carry)//10
                result = result.next
            else:
                result.next = Node((temp1.data + carry)%10)
                carry = (temp1.data + carry) // 10
                result = result.next
        else:
            result.next = Node(temp1.data)
            result = result.next
        temp1 = temp1.next
    while temp2 is not None:
        if carry > 0:
            if temp1.data+carry < 10:
                result.next = Node(temp1.data+carry)
                carry = (temp1.data+carry)//10
                result = result.next
            else:
                result.next = Node((temp1.data + carry)%10)
                carry = (temp1.data + carry) // 10
                result = result.next
        else:
            result.next = Node(temp1.data)
            result = result.next
        temp2 = temp2.next
    if carry > 0:
       result.next = Node(carry)
    view(llist3.head)
add_list()
