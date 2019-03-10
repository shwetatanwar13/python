l=[]
def reverse_string_recursive(s):
    s=list(i for i in s)
    if len(s)!=0:
     l.append(s.pop())
     reverse_string_recursive(s)

reverse_string_recursive("Sony is going to introduce Internet TV soon")

print(''.join(i for i in l))
