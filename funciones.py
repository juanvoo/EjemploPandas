def suma (a,b):
    return print(a+b)
    
def resta (a,b):
    return print(a-b)

def multiplicacion (a,b):
    return print(a*b)

def division (a,b):
    try:
        return print(a/b)
    except:
        return print("No se puede dividir entre 0")
    # if b == 0:
    #     return print("Error, no se puede dividir entre 0")
    # else:
    #     return print(a/b) 