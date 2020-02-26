import tkinter as tk
from tkinter import ttk

def funcion_click():
    ventana2=tk.Tk()
    ventana2.title("resultados")
    ventana2.geometry("200x200")
    etiqueta3=ttk.Label(ventana2,text="lo sentimos pero no se termino el programa :'(")
   
    etiqueta3.grid(column=0,row=0)

ventana= tk.Tk()
ventana.title("Examen")
ventana.geometry("1000x500")
# pregunta 1
etiqueta=ttk.Label(ventana,text='1.Que dice el articulo 4?')
etiqueta.grid(column=0,row=0)
respuesta1 = tk.StringVar()
entrada= ttk.Entry(ventana, width = 12, textvariable=respuesta1)
respuesta1=entrada
entrada.grid(column=1,row=0)


#pregunta 2
etiqueta2=ttk.Label(ventana,text="2.Que es ley?")
etiqueta2.grid(column=0,row=1)
respuesta2 = tk.StringVar()
entrada2= ttk.Entry(ventana, width = 12, textvariable=respuesta2)
respuesta2=entrada2
entrada2.grid(column=1,row=1)

#RadioButtons
#pregunta 3
ttk.Label(ventana, text= "algo al cual tienes acceso desde que naces"). grid(column=0, row=2)
opcion = tk.IntVar()
aux = opcion.get()  
radio1 = tk.Radiobutton(ventana, text= "derecho", variable= opcion, value=1)
radio1.grid(column=0,row=3)
radio2 = tk.Radiobutton(ventana, text= "comodidad", variable= opcion, value=2)
radio2.grid(column=1,row=3)
radio3 = tk.Radiobutton(ventana, text= "dinero", variable= opcion, value=3)
radio3.grid(column=2,row=3)
radio4 = tk.Radiobutton(ventana, text= "familia", variable= opcion, value=4)
radio4.grid(column=3,row=3)
radio5 = tk.Radiobutton(ventana, text= "amigos", variable= opcion, value=5)
radio5.grid(column=4,row=3)

#pregunta 4
#RadioButtons
ttk.Label(ventana, text= "Regla la cual debes de seguir puesta por el gobierno"). grid(column=0, row=4)
opcion = tk.IntVar()
aux = opcion.get()  
radio1 = tk.Radiobutton(ventana, text= "decreto", variable= opcion, value=1)
radio1.grid(column=0,row=5)
radio2 = tk.Radiobutton(ventana, text= "ley", variable= opcion, value=2)
radio2.grid(column=1,row=5)
radio3 = tk.Radiobutton(ventana, text= "legislacion", variable= opcion, value=3)
radio3.grid(column=2,row=5)
radio4 = tk.Radiobutton(ventana, text= "ayuda", variable= opcion, value=4)
radio4.grid(column=3,row=5)
radio5 = tk.Radiobutton(ventana, text= "derecho", variable= opcion, value=5)
radio5.grid(column=4,row=5)

#pregunta 3
ttk.Label(ventana, text= "que articulo habla sobre el derecho de los niños"). grid(column=1, row=7)
var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()
var4 = tk.IntVar()
var5 = tk.IntVar()
chk = tk.Checkbutton(ventana, text="Art 3", variable=var1)
chk.grid(column=0, row=8)
chk2 = tk.Checkbutton(ventana, text="Art 4", variable=var2)
chk2.grid(column=1,row=8)
chk3 = tk.Checkbutton(ventana, text="Art 14", variable=var3)
chk3.grid(column=2,row=8)
chk4 = tk.Checkbutton(ventana, text="Art 15", variable=var4)
chk4.grid(column=3,row=8)
chk5 = tk.Checkbutton(ventana, text="Art 27", variable=var5)
chk5.grid(column=4,row=8)

accion2=ttk.Button(ventana,text="Registrar", command=funcion_click)
accion2.grid(column=1, row=18)
ventana.mainloop()

