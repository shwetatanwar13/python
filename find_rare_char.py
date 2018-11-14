f1=open('C:/Users/amolm/OneDrive/Desktop/Python/file1.txt')
str1=f1.read()
dict1=dict()
for i in str1:
    if i in dict1.keys():
        dict1[i]+=1
    else:
        dict1[i] = 1
print(dict1.items())
