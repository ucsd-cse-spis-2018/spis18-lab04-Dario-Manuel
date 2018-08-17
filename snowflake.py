import turtle
t = turtle.Turtle()
t.speed(0)
def snowflake(length, level, t):
    angle = 60
    segment = length/3
    if level <= 0:
        t.fd(segment)
        return
    else:
        snowflake(segment, level - 1, t)
        t.rt(60)
        snowflake(segment, level - 1, t)
        t.lt(120)
        snowflake(segment, level - 1, t)
        t.rt(60)
        snowflake(segment, level - 1, t)

def snowflakeLauncher( length, level, t):
    snowflake(length, level, t)
    t.lt(120)
    snowflake(length, level, t)
    t.lt(120)
    snowflake(length, level, t)
    t.lt(120)

t.back(300)
snowflakeLauncher(1500, 0, t)
snowflakeLauncher(1500, 1, t)
snowflakeLauncher(1500, 2, t)
snowflakeLauncher(1500, 3, t)
snowflakeLauncher(1500, 4, t)
