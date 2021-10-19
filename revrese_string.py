def reverse(st):
    if len(st) == 0:
     return "Enter Something to reverse, I can't reverse nothing!"
    if len(st) == 1:
     return st
    else:
     return st[-1] + reverse(st[:-1])

print(reverse(''))