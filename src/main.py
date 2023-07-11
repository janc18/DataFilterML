import tkinter as tk
from tkinter import *
from tkinter import ttk
import sv_ttk
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
        
        Self.ToolsSettings = ttk.Frame(Self.Graph, width=200)
        Self.ToolsSettings.pack(side='left', fill='y')
        
        Tab1 = ttk.Frame(Self.Notebook)
        Tab2 = ttk.Frame(Self.Notebook)
        Tab3 = ttk.Frame(Self.Notebook)
        Tab4 = ttk.Frame(Self.Notebook)
        

        Self.Notebook.add(Tab1, text='File')
        Self.Notebook.add(Tab2, text='Edition')
        Self.Notebook.add(Tab3, text='Data')
        Self.Notebook.add(Tab4, text='Tools') 
        
Root = tk.Tk()

App = MyApplication(Master=Root)
sv_ttk.set_theme('white')
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
