import tkinter as tk


def submit_input():
    input_value = input_field.get()
    print(f"You submitted: {input_value}")


# Crear la ventana
window = tk.Tk()
window.geometry("200x100")

# Centrar la ventana en la pantalla
window.eval('tk::PlaceWindow . center')

# Definir las instrucciones
instructions_label = tk.Label(window, text="Ingrese una expresión regular:")
instructions_label.pack()

# Definir el input field
input_field = tk.Entry(window)
input_field.pack()

# Definir el botón de submit
submit_button = tk.Button(window, text="Submit", command=submit_input)
submit_button.pack()

# Mostrar la ventana
window.mainloop()
