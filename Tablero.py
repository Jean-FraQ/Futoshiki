""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"IMPORTACIONES"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
from random import randint
from tkinter import*
from tkinter import messagebox 
import pickle
import subprocess

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_FUNCIONES_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def inicio ():
    #Crea la vantana principal
    global Vent
    Vent = Tk()

    global alternar
    #Creación del frame inicial
    Fr = Frame(Vent)
    Fr.pack(anchor = 'center')
    Fr.config(bg = "#B3FFB3")

    #Creación de los radiobuttons de seleccion de valor
    valor = IntVar()

    
    Gridselect = Frame(Fr)
    Gridselect.config(bg = "#B3FFB3")
    Gridselect.grid(row = 1, column = 2)
    
    global lista_de_selectores
    lista_de_selectores = []
    
    colocar_1 = Radiobutton(Gridselect, text="1", variable = valor, value = 1, indicatoron = False,width="5",height="2",font=("Times New Roman",14))
    colocar_1.grid(row=0, column =0)
    lista_de_selectores.append(colocar_1)
    
    colocar_2 = Radiobutton(Gridselect, text="2", variable = valor, value = 2, indicatoron = False,width="5",height="2",font=("Times New Roman",14))
    colocar_2.grid(row=1, column =0,pady = (20,0))
    lista_de_selectores.append(colocar_2)

    colocar_3 = Radiobutton(Gridselect, text="3", variable = valor, value = 3, indicatoron = False,width="5",height="2",font=("Times New Roman",14))
    colocar_3.grid(row=2, column =0,pady = (20,0))
    lista_de_selectores.append(colocar_3)

    colocar_4 = Radiobutton(Gridselect, text="4", variable = valor, value = 4, indicatoron = False,width="5",height="2",font=("Times New Roman",14))
    colocar_4.grid(row=3, column =0,pady = (20,0))
    lista_de_selectores.append(colocar_4)

    colocar_5 = Radiobutton(Gridselect, text="5", variable = valor, value = 5, indicatoron = False,width="5",height="2",font=("Times New Roman",14))
    colocar_5.grid(row=4, column =0,pady = (20,0))
    lista_de_selectores.append(colocar_5)

    Borrar_Número = Radiobutton(Gridselect, text="Borrar", variable = valor, value = 6, indicatoron = False,width="7",height="3")
    Borrar_Número.grid(row=5, column =0,pady = (20,0))
    lista_de_selectores.append(Borrar_Número)

    Gridtablero = LabelFrame(Fr)
    Gridtablero.config(bg = "#B3FFB3")
    Gridtablero.grid(row=1, column=1,padx = 20)

    global tablero
    filaBotones = [] # Guarda grupos de 5 botones
    tablero = [] #Guarda los 5 grupos de 5 botones, creando así la matriz de los botones del tablero    

