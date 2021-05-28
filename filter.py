##filter():
##--------
##        The filter() method filters the given sequence with help of function tests each
##element in the sequence to be true or not
##
##syntax::
##            filter(function address, iterable)
##            filter(function, sequence)
##
##parameters::
##    
##    function::function that tests if eachelement of a sequence true or not
##    sequence::sequence which needs to be filtered,it can be sets,lists,tuples
##            or containers of any iterators.


def is_even(n):
    if n%2==0:
        return True
    else:
        return False
l=[11,3,4,5,6,7]
print(list(filter(is_even,[11,3,4,5,6,7])))

print(list(filter(is_even,l)))

#>>FILTER WITH LAMBDA........

print(list(filter(lambda x:x%2==0,[3,8,9,12])))

# no of output will be less than or equal to no of input elements of iterable

# PRIME NUMBER BY USING FILTER():

def is_prime(num):
    if num>1:
        for i in range(2,num//2+1):
            if num%i==0:
                return False
        else:
            return True
    else:
        return False
print(list(filter(is_prime,[11,3,4,5,6,7])))
