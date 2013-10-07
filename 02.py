#Finding the sum of the even-valued Fibonacci terms (without exceeding the four million
def F(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return F(n-1)+F(n-2)


fibo=[]
for x in range(0,4000000):
    fibo.append(F(x))
    if F(x)>=4000000:
        break
print("Sum: "+str(sum([fibo[x] for x in range(len(fibo)) if fibo[x]%2==0])))