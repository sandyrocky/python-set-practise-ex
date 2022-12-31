'''Write a Python program to create set difference.'''


s = set()
for i in range(1,4):
    print("Pleaase provide here alphabet  : ")
    i = str(input("enter your alphbet s : "))
    s.add(i)

print(s)

s2 = set()
for i in range(1,4):
    print("plese provide alphabet : ")
    print("")
    i = str(input("enter your alphbate s2 : "))
    s2.add(i)
print(s2)
print("")
print("Here is your two set : ",s,"\nand",s2 )

if  (s.difference(s2)) or (s2.difference(s)):
    print("here are difference b/w two set : ",s.difference(s2),s2.difference(s))
else:
    print("here is no difference b/w two set : ")


'''output -
Pleaase provide here alphabet  : 
enter your alphbet s : q
Pleaase provide here alphabet  : 
enter your alphbet s : w
Pleaase provide here alphabet  : 
enter your alphbet s : e
{'q', 'e', 'w'}
plese provide alphabet : 

enter your alphbate s2 : a
plese provide alphabet : 

enter your alphbate s2 : s
plese provide alphabet : 

enter your alphbate s2 : d
{'s', 'd', 'a'}

Here is your two set :  {'q', 'e', 'w'} 
and {'s', 'd', 'a'}
here are difference b/w two set :  {'q', 'e', 'w'} {'s', 'a', 'd'}
'''