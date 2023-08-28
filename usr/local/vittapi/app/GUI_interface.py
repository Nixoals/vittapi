from tkinter import Tk, Label


def run_tkinter(counter):
    root = Tk()
    root.title("Flask Server Monitor")

    label = Label(root, text="Initial state")
    label.pack()

    def update_label():
        
        label.config(text=f"/send-command called {counter} times")
        label.after(1000, update_label)  # Mise à jour chaque seconde

    update_label()
    # root.mainloop()