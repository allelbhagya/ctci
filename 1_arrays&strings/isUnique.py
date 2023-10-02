f = "qwrty ajlpm xzvun bhkco"
final = ''.join(f.split())
check=dict()
flag = True
for i in final:
    if i in check:
        flag = False
        break
    else:
        check[i]=1
print(flag)