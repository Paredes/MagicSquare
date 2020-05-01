step_by_step = True
DEBUG=True
#generar un cuadrado magico de orden impar

def show_square():
    for fila in matriz:
        string_fila = " ".join([str(i) if i >= 10 else " {}".format(i) for i in fila])
        print("|" + string_fila + "|")
    print("_"*(3*n))
    if step_by_step:
        input()

#de partida, solo generar cuadrado mágico de orden 3, luego extender a mayor orden
n = 5
#generar la matriz
matriz = []
#secuencia de progresion aritmetica
sec = [i for i in range( 1, n**2 + 1 )]
print(sec)
for i in range(n):
    fila=[]
    for j in range(n):
        fila.append(0)
    matriz.append(fila) 
#seleccionar punto de partida de diagonales
x_inicial, y_inicial = -2,2
# seleccionar sentido de las diagonales
# arr_der = -1,1 arr_izq = -1,-1 ab_der = 1,1 ab_izq = 1,-1
sentido = 1,1
rango=range(0)
i = 0
#recorrer con diagonales la matriz, llenar la matriz segun casos
for _ in range(n):
    x, y = x_inicial, y_inicial
    for _ in range(n):
        # dentro de la matriz se agrega directamente
        if x in range(n) and y in range(n):
            matriz[x][y] = sec[i]
        # 4 casos fuera de la matriz---> simetría vertical/horizontal
        # caso derecho
        elif x >= 0 and y>=n:
            matriz[ x ][ y - n ] = sec[i]
        # caso izquierdo
        elif x >= 0 and y < 0:
            matriz[ x ][ y + n ] = sec[i]
        # caso arriba
        elif x < 0 and y >= 0:
            matriz[ x + n ][ y ] = sec[i]
        # caso abajo
        elif x >= n and y >= 0:
            matriz[ x - n ][ y ] = sec[i]
        else:
            print(f"caso no contemplado:x:{x},y:{y}")
        i+=1
        x+=sentido[0]
        y+=sentido[1]
        if DEBUG:
            show_square()
    x=x_inicial + sentido[0]
    y=y_inicial + sentido[1]*-1
    x_inicial = x
    y_inicial = y




