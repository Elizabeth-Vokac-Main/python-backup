# Liz VM CIS 150 Project 2 math
# this code requests two integer values and then performs math operations considering error
var1 = int(input("enter any integer: "))
var2 = int(input("enter another ingeter: "))

if var1 != int:
    print("please enter an integer")
    var1 = int(input("enter any integer: "))
if var2 != int:
    print("please enter an integer")
    var2 = int(input("enter any integer: "))

if var2 == 0:
    print("please enter a nonzero integer")
    var2 = int(input("enter a nonzero integer"))


print(var1)
print(var2)
# next find the sum of the variables
result = var1 + var2
print(var1, "+", var2, "=", result)

#find the difference
result = var1 - var2
print(var1, "-", var2, "=", result)

result = var1 % var2
result = var1 / var2
print(var1, "%", var2, "=", result)
print(var1, "/", var2, "=", result)
