#Find the largest palindrome number made from product of two 3-digit numbers
maxi=0
for x in range(100,999):
    for y in range(100,999):
        s=str(x*y)
        #  accept only number with even number of digits
        if len(str(x*y)) % 2 == 0:
            #cut the string in half
             s1=s[:(len(str(x*y))/2)]
             s2=s[(len(str(x*y))/2):]
             #reverse the string
             s3=s2[::-1]
             #check for equality#
             if s1==s3:
                 #set max palindrome number
                 if (int(s1+s2))>=maxi:
                     maxi = int(s1 + s2)
#print the max
print "Maximum palindrome number: "+str(maxi)