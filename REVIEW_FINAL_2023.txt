import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Review:
    id_usuario_counter = 1
    id_destino_counter = 1001

    def __init__(self, destino, caracteristicas, calificacion, animo, comentario):
        self.id_destino = Review.id_destino_counter
        Review.id_destino_counter += 1
        self.id_usuario = Review.id_usuario_counter
        Review.id_usuario_counter += 1
        self.destino = destino
        self.caracteristicas = caracteristicas
        self.calificacion = calificacion
        self.animo = animo
        self.comentario = comentario

historial_reviews = []

def cargar_destino(event=None):
    seleccion = destino_combobox.get()
    if seleccion in destinos:
        comentario_text.delete("1.0", "end")
        comentario_text.insert("1.0", destinos[seleccion]["caracteristicas"])
        calificacion_var.set(destinos[seleccion]["calificacion"])
        animo_var.set(destinos[seleccion]["animo"])

def get_stars_from_rating(rating):
    try:
        rating = int(rating)
        return "★" * rating + "☆" * (5 - rating)
    except ValueError:
        return "N/A"

def mostrar_review_guardada():
    if review_popup is None or not review_popup.winfo_exists():
        crear_review_popup()

    review_text.config(state="normal")  # Enable the text widget
    review_text.delete("1.0", "end")  # Clear previous content

    # Update the review history content with the latest information
    for review in historial_reviews:
        review_text.insert("end", f"ID Usuario: {review.id_usuario}\n")
        review_text.insert("end", f"ID Destino: {review.id_destino}\n")
        review_text.insert("end", f"Destino: {review.destino}\n")
        review_text.insert("end", f"Características del Lugar: {review.caracteristicas}\n")
        review_text.insert("end", f"Calificación: {get_stars_from_rating(review.calificacion)}\n")
        review_text.insert("end", f"Ánimo: {review.animo}\n")
        review_text.insert("end", "Comentarios del Visitante:\n")
        review_text.insert("end", f"Comentario: {review.comentario}\n")
        review_text.insert("end", "----------------------------------------\n")

    review_text.config(state="disabled")  # Disable the text widget after updating

def crear_review_popup():
    global review_popup, review_text

    review_popup = tk.Toplevel(ventana)
    review_popup.title("Historial de Reviews")
    review_popup.attributes('-topmost', True)

    style = ttk.Style(review_popup)
    style.theme_use('clam')

    tk.Label(review_popup, text="Historial de Reviews:", font=("Arial", 14, "bold")).pack(padx=10, pady=10)

    review_text = tk.Text(review_popup, height=20, width=70, wrap=tk.WORD, font=("Arial", 12))
    review_text.pack(padx=10, pady=10)

    review_text.config(state="disabled")  # Disable the text widget initially

def guardar_review():
    seleccion = destino_combobox.get()
    calificacion = calificacion_combobox.get()
    animo = animo_combobox.get()
    comentario = comentario_visitante_text.get("1.0", "end").strip()

    if not seleccion or not calificacion or not animo or not comentario:
        messagebox.showerror("Error", "Completa todos los campos antes de guardar la review.")
        return

    if seleccion in destinos:
        caracteristicas = destinos[seleccion]["caracteristicas"]
        review = Review(seleccion, caracteristicas, calificacion, animo, comentario)
        historial_reviews.append(review)
        mostrar_review_guardada()
        comentario_visitante_text.delete("1.0", "end")
        destino_combobox.set("")  # Clear the selected destination after saving
    else:
        messagebox.showerror("Error", "Selecciona un destino válido.")

def nuevo_usuario():
    comentario_text.delete("1.0", "end")
    calificacion_combobox.set("")
    animo_combobox.set("")
    comentario_visitante_text.delete("1.0", "end")
    destino_combobox.set("")

