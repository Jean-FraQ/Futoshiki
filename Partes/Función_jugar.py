from tkinter import*

#Creacion de la raiz del programa principal
raiz = Tk()
raiz.title("Futoshiki")

#Creacion del frame que contendrá todos los elementos
Ventana_principal = Frame(raiz)
Ventana_principal.pack(anchor= 'center')

#Datos para la prueba
Datos_iniciales = [['','','','',''],
                  ['4','','','','2'],
                  ['','','4','',''],
                  ['','','','','4'],
                  ['','','','','']]

global Datos
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

#Funcion para actualizar el tablero según Datos
def actualizar_tablero(botmat,Datos):
    for fila in range (5):
            
            for columna in range (5):
                botmat[fila][columna].config(text = Datos[fila][columna],fg = 'black')

#Ddetermina las posibles jugadas para una casilla
def posibles_jugadas(valor,fila,columna,Datos,Datos_iniciales,botmat,rest_hor,rest_ver):

    actualizar_tablero(botmat,Datos)

    #Crea la variable que almacenará las posibles jugada
    posibilidades = ""

    for pos in range (1,6):
        #Evalua todas las restricciones que procesará la función
        valor = pos
        if rest_fila (valor,fila,columna,Datos) == 1 :
            continue
        if rest_columna (valor,fila,columna,Datos) == 2 :
            continue
        if rest_mayor (valor,fila,columna,Datos,rest_hor,rest_ver) in [3,6,7] :
            continue
        if rest_menor (valor,fila,columna,Datos,rest_hor,rest_ver) in [4,6,7] :
            continue
        if rest_fijo (fila,columna,Datos_iniciales) == 5 :
            continue

        # Si el valor llega a este punto es una posible jugada válida
        if len(posibilidades) == 0:  
            posibilidades += str(pos)

        else:
            posibilidades += (','+str(pos))

    #Si no hay jugadas posibles informa al usuario
    if len(posibilidades) == 0:
        return "No hay movimientos para esta casilla"

    #De haberlas, las retorna
    else:
        botmat[fila][columna].config(text = posibilidades, fg = 'green')
        return 
        


    
def rest_fila (valor,fila,columna,Datos):
    #Se revisa la fila
    for Columna in range (5):
        #Omite el valor ya en la casilla
        if Columna == columna:
            continue
        if str(valor) == Datos[fila][Columna]:
            return 1
    return 0

def rest_columna (valor,fila,columna,Datos):
    #Se revisa la columna
    for Fila in range (5):
        #Omite el valor ya en la casilla
        if Fila == fila:
            continue
        if str(valor) == Datos[Fila][columna]:
            return 2
    return 0

def rest_mayor (valor,fila,columna,Datos,rest_hor,rest_ver):

    #Se revisan las inequidades de mayor
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

    for símbolo in rest_ver:
        #Mayores en posición vertical
        if símbolo[2] == "V":
            #Ver si la jugada coincide con la casilla mayor de la inequidad
            if (fila,columna) == (símbolo[0],símbolo[3]):
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
                #El 5 no puede ser el menor
                if valor == 5:
                        return 7
                #Si la otra no está vacía
                if not Datos[símbolo[0]][símbolo[3]]== "":
                    #Compararlas
                    if not int(valor) < int(Datos[símbolo[0]][símbolo[3]]):
                        return 3
    return 0

def rest_menor (valor,fila,columna,Datos,rest_hor,rest_ver):
    #Verificar menores
    for símbolo in rest_hor:
        #Menores horizontales
        if símbolo[1] == "<":
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
                    
    for símbolo in rest_ver:
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
        return 5
    
    return 0


#Ejecuta todas las restricciones y retorna el mensaje apropiado
def validar (valor,fila,columna,Datos,Datos_iniciales,rest_hor,rest_ver):

    if rest_fila(valor,fila,columna,Datos) == 1: # movimiento((4,1,1),Datos,Datos_iniciales,rest_hor,rest_ver)
         print('Elemento ya en la fila')
         return False
    if rest_columna(valor,fila,columna,Datos) == 2: # movimiento((4,0,0),Datos,Datos_iniciales,rest_hor,rest_ver)
         print('Elemento ya en la columna')
         return False
    hor = rest_mayor(valor,fila,columna,Datos,rest_hor,rest_ver)
    if hor == 3: # movimiento((5,1,1),Datos,Datos_iniciales,rest_hor,rest_ver)
         print('No se cumplió restriccion de mayor')
         return False
    ver = rest_menor(valor,fila,columna,Datos,rest_hor,rest_ver)
    if ver == 4: # movimiento((5,1,2),Datos,Datos_iniciales,rest_hor,rest_ver)
         print('No se cumplió restriccion de menor')
         return False
    if rest_fijo(fila,columna,Datos_iniciales) == 5: # movimiento((4,1,0),Datos,Datos_iniciales,rest_hor,rest_ver)
         print('El valor de la casilla es fijo')
         return False
    if hor == 6 or ver == 6:
         print('El 1 no puede ser el mayor de una desigualdad')
         return False
    if ver == 7 or hor == 7:
         print('El 5 no puede ser el menor de una desigualdad')
         return False
    
    return True # movimiento((3,1,3),Datos,Datos_iniciales,rest_hor,rest_ver)


