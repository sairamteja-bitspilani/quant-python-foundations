age= int(input("enter ur age"))
if (age>=18):
    print("you are old enough")
    W=input("enter ur weight")
    H=input("enter ur height")
    BMI=int(W)/(float(H)**2)
    x=round(BMI,1)
    print("your BMI is ",x)
    if x<18.5:
        print("ur underweight")
    else:
        if x <= 24.9:
            print("ur fit")
        else:
            print("ur unhealthy")
else:
    print("ur still kid")