#Creacion de los botones del tablero
    for fila in range(5):
        
        for columna in range(5):
        
            Boton = Button(Gridtablero,width="5",height="2",font=("Times New Roman",14),text = Datos[fila][columna], command = lambda fila = fila, columna = columna: movimiento(valor.get(),fila,columna))
            filaBotones.append(Boton) #Se une el boton a la fila
                     
        tablero.append(filaBotones) #Se une la fila a la matriz
        filaBotones = []

    grid_fila = 0 #Posicion x inicial de la fila 0
    grid_columna = 0 #Posicion y inicial de la columna 0
    
    #Ordena los botones para crear el tablero
    for fila in range(0,5):
        
        for columna in range(0,5):
            
            tablero[fila][columna].grid(row=grid_fila, column = grid_columna,padx = 5)
            #Desplaza la columna
            grid_columna += 2
        #Restaura la columa y avanza la fila    
        grid_fila += 2
        grid_columna = 0

    # Coloca las restricciones horizontales
    fila_h = 0
    columna_h = 1
    global listor
    listor = []
    
    for fila in range(5):
        filor = []
        for columna in range(4):
            
            rest = Label(Gridtablero, text = restricciones_horizontales[fila][columna],font=("Arial",14),bg = "#B3FFB3")
            rest.grid(row = fila_h,column= columna_h)
            filor += [rest]
            #Desplaza la columna
            columna_h += 2
        #Restaura la columa y avanza la fila
        listor += [filor]
        fila_h += 2
        columna_h = 1

    # Coloca las restricciones verticales
    fila_v = 1
    columna_v = 0
    global listver
    listver = []
    
    for fila in range(4):
        filver = []
        for columna in range(5):

            rest = Label(Gridtablero, text = restricciones_verticales[fila][columna],font=("Arial",14),bg = "#B3FFB3")
            rest.grid(row = fila_v,column= columna_v)
            filver += [rest]
            #Desplaza la columna
            columna_v += 2
        #Restaura la columa y avanza la fila
        listver += [filver]
        fila_v += 2
        columna_v = 0

    BFrame = Frame(Fr)
    BFrame.config(bg = "#B3FFB3")
    BFrame.grid(row = 1,column = 0,padx = (20,0))

    Iniciar_partida = Button(BFrame, text="INICIAR JUEGO", width = 21, height = 2, bg = "#55EA3E", state = "disabled", command = lambda:iniciar())
    Iniciar_partida.grid(row = 0, column = 0, columnspan = 2,pady =(0,10))
    Iniciar_partida.config(font=("Times New Roman",14) )

    Borrar_jugada = Button(BFrame, text ="BORRAR\nJUGADA", width = 10, height = 4, bg = "#2CD29E",command = lambda:Borrar())
    Borrar_jugada.grid(row = 1 ,column = 0 ,padx = (0,20) ,pady = 20)
    Borrar_jugada.config(font=("Times New Roman",14) )

    Rehacer_jugada = Button(BFrame, text ="REHACER\nJUGADA", width = 10, height = 4, bg = "#2CD29E",command = lambda:Rehacer())
    Rehacer_jugada.grid(row = 1, column = 1)
    Rehacer_jugada.config(font=("Times New Roman",14) )

    Terminar_partida = Button(BFrame, text ="TERMINAR\nPARTIDA", width = 10, height = 4, bg = "#CD0E0E",command = lambda:Terminar())
    Terminar_partida.grid(row = 2, column = 0,padx = (0,20),pady = 20)
    Terminar_partida.config(font=("Times New Roman",14) )

    Borrar_juego = Button(BFrame, text ="BORRAR\nJUEGO", width = 10, height = 4, bg = "#FFFC00",command = lambda:Borrar_partida ())
    Borrar_juego.grid(row = 2, column = 1)
    Borrar_juego.config(font=("Times New Roman",14) )

    Top_10 = Button(BFrame, text="TOP 10", width = 10, bg = "#FF005F", command = lambda:print("H"))
    Top_10.grid(row = 3, column = 0, columnspan = 2,pady = (10,0))
    Top_10.config(font=("Times New Roman",14) )

    BFrame_GyC = Frame(Fr)
    BFrame_GyC.grid(row = 2, column = 1, columnspan = 2, pady = 30)

    Guardar_juego = Button(BFrame_GyC, text ="GUARDAR JUEGO", width = 20, command = lambda: Guardar())
    Guardar_juego.grid(row = 0, column = 0)
    Guardar_juego.config(font=("Times New Roman",14) )

    Cargar_juego = Button(BFrame_GyC, text ="CARGAR JUEGO", width = 20,state = 'disabled', command = lambda: Cargar())
    Cargar_juego.grid(row = 0, column = 1)
    Cargar_juego.config(font=("Times New Roman",14) )

    Ayuda = Button(Fr, text ="Ayuda", width = 10,command = lambda: M_U())
    Ayuda.grid(row = 0, column = 2,pady = (0,20))
    Ayuda.config(font=("Times New Roman",14) )

    guardar_cargar = Frame(Fr)

    alternar +=[Iniciar_partida,
                Borrar_jugada,
                Rehacer_jugada,
                Terminar_partida,
                Borrar_juego,
                Guardar_juego,
                Cargar_juego]

    alternar_botones()
    apagar_tablero()

    Vent.mainloop()

    

