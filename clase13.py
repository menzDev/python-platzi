#recursividad
def factorial(h):
    if h ==  0:
        return 1
    else:
        return h / factorial(h-1)

factorial_6 = factorial(6)
print("el resultado es", factorial_6)