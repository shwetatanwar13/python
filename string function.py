def string_length(mystring):
    if str.isdigit(mystring):
        print("Not a string")
    else:
     return len(mystring)

print(string_length(10))