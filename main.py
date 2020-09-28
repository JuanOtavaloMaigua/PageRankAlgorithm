# TODO Hacer el dibujo de la matriz estocastica
# TODO Implementar la filosofia Page Rank
# TODO Hacer un camino para recorrer todos los años
# TODO Implementar el algoritmo de power iteration
# TODO Mostrar el vector r y el metodo para detectar trampas, preguntar al usuario si quiere hace teletransportacion
# TODO enviar el archivo
import  numpy as np
import pandas as pd
import random as rd

import  networkx as nx
import matplotlib.pyplot as plt

np.set_printoptions(linewidth=np.inf)

# Lectura de matriz estocastica
MatrizEstocastica = pd.read_excel('matrizAdyancete.xlsx', index_col=0)


# # Dibujar el grafo dirigido
# grafo = nx.DiGraph()
#
# listaNombreNodos = MatrizEstocastica.columns.values
# grafo.add_nodes_from(listaNombreNodos)
# #
MatrizEstocasticaNumpy = MatrizEstocastica.to_numpy()
tamanoMatriz = MatrizEstocastica.__len__()
#
# print('Tamano matriz: '+str(tamanoMatriz))
#
#
# for indiceListTemp in range(0, len(MatrizEstocasticaNumpy)):
#     listaTemp = MatrizEstocasticaNumpy[indiceListTemp]
#     for indiceValoresTemp in range(0,len(listaTemp)):
#         listTempValores = listaTemp[indiceValoresTemp]
#         if listTempValores!=0:
#             grafo.add_edge('N'+str(indiceValoresTemp+1), 'N'+str(indiceListTemp+1))
#
# nx.draw_networkx(grafo, arrows=True, arrowsize=10, with_labels=True)
# plt.draw()
# plt.show()



print(MatrizEstocastica)


#Power iteration
indiceValorMaximo = 19
rt = np.transpose(np.ones(tamanoMatriz)*1/tamanoMatriz) #1/20 en este caso es 20 por el numero de nodos
pt = np.transpose(np.zeros(tamanoMatriz))
pt[indiceValorMaximo] = 0.5


listaNodosVisitados = []
listaNodosVisitados.append(indiceValorMaximo+1)
listaRt = []

flag = 0
cont = 1


while cont<35: #Cambar esto para que itere hasta que se logre visitar todos los nodos
    print('****************************Usted esta en el nodo: '+ str(indiceValorMaximo+1))
    print(MatrizEstocasticaNumpy)
    print('rt: ')
    print(rt)
    print('pt: ')
    print(pt)
    print('Nodos visitados: ')
    print(listaNodosVisitados)
    # print('Analisis Sumas: ')
    # print(listaSumas)
    print('----------------------------------------------------------------------------------------------------------------------')


    rt = np.round(np.dot(MatrizEstocasticaNumpy,rt),2) # M * r(t)

    pt = np.round(np.dot(MatrizEstocasticaNumpy, pt),2)# M * p(t)

    listaRt.append(np.count_nonzero(rt==min(rt)))

    matrizCeros = np.asarray(np.zeros(tamanoMatriz)) #Array de ceros


    indiceValorMaximo = np.argmax(pt)
    # valorMaximo = max(pt)  #Encuentra el valor maximo del vector de probabilidades
    # matrizCeros[indiceValorMaximo] = valorMaximo  #Escoge el valor maximo TODO hay que modificar esto a random

    listaNodosVisitados.append((indiceValorMaximo+1))

    #Dead ends
    if list(set(MatrizEstocastica.loc[: , 'N'+str(indiceValorMaximo+1)])).__len__()==1 or sum(MatrizEstocastica.loc[: , 'N'+str(indiceValorMaximo+1)])==0:
        print('Has entrado ha un Dead End')
        opcionUsuario = input('Desea teletransportarse? s/n:  ')
        if opcionUsuario == 's':
            MatrizEstocasticaNumpy[:,indiceValorMaximo] = np.ones(tamanoMatriz)*1/tamanoMatriz

            indiceCambiado = rd.randrange(0,tamanoMatriz)
            while indiceCambiado == indiceValorMaximo and listaNodosVisitados.__contains__(indiceCambiado):
                indiceCambiado = rd.randrange(0,tamanoMatriz)

            #Fila, Columna
            MatrizEstocasticaNumpy[indiceCambiado, indiceValorMaximo] = 0.9


            print('Nueva Matriz Estocastica')

            flag = 1



    # SpyderTrap
    if listaRt.__len__()>=3 and (listaRt[listaRt.__len__() - 3]-listaRt[listaRt.__len__() - 1])==0 and listaRt[listaRt.__len__() - 3]>0 and flag==0:
        print('Has entrado ha un Spyder Trap')

        opcionUsuario = input('Desea teletransportarse? s/n:  ')

        if opcionUsuario == 's':

            listaRt = []
            unoSobreTamano = np.asarray(np.ones((20, 20)))*1/tamanoMatriz

            MatrizEstocasticaNumpy = np.array((np.asarray(MatrizEstocasticaNumpy)*0.85)+(0.15*unoSobreTamano))

            indiceCambiado = rd.randrange(0,tamanoMatriz)
            while indiceCambiado == indiceValorMaximo and listaNodosVisitados.__contains__(indiceCambiado):
                indiceCambiado = rd.randrange(0,tamanoMatriz)

            #Fila, Columna
            MatrizEstocasticaNumpy[indiceCambiado, indiceValorMaximo] = 0.9

            print('Nueva Matriz Estocastica')

    flag = 0
    cont = cont + 1

