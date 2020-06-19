  
def stack_push(stack,element):  
    stack.append(element)
def check_parentesis(pattern):
    stack = []
    bracket1 = ['(', ')']
    bracket2 = ['{', '}']
    bracket3 = ['[', ']']
    start_bracket = ['(', '{', '[']
    for element in pattern:
        if element in start_bracket:
            stack_push(stack,element)
            print(stack)
        else:
            if len(stack) == 0:
                print("invalid")
            else:
                element1 = element
                for i in range(len(stack)-1,-1,-1):
                    if stack[i] in start_bracket:
                        matching_bracket = stack[i]
                        break
                if element1 in bracket1:
                    open_bracket = bracket1[0]
                elif element1 in bracket2:
                    open_bracket = bracket2[0]
                elif element1 in bracket3:
                    open_bracket = bracket3[0]
                if open_bracket == matching_bracket:
                    stack.pop()
    if len(stack) != 0:
        print("invalid")
    else:
        print("valid")
check_parentesis("[(])")
