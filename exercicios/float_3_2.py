hrs = input("Enter Hours:")
try:
    h = float(hrs)
except:
    print("Error, please enter numeric input")
    quit()

rat = input("Enter Rate:")
try:
    r = float(rat)
except:
    print("Error, please enter numeric input")
    quit()
    
print(h,r)
if h>40 : 
    pay = 40 * r
    pt = (h-40)*(r*1.5)+pay
else : 
    pt = h*r
print(pt) 