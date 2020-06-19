def stack_push(stack,element):
    stack.append(element)
    return stack
def stack_pop(stack):
    if if_empty:
        stack.pop()
    return stack
def if_empty(stack):
    if stack == []:
        return True
    else:
        return False
def display(stack):
    if if_empty(stack):
        stack = []
    else:
        stack = stack[::1]
    return stack