#--------------------------------------------------------------------------------------------------------------

def iniciar():

    global Partida
    global Lista_jugadas
    global Datos
    global Datos_iniciales
    global tablero
    global rest_hor
    global rest_ver
    global Horizontal
    global Vertical

    if Partida == ((('','','','',''),('','','','',''),('','','','',''),('','','','',''),('','','','','')),
            (('  ','  ','  ','  '),('','','',''),('','','',''),('','','',''),('','','','')),
            (('','','','',''),('','','','',''),('','','','',''),('','','','',''))):

        with open("Futoshiki2021partidas.dat","br") as Guardadas:
            partidas = pickle.load(Guardadas)
            
                
        nivel = randint(0,2)
        partida = randint(0,(len(partidas)-1))

        Partida = partidas[nivel][partida]
##        print(Partida)
##
##        print("Tablero:")
##        for fila in Partida[0]:
##            print(fila)
##        print("Horizontales:")
##        for fila in Partida[1]:
##            print(fila)
##        print("Verticales:")
##        for fila in Partida[2]:
##            print(fila)

        Datos_iniciales = Partida[0]

        restricciones_horizontales = Partida[1]

        restricciones_verticales = Partida[2]

        Datos = []
        for fila in Datos_iniciales:
            fila = list(fila)
            Datos += [fila]

        rest_hor = determinar_restricciones(restricciones_horizontales)
        rest_ver = determinar_restricciones(restricciones_verticales)
        
        Lista_jugadas = []
        Lista_borradas = []  

        actualizar_tablero ()
        cargar_restricciones (restricciones_horizontales,restricciones_verticales)
    else:
        
        alternar_botones()
        encender_tablero()
    
#--------------------------------------------------------------------------------------------------------------

#Realizacion de una jugadaa
def movimiento(valor,fila,columna):

    global Lista_jugadas
    global Lista_borradas
    
    #valida la jugada
    Error = validar(valor,fila,columna)
    if Error:
        messagebox.showinfo("Jugada no válida", Error)
        return

    else:
        if valor == 6:
            valor = ""
            Datos[fila][columna] = valor
        else:
            pass
        Datos[fila][columna] = str(valor)
        Lista_jugadas += [(valor,fila,columna)]
        Lista_borradas = []
        actualizar_tablero()
##        print(Lista_jugadas,"\n",Lista_borradas)
##        print(Datos)

        completado = True

        for fila in Datos:
            for casilla in fila:
                if casilla == "":
                    completado = False
                    break

        if completado:
            messagebox.showinfo(title="Victoria!", message="Felcidades!\nJuego Completado!")
            Terminar(True)
        return

#Ejecuta todas las restricciones y retorna el mensaje apropiado
def validar (valor,fila,columna):

    global Datos
    global Datos_iniciales
    global rest_hor
    global rest_ver
   
    #Bandera para controlar errores
    Error = False
    
    if valor == 6:
        if rest_fijo(fila,columna,Datos_iniciales) == True:
            Error = 'El valor de la casilla es fijo'
            return Error
        else:
            return Error


    if rest_fila(valor,fila,columna,Datos) == True: # movimiento((4,1,1),Datos,Datos_iniciales,rest_hor,rest_ver)
         Error = 'Elemento ya en la fila'
         
    if rest_columna(valor,fila,columna,Datos) == True: # movimiento((4,0,0),Datos,Datos_iniciales,rest_hor,rest_ver)
         Error = 'Elemento ya en la columna'
         
    #Estado de las restriccions horizontales     
    hor = rest_horizontal(valor,fila,columna,Datos,rest_hor)
    #Estado de las restriccions horizontales
    ver = rest_vertical(valor,fila,columna,Datos,rest_ver)

