def math(a,c,b):
    if c == "+":
        print(a + b)
    elif c == "-":
        print(a - b)
    elif c == "*":
        print(a * b)
    elif c == "/":
        print(a / b)
a = int(input())
c = input()
b = int(input())
math(a,c,b)