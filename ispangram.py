import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    return(True if len(set(alphabet).difference(set(str1.lower())))==0 else False)

print(ispangram("The quick brown fox jumps over the Lazy dog"))
