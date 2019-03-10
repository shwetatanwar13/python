import random
def rand_num(low,high,n):
    for i in range(n):
      yield random.randint(low,high)

print(list(rand_num(1,10,12)))