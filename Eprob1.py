#name variable for what to add
def multiples_of_3_or5():
    for number in xrange(1000) :
        if not number % 3 or not number % 5:
            yield number
#use sum command to execute the problem
print sum(multiples_of_3_or5())
