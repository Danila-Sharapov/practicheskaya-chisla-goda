year = int(input("Введите год: "))
res = 0
for i in range (12):
    l=i+1
    if l>=8:
        l+=1
    if l==2:
        if year%4 == 0 and year%100 != 0 or year%400 == 0:
            for j in range (29):
                for n in str(j+1):
                    res+=int(n)
        else:
            for j in range (28):
                for n in str(j+1):
                    res+=int(n)
    elif l%2 == 0:
        for j in range (30):
                for n in str(j+1):
                    res+=int(n)
    elif l/2 != 0:
        for j in range (31):
                for n in str(j+1):
                    res+=int(n)
print (res)