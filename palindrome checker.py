def palindrome(a):
    a=str(a)
    a.replace(' ','')
    if a==a[::-1]:
        print("palindrome")
    else:
        print("not a palindrome")

palindrome(1331)