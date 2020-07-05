a = 0
b = 1
c = a+b
print(a)
print(b)
while c < 10:
    print(c)
    a = b
    b = c
    c = a+b
    