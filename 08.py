#Find the greatest product of five consecutive digits in a random 1000-digit number.
#importing the function randint from the library random
from random import randint

#Create a random generator
def random_digit_gen(n):
    lowest_value = 10**(n-1) #Start from the lowest value ex. 2 digit will produce the number 10
    highest_value = (10**n)-1 #Set an upper bound for the value, ex 2 digit will product the number 99
    return randint(lowest_value,highest_value)



if __name__ == '__main__':
    #Generate the number
    solution = random_digit_gen(1000)
    string_solution = str(solution) #Convert it to string
    max=0
    for sol in range(len(string_solution)): #Loop through the string
        multiplication=1
        for sol in string_solution[int(sol):int(sol)+5]: # Set a max and multiply each number with each 4 next consecutive numbers
            multiplication*=int(sol)
            if multiplication>=max:
                max=multiplication
    print 'The solution is : ' + str(max)


