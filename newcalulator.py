print("hello to my calculator")
print("please put in first integer")
a = int(input())
print("please put second integer")
b = int(input())
print("please put in an operation. You can choose plus, minus, divide, times, square first, square second, cube first, cube second.")
o = input()
#below is the calulator
if o == "plus":
    n = a + b
elif o == "divide":
    n = a/b
elif o == "times":
    n = a*b
elif o == "minus":

    n = a - b
elif o == "square first":
    n = a * a
elif o == "square second":
    n = b * b
elif o == "cube first":
    n = a * a * a
elif o == "cube second":
    n = b * b * b
else:
    n = "error"
#below is the print for the awnser
if n == 0:
    print("the awnser is zero")
elif n > 0:
    print("the awnser is")
    print(n)
    print("which is positive")
elif n < 0:
    print("the awnser is")
    print(n)
    print("which is negative")
else:
    print("calculator broken")
#below is the even or odd finder
if n%2 == 0:
    print("and a even number")
else:
    print("an a odd number")
#below is the factoring
print("the factors of your awnser is:")

x = 1
while x <= n:
    if n % x == 0:
        print(x)
        x = x + 1
    else:
        x = x+1 
#this is the end of the code