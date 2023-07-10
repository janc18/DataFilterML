import markdown
import tkinter as tk
from tkinter import ttk,Frame
from tkinterweb import HtmlFrame,HtmlLabel
def TextToHtml(Text):
    """
    Return a string in html format from text in markdown format

    :param Text: string in markdown format
    :return: string in html format.

    """
    return markdown.markdown(Text,extensions=['tables'])

def MarkdownToHtml(Path):
    """
    Return a string in html format from markdown file

    :param Path: path from markdown file.
    :return: string in html format.

    """
 
    with open(Path,"r",encoding="utf-8") as InputFile:
        Text=InputFile.read()
        return markdown.markdown(Text,extensions=['tables'])

def ConcatenateCssAndHmtl(PathCSS,MarkdownString):
    return f'''<link rel="stylesheet" href="{PathCSS}"/>\n''' + TextToHtml(MarkdownString)

class EmergentWindow:
    def __init__(self,EmergentWindowData):
        self.EmergentWindowData=EmergentWindowData
        self.Buttons={}
            
    def CreatePopUpWindow(self):
        win=tk.Toplevel()
        win.wm_title(self.EmergentWindowData[0])
        win.geometry("800x600+0+0")
        myhtmlframe = HtmlFrame(win) #create HTML browser
        myhtmlframe.load_html(ConcatenateCssAndHmtl("all.css",self.EmergentWindowData[1]))
        myhtmlframe.add_css("all.css")
        #myhtmlframe.geometry("500x500")
        #myhtmlframe.pack(x=500,y=500, expand=True) #attach the HtmlFrame widget to the parent window
        myhtmlframe.pack()#attach the HtmlFrame widget to the parent window
        Buttons=len(self.EmergentWindowData[2])
        print(ConcatenateCssAndHmtl("all.css",self.EmergentWindowData[1]))

        for i in range(Buttons):
            self.Buttons["Button {0}".format(i)]=ttk.Button(win,text=self.EmergentWindowData[2][i],command=win.destroy, width=200)
            self.Buttons["Button {0}".format(i)].pack(fill="both",expand=True)
            print(self.EmergentWindowData[2][i])

