''''Write a Python program to find maximum and the minimum value in a set.'''

s1 = set()
for i in range(1,5):
    i = int(input("enter your number set 1 : "))
    s1.add(i)
print(s1)
print("")

print("the maximum value of set is ",max(s1),".")
print("the minimum value of set is ",min(s1),".")