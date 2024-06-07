#step 1
# learn the flow of the recursive algorithm first 
# for fact we can write 
# n! = n * (n-1)!

#step 2 
#define base case 
#if n is 0 or 1 return 1

#step 3 
# unintensional condition handling
def fact(n):
    assert n>=0 and int(n)==n, "the number must be integer"
    if n in [0,1]:
        return 1
    else:
        return n*fact(n-1)


print(fact(3))
