x=5
if (type(x) is int):
    print("True")
else:
    print("False")

x= 5.0
if (type(x) is float):
    print("True")
else:
    print("False")


x=20
y=20

if (x is y):
    print("x and y store the same value.")
else: 
    print("x and y dont store the same value.")

y=-20

if (x is not y):
    print("x and y dont store the same value.")