#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
#answer influenced from stack overflow
#check list excludes numbers whose multiplier is lower or equal to 20
check_list = [11, 13, 14, 16, 17, 18, 19, 20]

def find_solution(step):
    for num in xrange(step, 999999999, step):
        if all(num % n == 0 for n in check_list):
            return num
    return None
#Step is 2520 because our solution must be divided evenly by 2520. 2520 is divided evenly by the numbers from 1 to 10.
if __name__ == '__main__':
    solution = find_solution(2520)
    if solution is None:
        print "No answer found"
    else:
        print "found an answer:", solution

