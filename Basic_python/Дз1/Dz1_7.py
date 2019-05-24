x = int(input("Введите натуральное число(В десятиричной системе): "))
n = ""
vrem=x

while x > 0:
    y = str(x % 8)
    n=y + n
    x = int(x / 8)
print (n)    
x=vrem
n=""

while x > 0:
    y = str(x % 2)
    n = y + n
    x = int(x / 2)
print(n)    
x=vrem
n=""

while x > 0:
    y = str(x % 16)
    n = y + n
    x = int(x / 16)
    
print (n)


