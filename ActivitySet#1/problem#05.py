# Functions

def computepay(h, r):
    if hours > 40:
        overtime=(hours-40)*(r*1.5)
        pay=(40*r)+overtime
        else :
        pay=(h*r)
        return pay
    h=float(input("Enter hours"))
    r=float(input("Enter rate"))
    p=computepay(h,r)
    print("pay",p)