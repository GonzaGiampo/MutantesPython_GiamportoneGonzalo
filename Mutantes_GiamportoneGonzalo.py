#ParcialIntegrador_GonzaloGiamportone_TurnoTard
import random
print("Bienvenido...")
print("Comienza el analisis:")
adn=[]
n=6
gen_mutante=0

#funcion para llenar la matriz
for i in range(n):
    adn.append([])
    for j in range(n):
        while(True):
            print("Secuencia n°: |",i,"|-|",j,"| Ingrese la base: A-T-C-G")
            valor=input().upper()
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

#funcion para buscar coincidencias en filas
print("Buscando mutaciones horizontales...")
print("-----------------------------------------------")
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
        
print("aqui se muestran horizontales: ",gen_mutante)
print("-----------------------------------------------")
#funcion para buscar coincidencias en columna
print("Buscando mutaciones verticales...")
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
print("-----------------------------------------------")
print("aqui se muestran verticales: ",gen_mutante)
print("-----------------------------------------------")
print("Buscando mutaciones en diagonal...")

#funcion para buscar coincidencias en oblicuas
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
print("-----------------------------------------------")
print("aqui se muestran oblicuas: ",gen_mutante)
print("-----------------------------------------------")
print("buscando mutaciones en diagonal inversa...")
#funcion para buscar coincidencias en oblicuas inversas
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
print("-----------------------------------------------")
print("aqui se muestran inversas: ",gen_mutante)
print("-----------------------------------------------")
print("aqui se muestra la cantidad de genes mutantes: ",gen_mutante)
print("-----------------------------------------------")
if(gen_mutante>1):
    print("Es un mutante, reclutelo!")
else:
    print("Es un simple humano...")