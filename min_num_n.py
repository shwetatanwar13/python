import random
# number of elements
#n = int(raw_input("Enter number of elements : "))

# Below line read inputs from user using map() function
#l = list(map(int,raw_input("Enter the numbers : ").strip().split()))[:n]
l= random.sample(range(1,10000),5000)
print(l)

min_num = l[0]
for i in l:
    if min_num > i:
        min_num = i
print(min_num)
