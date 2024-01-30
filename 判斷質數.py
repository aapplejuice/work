n = int(input("請輸入一ㄍ數字："))
prime = True

if n<2:
    prime = False
else:
    for i in range(2, n):
        if n%i==0:
            prime = False
            break
            
if prime == True:
    print("是質數")
else:
    print("不是質數")
