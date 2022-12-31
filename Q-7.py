'''Write a Python program to create a union of sets'''


s1 = set()
for a in range(1,5):
    print("Please provide a number here : ")
    a = int(input("enter your values set1 : "))
    s1.add(a)
print(s1)
print("")# it is provide us space
s2 = set()
for b in range(1,5):
    print("Please provide here alphbet ")
    b = str(input("enter your values set2 : "))
    s2.add(b)
print(s2)
print("")
print("here is your two set s1 ",s1,"\nand set s2 ",s2)
print("")
c = s1.union(s2)
print("Here is your union set : ",c)

'''output - 
Please provide a number here : 
enter your values set1 : 1
Please provide a number here : 
enter your values set1 : 2
Please provide a number here : 
enter your values set1 : 3
Please provide a number here : 
enter your values set1 : 4
{1, 2, 3, 4}

Please provide here alphbet 
enter your values set2 : a
Please provide here alphbet 
enter your values set2 : s
Please provide here alphbet 
enter your values set2 : d
Please provide here alphbet 
enter your values set2 : f
{'d', 'a', 'f', 's'}

here is your two set s1  {1, 2, 3, 4} 
and set s2  {'d', 'a', 'f', 's'}

Here is your union set :  {1, 2, 3, 4, 'd', 'a', 'f', 's'}
'''