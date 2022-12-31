'''Write a Python program to check if two given sets have no elements in common.'''

s = {1,2,3,4,5}
s1 = {"baldeep","kuldeep","sandeep"}
if s not in s1:
    print("yes, your given set have  no element common .")
else:
    print("no , your given set hve  common element .")

# output - yes, your given set have  no element common .

# you can also use set method and set method is disjoint , it is give true or false result in bollean value .
# if both set have no common element it is give you true value .
#if both set have common element it is give false value .

print( "it will give you ",s.isdisjoint(s1),"result .")
# output - it will give you True result .
