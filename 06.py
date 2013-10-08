#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
#First is the sum of the squares of the first 100 natural numbers
first = sum([x*x for x in range(101)])
#Second is the square of the sum of the first 100 natural numbers
second = sum(range(101))**2
print second-first