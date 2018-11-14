import math
x=float(input('digite cateto oposto'))
y=float(input('digite cateto adjacente '))
hipotenusa=math.hypot(x,y)
print('sua hipotenusa será{:.3f}'.format(hipotenusa))