import turtle
t= turtle.Turtle()
def drawSpiral (initialLength, angle, multiplier, t):
    if multiplier < 1 and initialLength < 1 :
        return
    elif multiplier > 1 and initialLength > 200:
        return
    else:
        t.forward(initialLength)
        t.right(angle)
        drawSpiral(initialLength * multiplier, angle, multiplier, t)

        
drawSpiral(1, -45, 1.1, t)
