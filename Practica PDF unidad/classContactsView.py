import tkinter as tk
from classContactList import *
from classUpdateContac import *
from classNewContact import *
class ContactsView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Lista de Contactos")
        self.list = ContactList(self, height=15)
        self.form = UpdateContactForm(self)
        self.btn_new = tk.Button(self, text="Agregar Contacto")
        self.list.pack(side=tk.LEFT, padx=10, pady=10)
        self.form.pack(padx=10, pady=10)
        self.btn_new.pack(side=tk.BOTTOM, pady=5)
    def setControlador(self, ctrl):
#vincula la vista con el controlador
        self.btn_new.config(command=ctrl.crearContacto)
        self.list.bind_doble_click(ctrl.seleccionarContacto)
        self.form.bind_save(ctrl.modificarContacto)
        self.form.bind_delete(ctrl.borrarContacto)
    def agregarContacto(self, contacto):
        self.list.insertar(contacto)
    def modificarContacto(self, contacto, index):
        self.list.modificar(contacto, index)
    def borrarContacto(self, index):
        self.form.limpiar()
        self.list.borrar(index)
#obtiene los valores del formulario y crea un nuevo contacto
    def obtenerDetalles(self):
        return self.form.crearContactoDesdeFormulario()
#Ver estado de Contacto en formulario de contactos
    def verContactoEnForm(self, contacto):
        self.form.mostrarEstadoContactoEnFormulario(contacto)