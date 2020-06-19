def stack_push(stack, element):  # last in
    stack.append(element)
    return stack
def polish_notation(eqn):
    stack = []
    for element in eqn:
        operator = ['+', '-', '*', '/']
        if element not in operator:
            stack_push(stack, element)
        else:
            a = int(stack.pop())
            b = int(stack.pop())
            if element == '+':
                stack_push(stack, a + b)
            elif element == '-':
                stack_push(stack, b - a)
            elif element == '*':
                stack_push(stack, a * b)
            elif element == '/':
                stack_push(stack, b / a)
    print(stack)
polish_notation("24+34+*")
