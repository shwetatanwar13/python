def num_sum(num_list):
    if len(num_list)==1:
      return num_list[0]
    else:
      return num_list[0] + num_sum(num_list[1:])

print(num_sum([1,2,3,4,5,6]))
