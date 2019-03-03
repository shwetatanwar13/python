def palindrome(s):
    s=s.replace(' ','')
    if s==s[::-1]:
        return("Palindrome")
    else:
        return("Not Palindrome")

print(palindrome('nurses run'))