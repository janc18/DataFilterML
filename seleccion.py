import tkinter as tk
from tkinter import *
from tkinter import ttk
import pandas as pd
import re

root = tk.Tk()
frm1 = ttk.Frame(root, height=800, width=800)
frm1.pack()
ttk.Label(frm1, text="primer paso").place(relx=0.5, rely= 0.2)

root.mainloop()

"""

with open(ruta, 'r') as f:
    text = f.read()

    lines = text.split('\n')

    contador=0
    for line in lines:
        contador+=1
        match = re.search('^\d{1,2}/\d{1,2}/\d{2,4}', line)
        if match:
            break
        
with pd.read_csv(archivo, chunksize=10000, skiprows=contador-2) as reader:
    for j, chunk in enumerate(reader):
        totalshape=totalshape+len(chunk)
        if j==0:
            encabezados=list(chunk.columns)

        chunk['Times'] = pd.to_datetime(chunk['Time']).dt.time
        chunk['Times_sec'] = chunk['Times'].apply(time_to_sec)
        listilla.append(chunk)
"""