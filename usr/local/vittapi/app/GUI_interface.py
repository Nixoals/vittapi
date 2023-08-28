from tkinter import Tk, Label

code_to_send = 'Envoyer du code depuyis la plateforme vittascience'  # Variable globale pour compter les appels

def update_code(code):
    global code_to_send
    code_to_send = code

def run_tkinter():
    global counter
    root = Tk()
    root.geometry("400x200")
    root.title("Vittapi GUI")

    label = Label(root, text="Initial state")
    label.pack()

    def update_label():
        global counter
        label.config(text=code_to_send)
        label.after(1000, update_label)  # Mise à jour chaque seconde

    update_label()
    root.mainloop()
