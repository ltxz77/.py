import math
angulo= float (input('digite um valor'))
seno=math.sin(math.radians(angulo))
print('o angulo de {} tem o valor do seno de {:.2f}'.format(angulo,seno))
coseno= math.cos(math.radians(angulo))
print('o angulo de {} tem o valor do coseno de {:.2f}'.format(angulo,coseno))
tangente= math.tan(math.radians(angulo))
print('o angulo de {} tem o valor do tangente de {:.2f}'.format(angulo,tangente))

