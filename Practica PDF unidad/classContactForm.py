import tkinter as tk
from tkinter import messagebox
from classContacto import Contacto
class ContactForm(tk.LabelFrame):
    fields = ("Apellido", "Nombre", "Email", "Teléfono")
    def __init__(self, master, **kwargs):
        super().__init__(master, text="Contacto", padx=10, pady=10, **kwargs)
        self.frame = tk.Frame(self)
        self.entries = list(map(self.crearCampo, enumerate(self.fields)))
        self.frame.pack()
    def crearCampo(self, field):
        position, text = field
        label = tk.Label(self.frame, text=text)
        entry = tk.Entry(self.frame, width=25)
        label.grid(row=position, column=0, pady=5)
        entry.grid(row=position, column=1, pady=5)
        return entry
    def mostrarEstadoContactoEnFormulario(self, contacto):
# a partir de un contacto, obtiene el estado
# y establece en los valores en el formulario de entrada
        values = (contacto.getApellido(), contacto.getNombre(),
        contacto.getEmail(), contacto.getTelefono())
        for entry, value in zip(self.entries, values):
            entry.delete(0, tk.END)
            entry.insert(0, value)
    def crearContactoDesdeFormulario(self):
#obtiene los valores de los campos del formulario
#para crear un nuevo contacto
        values = [e.get() for e in self.entries]
        contacto=None   
        try:
            contacto = Contacto(*values)
        except ValueError as e:
            messagebox.showerror("Error de Validación", str(e), parent=self)
        return contacto
    def limpiar(self):
        for entry in self.entries:
            entry.delete(0, tk.END)