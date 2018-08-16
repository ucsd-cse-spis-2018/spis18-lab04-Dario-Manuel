import turtle
import time

t = turtle.Turtle()
t.lt(90)
t.speed(0)
def tree(trunkLength, height, t):
    branchAngle = 45
    branchMult = .9
    recursionMult = .35
    if height == 0:
        return 0
    elif height > 1:
        # Base of the tree
        t.fd(trunkLength)
        t.lt(branchAngle)
        t.fd(trunkLength * branchMult)

        # t.lt(branchAngle)
        # Recursion Left
        t.lt(branchAngle)
        tree(trunkLength*recursionMult, height - 1, t)
        t.rt(branchAngle*2)
        tree(trunkLength*recursionMult, height - 1, t)

        # Return to branch
        t.lt(branchAngle)
        t.bk(trunkLength * branchMult)
        t.rt(branchAngle * 2)
        t.fd(trunkLength * branchMult)

        # Recursion Right 
        t.lt(branchAngle)
        tree(trunkLength*recursionMult, height - 1, t)
        t.rt(branchAngle*2)
        tree(trunkLength*recursionMult, height - 1, t)

        # Return to base
        t.lt(branchAngle)
        t.bk(trunkLength * branchMult)
        t.lt(branchAngle)
        t.bk(trunkLength)

