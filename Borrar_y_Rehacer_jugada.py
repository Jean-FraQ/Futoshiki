""" Esta función es un prototipo, más adelante se le integrarán
elementos de tkinter para que sea compatible con furoshiki.py"""

from tkinter import*



#Datos para la prueba


#Carga una partida 
Partida = ((('','','','',''),('4','','','','2'),('','','4','',''),('','','','','4'),('','','','','')),
           (('>','','>','>'),('>','','',''),('','','',''),('','','','<'),('<','<','','')),
           (('','','','',''),('','','^','',''),('','','','',''),('','','','','v',)))

#Establece el estado inicial de los datos           
Datos_iniciales = Partida[0]

restricciones_horizontales = Partida[1]

restricciones_verticales = Partida[2]


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
print(rest_hor)

rest_ver = determinar_restricciones(restricciones_verticales)
print(rest_ver)




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

print(rest_hor)
print(rest_ver)

Lista_jugadas = [(1,0,2),(2,4,1),(3,0,2)]
global Lista_borradas
Lista_borradas = [(1,4,3),(5,2,4)]

#Funcion para actualizar el tablero según Datos
def actualizar_tablero(botmat,Datos):
    for fila in range (5):
            
            for columna in range (5):
                botmat[fila][columna].config(text = Datos[fila][columna])

def colocar(self,valor): #probando que el radiobutton reciba el valor apropiado
    if valor == 0:
        print("Seleccione un valor válido")
        return

    Lista_borradas = []
    print(valor)
    self.config(text = valor)

def inicio ():
    #Crea la ventana
    
    Vent = Tk()

    #Creación del frame inicial
    Fr = Frame(Vent)
    Fr.pack(anchor = 'center')

    #Creación de los radiobuttons de seleccion de valor
    valor = IntVar()

    Gridselect = LabelFrame(Fr)
    Gridselect.grid(row = 0, column = 1)
    
    colocar_1 = Radiobutton(Gridselect, text="1", variable = valor, value = 1, indicatoron = False,width="7",height="3")
    colocar_1.grid(row=0, column =0,padx = 10)
    
    colocar_2 = Radiobutton(Gridselect, text="2", variable = valor, value = 2, indicatoron = False,width="7",height="3")
    colocar_2.grid(row=1, column =0,padx = 10)

    colocar_3 = Radiobutton(Gridselect, text="3", variable = valor, value = 3, indicatoron = False,width="7",height="3")
    colocar_3.grid(row=2, column =0,padx = 10)

    colocar_4 = Radiobutton(Gridselect, text="4", variable = valor, value = 4, indicatoron = False,width="7",height="3")
    colocar_4.grid(row=3, column =0,padx = 10)

    colocar_5 = Radiobutton(Gridselect, text="5", variable = valor, value = 5, indicatoron = False,width="7",height="3")
    colocar_5.grid(row=4, column =0,padx = 10)

    
    Gridtablero = LabelFrame(Fr)
    Gridtablero.grid(row=0, column=0)

    filaBotones = [] # Guarda grupos de 5 botones
    botmat = [] #Guarda los 5grupos de 5 botones, creando así la matriz de los botones del tablesro    

#Creacion de los botones del tablero
    for fila in range(5):
        
        for columna in range(5):
            
            Boton00 = Button(Gridtablero, width = 7, height = 3,text = Datos[fila][columna], command = lambda fila = fila, columna = columna: colocar(botmat[fila][columna],valor.get()))
            filaBotones.append(Boton00) #Se une el boton a la fila
                     
        botmat.append(filaBotones) #Se une la fila a la matriz
        filaBotones = []

    grid_fila = 0 #Posicion x inicial de la fila 0
    grid_columna = 0 #Posicion y inicial de la columna 0
    
    #Ordena los botones para crear el tablero
    for fila in range(0,5):
        
        for columna in range(0,5):
            
            botmat[fila][columna].grid(row=grid_fila, column =grid_columna)
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

    BFrame = LabelFrame(Fr)
    BFrame.grid(row=1,column=0)

    borrar_jugada = Button(BFrame, text ="BORRAR JUGADA", width = 20, bg = "#2CD29E",command = lambda:Borrar_jugada (Lista_jugadas,Lista_borradas,Datos,Datos_iniciales,botmat))
    borrar_jugada.grid(row=0,column=0)
    borrar_jugada.config(font=("Times New Roman",14) )

    
    rehacer_jugada = Button(BFrame, text ="REHACER JUGADA", width = 20, bg = "#2CD29E",command = lambda:Rehacer_jugada(Lista_jugadas,Lista_borradas,Datos,Datos_iniciales,botmat))
    rehacer_jugada.grid(row=0,column=1)
    rehacer_jugada.config(font=("Times New Roman",14) )

    
    
def Borrar_jugada(Lista_jugadas,Lista_borradas,Datos,Datos_iniciales,botmat):

    #Analiza las lista de jugadas
    if len (Lista_jugadas) == 0:
        #Si no hay jugadas, le notifica al usurio y no hace nada
        print("No quedan movimientos para borrar")
        return
    
    if len (Lista_jugadas) == 1:
        #Si solo hay una jugada, la función se ejecuta
        Elim = Lista_jugadas.pop()
        Lista_borradas.append(Elim)
        
        #pero como no existe un estado anterior, re-establece al estado inicial
        Datos = Datos_iniciales[:]

        actualizar_tablero(botmat,Datos)

        
    #De lo contrario se ejecuta de manera normal    
    else:
        
        Elim = Lista_jugadas.pop()
        Lista_borradas.append(Elim)

        Datos[Elim[1]][Elim[2]] = ''
        botmat[Elim[1]][Elim[2]].config(text = '')
        
        for jugadant in Lista_jugadas:
            if Elim[1] == jugadant[1] and Elim[2] == jugadant[2]:
                Datos[jugadant[1]][jugadant[2]] = jugadant[0]

        

        #Establece al estado anterior

        #Tambien cambia el texto de los botones
        actualizar_tablero(botmat,Datos)

    
    print('Jugadas',Lista_jugadas)
    print('Borradas',Lista_borradas)
    
    
    return Lista_jugadas,Lista_borradas,Datos,botmat

def Rehacer_jugada(Lista_jugadas,Lista_borradas,Datos,Datos_iniciales,botmat):
    if len(Lista_borradas) == 0:
        return print('No hay movimientos que rehacer')
    else:
        Reh = Lista_borradas.pop()
        Lista_jugadas.append(Reh)

        Datos[Reh[1]][Reh[2]] = Reh[0]

        actualizar_tablero(botmat,Datos)

    print('Jugadas',Lista_jugadas)
    print('Borradas',Lista_borradas)

        
inicio()
            
    
    
