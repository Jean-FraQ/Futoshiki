""" Esta función es un prototipo, más adelante se le integrarán
elementos de tkinter para que sea compatible con furoshiki.py"""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"IMPORTACIONES"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
from tkinter import*
from tkinter import messagebox 

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

    #Creación de los radiobuttons de seleccion de valor
    valor = IntVar()

    global lista_de_selectores
    lista_de_selectores = []
    global Gridselectores
    Gridselect = LabelFrame(Fr)
    Gridselect.grid(row = 0, column = 1)
    
    colocar_1 = Radiobutton(Gridselect, text="1", variable = valor, value = 1, indicatoron = False,width="7",height="3")
    colocar_1.grid(row=0, column =0,pady = 5)
    lista_de_selectores.append(colocar_1)
    
    colocar_2 = Radiobutton(Gridselect, text="2", variable = valor, value = 2, indicatoron = False,width="7",height="3")
    colocar_2.grid(row=1, column =0,pady = 20)
    lista_de_selectores.append(colocar_2)

    colocar_3 = Radiobutton(Gridselect, text="3", variable = valor, value = 3, indicatoron = False,width="7",height="3")
    colocar_3.grid(row=2, column =0,pady = 5, padx = 5)
    lista_de_selectores.append(colocar_3)

    colocar_4 = Radiobutton(Gridselect, text="4", variable = valor, value = 4, indicatoron = False,width="7",height="3")
    colocar_4.grid(row=3, column =0,pady = 20)
    lista_de_selectores.append(colocar_4)

    colocar_5 = Radiobutton(Gridselect, text="5", variable = valor, value = 5, indicatoron = False,width="7",height="3")
    colocar_5.grid(row=4, column =0,pady = 5)
    lista_de_selectores.append(colocar_5)

    Borrar_Número = Radiobutton(Gridselect, text="Borrar", variable = valor, value = 6, indicatoron = False,width="7",height="3")
    Borrar_Número.grid(row=5, column =0,pady = 5)
    lista_de_selectores.append(Borrar_Número)

    global Gridtablero
    Gridtablero = LabelFrame(Fr)
    Gridtablero.grid(row=0, column=0)

    global tablero
    filaBotones = [] # Guarda grupos de 5 botones
    tablero = [] #Guarda los 5 grupos de 5 botones, creando así la matriz de los botones del tablero    

#Creacion de los botones del tablero
    for fila in range(5):
        
        for columna in range(5):
        
            Boton = Button(Gridtablero, width = 7, height = 3,text = Datos[fila][columna], command = lambda fila = fila, columna = columna: colocar(tablero[fila][columna],valor.get()))
            filaBotones.append(Boton) #Se une el boton a la fila
                     
        tablero.append(filaBotones) #Se une la fila a la matriz
        filaBotones = []

    grid_fila = 0 #Posicion x inicial de la fila 0
    grid_columna = 0 #Posicion y inicial de la columna 0
    
    #Ordena los botones para crear el tablero
    for fila in range(0,5):
        
        for columna in range(0,5):
            
            tablero[fila][columna].grid(row=grid_fila, column = grid_columna)
            #Desplaza la columna
            grid_columna += 2
        #Restaura la columa y avanza la fila    
        grid_fila += 2
        grid_columna = 0


    # Coloca las restricciones horizontales
    fila_h = 0
    columna_h = 1
    
    for fila in range(5):

        for columna in range(4):
            
            rest = Label(Gridtablero, text = restricciones_horizontales[fila][columna],font=("Times New Roman",14))
            rest.grid(row = fila_h,column= columna_h)
            #Desplaza la columna
            columna_h += 2
        #Restaura la columa y avanza la fila
        fila_h += 2
        columna_h = 1

    # Coloca las restricciones verticales
    fila_v = 1
    columna_v = 0
    
    for fila in range(4):

        for columna in range(5):

            rest = Label(Gridtablero, text = restricciones_verticales[fila][columna],font=("Times New Roman",14))
            rest.grid(row = fila_v,column= columna_v)
            #Desplaza la columna
            columna_v += 2
        #Restaura la columa y avanza la fila
        fila_v += 2
        columna_v = 0

    BFrame = LabelFrame(Fr)
    BFrame.grid(row = 1,column = 0)

    Borrar_jugada = Button(BFrame, text ="BORRAR JUGADA", width = 20, bg = "#2CD29E",command = lambda:Borrar())
    Borrar_jugada.grid(row= 0 ,column= 0 )
    Borrar_jugada.config(font=("Times New Roman",14) )

    Rehacer_jugada = Button(BFrame, text ="REHACER JUGADA", width = 20, bg = "#2CD29E",command = lambda:Rehacer())
    Rehacer_jugada.grid(row = 0, column = 1)
    Rehacer_jugada.config(font=("Times New Roman",14) )

    Terminar_partida = Button(BFrame, text ="TERMINAR PARTIDA", width = 20, bg = "#CD0E0E",command = lambda:Terminar())
    Terminar_partida.grid(row = 1,column = 0)
    Terminar_partida.config(font=("Times New Roman",14) )

    Borrar_juego = Button(BFrame, text ="BORRAR JUEGO", width = 20, bg = "#FFFC00",command = lambda:Borrar_partida ())
    Borrar_juego.grid(row=1,column=1)
    Borrar_juego.config(font=("Times New Roman",14) )

    alternar +=[Borrar_jugada,Rehacer_jugada,Terminar_partida]

 #--------------------------------------------------------------------------------------------------------------------   
    
