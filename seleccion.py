import pandas as pd
import re
from tkinter import *
from tkinter import ttk

root = ttk.Frame(padding=10, height=800, width=800)
root.pack
ttk.Label(root, text="primer paso").pack()



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