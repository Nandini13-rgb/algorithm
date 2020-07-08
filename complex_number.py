class complex_number:
    def represent(real,imaginary):
        print('%d + %di' %(real,imaginary))
def operation(operator,number1,number2):
    for i in range(len(number1)):
        if number1[i] == "+": # to find the real term of number1
            index1 = i
    for i in range(len(number2)): # to find ral term of number2
        if number2[i] == "+":
            index2 = i
    if operator == "sum":
        real = int(number1[0:index1-1]) + int(number2[0:index2-1]) # real1 + real 2
        imaginary = int(number1[index1+1:len(number1)-1]) + int(number2[index2+1:len(number2)-1])
        complex_number.represent(real,imaginary)
    elif operator == "sub":
        real = int(number1[0:index1-1]) - int(number2[0:index2-1])
        imaginary = int(number1[index1+1:len(number1)-1]) + int(number2[index2+1:len(number2)-1])
        complex_number.represent(real,imaginary)
    elif operator == "multiply":
        real = (int(number1[0:index1-1]) * int(number2[0:index2-1])) - (int(number1[index1+1:len(number1)-1]) * int(number2[index2+1:len(number2)-1]))
        imaginary = int(number1[0:index1-1]) * int(number2[index2+1:len(number2)-1]) + (int(number1[index1+1:len(number1)-1]) * int(number2[0:index2-1]))
        complex_number.represent(real, imaginary)
operation("multiply","32 + 2i","3 + 2i")