##    print(hor,ver)
    
    if hor == 3 or ver == 3: # movimiento((5,1,1),Datos,Datos_iniciales,rest_hor,rest_ver)
         Error = 'No se cumplió la restriccion de mayor'

    if hor == 4 or ver == 4: # movimiento((5,1,2),Datos,Datos_iniciales,rest_hor,rest_ver)
         Error = 'No se cumplió la restriccion de menor'

    if hor == 6 or ver == 6:
         Error = 'El 1 no puede ser el mayor de una desigualdad'
         
    if ver == 7 or hor == 7:
         Error = 'El 5 no puede ser el menor de una desigualdad'
         
    if rest_fijo(fila,columna,Datos_iniciales) == True: # movimiento((4,1,0),Datos,Datos_iniciales,rest_hor,rest_ver)
         Error = 'El valor de la casilla es fijo'
         
    
    return Error # movimiento((3,1,3),Datos,Datos_iniciales,rest_hor,rest_ver)


def rest_fila (valor,fila,columna,Datos):
    #Se revisa la fila
    for Columna in range (5):
        #Omite el valor ya en la casilla
        if Columna == columna:
            continue
        if str(valor) == Datos[fila][Columna]:
            return True
    return 0

def rest_columna (valor,fila,columna,Datos):
    #Se revisa la columna
    for Fila in range (5):
        #Omite el valor ya en la casilla
        if Fila == fila:
            continue
        if str(valor) == Datos[Fila][columna]:
            return True
    return 0

def rest_horizontal (valor,fila,columna,Datos,rest_hor):

    #Revisa las inequidades horizontales
    for símbolo in rest_hor:
        #Mayores en posicion horizontal
        if símbolo[1] == ">":
            #Ver si la jugada coincide con la casilla mayor de la inequidad
            if (fila,columna) == (símbolo[0],símbolo[2]):
                # El 1 no puede ser el mayor
                if valor == 1:
                        return 6
                #Si la otra no está vacía
                if not Datos[símbolo[0]][símbolo[3]]== "":
                    #Compararlas
                    if not int(valor) > int(Datos[símbolo[0]][símbolo[3]]):
                        return 3

            #Ver si la jugada coincide con la casilla menor de la inequidad
            if (fila,columna) == (símbolo[0],símbolo[3]):
                #El 5 no puede ser el menor
                if valor == 5:
                        return 7
                #Si la otra no está vacía
                if not Datos[símbolo[0]][símbolo[2]]== "":
                    #Compararlas
                    if not int(valor) < int(Datos[símbolo[0]][símbolo[2]]):
                        return 3
        #Menores horizontales
        else:
            #Ver si la jugada coincide con la casilla menor de la inequidad
            if (fila,columna) == (símbolo[0],símbolo[2]):
                #El 5 no puede ser el menor
                if valor == 5:
                        return 7
                #Si la otra no está vacía
                if not Datos[símbolo[0]][símbolo[3]]== "":
                    #Compararlas
                    if not int(valor) < int(Datos[símbolo[0]][símbolo[3]]):
                        return 4

            #Ver si la jugada coincide con la casilla mayor de la inequidad
            if (fila,columna) == (símbolo[0],símbolo[3]):
                # El 1 no puede ser el mayor
                if valor == 1:
                        return 6
                #Si la otra no está vacía
                if not Datos[símbolo[0]][símbolo[2]]== "":
                    #Compararlas
                    if not int(valor) > int(Datos[símbolo[0]][símbolo[2]]):
                        return 4
    return 0

def rest_vertical (valor,fila,columna,Datos,rest_ver):
    #Verificar Verticales
    for símbolo in rest_ver:
##        print(símbolo)
        #Mayores en posición vertical
        if símbolo[2] == "v":
            #Ver si la jugada coincide con la casilla mayor de la inequidad
            if (fila,columna) == (símbolo[0],símbolo[3]):
