def blackjack(*args):
    if sum(args)<=21:
        return sum(args)
    elif sum(args)>21:
        if args[0]==11 or args[1]==11 or args[2]==11:
            return sum(args)-10
        else:
            return 'BUST'

print(blackjack(9,9,11))