import json
from difflib import get_close_matches
data=json.load(open("data.json"))
def find_meaning(word):
    word=word.lower()
    if data.get(word,data.get(word.capitalize())) is None:
        return(wrong_word(word))
    else:
        return data.get(word,data.get(word.capitalize()))

def wrong_word(word):
    if len(get_close_matches(word,data.keys(),n=3))>0:
         yesno=input("Did you mean any of these words %s..if yes type the word else type [n/N]?" %get_close_matches(word,data.keys(),n=3))
         if yesno not in ['n','N']:
             return data.get(yesno)
         else:
             return (["Word doesn't exist"])
    else:
        return(["Word doesn't exist"])
choice=''
while choice!='exit':

 word=input("Enter the word whose meaning you want to know:")
 print('\n'+'\n'.join(i for i in find_meaning(word)))
 choice=input("\nTo Exit Dictionary Type exit or Press any key to continue..\n")
