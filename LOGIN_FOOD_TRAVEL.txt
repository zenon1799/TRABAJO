import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox

# Función para validar las credenciales ingresadas
def validar_login():
    usuario_ingresado = entry_usuario.get()
    contrasena_ingresada = entry_contrasena.get()

    # Aquí puedes realizar la lógica para verificar las credenciales,
    # como comparar con una base de datos o valores predefinidos.
    # Por simplicidad, aquí se asume que el usuario es "admin" y la contraseña es "1234".
    if usuario_ingresado == "admin" and contrasena_ingresada == "1234":
        login_window.destroy()  # Cerramos la ventana de login
        # Puedes agregar aquí la lógica para mostrar la ventana principal o realizar cualquier otra acción
    else:
        messagebox.showerror("Error de inicio de sesión", "Usuario o contraseña incorrectos.")

# Crear la ventana de login
login_window = tk.Tk()
login_window.title("Login")
login_window.configure(background="light blue")

# Estilo para dar un aspecto más moderno a los widgets del login
style_login = ttk.Style()
style_login.theme_use("clam")
style_login.configure("TLabel", background="blue", foreground="white", font=("Arial", 12, "bold"))
style_login.configure("TButton", background="blue", font=("Arial", 12, "bold"))

# Etiquetas y campos de entrada para el login
label_usuario = ttk.Label(login_window, text="Usuario:")
entry_usuario = ttk.Entry(login_window)
label_contrasena = ttk.Label(login_window, text="Contraseña:")
entry_contrasena = ttk.Entry(login_window, show="*")
btn_login = ttk.Button(login_window, text="Iniciar sesión", command=validar_login)

# Posicionar elementos en la ventana de login
label_usuario.grid(row=0, column=0, padx=5, pady=5)
entry_usuario.grid(row=0, column=1, padx=5, pady=5)
label_contrasena.grid(row=1, column=0, padx=5, pady=5)
entry_contrasena.grid(row=1, column=1, padx=5, pady=5)
btn_login.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Ejecutar la interfaz de login
login_window.mainloop()