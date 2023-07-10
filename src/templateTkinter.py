from tkinter import *
import msgMarkdown as msgM

mensaje="""
# noches

parrafo

## lista 1

- CD
- df
- per

_italica_

|ud|ls|cantidad|
|-|-|-|
|lolcito|1|3|
|1|5|6|
|2|5|4|

"""

MessageError=[
        "lolcito",
        mensaje,
        ["boton1","boton3","boton2"]
        ]

ErrorW=msgM.EmergentWindow(MessageError)
window = Tk()
window.title("Welcome to LikeGeeks app")
btn = Button(window, text="Click Me",command=ErrorW.CreatePopUpWindow)
btn.grid(column=1, row=0)
window.mainloop()
