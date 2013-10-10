#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.
#a < b < c
if __name__ == '__main__':
    s = 1000
    for a in range((s/3)-1): #a<b<c thus we loop only for <300 numbers
        for b in range((s/2)-1):#a<b<c thus we loop only for <500 numbers
            c = s-a-b #a+b+c=1000 thus c=1000-a-b
            if a**2 + b**2 == c**2:#Checking for potential triplet
                print "The triplet is: " + str(a) + "," + str(b) + "," + str(c)
                print "The product of this triplet is: " + str(a*b*c)