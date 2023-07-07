import tkinter as tk
from tkinter import *
from tkinter import ttk
import pandas as pd
import re
import msgMarkdown
import re

class MyApplication(ttk.Frame):
    def __init__(Self, Master = None):
        super().__init__(Master)
        Self.Master = Master
        Self.Master.title('DataFilterML')
        Self.Master.state('zoomed')
        
        Self.Notebook = ttk.Notebook(Self.Master, height=100)
        Self.Notebook.pack(side='top', fill='x')
        
        Self.Graph = Frame(Self.Master, bg='white')
        Self.Graph.pack(side='bottom', fill='both', expand=True)
        
        style = ttk.Style()
        style.configure('Red.TFrame', background='red')
        
        Self.ToolsSettings = ttk.Frame(Self.Graph, width=100, style='Red.TFrame')
        Self.ToolsSettings.pack(side='left', fill='y')
        
Root = tk.Tk()

App = MyApplication(Master=Root)
App.mainloop()
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
