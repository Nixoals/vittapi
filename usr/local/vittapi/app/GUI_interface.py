from tkinter import Tk, Text, Scrollbar, Y, END, Label
import re

code_to_send = 'Envoyer du code depuis la plateforme vittascience'  # Variable globale

connection = False

def update_connection(value):
    global connection
    connection = value


def update_code(code='Envoyer du code depuis la plateforme vittascience'):
    global code_to_send
    code_to_send = code


def syntax_highlight(text_widget):
    text_widget.tag_remove("python_comment", "1.0", END)
    text_widget.tag_remove("python_keyword", "1.0", END)

    content = text_widget.get("1.0", END)

    # Coloration des commentaires
    for match in re.finditer("#.*", content):
        text_widget.tag_add(
            "python_comment", f"1.0 + {match.start()} chars", f"1.0 + {match.end()} chars")

    # Coloration des mots-clés Python
    for keyword in ["import", "from", "def", "return", "for", "while", "if", "else", "elif"]:
        for match in re.finditer(f"\\b{keyword}\\b", content):
            text_widget.tag_add(
                "python_keyword", f"1.0 + {match.start()} chars", f"1.0 + {match.end()} chars")
    for keyword in ["print"]:
        for match in re.finditer(f"\\b{keyword}\\b", content):
            text_widget.tag_add(
                "python_print", f"1.0 + {match.start()} chars", f"1.0 + {match.end()} chars")
    for keyword in ["True", "False", "None"]:
        for match in re.finditer(f"\\b{keyword}\\b", content):
            text_widget.tag_add(
                "python_boolean", f"1.0 + {match.start()} chars", f"1.0 + {match.end()} chars")
    

def run_tkinter():
    global code_to_send
    root = Tk()
    root.geometry("600x400")
    root.title("Vittapi GUI")

    def update_label_connection():
        global connection
        if (connection):
            connection_state = Label( root, text ="Connecté")
        else:
            connection_state = Label( root, text ="Deconnecté")

        connection_state.pack()
        connection_state.after(1000, update_label_connection)

    text = Text(root, wrap='word')
    scrollbar = Scrollbar(root, orient='vertical', command=text.yview)

    # Mise en place de la coloration syntaxique
    text.tag_configure("python_comment", foreground="green")
    text.tag_configure("python_keyword", foreground="blue")
    text.tag_configure("python_print", foreground="orange")
    text.tag_configure("python_boolean", foreground="red")

    text.config(yscrollcommand=scrollbar.set)

    text.pack(side='left', fill='both', expand=1)
    scrollbar.pack(side='right', fill='y')

    def update_text():
        global code_to_send
        text.delete(1.0, END)
        text.insert(END, code_to_send)
        syntax_highlight(text)  # Appliquer la coloration syntaxique
        text.after(1000, update_text)  # Mise à jour chaque seconde

    update_text()
    root.mainloop()


# Pour tester la mise à jour et la coloration syntaxique
#update_code("import sys\n# Ceci est un commentaire\ndef foo():\n    return 'bar'")
#run_tkinter()
