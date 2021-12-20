from tkinter import *
from tkinter import ttk



class Gui:
  def __init__(self):
    ws  = Tk()
    ws.title('NBA Database Management')
    frame = ttk.Frame(ws, padding = 10, width = 100)
    ws.geometry('800x600')
    # frame.grid()
    
    variable = StringVar(ws)
    variable.set("Players")
    w = OptionMenu(ws, variable, "Players", "Teams", "Games")
    w.pack()    
    
    submit = ttk.Button(ws, text='Submit', command = self.represent_data("Players"))
    submit.pack()

    button = ttk.Button(ws, text='Quit', command=ws.destroy)
    button.pack()
    
    ws.mainloop()
        
  def represent_data(self,table_name):
    if (table_name == 'Players'):
      print("Players")