destinos = {
    "Parrilla Don Gauchito": {"caracteristicas": "Tipo de cocina: Asado argentino (carne de res, chorizo, morcilla).", "calificacion": "", "animo": ""},
    "Restaurante La Tradicion": {"caracteristicas": "Comida regional (empanadas, locro, humitas).", "calificacion": "", "animo": ""},
    "Cafeteria Sabor Andino": {"caracteristicas": "Café y té (café de altura, mate cocido varios sabores, té de coca, té de burro, té de toronjil, entre otros).", "calificacion": "", "animo": ""},
    "Tratoria Bella Italia": {"caracteristicas": "Comida italiana (pastas frescas, pizzas napolitana, salsa pomodoro, postres tiramisu).", "calificacion": "", "animo": ""},
    "Sushi Garden": {"caracteristicas": "Comida japonesa (sushi variado, sashimi, tempora).", "calificacion": "", "animo": ""},
    "Sabores Hindues de Salta": {"caracteristicas": "Tipo de cocina hindú (curry, Naan, Masala Chai).", "calificacion": "", "animo": ""}
}

categorias_calificacion = ["★", "★★", "★★★", "★★★★", "★★★★★"]
rango_animo = list(range(1, 11))

ventana = tk.Tk()
ventana.title("Puntuación de Destinos Culinarios")

calificacion_var = tk.StringVar()
animo_var = tk.StringVar()

color_naranja = "#FF8C00"
color_gris_azulado = "#B0C4DE"
color_verde_claro = "#98FB98"
color_azul_claro = "#87CEFA"

ventana.configure(bg=color_verde_claro)

tk.Label(ventana, text="REVIEW", bg=color_naranja, fg="white", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="ew")
tk.Label(ventana, text="Modo Selección de Destino", bg=color_gris_azulado, fg="white", font=("Arial", 14, "bold")).grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

tk.Label(ventana, text="Destino:", font=("Arial", 12)).grid(row=2, column=0, padx=5, pady=5)
tk.Label(ventana, text="Calificación:", font=("Arial", 12)).grid(row=3, column=0, padx=5, pady=5)
tk.Label(ventana, text="Ánimo:", font=("Arial", 12)).grid(row=4, column=0, padx=5, pady=5)
tk.Label(ventana, text="Comentarios del Visitante:", font=("Arial", 12)).grid(row=6, column=0, padx=5, pady=5)

destino_combobox = ttk.Combobox(ventana, values=list(destinos.keys()), font=("Arial", 12), state='readonly')
destino_combobox.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
destino_combobox.bind("<<ComboboxSelected>>", cargar_destino)

calificacion_combobox = ttk.Combobox(ventana, values=categorias_calificacion, font=("Arial", 12), state='readonly')
calificacion_combobox.grid(row=3, column=1, padx=5, pady=5, sticky="ew")

animo_combobox = ttk.Combobox(ventana, values=rango_animo, font=("Arial", 12), state='readonly')
animo_combobox.grid(row=4, column=1, padx=5, pady=5, sticky="ew")

comentario_text = tk.Text(ventana, height=5, width=30, wrap=tk.WORD, insertborderwidth=2, relief=tk.SOLID, borderwidth=1, font=("Arial", 12))
comentario_text.grid(row=5, column=1, padx=5, pady=5, sticky="ew")

comentario_visitante_text = tk.Text(ventana, height=5, width=30, wrap=tk.WORD, insertborderwidth=2, relief=tk.SOLID, borderwidth=1, font=("Arial", 12))
comentario_visitante_text.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

tk.Button(ventana, text="Guardar Review", command=guardar_review, font=("Arial", 12)).grid(row=8, column=0, columnspan=2, padx=5, pady=10, sticky="ew")
tk.Button(ventana, text="Nuevo Usuario", command=nuevo_usuario, font=("Arial", 12)).grid(row=9, column=0, columnspan=2, padx=5, pady=10, sticky="ew")

ventana.option_add("*Entry*background", color_gris_azulado)
ventana.option_add("*Entry*foreground", "black")
ventana.option_add("*Entry*font", ("Arial", 12))
ventana.option_add("*Button*background", color_azul_claro)
ventana.option_add("*Button*foreground", "black")
ventana.option_add("*Button*font", ("Arial", 12))

# Call the function to create the review history popup window
crear_review_popup()

ventana.mainloop()