money = int(input("消費金額(介於1~1000之間)："))

if money>500:
    a = "0"
    b = int((1000-money)/100)
    c = int((1000-money-(100*b))/50)
    d = int((1000-money-(100*b)-(50*c))/10)
    e = int((1000-money-(100*b)-(50*c)-(10*d))/5)
    f = int((1000-money-(100*b)-(50*c)-(10*d)-(5*e))/1)
    
else:
    a = "1"
    b = int((500-money)/100)
    c = int((500-money-100*b)/50)
    d = int((500-money-50*c-100*b)/10)
    e = int((500-money-50*c-100*b-10*d)/5)
    f = int((500-money-50*c-100*b-10*d-5*e)/1)
    
print(a ,b ,c ,d ,e ,f)
