import random
# number of elements
#n = int(raw_input("Enter number of elements : "))

# Below line read inputs from user using map() function
#l = list(map(int,raw_input("Enter the numbers : ").strip().split()))[:n]
l= random.sample(range(1,100000000),50000000)
#print(l)
flag=1
for i in l:
  flag = 1
  for j in l:
    if i>j:
      flag = 0
      break
  if flag == 1:
    min_num = i
    break
print(min_num)