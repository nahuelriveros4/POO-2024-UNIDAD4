import tkinter as tk
from tkinter import messagebox
from classContacto import Contacto
from classContactForm import *

class NewContact(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.contacto = None
        self.form = ContactForm(self)
        self.btn_add = tk.Button(self, text="Confirmar", command=self.confirmar)
        self.form.pack(padx=10, pady=10)
        self.btn_add.pack(pady=10)
    def confirmar(self):
        self.contacto = self.form.crearContactoDesdeFormulario()
        if self.contacto:
            self.destroy()
    def show(self):
        self.grab_set()
        self.wait_window()
        return self.contacto