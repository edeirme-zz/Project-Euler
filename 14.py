def collatz(n,rep=0):
    if n==1:
        rep+=1
        print n
        return rep
    elif n%2==0:
        rep+=1
        print n
        return collatz(n/2,rep)
    elif n%2!=0:
        rep+=1
        print n
        return collatz((3*n)+1,rep)

def collatz2(n):
    i=n
    k=0
    while n!=1 and n>=i:
        k+=1
        if n%2==0:
            n=n/2
        else:
            n=n*3+1
    return k,n


if __name__=='__main__':
    num_chain=1
    seqlength=0
    startingnumber=0
    cache=[0]*1000000
    #number=1000000
    for i in range(2,1000000):
        x,y=collatz2(i)
        cache[i]=int(x)+int(cache[y])
        if cache[i]>seqlength:
           seqlength=cache[i]
           startingnumber=i
    print seqlength,startingnumber
