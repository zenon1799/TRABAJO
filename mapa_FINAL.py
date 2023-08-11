import tkinter as tk
from tkintermapview import TkinterMapView
from PIL import Image, ImageTk

class DestinoCulinario:
    def __init__(self, nombre, latitud, longitud, tipo_cocina, ingredientes, precio_minimo, precio_maximo, popularidad, imagen):
        self.nombre = nombre
        self.latitud = latitud
        self.longitud = longitud
        self.tipo_cocina = tipo_cocina
        self.ingredientes = ingredientes
        self.precio_minimo = precio_minimo
        self.precio_maximo = precio_maximo
        self.popularidad = popularidad
        self.imagen = imagen

class FoodieTourApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("FoodieTour")
        self.geometry("1000x600")

        self.destinos = self.cargar_destinos()

        self.scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL)
        self.lista_destinos = tk.Listbox(self, width=30, yscrollcommand=self.scrollbar.set)
        self.lista_destinos.pack(side='left', fill='both', expand=True)
        self.scrollbar.config(command=self.lista_destinos.yview)
        self.scrollbar.pack(side='left', fill='y')

        self.actualizar_lista_destinos()

        self.mapa = TkinterMapView(self, width=700, height=600, corner_radius=0)
        self.mapa.set_zoom(12)
        self.mapa.pack(side='right')

        self.label_info_detallada = tk.Label(self, text="", justify=tk.LEFT)
        self.label_info_detallada.pack(side='bottom', padx=10, pady=10)

        self.label_imagen = tk.Label(self, width=300, height=200)
        self.label_imagen.pack(side='bottom', padx=10, pady=10)

        self.mostrar_info_destino_seleccionado()

        self.lista_destinos.bind('<<ListboxSelect>>', self.mostrar_info_destino_seleccionado)

    def cargar_destinos(self):
        destinos = [
            DestinoCulinario("Parrilla Don Gauchito", -24.785172, -65.412609, "Argentina", ["Empanadas", "Asado"], 20.0, 60.0, 4.3, "ruta_de_la_imagen/parrilla_don_gauchito.jpg"),
            DestinoCulinario("Restaurante La Tradicion", -24.780037, -65.409850, "Parrilla", ["Asado", "Bife de chorizo"], 30.0, 70.0, 4.5, "ruta_de_la_imagen/restaurante_la_tradicion.jpg"),
            DestinoCulinario("Cafeteria Sabor Andino", -24.785587, -65.409500, "Cafetería", ["Café", "Medialunas"], 5.0, 15.0, 4.0, "ruta_de_la_imagen/cafeteria_sabor_andino.jpg"),
            DestinoCulinario("Tratoria Bella Italia", -24.787021, -65.413409, "Comida regional", ["Locro", "Humita"], 25.0, 50.0, 4.2, "ruta_de_la_imagen/trattoria_bella_italia.jpg"),
            DestinoCulinario("Sushi Garden", -24.790210, -65.416870, "Japonesa", ["Sushi", "Sashimi"], 40.0, 100.0, 4.8, "ruta_de_la_imagen/sushi_garden.jpg"),
            DestinoCulinario("Sabores Hindues", -24.779256, -65.412586, "Heladería", ["Helado", "Dulce de leche"], 10.0, 25.0, 4.1, "ruta_de_la_imagen/sabores_hindues.jpg"),
            # Agrega más destinos aquí...
        ]
        return destinos

    def actualizar_lista_destinos(self):
        self.lista_destinos.delete(0, tk.END)
        for destino in self.destinos:
            self.lista_destinos.insert(tk.END, f"{destino.nombre} - Popularidad: {destino.popularidad}")

    def mostrar_info_destino_seleccionado(self, event=None):
        if not self.lista_destinos.curselection():
            return

        index = self.lista_destinos.curselection()[0]
        destino = self.destinos[index]

        self.mapa.set_position(destino.latitud, destino.longitud)
        self.mapa.clear_markers()
        self.mapa.add_marker(destino.latitud, destino.longitud, destino.nombre)

        info_detallada = f"""
        Nombre: {destino.nombre}
        Tipo de Cocina: {destino.tipo_cocina}
        Ingredientes: {', '.join(destino.ingredientes)}
        Precio Mínimo: {destino.precio_minimo}
        Precio Máximo: {destino.precio_maximo}
        Popularidad: {destino.popularidad}
        """
        self.label_info_detallada.config(text=info_detallada)

        imagen = Image.open(destino.imagen)
        imagen = imagen.resize((300, 200), Image.ANTIALIAS)
        imagen_tk = ImageTk.PhotoImage(imagen)
        self.label_imagen.config(image=imagen_tk)
        self.label_imagen.image = imagen_tk

if __name__ == "__main__":
    app = FoodieTourApp()
    app.mainloop()