#ParcialIntegrador_GonzaloGiamportone_TurnoTarde
print("Bienvenido...")
print("Comienza el analisis:")
adn=[]
n=6
#funcion para llenar la matriz
for i in range(n):
    adn.append([])
    for j in range(n):
        while(True):
            print("Secuencia n°: |",i,"|-|",j,"| Ingrese la base: A-T-C-G")
            valor=input()
            if(valor=='A' or valor=='T' or valor=='C' or valor=='G'):
                adn[i].append(valor)
                break

#funcion para mostrar la matriz
def muestra(adn,n):
    for i in range(n):
        for j in range(n):
            print(adn[i][j],end="| ")
        print(" ")    


muestra(adn,n)

gen_mutante=0
#funcion para buscar coincidencias en filas
print("Buscando mutaciones horizontales...")
iterador=0
for i in range(n):
    iterador=0
    for j in range(0,5):
        if(adn[i][j]==adn[i][j+1]):
            iterador=iterador+1
        else:
            iterador=0
    if(iterador>=3):
        gen_mutante=gen_mutante+1
        break

#funcion para buscar coincidencias en columna
print("Buscando mutaciones verticales...")
iterador=0
for i in range(n):
    iterador=0
    for j in range(0,5):
        if(adn[j][i]==adn[j+1][i]):
            iterador=iterador+1
        else:
            iterador=0
    if(iterador>=3):
        gen_mutante=gen_mutante+1
        break 

#funcion para buscar coincidencias en oblicuas
print("Buscando mutaciones en diagonal...")
iterador=0
for i in range(0,3):
    num=4
    for j in range(0,3):
        for k in range(1,num):
            if(adn[i][j]==adn[i+k][j+k]):
                iterador=iterador+1
            else:
                iterador=0
                break
            if(iterador>=3):
                gen_mutante=gen_mutante+1
                break
        num=num-1

#funcion para buscar coincidencias en oblicuas inversas
iterador=0
for i in range(5,2,-1):
    num=5
    for j in range(0,3):
        for k in range(1,num):
            if(adn[i][j]==adn[i-k][j+k]):
                iterador=iterador+1
            else:
                iterador=0
                break
            if(iterador>=3):
                gen_mutante=gen_mutante+1
                break
        num=num-1

print("aqui se muestra la cantidad de genes mutantes: ",gen_mutante)
if(gen_mutante>1):
    print("Es un mutante, reclutelo!")
else:
    print("Es un simple humano...")