##                print(valor,"A",Datos[símbolo[1]][símbolo[3]])
                # El 1 no puede ser el mayor
                if valor == 1:
                        return 6
                #Si la otra no está vacía
                if not Datos[símbolo[1]][símbolo[3]]== "":
                    #Compararlas
                    if not int(valor) > int(Datos[símbolo[1]][símbolo[3]]):
                        return 3

            #Ver si la jugada coincide con la casilla menor de la inequidad
            if (fila,columna) == (símbolo[1],símbolo[3]):
##                print(Datos[símbolo[1]][símbolo[3]],"B",valor)
                #El 5 no puede ser el menor
                if valor == 5:
                        return 7
                #Si la otra no está vacía
                if not Datos[símbolo[0]][símbolo[3]]== "":
                    #Compararlas
                    if not int(valor) < int(Datos[símbolo[0]][símbolo[3]]):
                        return 3                
        #Menores en posición vertical
        if símbolo[2] == "^":
            #Ver si la jugada coincide con la casilla menor de la inequidad
            if (fila,columna) == (símbolo[0],símbolo[3]):
                #El 5 no puede ser el menor
                if valor == 5:
                        return 7
                #Si la otra no está vacía
                if not Datos[símbolo[1]][símbolo[3]]== "":
                    #Compararlas
                    if not int(valor) < int(Datos[símbolo[1]][símbolo[3]]):
                        return 4

            #Ver si la jugada coincide con la casilla mayor de la inequidad
            if (fila,columna) == (símbolo[1],símbolo[3]):
                # El 1 no puede ser el mayor
                if valor == 1:
                        return 6
                #Si la otra no está vacía
                if not Datos[símbolo[0]][símbolo[3]]== "":
                    #Compararlas
                    if not int(valor) > int(Datos[símbolo[0]][símbolo[3]]):
                        return 4
    return 0

#determina si ya hay un valor fijo en la casilla
def rest_fijo (fila,columna,Datos_iniciales):
    if Datos_iniciales[fila][columna] != '':
        return True
    
    return 0
    
#--------------------------------------------------------------------------------------------------------------------   
    
def Borrar(consecutividad = False):

    global Lista_jugadas
    global Lista_borradas
    global Datos
    global Datos_iniciales
    global tablero

    #Analiza si hay jugadas para borrar
    if Lista_jugadas == []:
        if consecutividad == True:
            return
        else:
            messagebox.showinfo("Borrar Jugada", "No hay jugadas que borrar")
            return
    
    #Si las hay, borra la última    
    else:
        
        Elim = Lista_jugadas.pop()
        Lista_borradas.append(Elim)

        #Deja la casilla en blanco
        Datos[Elim[1]][Elim[2]] = ''
        tablero[Elim[1]][Elim[2]].config(text = '')

        #Revisa la lista de jugadas para determinar si hubo antes otra jugada en esa casilla
        for jugadant in Lista_jugadas:
            #Si encuentra alguna la coloca
            if Elim[1] == jugadant[1] and Elim[2] == jugadant[2]:
                Datos[jugadant[1]][jugadant[2]] = jugadant[0]

        #Tambien cambia el texto de los botones
        actualizar_tablero()
    
    print('Jugadas',Lista_jugadas)
    print('Borradas',Lista_borradas)
##    print("\n","\n",Datos,"\n","\n")
    return

def Rehacer():

    global Lista_jugadas
    global Lista_borradas
    global Datos
    global tablero

    if Lista_borradas == []:
        messagebox.showinfo("Rehacer Jugada", "No hay jugadas que rehacer")
        return

    else:
        Reh = Lista_borradas.pop()
        Lista_jugadas.append(Reh)

        Datos[Reh[1]][Reh[2]] = str(Reh[0])

        actualizar_tablero()

    print('Jugadas',Lista_jugadas)
    print('Borradas',Lista_borradas)
##    print("\n","\n",Datos,"\n","\n")

#----------------------------------------------------------------------------------------------------------------

