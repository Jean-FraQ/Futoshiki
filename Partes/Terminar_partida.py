"""IMPORTACIONES"""
from tkinter import *
from tkinter import messagebox

#######################################################DATOS##################################################


Datos_iniciales = [['','','','',''],
                  ['4','','','','2'],
                  ['','','4','',''],
                  ['','','','','4'],
                  ['','','','','']]

Datos = [['','','3','',''],
	['4','','','','2'],
	['','','4','',''],
	['','','','','4'],
	['','2','','','']]

Horizontal = [['>','','>','>'],
           ['>','','',''],
           ['','','',''],
           ['','','','<'],
           ['<','<','','']]

Vertical = [['','','','',''],
            ['','','^','',''],
            ['','','','',''],
            ['','','','','V']]

rest_hor = [(0,">",0,1),(0,">",2,3),(0,">",3,4),(1,">",0,1),(3,"<",3,4),(4,"<",0,1),(4,"<",1,2)]

rest_ver = [(1,2,"^",2),(3,4,"V",4)]

Lista_jugadas = [(2,4,1),(3,0,2)]

partida_actual = []

alternar = []

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
            
            rest = Label(Gridtablero, text = Horizontal[fila][columna],font=("Times New Roman",14))
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

            rest = Label(Gridtablero, text = Vertical[fila][columna],font=("Times New Roman",14))
            rest.grid(row = fila_v,column= columna_v)
            #Desplaza la columna
            columna_v += 2
        #Restaura la columa y avanza la fila
        fila_v += 2
        columna_v = 0

    
    Terminar_partida = Button(Fr, text ="TERMINAR PARTIDA", width = 20, bg = "#CD0E0E",command = lambda:Terminar())
    Terminar_partida.grid(row=1,column=0)
    Terminar_partida.config(font=("Times New Roman",14) )
    alternar += [Terminar_partida]

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

    Horizontal = [['','','',''],['','','',''],['','','',''],['','','',''],['','','','',]]
    Verical = [['a','a','a','a','a'],['','','','','',],['','','','',''],['','','','','',]]

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
#--------------------------------------------------------------------------------------------------------------

def desactivar_activar(boton):
    if boton['state'] == 'normal':
            boton['state'] = 'disabled'
    else:
        boton['state'] = 'normal'

    
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
             
def des_activ_partida():
    
    for boton in alternar:
        if boton['state'] == 'normal':
            boton['state'] = 'disabled'
        else:
            boton['state'] = 'normal'

    des_activ_tablero(True)

#def finalizar_parida()
            
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

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""PROGRAMA PRINCIPAL"""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    
inicio()
Vent.mainloop()
 


    
    
    
