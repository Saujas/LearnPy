def prime(n):
    c = 0
    for i in range(1,n+1):
        if(n%i==0):
            c+=1
    if(c==2):
        return 1
    else:
        return 0
var = int(input("Enter end point of range: "))
for j in range(1,var+1):
    if(prime(j)):
        print(j,"is prime")
    else:
        print(j, "is not prime")
