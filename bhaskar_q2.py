''' Count the latter in the sentense. Sentense should taken from the users
'''
s=input("Enter the sentense")
dic = {}
for i in s:
    if(i in dic):
        dic[i]+=1
    else:
        dic[i]=1
print(dic)
