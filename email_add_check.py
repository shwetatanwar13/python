import re
def email_add(list_email):
    #Check if the email id is valid, if not remove it from the list
    regex = r'\b[A-Za-z0-9._%+-?/!#$=]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    i=0
    for i in range(len(list_email)):
        if (not re.match(regex, list_email[i])):
           list_email.pop(i)
    i=0
    for eml in list_email:
        #for each email id call the processor function
        list_email[i]= email_processor(eml)
        i=i+1
    #Set will remove duplicates so we will have unique email ids
    return (len(set(list_email)))

#Function to replace . and remove trailing characters after +
def email_processor(eml):
    eml=eml.split('@')[0].replace('.', '') + '@'+ eml.split('@')[1]
    return eml.split('+')[0]+ ('@'+ eml.split('@')[1] if eml.__contains__('+') else '')


print(email_add(["test.email+alex@peopledatalabs.com","test.e.mail+bob.cathy@peopledatalabs.com","testemail+david@people.data.labs.com"]))

print(email_add(["a@peopledatalabs.com","b@peopledatalabs.com","c@peopledatalabs.com"]))

