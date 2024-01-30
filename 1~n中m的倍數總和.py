n = int(input("n =  "))
m = int(input("m =  "))

sum = 0
for i in range(1, n+1):
    if i*m <= n:
        sum = sum + i*m
   

print(sum)