# MutantesPython_GiamportoneGonzalo
Trabajo final de programacion1
for i in range(n):
    adn.append([])
    for j in range(n):
        while(True):
            print("Secuencia n°: |",i,"|-|",j,"| Ingrese la base: A-T-C-G")
            valor=input()
            if(valor=='A' or valor=='T' or valor=='C' or valor=='G'):
                adn[i].append(valor)
                break
Para llenar la matriz recurri a hacer una lista de listas, de forma que sea mas entendible en cada pedido de elemento indico posicion del elemento que se pide. mediante un while establezco la condicion de como deben ingresarse los valores
