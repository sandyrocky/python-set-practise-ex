'''Write a Python program to remove an item from a set if it is present in the set.'''

s = {1,2,3,4,5,"sandeep"}
if "sandeep" in s:
    s.remove("sandeep")
    print("now print our new set with new value :",s)
else:
    print("this item is not presented in set ",s)