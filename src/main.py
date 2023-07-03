import tkinter as tk
from tkinter import *
from tkinter.ttk import _Padding
import msgMarkdown
from tkinter import ttk
import pandas as pd
import re

class MyApplication(ttk.Frame):
    def __init__(Self, Master = None):
        super().__init__(Master)
        Self.Master = Master
        Self.Master.title('DataFilterML')
        Self.Master.attributes("-fullscreen", True)

Root = tk.Tk()

App = MyApplication(Master=Root)
App.mainloop()

'''md='''
#titulo

## subtitulo

'''
mdlabel=HtmlLabel(root,msgMarkdown.MarkdownToHtml("./msgText.md"))
mdlabel.pack() #attach the HtmlFrame widget to the parent window
root.mainloop()'''

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
