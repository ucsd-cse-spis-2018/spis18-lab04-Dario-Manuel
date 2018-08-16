import turtle
t = turtle.Turtle()
def snowflake( length, level, t ):
    angle = 60
    segment = length/3
    if level == 0:
        t.fd(segment)
        return
    else:
        t.rt(60)
        t.fd(segment)
        snowflake( segment, level - 1, t )
        t.fd(segment)
        #t.lt(120)
        
        t.lt(120)
        t.fd(segment)
        snowflake( segment, level - 1, t )
        t.rt(60)
        

def snowflakeLauncher( length, level, t ):
    snowflake( length, level, t )
    t.lt(120)
    snowflake( length, level, t )
    t.lt(120)
    snowflake( length, level, t )
    t.lt(120) 
        
##
##        t.rt(60)
##        t.fd(segment)
##        snowflake( segment, level - 1, t )
##        t.rt(120)
##        t.fd(segment)
##        t.lt(120)

        #t.fd(segment)
        #snowflake( segment, level - 1, t )
        #t.fd(segment)
        #t.lt(120)


snowflakeLauncher( 100, 4, t ) 
