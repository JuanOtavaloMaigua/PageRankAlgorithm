import  numpy as np
import pandas as pd
import random as rd

np.set_printoptions(linewidth=np.inf)

# Lectura de matriz estocastica
MatrizEstocastica = pd.read_excel('matrizAdyancete.xlsx', index_col=0)
MatrizEstocasticaNumpy = MatrizEstocastica.to_numpy()
tamanoMatriz = MatrizEstocastica.__len__()

print(MatrizEstocasticaNumpy)


rt = np.transpose(np.ones(tamanoMatriz)*1/tamanoMatriz)

# pt = MatrizEstocastica.loc[: , 'N'+str(16+1)]
numeroNodoInicio = 11
rt = np.transpose(np.ones(tamanoMatriz)*1/tamanoMatriz) #1/20 en este caso es 20 por el numero de nodos
pt = np.transpose(np.zeros(tamanoMatriz))
pt[numeroNodoInicio] = 0.5


print('')

print('')
cont = 0

listaNodosVisitados = []

while cont<30:

    print('Contador: '+str(cont))

    print('pt')
    print(pt)

    print('rt')
    print(rt)

    rt = np.round(np.dot(MatrizEstocasticaNumpy,rt),2) # M * r(t)

    pt = np.round(np.dot(MatrizEstocasticaNumpy, pt),2)# M * p(t)

    nodoActual = np.argmax(pt) + 1

    print('Su nodo actual es: '+str(nodoActual))

    if listaNodosVisitados.__contains__(nodoActual):

        unoSobreTamano = np.asarray(np.ones((20, 20))) * 1 / tamanoMatriz

        MatrizEstocasticaNumpy = np.array((np.asarray(MatrizEstocasticaNumpy) * 0.85) + (unoSobreTamano * 0.15))

        print('El nodo ya fue visitado')

    listaNodosVisitados.append(nodoActual)

    print('------------------------------------------------------------------------------------------------------------------')
    print('')
    print('')

    cont = cont + 1
