def pi():
    u1 = 1
    sign=1
    total=0

    for i in range(100000):
        
        total+=(1/u1)*sign
        u1+=2
        sign*=-1


    return 4*total

print(pi())    

