def areAnagram(str1, str2):
    # Write your code here.
    check1= dict()
    check2 = dict()
    for i in str1:
        if i in check1:
            check1[i]+=1
        else:
            check1[i]=1
    for i in str2:
        if i in check2:
            check2[i]+=1
        else:
            check2[i]=1
    return(check1.keys()==check2.keys())
    pass