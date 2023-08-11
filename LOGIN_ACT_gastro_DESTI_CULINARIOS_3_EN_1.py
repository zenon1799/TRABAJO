import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import tkinter.messagebox as messagebox
import datetime

# Clase DestinoCulinario
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

# Clase Actividad
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

# Clase DestinosCulinariosApp
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

        ctk.CTkLabel(self.detalle_frame, text="Nombre:").grid(row=0, column=0, sticky="w")
        ctk.CTkLabel(self.detalle_frame, text=destino_seleccionado.nombre).grid(row=0, column=1, sticky="w")

        ctk.CTkLabel(self.detalle_frame, text="Tipo de cocina:").grid(row=1, column=0, sticky="w")
        ctk.CTkLabel(self.detalle_frame, text=destino_seleccionado.tipo_cocina).grid(row=1, column=1, sticky="w")

        ctk.CTkLabel(self.detalle_frame, text="Ingredientes:").grid(row=2, column=0, sticky="w")
        ctk.CTkLabel(self.detalle_frame, text=", ".join(destino_seleccionado.ingredientes)).grid(row=2, column=1, sticky="w")

        ctk.CTkLabel(self.detalle_frame, text="Precio mínimo:").grid(row=3, column=0, sticky="w")
        ctk.CTkLabel(self.detalle_frame, text=str(destino_seleccionado.precio_minimo)).grid(row=3, column=1, sticky="w")

        ctk.CTkLabel(self.detalle_frame, text="Precio máximo:").grid(row=4, column=0, sticky="w")
        ctk.CTkLabel(self.detalle_frame, text=str(destino_seleccionado.precio_maximo)).grid(row=4, column=1, sticky="w")

        ctk.CTkLabel(self.detalle_frame, text="Popularidad:").grid(row=5, column=0, sticky="w")
        ctk.CTkLabel(self.detalle_frame, text=str(destino_seleccionado.popularidad)).grid(row=5, column=1, sticky="w")

        ctk.CTkLabel(self.detalle_frame, text="Disponibilidad:").grid(row=6, column=0, sticky="w")
        ctk.CTkLabel(self.detalle_frame, text="Disponible" if destino_seleccionado.disponibilidad else "No disponible").grid(row=6, column=1, sticky="w")

def validar_login():
    usuario_ingresado = entry_usuario.get()
    contrasena_ingresada = entry_contrasena.get()

    if usuario_ingresado == "admin" and contrasena_ingresada == "1234":
        login_window.destroy()
        mostrar_ventana_principal()
    else:
        messagebox.showerror("Error de inicio de sesión", "Usuario o contraseña incorrectos.")

def mostrar_ventana_principal():
    destinos_culinarios_salta = cargar_destinos_culinarios()

    root = ctk.CTk()
    root.title("Destinos Culinarios y Actividades en Salta")

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

    # Etiqueta de título para Actividades
    titulo_actividades_label = ctk.CTkLabel(root, text="Actividades gastronómico-turísticas en Salta", font=("Helvetica", 14, "bold"))
    titulo_actividades_label.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="w")

    # Crear un listbox para mostrar la lista de actividades con checkboxes
    actividad_combobox = tk.Listbox(root, selectmode=tk.MULTIPLE)
    actividad_combobox.grid(row=5, column=0, columnspan=2, padx=10, pady=5, sticky="news")
    for actividad in actividades:
        actividad_combobox.insert(tk.END, str(actividad))

    # Botón para mostrar los detalles de las actividades seleccionadas
    def mostrar_detalle_actividades():
        indices_seleccionados = actividad_combobox.curselection()
        detalles = ""
        for index in indices_seleccionados:
            detalles += str(actividades[int(index)]) + "\n"
        detalle_label.configure(text=detalles)
        # Deseleccionar las actividades después de mostrar los detalles
        actividad_combobox.selection_clear(0, tk.END)

    mostrar_button = ctk.CTkButton(root, text="Mostrar Detalles", command=mostrar_detalle_actividades)
    mostrar_button.grid(row=6, column=0, columnspan=2, padx=10, pady=5, sticky="w")

    # Etiqueta para mostrar los detalles de las actividades seleccionadas
    detalle_label = ctk.CTkLabel(root, text="", wraplength=400)
    detalle_label.grid(row=7, column=0, columnspan=2, padx=10, pady=5, sticky="w")

    # Crear la aplicación para Destinos Culinarios
    app_destinos = DestinosCulinariosApp(root, destinos_culinarios_salta)

    # Ajustar el tamaño de la primera fila (que contiene el título) para que tenga un peso mayor
    root.grid_rowconfigure(0, weight=1)

    # Iniciar el bucle principal de la interfaz gráfica
    root.mainloop()

# Crear la ventana de login
login_window = ctk.CTk()
login_window._set_appearance_mode("dark")
login_window.resizable(False,False)
login_window.title("Login")

# Etiquetas y campos de entrada para el login
label_usuario = ctk.CTkLabel(login_window, text="Usuario:")
entry_usuario = ctk.CTkEntry(login_window)
label_contrasena = ctk.CTkLabel(login_window, text="Contraseña:")
entry_contrasena = ctk.CTkEntry(login_window, show="*")
btn_login = ctk.CTkButton(login_window, text="Iniciar sesión", command=validar_login)

# Posicionar elementos en la ventana de login
label_usuario.grid(row=0, column=0, padx=5, pady=5)
entry_usuario.grid(row=0, column=1, padx=5, pady=5)
label_contrasena.grid(row=1, column=0, padx=5, pady=5)
entry_contrasena.grid(row=1, column=1, padx=5, pady=5)
btn_login.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Ejecutar la interfaz de login
login_window.mainloop()