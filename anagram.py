def anagram(s1,s2):
   if len(s1)==len(s2):
    if len(set(s1.lower()).difference(s2.lower()))==0:
        print("Anagram")
    else:
        print("Not Anagram")
   else:
       print("Not Anagram")
anagram('Mary','armyt')