hrs = input("Enter Hours:") #input das horas em numero texto
h = float(hrs) #convertendo numero texto para numero decimal
rat = input("Enter Rate:")
r = float(rat)
if h>40 : #se trabalhou mais que 40 horas pagar o valor maximo normal mais o valor de hora extra
    pay = 40 * r
    pt = (h-40)*(r*1.5)+pay
else : #se não so multiplicar pelo valor normal de trabalho
    pt = h*r
print(pt) #imprimir valor total do pagamento em decimal

#3.1 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
#Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours.
#Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 
#You should use input to read a string and float() to convert the string to a number. 
#Do not worry about error checking the user input - assume the user types numbers properly.