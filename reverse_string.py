def reverse(string):
    #method 1
    string = string[::-1]
    print(string)
    #metod 2
    reversed_string = ""
    for i in range(len(string)-1,-1,-1):
        reversed_string += string[i]
    print(reversed_string)
reverse(input("Enter string"))