#Simula una jugada aplicada en el juego real  
def movimiento(jugada,Datos,Datos_iniciales,botmat,rest_hor,rest_ver):
    valor,fila,columna = jugada
    #Verifica que la entrada sea válida
    if not 1 <= valor <= 6:
        return 'Valor no válido inserte un valor entre 1 y 6'
    
#'Posibles Jugadas' será un elemento adicional a los radiobutons de selección de valor (6)
    if valor == 6:
        return posibles_jugadas (valor,fila,columna,Datos,Datos_iniciales,botmat,rest_hor,rest_ver)

#valida la jugada
    else:
        if validar(valor,fila,columna,Datos,Datos_iniciales,rest_hor,rest_ver) == True:
             
            Datos[fila][columna] = str(valor)
            actualizar_tablero(botmat,Datos)
            return
        else:
            return
##          if Verificar_tablero(Datos) == True:
##              Top10()
##              if multi == True:
##                  if dificultad_v == 3:
##                      #Terminar_partida
##                  else:
##                      dificultad_v += 1
##                      #importar partida
##              else:
##                  #Terminar_partida
##          else:
##              return
            
         
                        
         
    

def Verificar_tablero(Datos):

    for fila_c in Datos:
        for columna_c in Datos:
            if Datos[fila_c][columna_c] != '':
                continue
            else:
                return False
    return  True

def Pantalla_principal():


    filaBotones = [] # Guarda grupos de 5 botones
    botmat = [] #Guarda los 5grupos de 5 botones, creando así la matriz de los botones del tablesro    
    valor = IntVar()

    gridselect = LabelFrame(Ventana_principal)
    gridselect.grid(row=0,column=1)
    #Los radiobuttons que determinan qué valor reciben los botones del tablero (sí funcionan)(probar con Boton00)
    colocar_1 = Radiobutton(gridselect, text="1", variable = valor, value = 1, indicatoron = False,width="7",height="3")
    colocar_1.grid(row=0,column=0)
    
    colocar_2 = Radiobutton(gridselect, text="2", variable = valor, value = 2, indicatoron = False,width="7",height="3")
    colocar_2.grid(row=1,column=0)

    colocar_3 = Radiobutton(gridselect, text="3", variable = valor, value = 3, indicatoron = False,width="7",height="3")
    colocar_3.grid(row=2,column=0)

    colocar_4 = Radiobutton(gridselect, text="4", variable = valor, value = 4, indicatoron = False,width="7",height="3")
    colocar_4.grid(row=3,column=0)

    colocar_5 = Radiobutton(gridselect, text="5", variable = valor, value = 5, indicatoron = False,width="7",height="3")
    colocar_5.grid(row=4,column=0)

    PJ = Radiobutton(gridselect, text = "Posibles\njugadas",variable = valor, value = 6, indicatoron = False,width="7",height="3")
    PJ.grid(row=5,column=0)

    Gridtablero = LabelFrame(Ventana_principal, text ="Tablero")
    Gridtablero.grid(row=0,column = 0)

    

    #Creacion de los botones del tablero
    for fila in range(5):
        
        for columna in range(5):
            
            Boton00 = Button(Gridtablero, width = 7, height = 3, command = lambda fila = fila, columna = columna: movimiento((valor.get(),fila,columna),Datos,Datos_iniciales,botmat,rest_hor,rest_ver))
            filaBotones.append(Boton00) #Se une el boton a la fila
                     
        botmat.append(filaBotones) #Se une la fila a la matriz
        filaBotones = []

    actualizar_tablero(botmat,Datos)
    
            

    
    """estoy considerando crear un frame sólo para el tablero y así colocar los botones mediante una grid
    de esta manera podría colocar las restricciones de desigualdad como puntos medios entre los botones pero
    aún no desifro cómo"""

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

Pantalla_principal()
raiz.mainloop()

    
