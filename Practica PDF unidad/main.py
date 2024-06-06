# PROGRAMA PRINCIPAL
from classRepositorioContactosJSON import RespositorioContactos
from classContactsView import ContactsView
from classControladorContactos import ControladorContactos
from classObjectEncoder import ObjectEncoder
def main():
    conn=ObjectEncoder('contactos.json')
    repo=RespositorioContactos(conn)
    vista=ContactsView()
    ctrl=ControladorContactos(repo, vista)
    vista.setControlador(ctrl)
    ctrl.start()
    ctrl.salirGrabarDatos()
if __name__ == "__main__":
    main()