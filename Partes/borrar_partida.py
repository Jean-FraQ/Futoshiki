from tkinter import*

Vent = Tk()

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

def colocar(self,valor): #probando que el radiobutton reciba el valor apropiado
    if valor == 0:
        print("Seleccione un valor válido")
    
    print(valor)
    self.config(text = valor)

def inicio ():

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
    for fila in range(5):
        
        for columna in range(5):
            
            botmat[fila][columna].grid(row=grid_fila, column =grid_columna)
            grid_columna += 2
#,padx=10,pady=10   
        grid_fila += 2
        grid_columna = 0 #Reinicio la posicion de las filas para que vayan en linea con los botones generados

    fila_h = 0
    columna_h = 1
    
    for fila in range(5):

        for columna in range(4):

            rest = Label(Gridtablero, text = Horizontal[fila][columna],font=("Times New Roman",14))
            rest.grid(row = fila_h,column= columna_h)
            columna_h += 2

        fila_h += 2
        columna_h = 1

    fila_v = 1
    columna_v = 0
    
    for fila in range(4):

        for columna in range(5):

            rest = Label(Gridtablero, text = Vertical[fila][columna],font=("Times New Roman",14))
            rest.grid(row = fila_v,column= columna_v)
            columna_v += 2

        fila_v += 2
        columna_v = 0


    grid_fila = 0 #Posicion x inicial de la fila 0
    grid_columna = 0 #Posicion y inicial de la columna 0
    
    #Ordena los botones para crear el tablero
    for fila in range(0,5):
        
        for columna in range(0,5):
            
            botmat[fila][columna].grid(row=grid_fila, column =grid_columna)
            grid_columna += 2
            
        grid_fila += 2
        grid_columna = 0
        
    borrar_juego = Button(Fr, text ="BORRAR JUEGO", width = 20, bg = "#FFFC00",command = lambda:Borrar_juego (Lista_jugadas,Datos_iniciales,Datos,botmat))
    borrar_juego.grid(row=1,column=0)
    borrar_juego.config(font=("Times New Roman",14) )




def Borrar (Lista_jugadas,Datos_iniciales,Datos,botmat,advertencia):
    #Limpia todas la jugadas
    Lista_jugadas = []
    #Re-establece la matriz al estado inicial
    Datos = Datos_iniciales [:]

    #Cambia el texto de todos los botones para reflejar el estado inicial de la matriz
    for fila in range(0,5):
        for columna in range(0,5):
            botmat[fila][columna].config(text = Datos_iniciales[fila][columna])

    #Destruye la ventana de advertencia
    advertencia.destroy()
    return Lista_jugadas,Datos,botmat

def Borrar_juego (Lista_jugadas,Datos_iniciales,Datos,botmat):

    #Se crea la ventana de advertencia
    advertencia = Tk()
    advertencia.geometry("330x120")
    advertencia.resizable(False,False)
    advertencia.title("Borrar partida")

    #Label para recordarle al usuario lo que va a hacer
    Label(advertencia, text="¿Está seguro de que desea borrar la partida? \n perderá todo su progreso.",font=("Times New Roman",12)).place(x=10,y=15)
    #sigue con la función
    si = Button(advertencia, text="si",width=10, command= lambda: Borrar(Lista_jugadas,Datos_iniciales,Datos,botmat,advertencia)).place(x=50,y=80)
    #Destruye la ventana y no ejecuta ningun cambio
    no = Button(advertencia, text="no", width=10, command= advertencia.destroy).place(x= 200, y = 80)

inicio()
Vent.mainloop()
    

  


    
    
    
    
