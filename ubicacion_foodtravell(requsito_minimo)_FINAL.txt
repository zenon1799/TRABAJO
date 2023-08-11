import tkinter as tk
from tkinter import ttk

class Ubicacion:
    def __init__(self, id, nombre, direccion, coordenadas):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.coordenadas = coordenadas

    def __str__(self):
        return f"{self.nombre} - {self.direccion}"

def mostrar_detalle_ubicacion():
    seleccion = combobox_ubicaciones.current()
    ubicacion_seleccionada = ubicaciones[seleccion]
    detalle_text.config(text=f"{ubicacion_seleccionada}\nCoordenadas: {ubicacion_seleccionada.coordenadas}")

if __name__ == "__main__":
    # Ejemplos de ubicaciones en Salta Capital, Argentina
    ubicaciones = [
        Ubicacion(id=1, nombre="Parrilla Don Gauchito", direccion="Av. Bicentenario 1200", coordenadas=[-24.788214, -65.422127]),
        Ubicacion(id=2, nombre="Restaurante La Tradicion", direccion="Caseros 699", coordenadas=[-24.789738, -65.410995]),
        Ubicacion(id=3, nombre="Cafetería Sabor Andino", direccion="Zuviría 836", coordenadas=[-24.782574, -65.412470]),
        Ubicacion(id=4, nombre="Trattoria Bella Italia", direccion="Caseros 751", coordenadas=[-24.789506, -65.410968]),
        Ubicacion(id=5, nombre="Sushi Garden", direccion="Av. Reyes Catolicos 1350", coordenadas=[-24.767146, -65.415049]),
        Ubicacion(id=6, nombre="Sabores Hindúes", direccion="Alvarado 1079", coordenadas=[-24.785678, -65.408612]),
    ]

    # Crear ventana
    ventana = tk.Tk()
    ventana.title("Ubicaciones Gastronomía Salta")

    # Configuración de colores
    color_naranja_claro = "#FFDDBB"
    color_verde_claro = "#C7E9C0"
    color_gris_azulado = "#E6EBF0"
    ventana.configure(bg=color_naranja_claro)

    # Crear etiqueta para el título
    titulo_label = tk.Label(ventana, text="Ubicaciones Gastronomía Salta", font=("Arial", 16, "bold"), bg=color_naranja_claro)
    titulo_label.pack(pady=10)

    # Crear combobox (menú desplegable) para mostrar las ubicaciones
    combobox_ubicaciones = ttk.Combobox(ventana, values=[str(ubicacion) for ubicacion in ubicaciones], state="readonly", background=color_verde_claro)
    combobox_ubicaciones.pack(pady=10)

    # Crear botón para mostrar detalles
    boton_mostrar = tk.Button(ventana, text="Mostrar Detalles", command=mostrar_detalle_ubicacion, bg=color_verde_claro)
    boton_mostrar.pack()

    # Crear etiqueta para mostrar detalles de ubicación seleccionada
    detalle_text = tk.Label(ventana, text="", wraplength=300, justify=tk.LEFT, bg=color_gris_azulado)
    detalle_text.pack(pady=10)

    ventana.mainloop()
