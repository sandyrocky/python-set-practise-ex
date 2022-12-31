'''Write a Python program to check if a given set is superset of itself and superset of another
given set. '''

# we are creating here two set . and we are using issuperset  method of set.
# issuperset said that if any one or two or more element of a set is present in another set it give you true result
#  aur  hai bhai sab kuch depend karta hai yaha ki aap kisko orginial set bana rahe compare karne
#  k liye dushre set se  usi hisaab se result change ho jata hai.
s = {1,2,3,4,"a","b","c"}
s1 = {1,2,"a","b"}
a = s.issuperset(s1)
print(a)
# here s set is superset of s1 set if whole  element of set s1 is s.
# and which is set s have whole element of set s1.
# output - True
b = s1.issuperset(s)
print(b)
# here s1 set is superset of s set if whole  element of set s is s1.and whcih is  not. because s1 do not have
# whole element of  set s.
#output - False.

