#Problem 14 of Project Euler.
#The following iterative sequence is defined for the set of positive integers:
#n -> n/2 (n is even)
#n -> 3n + 1 (n is odd)
#Using the rule above and starting with 13, we generate the following sequence:
#13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
#It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
#Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#Which starting number, under one million, produces the longest chain?
#NOTE: Once the chain starts the terms are allowed to go above one million.
#---------Solution------#
#Method used inspired by http://www.mathblog.dk/project-euler-14/. Used cache method, we store each value to a list.
#If the starting number drops below it's starting value then we add the lower number value because
#it is already stored in the list
#That way we avoid lots of iterations and thus a lot of computation time
def collatz(number): #We compute the collatz sequence for a number till the point were the starting
    #value drops below it's value ex. 13 -> 40 -> 20 -> 10.
    temp = number
    counter = 0
    while number != 1 and number >= temp:
        counter += 1
        if number % 2 == 0:
            number = number/2
        else:
            number = number*3+1
    return counter, number

if __name__ == '__main__':
    sequence_length = 0
    starting_number = 0
    cache = [0]*1000000 #Creating a list of 1000000 items with zero value
    for i in range(2, 1000000):
        counter_x,number_y = collatz(i) #Use of collatz function and set it's return values to counter and value
        cache[i] = int(counter_x) + int(cache[number_y]) #Adding the number of iterations so far plus the number of the
        # iterations of the already stored number.
        if cache[i] > sequence_length: #Setting a max number
           sequence_length = cache[i]
           starting_number = i
    print "The number with the longest chain is : "+ str(starting_number) + " with a sequence of " + str(sequence_length) + " numbers."