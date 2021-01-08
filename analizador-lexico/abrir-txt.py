from tkinter import *;

raiz = Tk()
raiz.title("Abrir .txt")
raiz.resizable(0,0)
raiz.iconbitmap("icon.ico")

contentFrame = Frame()
contentFrame.pack()
contentFrame.config(bg="red")
contentFrame.config(width="800", height="600")
contentFrame.config(bd=10)
contentFrame.config(relief="sunken")

label1 = Label(contentFrame, text="Contenido del archivo:", font=(18))
label1.place(x=1, y=1);

f = open("example.txt", "r")

texto = Text(contentFrame, width=94, height=34)
texto.place(x=2, y=30)

scroll = Scrollbar(contentFrame, command=texto.yview)
scroll.place(x=763, y=30, width=17, height=548)
texto.config(yscrollcommand=scroll.set)

texto.insert(INSERT, f.read())

#contenidoArchivo guarda todo el texto del .txt
contenidoArchivo = str(texto.get("1.0", END))


logsFrame = Frame()
logsFrame.pack(side="top")
logsFrame.config(bg="green")
logsFrame.config(width="800", height="150")
logsFrame.config(bd=10)
logsFrame.config(relief="sunken")

logs = Text(logsFrame, width=94, height=7, bg="black", fg="white")
logs.place(x=2, y=9)

scroll2 = Scrollbar(logsFrame, command=logs.yview)
scroll2.place(x=763, y=9, width=17, height=116)
logs.config(yscrollcommand=scroll2.set)


buttonsFrame = Frame()
buttonsFrame.pack(side="bottom")
buttonsFrame.config(bg="blue")
buttonsFrame.config(width="800", height="50")

# Pasar el valor de contenidoArchivo a la consola con un boton (lineas 54-58)
#def moveText():
#    print(contenidoArchivo)
#   logs.insert(INSERT, contenidoArchivo)
#btnSelectTxt = Button(buttonsFrame, text="Pasar texto a la consola", command=moveText)
#btnSelectTxt.pack()

def selectFile():
    #CODE HERE
    print("hi")

btnSelectTxt = Button(buttonsFrame, text="Seleccionar archivo", command=selectFile)
btnSelectTxt.pack()

btnAnalize = Button(buttonsFrame, text="Analizar texto")
btnAnalize.pack()


raiz.mainloop()