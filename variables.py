mass = int(input('enter the weight of the person in kg:'))
height = float(input('enter the height of the person in meters:'))
bmi = (mass/height**2)
print('The BMI of the person is:',bmi)

#Pythagoreus logic
a = int(input('enter a:'))
b = int(input('enter b:'))
C = (a**2 + b**2)**0.5   #Finding c using pythagoreus theorem
print('The value of c is:',C)

#Currency calculator
#gathering the info about the amount of each currency that is available.
a = int(input('what do you left in pesos? ')) 
b = int(input('what do you left in soles? ')) 
c = int(input('what do you left in reais? ')) 
#conversion logic
p = (a*0.058)  # pesos to dollars
s = (b*0.29)   # soles to dollars
r = (c*0.2)    # reais to dollars
total = (p+s+r)
print('Total amount that is left in USD is:',total)
