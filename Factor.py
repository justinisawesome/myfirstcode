#the following is the function to calulate all the factors of the users awnser.
def factorformula(n):
    x = 1
    while x <= n:
        if n % x == 0:
            print(x)
            x = x + 1
        else:
             x = x+1

factorformula(24)