def Borrar_partida ():

    global Lista_jugadas

    if Lista_jugadas == []:
        messagebox.showinfo("Borrar Partida", "No hay jugadas que borrar")
        return

    advertencia = messagebox.askokcancel(title = "Borrar partida",
                                         message = "¿Está seguro de que desea Borrar toddas las jugadas?",
                                         parent = Vent)

    if not advertencia :
        return

    #Borra todas las jugadas 
    while len (Lista_jugadas) != 0:
        Borrar(True)
   
    return

#----------------------------------------------------------------------------------------------------------------
def Terminar(natural = False):
    #Termina la partida
    global Partida
    global Datos
    global Datos_iniciales
    global restricciones_horizontales
    global restricciones_verticales
    global rest_hor
    global rest_ver
    global Lista_jugadas
    global Lista_borradas
    
    #natural es verdadero si se accedió a la función porque se llenaron todas las casillas del tablero
    #Es falso si se le llama a la función desde el botón de TERMINAR PARTIDA
    if not natural:
        advertencia = messagebox.askokcancel(title = "Terminar partida",
                                            message = "¿Está seguro de que desea TERMINAR el juego? \n se perderán todos los datos no guardados",
                                            parent = Vent)

        if not advertencia :
            return

    Partida = ((('','','','',''),('','','','',''),('','','','',''),('','','','',''),('','','','','')),
               (('  ','  ','  ','  '),('','','',''),('','','',''),('','','',''),('','','','')),
               (('','','','',''),('','','','',''),('','','','',''),('','','','','')))

    #Borra las jugadas y los datos del tablero
    Datos_iniciales = Partida[0]

    restricciones_horizontales = Partida[1]

    restricciones_verticales = Partida[2]

    Datos = []
    for fila in Datos_iniciales:
        fila = list(fila)
        Datos += [fila]

    rest_hor = determinar_restricciones(restricciones_horizontales)

    rest_ver = determinar_restricciones(restricciones_verticales)

    Lista_jugadas = []
    Lista_borradas = []     

    alternar_botones()
    apagar_tablero()

    if not natural:
        actualizar_tablero ()
        cargar_restricciones (restricciones_horizontales,restricciones_verticales)
    

#------------------------------------------------------------------------------------------------------------------
def Guardar():
    #Guarda los datos relevantes en el archivo futoshiki2021juegoactual.dat
    partida_a_guardar  =[Partida,Datos,Lista_jugadas,Lista_borradas]

    almacenamiento = open("futoshiki2021juegoactual.dat","bw")
    pickle.dump(partida_a_guardar,almacenamiento)
    almacenamiento.close


def Cargar():

    global Partida
    global Datos
    global Datos_iniciales
    global restricciones_horizontales
    global restricciones_verticales
    global rest_hor
    global rest_ver
    global Lista_jugadas
    global Lista_borradas
    #Trata de cargar la partida guardada
    try:
        with open("futoshiki2021juegoactual.dat","br") as guardado:
            partida_guardada = pickle.load(guardado)
    #Si no existe notifica al usuario
    except:
        messagebox.showwarning(title="Cargar Partida", message="No tiene ninguna partida guardada")
        return
    
    Partida,Datos,Lista_jugadas,Lista_borradas = partida_guardada

    Datos_iniciales = Partida[0]

    restricciones_horizontales = Partida[1]

    restricciones_verticales = Partida[2]

    rest_hor = determinar_restricciones(restricciones_horizontales)
    rest_ver = determinar_restricciones(restricciones_verticales)
        
    actualizar_tablero ()
    cargar_restricciones (restricciones_horizontales,restricciones_verticales)
#------------------------------------------------------------------------------------------------------------------
def actualizar_tablero():
    #Actualiza el texto de todos ls botones para que calcen con la información en datos
    for fila in range (5):
            for columna in range (5):
               tablero [fila][columna].config(text = Datos[fila][columna])

#------------------------------------------------------------------------------------------------------------------
def desactivar_activar(boton):
    if boton['state'] == 'normal':
            boton['state'] = 'disabled'
    else:
        boton['state'] = 'normal'

