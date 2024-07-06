import tkinter as tk
import random

def leer_archivo():
    global lineas
    try:
        with open("files\\data.txt", "r+") as archivo:
            lineas = archivo.readlines()
    except FileNotFoundError:
        lineas = []
    mostrar_linea_aleatoria()
    actualizar_contador()

def mostrar_linea_aleatoria():
    if lineas:
        indice_aleatorio = random.randint(0, len(lineas) - 1)
        linea_aleatoria = lineas[indice_aleatorio]
        texto_pantalla.delete(1.0, tk.END)
        texto_pantalla.insert(tk.END, linea_aleatoria)
    else:
        texto_pantalla.delete(1.0, tk.END)
        texto_pantalla.insert(tk.END, "No hay más líneas en el archivo.")

def copiar_al_portapapeles():
    if lineas:
        linea_aleatoria = texto_pantalla.get(1.0, tk.END).strip()
        root.clipboard_clear()
        root.clipboard_append(linea_aleatoria)
        mostrar_mensaje("Línea copiada al portapapeles!")

def eliminar_linea():
    if lineas:
        indice_aleatorio = random.randint(0, len(lineas) - 1)
        linea_eliminada = lineas.pop(indice_aleatorio)

        try:
            with open("files\\data.txt", "w") as archivo:
                archivo.writelines(lineas)
        except Exception as error:
            mostrar_mensaje(f"Error al eliminar la línea: {error}")

        mostrar_linea_aleatoria()
        actualizar_contador()

def actualizar_contador():
    numero_lineas = len(lineas)
    texto_contador.config(text=f"Líneas restantes: {numero_lineas}")

def mostrar_mensaje(mensaje):
    mensaje_emergente = tk.Toplevel(root)
    mensaje_emergente.title("Mensaje")
    etiqueta_mensaje = tk.Label(mensaje_emergente, text=mensaje)
    etiqueta_mensaje.pack()

# Interfaz gráfica

root = tk.Tk()
root.title("Aplicación de enlaces aleatorios")

texto_pantalla = tk.Text(root, height=10, width=50)
texto_pantalla.pack()

boton_leer = tk.Button(root, text="Leer archivo", command=leer_archivo)
boton_leer.pack()

boton_copiar = tk.Button(root, text="Copiar", command=copiar_al_portapapeles)
boton_copiar.pack()

boton_eliminar = tk.Button(root, text="Eliminar y mostrar otra", command=eliminar_linea)
boton_eliminar.pack()

texto_contador = tk.Label(root, text="Líneas restantes: 0")
texto_contador.pack()

leer_archivo()  # Inicia la aplicación al abrir la ventana

root.mainloop()