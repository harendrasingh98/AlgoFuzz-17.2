#Harendra Singh

t=int(input())
while(t>0):
    n=int(input())
    r=range(1,n+1)
    x=len(r)
    while(x!=1):
        k=[]
        for i in range(1,x,2):
            k.append(r[i])
        r=k
        x=len(r)
    t=t-1
    print(r[0])


