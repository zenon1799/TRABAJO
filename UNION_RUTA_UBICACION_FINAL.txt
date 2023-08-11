import tkinter as tk
from tkinter import ttk
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

class Ubicacion:
    def __init__(self, id, nombre, direccion, coordenadas):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.coordenadas = coordenadas

    def __str__(self):
        return f"{self.nombre} - {self.direccion}"

def mostrar_caracteristicas_destino():
    indice_seleccionado = app.lst_destinos.curselection()
    if not indice_seleccionado:
        messagebox.showwarning("Error", "Por favor, seleccione un destino.")
        return

    destino_seleccionado = rutas_visita[indice_seleccionado[0]]

    caracteristicas = f"Nombre de la Ruta: {destino_seleccionado.nombre}\n\n"
    caracteristicas += f"Destino: {', '.join(destinos_culinarios[destino_seleccionado.nombre])}\n"

    messagebox.showinfo("Características del Destino", caracteristicas)

class SaltaGastronomiaApp(tk.Tk):
    def __init__(self, ubicaciones):
        super().__init__()
        self.title("Selección de Destinos y Ubicaciones")
        self.configure(bg="#FFDDBB")

        # Lista de destinos
        self.lst_destinos = tk.Listbox(self, width=50, height=6, bg="#C7E9C0", selectbackground="#FFDDBB")
        for ruta in rutas_visita:
            self.lst_destinos.insert(tk.END, ruta.nombre)
        self.lst_destinos.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Botón para mostrar las características del destino seleccionado
        btn_mostrar = tk.Button(self, text="Mostrar Características", command=mostrar_caracteristicas_destino, bg="#FFDDBB")
        btn_mostrar.pack(pady=10)

        # Combobox (menú desplegable) para mostrar las ubicaciones
        self.combobox_ubicaciones = ttk.Combobox(self, values=[str(ubicacion) for ubicacion in ubicaciones], state="readonly", background="#C7E9C0")
        self.combobox_ubicaciones.pack(pady=10)

        # Botón para mostrar detalles de ubicación
        boton_mostrar = tk.Button(self, text="Mostrar Detalles", command=self.mostrar_detalle_ubicacion, bg="#C7E9C0")
        boton_mostrar.pack()

        # Etiqueta para mostrar detalles de ubicación seleccionada
        self.detalle_text = tk.Label(self, text="", wraplength=300, justify=tk.LEFT, bg="#E6EBF0")
        self.detalle_text.pack(pady=10)

    def mostrar_detalle_ubicacion(self):
        seleccion = self.combobox_ubicaciones.current()
        if seleccion == -1:
            messagebox.showwarning("Error", "Por favor, seleccione una ubicación.")
            return

        ubicacion_seleccionada = ubicaciones[seleccion]
        self.detalle_text.config(text=f"{ubicacion_seleccionada}\nCoordenadas: {ubicacion_seleccionada.coordenadas}")

if __name__ == "__main__":
    ubicaciones = [
        Ubicacion(id=1, nombre="Parrilla Don Gauchito", direccion="Av. Bicentenario 1200", coordenadas=[-24.788214, -65.422127]),
        Ubicacion(id=2, nombre="Restaurante La Tradicion", direccion="Caseros 699", coordenadas=[-24.789738, -65.410995]),
        Ubicacion(id=3, nombre="Cafetería Sabor Andino", direccion="Zuviría 836", coordenadas=[-24.782574, -65.412470]),
        Ubicacion(id=4, nombre="Trattoria Bella Italia", direccion="Caseros 751", coordenadas=[-24.789506, -65.410968]),
        Ubicacion(id=5, nombre="Sushi Garden", direccion="Av. Reyes Catolicos 1350", coordenadas=[-24.767146, -65.415049]),
        Ubicacion(id=6, nombre="Sabores Hindúes", direccion="Alvarado 1079", coordenadas=[-24.785678, -65.408612]),
    ]
    
    app = SaltaGastronomiaApp(ubicaciones)
    app.mainloop()