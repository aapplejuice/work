for x in range(1, 10):
    for y in range(1, 10):
        if x * y < 10:
            print(str(y)+"*"+str(x)+"="+"0"+str(x*y), end= "|" )
        else:
            print(str(y)+"*"+str(x)+"="+str(x*y), end= "|" )
    print()

#y要在前面
#個位數字要加零    