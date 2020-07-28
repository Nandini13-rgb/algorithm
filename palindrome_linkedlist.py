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


def view(llist):
    temp = llist.head
    while temp:
        print(temp.data)
        temp = temp.next


llist1 = LinkedList()
llist1.head = insert(llist1.head, 1)
llist1.head = insert(llist1.head, 2)
llist1.head = insert(llist1.head, 3)
llist1.head = insert(llist1.head, 4)
llist1.head = insert(llist1.head, 2)
llist1.head = insert(llist1.head, 1)

# 123321, 123321
def check_palindrome(llist):
    slow = llist1.head
    fast = llist1.head
    while fast.next:
        if fast.next.next == None:
            break
        slow = slow.next
        fast = fast.next.next
    temp = slow.next
    prev = None
    while temp:
        next = temp.next
        temp.next = prev
        prev = temp
        temp = next
    reversed = LinkedList()
    reversed.head = prev
    temp1 = reversed.head
    temp2 = llist1.head
    while temp1:
        if temp2.data != temp1.data:
            return "not palindrome"
        temp1 = temp1.next
        temp2 = temp2.next
    return ("palindrome")

#view(reversed)
print(check_palindrome(llist1))