print(list(set(listaNodosVisitados)))








    # #SpyderTrap
    # if listaNodosVisitados.__len__()>=3 and listaRt.__len__()>=3:
    #     # ultimo = listaNodosVisitados[listaNodosVisitados.__len__() - 3:listaNodosVisitados.__len__()]
    #     # primero = listaNodosVisitados[listaNodosVisitados.__len__() - 6:listaNodosVisitados.__len__() - 3]
    #     #
    #     # if list(set(primero)&set(ultimo)).__len__()==3:
    #     #
    #     #
    #     #     print(primero,ultimo)
    #     #     print(list(set(primero)&set(ultimo)).__len__())
    #
    #     print('Has entrado ha un Spyder Trap')
    #     unoSobreTamano = np.asarray(np.ones((20, 20)))*1/tamanoMatriz
    #
    #     MatrizEstocasticaNumpy = np.array((np.asarray(MatrizEstocasticaNumpy)*0.8)+(unoSobreTamano*0.2))
    #
        # indiceCambiado = rd.randrange(0,tamanoMatriz)
        # while indiceCambiado == indiceValorMaximo and listaNodosVisitados.__contains__(indiceCambiado):
        #     indiceCambiado = rd.randrange(0,tamanoMatriz)

        #Fila, Columna
    #    # MatrizEstocasticaNumpy[indiceCambiado, indiceValorMaximo] = 0.9
    #
    #     print('Nueva Matriz Estocastica')
    #     print(MatrizEstocasticaNumpy)


    # print('')
    # print('')



    # #Detector de spider traps
    # if listaNodosVisitados.__len__()!= listaNodosNoRepetidos.__len__():
    #     listaNodosVisitados = listaNodosNoRepetidos
    #     print('Usted a ingresado a un spyder trap')
    #     unoSobreTamano = np.asarray(np.ones((20, 20)))*1/tamanoMatriz
    #
    #     MatrizEstocasticaNumpy = np.array((np.asarray(MatrizEstocasticaNumpy)*0.8)+(unoSobreTamano*0.2))
    #
    #     print('Rango Maximo')
    #     indiceCambiado = rd.randrange(0,tamanoMatriz)
    #     while indiceCambiado == indiceValorMaximo and listaNodosVisitados.__contains__(indiceCambiado):
    #         indiceCambiado = rd.randrange(0,tamanoMatriz)
    #
    #     #Fila, Columna
    #     MatrizEstocasticaNumpy[indiceCambiado, indiceValorMaximo] = 0.9
    #
    #     print('Nueva Matriz Estocastica: ')
    #     print(MatrizEstocasticaNumpy)
    #
    #
    # #Detector de dead ends
    # sumaColumna = sum(MatrizEstocastica.loc[: , 'N'+str(indiceValorMaximo+1)]) #Suma los valores de la columna con el indice maximo
    # if sumaColumna == 0:
    #     #Aqui va un input
    #     print('Usted a ingresado en un Dead End')
    #
    #     MatrizEstocasticaNumpy[:,indiceValorMaximo] = np.ones(tamanoMatriz)*1/tamanoMatriz
    #     print('Nueva Matriz Estocastica: ')
    #     print(MatrizEstocasticaNumpy)
