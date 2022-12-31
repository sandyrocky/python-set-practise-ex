'''Write a Python program to create a shallow copy of sets.'''

'''supoose you have a set of value and you want copy that value  '''

s = {1,2,3,4,5}
a= s.copy() # copy set and store the in new varibale
print(a)   #output - {1, 2, 3, 4, 5}
# if change or remove and add new item in your set . this will not impact the  variable a  set.

# we are removing element from set a
s.remove(5)
print(s)

# output - {1, 2, 3, 4}


