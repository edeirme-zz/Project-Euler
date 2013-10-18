#Project Euler problem 16
#2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#What is the sum of the digits of the number 2^1000?
#Simple implementation we transform the result of the 2**1000 into a string and seperate each digit by inserting it into
#a dictionary. At the same time we keep record with a counter "i"
def problem16(x):
    array16 = {}
    i = 0
    for digit in str(x): #Splitting each digit and trasnform them into int
        array16[i] = int(digit)
        i += 1
    return array16

if __name__ == '__main__':
    array = problem16(2**1000)
    print sum(array.values()) #Summing all the values of the dictionary