#Finding the sum of all the multiples of 3 or 5 below 1000
loulou=0
for makis in range(0,1000):
    if makis%3==0 or makis%5 == 0:
        loulou=loulou+makis
print loulou
