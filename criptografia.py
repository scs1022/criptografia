import tkinter as tk
from tkinter import ttk

# Funciones de encriptado y desencriptado
def encriptar_cesar(texto, n):
    alfabeto = 'abcdefghijklmnopqrstuvwxyzñ'
    resultado = ''
    for char in texto.lower():
        if char in alfabeto:
            nuevo_indice = (alfabeto.index(char) + n) % 27
            resultado += alfabeto[nuevo_indice]
        else:
            resultado += char
    return resultado

def desencriptar_cesar(texto, n):
    alfabeto = 'abcdefghijklmnopqrstuvwxyzñ'
    resultado = ''
    for char in texto.lower():
        if char in alfabeto:
            nuevo_indice = (alfabeto.index(char) - n) % 27
            resultado += alfabeto[nuevo_indice]
        else:
            resultado += char
    return resultado

# Funciones para los botones
def encriptar_texto():
    texto = texto_entry.get("1.0", tk.END).strip()
    try:
        n = int(corrimiento_entry.get())
        resultado = encriptar_cesar(texto, n)
        resultado_entry.delete("1.0", tk.END)
        resultado_entry.insert(tk.END, f"Encriptado: {resultado}")
    except ValueError:
        resultado_entry.delete("1.0", tk.END)
        resultado_entry.insert(tk.END, "Error: Corrimiento debe ser un número entero.")

def desencriptar_texto():
    texto = texto_entry.get("1.0", tk.END).strip()
    try:
        n = int(corrimiento_entry.get())
        resultado = desencriptar_cesar(texto, n)
        resultado_entry.delete("1.0", tk.END)
        resultado_entry.insert(tk.END, f"Desencriptado: {resultado}")
    except ValueError:
        resultado_entry.delete("1.0", tk.END)
        resultado_entry.insert(tk.END, "Error: Corrimiento debe ser un número entero.")

# Validación para permitir solo números
def validar_entrada(texto):
    return texto.isdigit() or texto == ""

# Configuración de la interfaz gráfica
ventana = tk.Tk()
ventana.title("Cifrado César Modificado")
ventana.geometry("500x400")
ventana.resizable(False, False)

# Estilo
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12), padding=10)
style.configure("TLabel", font=("Helvetica", 12))
style.configure("TEntry", font=("Helvetica", 12))

# Frame de entrada de texto
frame_texto = ttk.Frame(ventana, padding=10)
frame_texto.pack(fill='x')

texto_label = ttk.Label(frame_texto, text="Ingrese el texto:")
texto_label.pack(anchor='w')

texto_entry = tk.Text(frame_texto, height=5, width=50)
texto_entry.pack()

# Frame de entrada del corrimiento
frame_corrimiento = ttk.Frame(ventana, padding=10)
frame_corrimiento.pack(fill='x')

corrimiento_label = ttk.Label(frame_corrimiento, text="Ingrese el valor de corrimiento:")
corrimiento_label.pack(anchor='w')

vcmd = (ventana.register(validar_entrada), '%P')  # Validación
corrimiento_entry = ttk.Entry(frame_corrimiento, width=5, validate="key", validatecommand=vcmd)
corrimiento_entry.pack()

# Frame de botones
frame_botones = ttk.Frame(ventana, padding=10)
frame_botones.pack(fill='x')

boton_encriptar = ttk.Button(frame_botones, text="Encriptar", command=encriptar_texto)
boton_encriptar.pack(side='left', padx=5)

boton_desencriptar = ttk.Button(frame_botones, text="Desencriptar", command=desencriptar_texto)
boton_desencriptar.pack(side='left', padx=5)

# Frame de resultado
frame_resultado = ttk.Frame(ventana, padding=10)
frame_resultado.pack(fill='x')

resultado_label = ttk.Label(frame_resultado, text="Resultado:")
resultado_label.pack(anchor='w')

resultado_entry = tk.Text(frame_resultado, height=5, width=50)
resultado_entry.pack()

ventana.mainloop()
