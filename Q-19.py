'''Write a Python program to find the elements in a given set that are not in another set.'''

# saara lafda hai app kis ko orginal set mante ho aur kis ko app another set mante ho.
s = {1,2,3,4,"sandeep"}
s1 = {1,"sandeep",6,8,9}
a=s.difference(s1)
b=s1.difference(s)
print("these element are not ",a,"s1 .")
print("these element sre not ",b,"s .")