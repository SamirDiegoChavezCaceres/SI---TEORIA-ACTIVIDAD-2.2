""" Main module for the application.
"""


from tkinter import *
from tkinter import messagebox, ttk
from algorithms.atbash import AtbashAlgorithm
from algorithms.vignere import VignereAlgorithm


ALPHABET = "abcdefghijklmnñopqrstuvwxyz"
VIGNERE_KEY = "clave"
TILDES_ATBASH = {
    'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u', 'ü': 'u',
    'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U', 'Ü': 'U'
}
CASE_SENSITIVE_ATBASH = False
ATBASH_SPACES_TO = ""

def call_algorithm(widget, algorithm, message):
    """ Call the algorithm to execute the message.
    """
    response = algorithm.execute(message)
    widget.delete(0,END)
    widget.insert(0,response)
    return


def open_window(algorithm):
    """ Create secondary (or popup) window.
    """
    secondary_window = Toplevel()
    secondary_window.title("Algorithm Window")
    secondary_window.geometry("400x150")

    text_label = Label(secondary_window, text="Texto Entrada:")
    text_label.pack()
    text_entry = Entry(secondary_window,  width=50)
    text_entry.pack()

    # Create a button to close (destroy) this window.
    cipher_label = Label(secondary_window, text="Texto resultante:")
    cipher_entry = Entry(secondary_window,  width=50)
    button_close = ttk.Button(
        secondary_window,
        text="Ejecutar",
        command=lambda:call_algorithm(
            cipher_entry,
            algorithm,
            text_entry.get()
        )
    )
    button_close.pack()
    cipher_label.pack()
    cipher_entry.pack()


# Create the main tkinter window
root = Tk()
root.title("Informatic Security - Algorithms")
root.geometry('300x100')

# Create labels and entry fields for each input
question_label = Label(root, text="¿Que desea hacer?:")
question_label.pack()

atbash_button = Button(
    root,
    text="Cifrado Atbash",
    command=lambda:open_window(
        AtbashAlgorithm(
            alphabet=ALPHABET, 
            extraReplaces= TILDES_ATBASH,
            caseSensitive=CASE_SENSITIVE_ATBASH,
            spacesTo=ATBASH_SPACES_TO
        )
    )
)
atbash_button.pack()

vignere_button = Button(
    root,
    text="Descifrado Vignere",
    command=lambda:open_window(
        VignereAlgorithm(
            alphabet=ALPHABET,
            key=VIGNERE_KEY
        )
    )
)
vignere_button.pack()

root.mainloop()
