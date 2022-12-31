'''Write a Python program to check if a set is a subset of another set.'''

a = set({})
for s in range(1,4):
    s = int(input("enter your number set 1 : "))
    a.add(s)
print(a)
print("")
b = set()
for t in range(1,4):
    t = int(input("enter your number set 2 : "))
    b.add(t)
print(b)
print("")
c = a.issubset(b)
d = b.issubset(a)
if c or d:
    print("Here is your (issubset) a issubset b : ",c)
    print("Here is your b issubset a : ",d)

else:
    print("here a is no subset b and also b is no subset a\ntry again refresh the the programm ")

'''output -
enter your number set 1 : 1
enter your number set 1 : 2
enter your number set 1 : 3
{1, 2, 3}

enter your number set 2 : 1
enter your number set 2 : 2
enter your number set 2 : 3
{1, 2, 3}

Here is your (issubset) a issubset b :  True
Here is your b issubset a :  True
'''