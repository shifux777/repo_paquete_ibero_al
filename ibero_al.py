import math
#Primera funcion: Determinantes de matrices 2x2
def det2x2():
    a11 = float(input("Escriba el valor de a11: "))
    a12 = float(input("Escriba el valor de a12: "))
    a21 = float(input("Escriba el valor de a21: "))
    a22 = float(input("Escriba el valor de a22: "))

    determinante= a11 * a22 - a12 * a21
    print ("El valor del determinante de la matriz 2x2 es:", determinante)

    return determinante



#Segunda Función: Determinantes de matrcies 3x3
def det3x3():
    a11 = float(input("Escriba el valor de a11: "))
    a12 = float(input("Escriba el valor de a12: "))
    a13 = float(input("Escriba el valor de a13: "))
    a21 = float(input("Escriba el valor de a21: "))
    a22 = float(input("Escriba el valor de a22: "))
    a23 = float(input("Escriba el valor de a23: "))
    a31 = float(input("Escriba el valor de a31: "))
    a32 = float(input("Escriba el valor de a32: "))
    a33 = float(input("Escriba el valor de a33: "))

    determinante= (a11*a22*a33) + (a12*a23*a31) + (a13*a21*a32) - (a31*a22*a13) - (a32*a23*a11) - (a33*a21*a12)
    print ("El valor del determinante de la matriz 3x3 es:", determinante)

    return determinante



#Tercer Funcion: Calcular magnitud de vectores
def magnitud():
    x = float(input("Introduzca el valor x del vector: "))
    y = float(input("Introduzca el valor y del vector: "))

    magnitud = math.sqrt(x**2 + y**2)
    
    print ("La magnitud del vector es: ", magnitud)
    return magnitud


#Cuarta Función: Calcular Dirección de un vector
def direccion():
    x= float(input("Introduzca el valor x del vector: "))
    y= float(input("Introduzca el valor y del vector: "))
    division = y / x
    angulo = math.atan(division)
    grados = math.degrees(angulo)
    print(grados)
    return grados

#Multiplicación de matrices 2x2
def suma2v():
    x1=float(input("Introduzca el valor x del vector 1: "))
    y1=float(input("Introduzca el valor y del vector 1: "))
    x2=float(input("Introduzca el valor x del vector 2: "))
    y2=float(input("Introduzca el valor y del vector 2: "))

    sumadex=x1+x2
    sumadey=y1+y2

    print ("El vector resultante de la suma es:", sumadex, ",", sumadey)