#------------------------------------------------------------------------------------------------------------------
def apagar_tablero():
    #Apaga el tablero
    for fila in tablero:
        for boton in fila:
            boton.config(state = "disabled")
    for selector in lista_de_selectores:
        selector.config(state = "disabled")

def encender_tablero():
    #encende el tablero
    for fila in tablero:
        for boton in fila:
                boton['state'] = 'normal'
    for selector in lista_de_selectores:
        selector['state'] = 'normal'
                
#------------------------------------------------------------------------------------------------------------------             
def alternar_botones():
    #Alterna el estado de la mayoría de los botones del programa
    for boton in alternar:
        if boton['state'] == 'normal':
            boton['state'] = 'disabled'
        else:
            boton['state'] = 'normal'

#----------------------------------------------------------------------------------------------------------------
def cargar_restricciones (hori,verti):
    #Actualiza las restricciones horizontales desplegadas en el tablero 
    fila = 0
    for filrest in listor:
        columna = 0
        for restric in filrest:
            restric.config(text = hori[fila][columna])
            columna +=1
        fila += 1
    #Actualiza las restricciones verticales desplegadas en el tablero     
    fila = 0
    for filrest in listver:
        columna = 0
        for restric in filrest:
            restric.config(text = verti[fila][columna])
            columna +=1
        fila += 1

#----------------------------------------------------------------------------------------------------------------------

def determinar_restricciones(tipo_de_restriccion):
    rest = []
    #Crea tuplas con cada restriccion para realizar comparaciones
    for indice_f,fila in enumerate(tipo_de_restriccion):
        for casilla,elemento in enumerate(fila):
            if elemento == "" or elemento == '  ':
                continue
            else:
                if len(tipo_de_restriccion) == 5:
                    restriccion = (indice_f,elemento,casilla,casilla+1)
                else:
                    restriccion = (indice_f,indice_f+1,elemento,casilla)
                rest += [restriccion]
    return rest



#-----------------------------------------------------------------------------------------------------------
def M_U():
    #Despliega el manual de usuario
    ruta = 'Manual de Usuario Futoshiki.pdf'
    subprocess.Popen([ruta],shell = True)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"DATOS DE PRUEBA"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#Carga una partida 
##Partida = ((('','','','',''),('4','','','','2'),('','','4','',''),('','','','','4'),('','','','','')),
##           (('>','','>','>'),('>','','',''),('','','',''),('','','','<'),('<','<','','')),
##           (('','','','',''),('','','^','',''),('','','','',''),('','','','','v',)))

##Partida = ((('','','','',''),('','','','',''),('','','','','3'),('','','','1',''),('5','','','','')),
##               (('  ','  ','  ','  '),('','','',''),('>','','',''),('','','',''),('','','','')),
##               (('v','','','^',''),('','','^','^','^'),('','','','',''),('','^','','','')))

Partida = ((('','','','',''),('','','','',''),('','','','',''),('','','','',''),('','','','','')),
               (('  ','  ','  ','  '),('','','',''),('','','',''),('','','',''),('','','','')),
               (('','','','',''),('','','','',''),('','','','',''),('','','','','')))

##Partida = ((('','','','',''),('4','','','',''),('','','','',''),('','','','',''),('','','','','')),
##          (('','','>',''),('','','',''),('','','',''),('','','',''),('','','','')),
##          (('v','','^','v',''),('','','','','v'),('','','^','','v'),('','','','v','')))

#Establece el estado inicial de los datos           
Datos_iniciales = Partida[0]

restricciones_horizontales = Partida[1]

restricciones_verticales = Partida[2]

Datos = []
for fila in Datos_iniciales:
    fila = list(fila)
    Datos += [fila]

rest_hor = determinar_restricciones(restricciones_horizontales)

rest_ver = determinar_restricciones(restricciones_verticales)

Lista_jugadas = []
Lista_borradas = []

alternar = []       
inicio()
