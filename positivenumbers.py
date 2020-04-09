n=int(input("Enter the number of elements in the list"))
lista=[]
print("Enter ",n," elements")
for i in range(n):
    a=int(input())
    if a>=0:
        lista.append(a)
print("The positive numbers are ")
for num in lista:
    print(num)
