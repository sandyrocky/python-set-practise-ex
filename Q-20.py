'''Write a Python program to remove the intersection of a 2nd set from the 1st set.'''

set_1 = {"aloo","mirch","gobi"}
set_2 = {"gajar","ganna","aloo"}
a =set_1.intersection(set_2)
print(a)# output - {'aloo'}

# then we remove the intersection of set_2 set from the set_1
set_2.difference_update(set_1)
print(set_2)
# output - {'gajar', 'ganna'}
