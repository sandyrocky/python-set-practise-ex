''''Write a Python program to check if a given value is present in a set or not.'''

def check(a):
    s = {1,2,3,3,5,6,8}# set  s variable we define here.
    if a in s : # s set element is present in a
        print("your value  exists .")
    else:# s set element is not present in a
        print("your value does not exist .")
# we call here .
check(9)
check(8)

# output -
# your value does not exist .
# your value  exists .