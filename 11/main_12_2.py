import classes_12_2 as cl
import random as r
x = []

for i in range(3):
    x.append(cl.Circle(r.randint(1,20),r.randint(1,20),r.randint(1,20)))
    x.append(cl.Square(r.randint(1,20), r.randint(1,20), r.randint(1,20), r.randint(1,20)))
    x.append(cl.Triangle(r.randint(1,20),r.randint(1,20),r.randint(1,20),r.randint(1,20),r.randint(1,20),r.randint(1,20)))

square = 0
for figure in x:
    square += figure.get_square()

print('Square is ', square)