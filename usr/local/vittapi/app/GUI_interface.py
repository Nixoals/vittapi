from tkinter import Tk, Label

counter = 0  # Variable globale pour compter les appels

def update_counter():
    global counter
    counter += 1

def run_tkinter():
    global counter
    root = Tk()
    root.title("Flask Server Monitor")

    label = Label(root, text="Initial state")
    label.pack()

    def update_label():
        global counter
        label.config(text=f"/send-command called {counter} times")
        label.after(1000, update_label)  # Mise à jour chaque seconde

    update_label()
    root.mainloop()
