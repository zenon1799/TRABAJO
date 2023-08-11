import tkinter as tk
from tkinter import ttk

class DestinoCulinario:
    def __init__(self, id, nombre, tipo_cocina, ingredientes, precio_minimo,
                 precio_maximo, popularidad, disponibilidad, id_ubicacion, imagen):
        self.id = id
        self.nombre = nombre
        self.tipo_cocina = tipo_cocina
        self.ingredientes = ingredientes
        self.precio_minimo = precio_minimo
        self.precio_maximo = precio_maximo
        self.popularidad = popularidad
        self.disponibilidad = disponibilidad
        self.id_ubicacion = id_ubicacion
        self.imagen = imagen

def cargar_destinos_culinarios():
    destinos_culinarios = []

    destino_1 = DestinoCulinario(
        id=1,
        nombre="Parrilla Don Gauchito",
        tipo_cocina="Asado Argentino",
        ingredientes=["carne de res", "chorizo", "morcilla"],
        precio_minimo=250.0,
        precio_maximo=500.0,
        popularidad=4.7,
        disponibilidad=True,
        id_ubicacion="SAL-001",
        imagen="https://ejemplo.com/imagen_parrilla.jpg"
    )
    destinos_culinarios.append(destino_1)

    destino_2 = DestinoCulinario(
        id=2,
        nombre="Restaurante La Tradición",
        tipo_cocina="Comida Regional",
        ingredientes=["empanadas", "locro", "humita"],
        precio_minimo=180.0,
        precio_maximo=400.0,
        popularidad=4.5,
        disponibilidad=True,
        id_ubicacion="SAL-002",
        imagen="https://ejemplo.com/imagen_comida_regional.jpg"
    )
    destinos_culinarios.append(destino_2)

    destino_3 = DestinoCulinario(
        id=3,
        nombre="Cafetería Sabor Andino",
        tipo_cocina="Café y Té",
        ingredientes=["café de altura", "mate cocido", "té de coca"],
        precio_minimo=80.0,
        precio_maximo=150.0,
        popularidad=4.2,
        disponibilidad=True,
        id_ubicacion="SAL-003",
        imagen="https://ejemplo.com/imagen_cafeteria.jpg"
    )
    destinos_culinarios.append(destino_3)

    destino_4 = DestinoCulinario(
        id=4,
        nombre="Trattoria Bella Italia",
        tipo_cocina="Italiana",
        ingredientes=["pastas frescas", "salsa pomodoro", "tiramisú"],
        precio_minimo=200.0,
        precio_maximo=450.0,
        popularidad=4.6,
        disponibilidad=True,
        id_ubicacion="SAL-004",
        imagen="https://ejemplo.com/imagen_italiana.jpg"
    )
    destinos_culinarios.append(destino_4)

    destino_5 = DestinoCulinario(
        id=5,
        nombre="Sushi Garden",
        tipo_cocina="Japonesa",
        ingredientes=["sushi variado", "sashimi", "tempura"],
        precio_minimo=300.0,
        precio_maximo=600.0,
        popularidad=4.4,
        disponibilidad=True,
        id_ubicacion="SAL-005",
        imagen="https://ejemplo.com/imagen_sushi.jpg"
    )
    destinos_culinarios.append(destino_5)

    destino_6 = DestinoCulinario(
        id=6,
        nombre="Sabores Hindúes",
        tipo_cocina="Hindú",
        ingredientes=["curry", "naan", "masala chai"],
        precio_minimo=180.0,
        precio_maximo=400.0,
        popularidad=4.3,
        disponibilidad=True,
        id_ubicacion="SAL-006",
        imagen="https://ejemplo.com/imagen_hindu.jpg"
    )
    destinos_culinarios.append(destino_6)

    return destinos_culinarios

class DestinosCulinariosApp:
    def __init__(self, root, destinos):
        self.root = root
        self.destinos = destinos
        self.root.title("Destinos Culinarios en Salta, Argentina")

        self.frame = ttk.Frame(self.root, padding="20")
        self.frame.grid(row=0, column=0, sticky="nsew")

        self.create_widgets()

    def create_widgets(self):
        style = ttk.Style()
        style.configure("Titulo.TLabel", background="#ffa726", font=("Helvetica", 16, "bold"))
        style.configure("Detalle.TFrame", background="#eaffff")

        ttk.Label(self.frame, text="Destinos Culinarios en Salta, Argentina", style="Titulo.TLabel").grid(row=0, column=0, columnspan=2)

        # Combobox para elegir el destino culinario
        self.destino_var = tk.StringVar()
        self.destino_combobox = ttk.Combobox(self.frame, textvariable=self.destino_var, state="readonly")
        self.destino_combobox.grid(row=1, column=0, columnspan=2, sticky="ew")
        self.destino_combobox["values"] = [destino.nombre for destino in self.destinos]
        self.destino_combobox.bind("<<ComboboxSelected>>", self.mostrar_detalle_destino)

        # Sección para mostrar los detalles del destino seleccionado
        self.detalle_frame = ttk.Frame(self.frame, padding="10", style="Detalle.TFrame")
        self.detalle_frame.grid(row=2, column=0, columnspan=2)

    def mostrar_detalle_destino(self, event):
        seleccion = self.destino_var.get()
        destino_seleccionado = [destino for destino in self.destinos if destino.nombre == seleccion][0]

        for widget in self.detalle_frame.winfo_children():
            widget.destroy()

        ttk.Label(self.detalle_frame, text="Nombre:").grid(row=0, column=0, sticky="w")
        ttk.Label(self.detalle_frame, text=destino_seleccionado.nombre).grid(row=0, column=1, sticky="w")

        ttk.Label(self.detalle_frame, text="Tipo de cocina:").grid(row=1, column=0, sticky="w")
        ttk.Label(self.detalle_frame, text=destino_seleccionado.tipo_cocina).grid(row=1, column=1, sticky="w")

        ttk.Label(self.detalle_frame, text="Ingredientes:").grid(row=2, column=0, sticky="w")
        ttk.Label(self.detalle_frame, text=", ".join(destino_seleccionado.ingredientes)).grid(row=2, column=1, sticky="w")

        ttk.Label(self.detalle_frame, text="Precio mínimo:").grid(row=3, column=0, sticky="w")
        ttk.Label(self.detalle_frame, text=str(destino_seleccionado.precio_minimo)).grid(row=3, column=1, sticky="w")

        ttk.Label(self.detalle_frame, text="Precio máximo:").grid(row=4, column=0, sticky="w")
        ttk.Label(self.detalle_frame, text=str(destino_seleccionado.precio_maximo)).grid(row=4, column=1, sticky="w")

        ttk.Label(self.detalle_frame, text="Popularidad:").grid(row=5, column=0, sticky="w")
        ttk.Label(self.detalle_frame, text=str(destino_seleccionado.popularidad)).grid(row=5, column=1, sticky="w")

        ttk.Label(self.detalle_frame, text="Disponibilidad:").grid(row=6, column=0, sticky="w")
        ttk.Label(self.detalle_frame, text="Disponible" if destino_seleccionado.disponibilidad else "No disponible").grid(row=6, column=1, sticky="w")

if __name__ == "__main__":
    destinos_culinarios_salta = cargar_destinos_culinarios()

    root = tk.Tk()
    root.geometry("500x400")
    root.configure(bg="#e5f7fb")
    app = DestinosCulinariosApp(root, destinos_culinarios_salta)
    root.mainloop()