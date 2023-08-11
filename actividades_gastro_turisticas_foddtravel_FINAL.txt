import datetime
import tkinter as tk
from tkinter import ttk

class Actividad:
    def __init__(self, id_actividad, nombre, destino_id, hora_inicio):
        self.id_actividad = id_actividad
        self.nombre = nombre
        self.destino_id = destino_id
        self.hora_inicio = hora_inicio

    def __str__(self):
        return f"Actividad: {self.nombre}, ID: {self.id_actividad}, Destino ID: {self.destino_id}, Hora de inicio: {self.hora_inicio}"

# Lista de actividades ficticias en Salta Capital
actividades = [
    Actividad(1, "Cata de Vinos Salteños", 100, "2023-07-23T18:00:00"),
    Actividad(2, "Noche de Peña Folclórica", 101, "2023-07-24T20:30:00"),
    Actividad(3, "Tour Gastronómico por el Centro Histórico", 102, "2023-07-25T11:00:00"),
    Actividad(4, "Espectáculo de Tango Salteño", 103, "2023-07-26T21:00:00"),
    Actividad(5, "Cena Gourmet con Chef Local", 104, "2023-07-27T19:30:00"),
    Actividad(6, "Show de Malambo y Folklore", 105, "2023-07-28T19:00:00")
]

# Función para mostrar los detalles de las actividades seleccionadas
def mostrar_detalle_actividades():
    indices_seleccionados = actividad_combobox.curselection()
    detalles = ""
    for index in indices_seleccionados:
        detalles += str(actividades[int(index)]) + "\n"
    detalle_label.config(text=detalles)
    # Deseleccionar las actividades después de mostrar los detalles
    actividad_combobox.selection_clear(0, tk.END)

# Resto del código...

# Crear la ventana principal
root = tk.Tk()
root.title("Actividades gastronómico-turísticas en Salta")

# Colores
color_naranja = "#FF8C00"  # Naranja
color_gris_azulado = "#B0C4DE"  # Gris azulado
color_verde_claro = "#98FB98"  # Verde claro
color_azul_claro = "#87CEFA"  # Azul claro

# Configurar el tema "clam" para ttk
style = ttk.Style()
style.theme_use("clam")

# Configurar los colores de fondo para el tema "clam"
style.configure("TLabel", background=color_naranja)
style.configure("TListbox", background=color_gris_azulado, font=("Arial", 12))
style.configure("TButton", background=color_verde_claro, font=("Arial", 12))

# Etiqueta de título
titulo_label = ttk.Label(root, text="Actividades gastronómico-turísticas en Salta", font=("Helvetica", 14, "bold"))
titulo_label.grid(row=0, column=0, columnspan=2, padx=10, pady=5, sticky="w")

# Crear un listbox para mostrar la lista de actividades con checkboxes
actividad_combobox = tk.Listbox(root, selectmode=tk.MULTIPLE)
actividad_combobox.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky="news")
for actividad in actividades:
    actividad_combobox.insert(tk.END, str(actividad))

# Ajustar el tamaño de la primera fila (que contiene el título) para que tenga un peso mayor
root.grid_rowconfigure(0, weight=1)

# Botón para mostrar los detalles de las actividades seleccionadas
mostrar_button = ttk.Button(root, text="Mostrar Detalles", command=mostrar_detalle_actividades)
mostrar_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="w")

# Etiqueta para mostrar los detalles de las actividades seleccionadas
detalle_label = ttk.Label(root, text="", wraplength=400)
detalle_label.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="w")

# Iniciar el bucle principal de la interfaz gráfica
root.mainloop()