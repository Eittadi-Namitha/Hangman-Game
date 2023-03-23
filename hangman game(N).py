str=['y','e','l','l','o','w']
c=['m','a','r','o','o','n']
d=['r','e','d']
e=['b','l','u','e']
f=['c','r','i','c','k','e','t']
g=['b','a','d','m','i','n','t','o','n']
h=['e','d','u','c','a','t','i','o','n']
i=['s','c','h','o','o','l']
j=['a','p','p','l','e']
k=['h','o','u','s','e']
l=['w','a','r','a','n','g','a','l']
m=['c','a','r']
n=['b','i','k','e']
o=['m','o','v','i','e']
p=['g','r','o','u','n','d']
q=['h','i','g','h','w','a','y']
r=['f','e','v','e','r']
s=['p','h','o','t','o','g','r','a','p','h','y']
t=['i','n','d','i','a']
u=['l','a','p','t','o','p']
a=[]
for i in range(len(str)):
    a.append('_')
count=5
print(a)
while count>0:
    z=input("Enter alphabet: ")
    if(len(z)>1):
        print("Enter only alphabet")
        z=input("Enter only alphabet: ")
    find=False
    for i in range(len(a)):
        if(z==str[i]):
            find=True
            a[i]=z
        print(a[i],end=" ")
    if(find==True):
        print(" The chance is not lost")
    if(a==str):
        print("Congrats!!! You have guessed the word")
        break
    if(find==False):
        count=count-1
        print("Letter is not present")
        if(count!=0):
            print("You have",count,"chances left")
    if(count==0):
        print("Your chances are over")
