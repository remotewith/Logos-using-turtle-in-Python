from turtle import*


speed('fastest')
pensize(4)
pen(fillcolor='yellow')
begin_fill()
for a in range(115):
    forward(6)
    left(4)
right(60)
end_fill()
pen(fillcolor='yellow')
begin_fill()

for i in range(17):   # first ear
    forward(6)
    left(10)
right(63)
end_fill()

for j in range(18):
    forward(6)
    left(4)
right(60)
begin_fill()
for b in range(17):  # second ear
    forward(6)
    left(10)
end_fill()
left(35)


#first eye
penup()
forward(55)
pendown()
pencolor('yellow')
pen(fillcolor='yellow')
begin_fill()
circle(15)
end_fill()


#second eye
right(5)
penup()
forward(65)
pendown()
pencolor('yellow')
pen(fillcolor='yellow')
begin_fill()
circle(15)
end_fill()
# eyeball

left(90)
penup()
forward(15)
pendown()
pencolor('black')
dot(10)

left(90)
penup()
forward(67)
pendown()
dot(10)
penup()
forward(10)
pendown()

left(90)
penup()
forward(108)
pendown()
right(60)
# abdomen

pen(fillcolor='yellow')
begin_fill()

for s in range(75):
    left(2)
    forward(6)
left(19)


for t in range(71):
    left(2)
    forward(6)
end_fill()

# left hand
left(110)
penup()
forward(68)
left(90)
forward(90)
pendown()

right(15)
pen(fillcolor='yellow')
begin_fill()

for y in range(30):
    forward(5)
    right(1.6)
    
for u in range(13):
    forward(2)
    right(10)
for x in range(17):
    forward(6)
    right(1)
end_fill()
# right hand
penup()
left(13)
forward(254)

pendown()
left(10)
pen(fillcolor='yellow')
begin_fill()
for r in range(32):
    forward(5)
    left(2.5)
for o in range(12):
    forward(2)
    left(10)
for e in range(16):
    forward(6)
    left(1.1)
end_fill()

right(30)
left(10)
right(5)
#right leg

penup()
forward(20)
right(90)
forward(140)
right(60)
pendown()
pen(fillcolor='yellow')
begin_fill()
for q in range(20):
    forward(5)
    left(1.8)
for t in range(12):
    forward(2)
    left(10)
for z in range(19):
    forward(6)
    left(1.8)
end_fill()
#left leg
right(45)
penup()
forward(165)
left(90)
forward(37)
right(120)
pendown()
pen(fillcolor='yellow')
begin_fill()
for w in range(22):
    forward(5)
    right(1.8)
for m in range(12):
    forward(2)
    right(10)
for n in range(20):
    forward(6)
    right(2)
end_fill()
