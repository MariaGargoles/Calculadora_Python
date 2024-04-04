# Importamos el módulo tkinter para la creación de la interfaz gráfica
from tkinter import *

# Definimos la ventana
ventana = Tk()
ventana.title("Mi calculadora")
ventana.geometry("300x400")
ventana.minsize(300,400)
ventana.maxsize(300,400)

# Definimos una función para insertar un número en el cuadro de texto
def setNumero(numero):
    txt.insert(END, str(numero))

# Definimos una función para insertar un punto decimal en el cuadro de texto
def setDecimal():
    txt.insert(END, ".")

#Definimos una función para limpiar el contenido del cuadro de texto
def clear():
    txt.delete(0, END)

# Definimos una función para evaluar la expresión matemática y mostrar el resultado
def calcular():
    try:
        resultado = eval(txt.get())
        txt.delete(0, END)
        txt.insert(END, str(resultado))
    except:
        txt.delete(0, END)
        txt.insert(END, "Error")

# Entry
txt = Entry(ventana)
txt.grid(row=0, column=0, columnspan=4)
txt.config(width=15, font=('Arial', 20))

# Pondremos un bucle para crear los botones de los números
numero = 1
for fila in range(1, 4):
    for columna in range(3):
        btn = Button(ventana, text=str(numero), command=lambda num=numero: setNumero(num))
        btn.grid(row=fila, column=columna)
        btn.config(width=6, height=3, font=('Arial', 12))
        numero += 1

# Botón de "0"
btn = Button(ventana, text="0", command=lambda: setNumero(0))
btn.grid(row=4, column=1)
btn.config(width=6, height=3, font=('Arial', 12))

# Botón de punto decimal
btn_decimal = Button(ventana, text=".", command=setDecimal)
btn_decimal.grid(row=4, column=0)
btn_decimal.config(width=6, height=3, font=('Arial', 12))

# Botones de operaciones
operadores = ["+", "-", "*", "/"]
for i, operador in enumerate(operadores):
    btn = Button(ventana, text=operador, command=lambda op=operador: setNumero(op))
    btn.grid(row=i+1, column=3)
    btn.config(width=6, height=3, font=('Arial', 12))

# Botón de "C"
btn_clear = Button(ventana, text="C", command=clear)
btn_clear.grid(row=4, column=2)
btn_clear.config(width=6, height=3, font=('Arial', 12))


# Botón de "="
btn_igual = Button(ventana, text="=", command=calcular)
btn_igual.grid(row=4, column=3)
btn_igual.config(width=6, height=3, font=('Arial', 12))


ventana.mainloop()