def Borrar():

    global Lista_jugadas
    global Lista_borradas
    global Datos
    global Datos_iniciales
    global tablero

    #Analiza si hay jugadas para borrar
    if len (Lista_jugadas) == 0:
        #Si no hay jugadas, le notifica al usurio y no hace nada
        print("No quedan movimientos para borrar")
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
    print("\n","\n",Datos,"\n","\n")
    return

def Rehacer():

    global Lista_jugadas
    global Lista_borradas
    global Datos
    global tablero

    if len(Lista_borradas) == 0:
        return print('No hay movimientos que rehacer')
    else:
        Reh = Lista_borradas.pop()
        Lista_jugadas.append(Reh)

        Datos[Reh[1]][Reh[2]] = Reh[0]

        actualizar_tablero()

    print('Jugadas',Lista_jugadas)
    print('Borradas',Lista_borradas)
    print("\n","\n",Datos,"\n","\n")

#----------------------------------------------------------------------------------------------------------------

def Borrar_partida ():

    global Lista_jugadas

    advertencia = messagebox.askokcancel(title = "Borrar partida",
                                         message = "¿Está seguro de que desea Borrar toddas las jugadas?",
                                         parent = Vent)

    if not advertencia :
        return

    #Borra todas las jugadas 
    while len (Lista_jugadas) != 0:
        Borrar()
   
    return

#----------------------------------------------------------------------------------------------------------------
def Terminar():
    global Lista_jugadas
    global Datos
    global Datos_iniciales
    global tablero
    global rest_hor
    global rest_ver
    global Horizontal
    global Vertical

    advertencia = messagebox.askokcancel(title = "Terminar partida",
                                         message = "¿Está seguro de que desea TERMINAR el juego? \n se perderán todos los datos no guardados",
                                         parent = Vent)

    if not advertencia :
        return

    #Borra las jugadas y los datos del tablero
    Lista_jugadas = []
    Datos = []
    Datos_iniciales = []

    restricciones_horizontales = []
    restricciones_verticales = []

    #Desactiva el tablero
    des_activ_partida()
            

     # Coloca las restricciones horizontales
    fila_h = 0
    columna_h = 1
    
    for fila in range(5):

        for columna in range(4):
            
            rest = Label(Gridtablero, text = ' ' ,font=("Times New Roman",14))
            rest.grid(row = fila_h,column= columna_h)
            #Desplaza la columna
            columna_h += 2
        #Restaura la columa y avanza la fila
        fila_h += 2
        columna_h = 1

    # Coloca las restricciones verticales
    fila_v = 1
    columna_v = 0
    
    for fila in range(4):

        for columna in range(5):

            rest = Label(Gridtablero, text = ' ',font=("Times New Roman",14))
            rest.grid(row = fila_v,column= columna_v)
            #Desplaza la columna
            columna_v += 2
        #Restaura la columa y avanza la fila
        fila_v += 2
        columna_v = 0
#------------------------------------------------------------------------------------------------------------------
#Funcion para actualizar el tablero según Datos
def actualizar_tablero():

    global tablero
    global Datos

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
def des_activ_tablero(fin = False):
    if fin:
        for fila in tablero:
            for boton in fila:
                boton.config(state = "disabled", text = "")
        for selector in lista_de_selectores:
            selector.config(state = "disabled")
            
    else:    
        for fila in tablero:
            for boton in fila:
                if boton['state'] == 'normal':
                        boton['state'] = 'disabled'
                else:
                    boton['state'] = 'normal'

        for selector in lista_de_selectores:
            if selector['state'] == 'normal':
                selector['state'] = 'disabled'
            else:
                selector['state'] = 'normal'
#------------------------------------------------------------------------------------------------------------------             
def des_activ_partida():
    
    for boton in alternar:
        if boton['state'] == 'normal':
            boton['state'] = 'disabled'
        else:
            boton['state'] = 'normal'

    des_activ_tablero(True)
#--------------------------------------------------------------------------------------------------------------
def colocar(self,valor): #probando que el radiobutton reciba el valor apropiado
    if valor == 0:
        print("Seleccione un valor válido")
        return
    
    if valor == 6:
        print("Valor Borrado")
        self.config(text = "")
        return
    
    print(valor)
    self.config(text = valor)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"DATOS DE PRUEBA"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"_"""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#Carga una partida 
Partida = ((('','','','',''),('4','','','','2'),('','','4','',''),('','','','','4'),('','','','','')),
           (('>','','>','>'),('>','','',''),('','','',''),('','','','<'),('<','<','','')),
           (('','','','',''),('','','^','',''),('','','','',''),('','','','','v',)))

#Establece el estado inicial de los datos           
Datos_iniciales = Partida[0]

restricciones_horizontales = Partida[1]

restricciones_verticales = Partida[2]

Datos = []
for fila in Datos_iniciales:
    fila = list(fila)
    Datos += [fila]

def determinar_restricciones(tipo_de_restriccion):
    rest = []
    #Crea tuplas con cada restriccion para realizar comparaciones
    for indice_f,fila in enumerate(tipo_de_restriccion):
        for casilla,elemento in enumerate(fila):
            if elemento == "":
                continue
            else:
                if len(tipo_de_restriccion) == 5:
                    restriccion = (indice_f,elemento,casilla,casilla+1)
                else:
                    restriccion = (indice_f,indice_f+1,elemento,casilla)
                rest += [restriccion]
    return rest

rest_hor = determinar_restricciones(restricciones_horizontales)

rest_ver = determinar_restricciones(restricciones_verticales)

Lista_jugadas = [(1,0,2),(2,4,1),(3,0,2)]

Lista_borradas = [(1,4,3),(5,2,4)]

alternar = []       
inicio()
            
    
    
