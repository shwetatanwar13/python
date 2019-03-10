def closest_match(word):
    dictionary={'vil','sit','flick','pat','pluck','sat','vat'}
    result=[]
    for i in dictionary:
        if len(set(word).difference(i))==1:
            result.append(i)
    print(result)

closest_match('si')


