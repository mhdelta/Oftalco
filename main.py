
import tkinter as tk
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk
from facts import *
from proyecto_progra import *



# #//////////////////////////             GUI             //////////////////////////

globcount = -1 # El contador va a recorrer la lista de sintomas, sin embargo el ultimo termino es ' ', por lo que empezar desde alli permite el truco de : "presione enter para inciar"

global lista_sintomas #Declarar una variable global, la variable va a almacenar la lista de sintomas
lista_sintomas = []

for x in sintoma(X):  			# Creacion de la lista con todos los posibles sintomas, 40 en total
  lista_sintomas.append(x[0])
lista_sintomas.append(' ')

def posicionar(frame):					#Funcion [ara que todas las Frames salgan en el centro de la pantalla
    w = 600 # width for the Tk root
    h = 200 # height for the Tk root

    # get screen width and height
    ws = frame.winfo_screenwidth() # width of the screen
    hs = frame.winfo_screenheight() # height of the screen

    # calculate x and y coordinates for the Tk frame window
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    # set the dimensions of the screen 
    # and where it is placed
    frame.geometry('%dx%d+%d+%d' % (w, h, x, y))
    frame.mainloop()


def regresar(frame):	#Funcion para destruir la ventana actual y regresar a la ventana root
    frame.destroy()
    root.deiconify()

def update_the_label(label, entry, frame):	#Funcion que permite mostrar los sintomas y recibir la entrada del usuario, esta localizada en la ventana diagnostico
    entry.focus_set()
    global globcount
    global lista_sintomas
    label.configure(text = lista_sintomas[globcount+1]) #Actualiza el texto de label

    verificar(lista_sintomas[globcount], entry.get()) 

    print("Sintomas ya reconocidos:", yes(X))
    progreso = ((globcount+2)/40)*100

    print("\nProbabilidad de encontrar la enfermedad en la siguiente iteracion: ", progreso, "% ")  
    print("*"*int(progreso))
    if(len_(enfermedad(X))>0):
        print("..DONE..")
        globcount = -1
        progreso = 0
        enfermedad_found(frame)
        return 0

    globcount = globcount + 1
    entry.delete(0,tk.END)

def enfermedad_found(frame):       #Ventana creada al momento de satisfacer una de las reglas para las enfermedades archivo facts.py
    frame.destroy()
    last_window = tk.Tk()

    texto1 = tk.Label(last_window, text = "...Posible enfermedad encontrada...!\n", font = "Courier10Pitch")
    texto1.pack()
    
    texto2 = tk.Label(last_window, text = enfermedad(Enfermedad), font = "Courier10Pitch")
    texto2.pack()
    
    b1 = tk.Button(last_window, text="REGRESAR", command =lambda:regresar(last_window) ,font = "Courier10Pitch")
    b1.pack()
    posicionar(last_window)

def acerca_de_nosotros():
    root.withdraw()
    ventana = tk.Tk()

    mensaje = tk.Message(ventana, text="Integrantes del grupo:\n\n* Juliana Pineda\n* Miguel Angel Henao\n* Cristian Andres Arce\n\n Proyecto completo: www.github.com/mhdelta/Oftalco" , font = "Courier10Pitch")
    mensaje.pack()
    b1 = tk.Button(ventana, text="REGRESAR", command =lambda:regresar(ventana) ,font = "Courier10Pitch")
    b1.pack()
    posicionar(ventana)

def diagnostico():
    print(chr(27) + "[2J")
    borrar_sintomas(yes)
    root.withdraw()
    diagnostico = tk.Tk()

#MENSAJE
    texto = tk.Label(diagnostico, text = "Presione ENTER para comenzar", font = "Courier10Pitch")
    texto.pack()

#ENTRADA DE TEXTO
    e = tk.Entry(diagnostico)
    e.pack()
#ACCIONAR CON ENTER    
    diagnostico.bind('<Return>', lambda x: update_the_label(texto, e, diagnostico))
#BOTON
    b1 = tk.Button(diagnostico, text="REGRESAR", command =lambda:regresar(diagnostico) ,font = "Courier10Pitch")
    b1.pack()
    
    posicionar(diagnostico)

#=========================================================================================================================================
root = tk.Tk()

photo = Image.open("ojo.jpg")
photo = photo.resize((350, 100), Image.ANTIALIAS) # Redibujar la imagene ahora reducida
photon = ImageTk.PhotoImage(photo)
    
label = tk.Label(image=photon)
label.image = photon # keep a reference!
label.pack()

b1 = tk.Button( text="Diagnostico", command = diagnostico,font = "Courier10Pitch")       #this font probably wont work, change it or install it.
b2 = tk.Button( text="Acerca de nosotros", command=acerca_de_nosotros, font = "Courier10Pitch")

b1.pack()
b2.pack()

posicionar(root)    
#============================================================================================================================================

