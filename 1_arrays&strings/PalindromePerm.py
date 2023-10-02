def palindromeString(s):
    check=dict()
    for i in s:
        if i in check:
            check[i]+=1
        else:
            check[i]=1
    odds = 0
    for i in check.values():
        if i%2 != 0:
            odds+=1
    if len(s)%2==0:
        return odds == 0
    else:
        return odds == 1
    pass