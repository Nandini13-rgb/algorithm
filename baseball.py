def stack_push(stack,element):  # last in
    stack.append(element)
    return stack
def count_point(arr):
    stack = []
    operator = ['c', 'd', '+']
    if arr[0] not in operator:
        stack_push(stack,arr[0])
        for i in range(1,len(arr)):
            if arr[i] not in operator:
                stack_push(stack,arr[i])
            else:
                if arr[i] == '+':
                    if len(stack) >= 2:
                        result = stack[len(stack)-2]+stack[len(stack)-1]
                        stack_push(stack,result)
                    else:
                        print("invalid")
                        break
                elif arr[i] == 'd':
                    stack_push(stack,stack[len(stack)-1]*2)
                elif arr[i] == 'c':
                    if len(stack) >= 1:
                        stack.pop()
                    else:
                        print("invalid")
                        break
    else:
        print(" invalid")

    print(stack)
    score = 0
    for i in range(len(stack)):
        score += stack[i]
    print(score)

count_point([5, 10,20,'c','d','c','+','d',10])
