n=int(input("Enter the number of elements in the list"))
a=0
b=1
print(a)
print(b)
for i in range(n-1):
    c=a+b
    a=b
    b=c
    print(c)
