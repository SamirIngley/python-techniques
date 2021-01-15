
# UNPACKING A SEQUENCE INTO MULTIPLE VAIRBALES
# this actually works with any objects that happens to be an iterable, not just lists or tuples. Also strings, files, generators

# Problem: you have an N-element tuple or sequence that you would like to unpack into a collection of N variables.
# Example:
# >>> p = (4,5)
# >>> x, y = p
# >>> x
# 4
# >>> y
# 5

# >>> data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
# >>> name, sahres, price, date = data
# >>> name
#'ACME'
# >>> date
# (2012, 12, 21)

# if there is a mismatch in the number of elements, you'll get an error ( such as: need more than two values to unpack)
# use _ as a throwaway variable name for a value you want to discard


# UNPACKING ELEMENTS FROM ITERABLES OF ARBITRARY LENGTH

# Problem: You need to unpack N elements from an iterable, but the iterable may be longer than N elements, causing a "too many values to unpack"
# exception. 

# Solution: Python "star expressions" can be used to address this problem.
# specifically made to address iterables of arbitrary length
# say you want to average 24 grades for a class and drop the first and last grades
def drop_first_last(grades):
    first, *middle, last = grades
    return average(middle)

# >>> record = ('Dave', 'dave@exasmple.com', '773-555-1212', '842-234-7890')
# >>> name, email, *phone_numbers = record


