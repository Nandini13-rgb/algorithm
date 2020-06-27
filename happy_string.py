def happy_string(input,elements):
    def findindex(element, input):
        for i in range(len(input)):
            if input[i] == element:
                return i
    max_index = findindex(max(input), input)
    #print(max_index)
    n = input[max_index]

    output = []
    # n = input[max_index]
    while n:
        output.append(elements[max_index])
        n -= 1
    #print(output)
    input.pop(max_index)
    elements.pop(max_index)
    index = 2
    while input[0] > 0:
        output.insert(index, elements[0])
        index += 3
        input[0] -= 1
    ndex = 3
    while input[1] > 0:
        output.insert(index,elements[1])
        index += 4
        input[1] -= 1
    j = len(output)-1
    if output[j] == output[j-1]:
        if output[j] == output[j-2]:
            output.pop(j)
            output.pop(j-1)
            output.pop(j-2)
    return output

input = [7, 7, 7]
elements = ['a', 'b', 'c']
print(happy_string(input,elements))
