m = [1,3,5,7,9,11,13,15]
for i in m:
    for i1 in m:
        for i2 in m:
            print(i1+i2+i)
            if i1+i2+i==30:print(i1,i2,i)