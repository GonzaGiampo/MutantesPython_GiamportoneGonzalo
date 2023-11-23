
<em> # Trabajo final de programacion1-Giamportone Gonzalo </em>

TURNO TARDE-LEGAJO 51551
Para llenar la matriz recurrÍ a hacer una lista de listas, de forma que sea mas entendible en cada pedido de elemento indico posicion del elemento que se pide. mediante un while establezco la condicion de como deben ingresarse los valores
    
    adn.append([])
    for j in range(n):
        while(True):
            print("Secuencia n°: |",i,"|-|",j,"| Ingrese la base: A-T-C-G")
            valor=input()
            if(valor=='A' or valor=='T' or valor=='C' or valor=='G'):
                adn[i].append(valor)
                break
Cuando queria mostrar la matriz recurri a usar una funcion con su correspondiente invocacion
    
    def muestra(adn,n):
    for i in range(n):
        for j in range(n):
            print(adn[i][j],end="| ")
        print(" ") 
    muestra(adn,n)

Finalmente use 4 diferentes estructura de codigos para buscar las coincidencias. En todos lo casos empleando dos bucles for anidados, y en las coincidencias oblicuas tres bucles for, para recorrer la matriz y encontrar las semejanzas.
De forma horizontal o por filas:

    iterador=0
    for i in range(0,6):
        for j in range(0,5):
            if(adn[i][j]==adn[i][j+1]):
                iterador=iterador+1
            elif(adn[i][j]!=adn[i][j+1]):
                iterador=0
            if(iterador==3):
                gen_mutante=gen_mutante+1
        iterador=0

De forma vertical o por columnas:

    iterador=0
    for i in range(0,6):
        for j in range(0,5):
            if(adn[j][i]==adn[j+1][i]):
                iterador=iterador+1
            elif(adn[j][i]!=adn[j+1][i]):
                iterador=0
            if(iterador==3):
                gen_mutante=gen_mutante+1
        iterador=0

De forma oblicua de derecha a izquierda

    iterador=0
    num=4
    for i in range(0,3):
        for j in range(0,3):
            for k in range(1,num):
                if(adn[i][j]==adn[i+k][j+k]):
                    iterador=iterador+1
                elif(adn[i][j]!=adn[i+k][j+k]):
                    iterador=0
                if(iterador==3):
                    gen_mutante=gen_mutante+1
                    iterador=0
            num=num-1
        num=num+2
        iterador=0

De forma oblicua de forma inversa:

    iterador=0
    num=4
    for i in range(0,3):
        for j in range(5,2,-1):
            for k in range(1,num):
                if(adn[i][j]==adn[i+k][j-k]):
                    iterador=iterador+1
                elif(adn[i][j]!=adn[i+k][j-k]):
                    iterador=0
                if(iterador==3):
                    gen_mutante=gen_mutante+1
                    iterador=0
            num=num-1
        num=num+2   
Y para terminar hago una devolucion del chequeo de la matriz
    
    if(gen_mutante>1):
        print("Es un mutante, reclutelo!")
    else:
        print("Es un simple humano...")


#extras: al momento de chequear para evitar el trabajo engorroso de llenar la matriz de forma manual. Use un metodo para generar matrices con los caracteres solicitados, en una matriz de 6x6 de forma random#

    # Definir los caracteres posibles
    caracteres = ['A', 'T', 'C', 'G']

    # Crear una matriz de 6x6 con elementos aleatorios
    adn = [[random.choice(caracteres) for _ in range(6)] for _ in range(6)]
   
