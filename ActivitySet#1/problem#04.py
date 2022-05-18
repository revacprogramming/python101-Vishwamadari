# Conditional Execution

hrs=input('enter hours')
h=float(hrs)
rate=input('enter rate')
r=float(rate)

if h<=40:
    pay=h*r
  
else: 
    pay=40*r
    pay=pay+(h-40)*(1.5*r)
    
    print(pay)
    