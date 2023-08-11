import tkinter as tk
from tkinter import messagebox

class RutaVisita:
    def __init__(self, id, nombre, destinos):
        self.id = id
        self.nombre = nombre
        self.destinos = destinos

# Datos de ejemplo con destinos culinarios relacionados
ruta_1 = RutaVisita(1, "Ruta de Tapas", ["Empanadas Salteñas", "Locro", "Humita"])
ruta_2 = RutaVisita(2, "Ruta Gastronómica", ["Asado Criollo", "Tamal Salteño", "Mollejas"])
ruta_3 = RutaVisita(3, "Ruta del Vino", ["Vinos Salteños", "Empanadas de Carne", "Quesillo"])
ruta_4 = RutaVisita(4, "Ruta de Sabores Regionales", ["Tamales", "Frituras Salteñas", "Locro Salteño"])
ruta_5 = RutaVisita(5, "Ruta del Dulce de Leche", ["Dulce de Leche", "Alfajores", "Tortitas Negras"])
ruta_6 = RutaVisita(6, "Ruta de Comidas Regionales", ["Carbonada", "Sopa de Maní", "Locro del Valle"])

# Diccionario que relaciona cada ruta con sus destinos culinarios
destinos_culinarios = {
    "Ruta de Tapas": ["Parrilla Don Gauchito", "Restaurante La Tradición"],
    "Ruta Gastronómica": ["Cafetería Sabor Andino", "Trattoria Bella Italia"],
    "Ruta del Vino": ["Sushi Garden", "Sabores Hindúes de Salta Capital Argentina"],
    "Ruta de Sabores Regionales": ["Restaurante Lo de Juan", "Chichería Mi Pachamama"],
    "Ruta del Dulce de Leche": ["Confitería El Paraíso", "Café Dulcería Los Nietitos"],
    "Ruta de Comidas Regionales": ["Comedor Doña Salta", "Pizzería Don Antonio"]
}

rutas_visita = [ruta_1, ruta_2, ruta_3, ruta_4, ruta_5, ruta_6]

def mostrar_caracteristicas_destino():
    indice_seleccionado = lst_destinos.curselection()[0]
    destino_seleccionado = rutas_visita[indice_seleccionado]

    caracteristicas = f"Nombre de la Ruta: {destino_seleccionado.nombre}\n\n"
    caracteristicas += f"Destino: {', '.join(destinos_culinarios[destino_seleccionado.nombre])}\n"

    messagebox.showinfo("Características del Destino", caracteristicas)

# Crear la interfaz gráfica
root = tk.Tk()
root.title("Selección de Destinos")

# Configuración de colores
color_naranja_claro = "#FFDDBB"
color_verde_claro = "#C7E9C0"
root.configure(bg=color_naranja_claro)

# Lista de destinos
lst_destinos = tk.Listbox(root, width=50, height=6, bg=color_verde_claro, selectbackground=color_naranja_claro)
# Ajustamos el ancho y altura de la lista de destinos
for ruta in rutas_visita:
    lst_destinos.insert(tk.END, ruta.nombre)
lst_destinos.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)  # Ajustamos el tamaño y posición

# Botón para mostrar las características del destino seleccionado
btn_mostrar = tk.Button(root, text="Mostrar Características", command=mostrar_caracteristicas_destino, bg=color_naranja_claro)
btn_mostrar.pack(pady=10)

root.mainloop()