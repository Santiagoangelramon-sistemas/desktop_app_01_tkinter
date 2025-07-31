# Se importa la libreria de tkinter con todas sus funciones

from tkinter import *  

#-------------------------------------------------------------
# Funciones de la app
#-------------------------------------------------------------

#
# Ventana principal de la app
#

# Se declara una variable llamada ventana_principal, que adquiere la caracteristicas de un objeto de tipo Tk()

vetana_principal = Tk()

# Titulo de la ventana 
vetana_principal.title("Choripan con Queso")

# Tamaño de la ventana
vetana_principal.geometry("800x500")

# Metodo principal que despliega la ventana en pantalla
vetana_principal.mainloop()