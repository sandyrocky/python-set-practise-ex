''' Write a Python program to create an intersection of sets.'''

# creating new 2set , its name s1 and s2 then we create will intersection set.
#this s1 is emtpy and we assign set here to store the value which will come from  for loop.
s1 = set()
for a in range(1,5):
    a = int(input("enter your values set1 : "))
    s1.add(a)
print(s1)
print("")# it is provide us space
s2 = set()
for b in range(1,5):
    b = int(input("enter your values set2 : "))
    s2.add(b)
print(s2)
print("")
print("here is your two set s1 ",s1,"\nand set s2 ",s2)
print("")
c = s1.intersection(s2)
print("Here is your inersection set : ",c)

'''output -
enter your values set1 : 1
enter your values set1 : 2
enter your values set1 : 3
enter your values set1 : 4
{1, 2, 3, 4}

enter your values set2 : 1
enter your values set2 : 2
enter your values set2 : 5
enter your values set2 : 6
{1, 2, 5, 6}

here is your two set s1  {1, 2, 3, 4} 
and set s2  {1, 2, 5, 6}

Here is your inersection set :  {1, 2}
'''
