'''Count the number of worlds in tne sentence.
 The sentense should be Taken from the users.'''
s=str(input())
c=0
for i in s:
    if i==" ":
        c+=1
print(c)

