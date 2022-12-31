'''Write a Python program to create a symmetric difference.'''

a = set()

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

if a.symmetric_difference(b) or b.symmetric_difference(a):
    print("Here is your symmetric difference : ",a.symmetric_difference(b))
    print("Here is your symmetric difference : ",b.symmetric_difference(a))
else:
    print("here is no difference symmetric ,\ntry again refresh the the programm ")

