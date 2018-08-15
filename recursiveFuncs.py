# Implement a function that multiply integers without using the '*' operator
def recProduct(a, b):
    ''' Returns the product of two integers a and b without using the * operator
    This function should use recursion '''
    if b == 0:
        return 0
    elif b > 0:
        return recProduct(a, b-1) + a
    return 'stub'
