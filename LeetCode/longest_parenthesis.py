def solve(parenthesis):
    stack = []
    cur_max=0
    max_final=0
    for i in parenthesis:
        if i == '(':
            stack.append(i)
        elif i == ')' and len(stack)>0:
            if stack.pop()=='(':
                cur_max += 2
        elif i == ')' and len(stack)==0:
            if cur_max>max_final:
                max_final=cur_max
            cur_max=0
    #max_final = cur_max
    return max(max_final,cur_max)
t=int(input())
for i in range(t):
    s=input()
    r=solve(s)
    print(r)