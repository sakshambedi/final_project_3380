from tkinter import * 
from tkinter import ttk
from database import DataBase


class Gui:
  def __init__(self):
    self.db = DataBase(False)

    ws = Tk()
    ws.title('NBA Database Management')
    ws.geometry('800x600')

    view_table = ttk.Button(ws, text = 'View Tables', command = self.view_table)
    view_table.pack()

    quit = ttk.Button(ws, text = 'Quit', command = ws.destroy)
    quit.pack()

    ws.mainloop()

  def view_table(self):
    player_window = Tk()
    player_window.title('View Table')
    player_window.geometry('200x200')
    player_window_frame = Frame(player_window, bg = '#AC99F2')
    player_window_frame.pack()
    
    tkvar = StringVar(player_window)
    tkvar.set("Select a Table")
    choices = ["nba_player", "nba_player_stats", "nonNBA_Player","arena" ,"city", "country", "draft_player", "game", "game_stats","oversee","refree","season","team"]
    select_table = ttk.Label(player_window, text = 'Select Table')
    select_table.pack()
    
    
    w = OptionMenu(player_window,tkvar, *choices).pack()
    submit=ttk.Button(player_window, text='Submit', command=lambda: self.represent_data(str(tkvar.get())))
    submit.config(width = 10)
    submit.pack()
    
    quit = ttk.Button(player_window, text='Quit', command=player_window.destroy)
    quit.pack()


    """[summary] Represent data in a table using tkinker library
    """
  def represent_data(self, table_name):
    if(table_name == 'nba_player'  or table_name == 'arena' or table_name == 'nba_player_stats' or table_name == 'nonNBA_Player' or table_name == 'city' or table_name == 'country' or table_name == 'draft_player' or table_name == 'game' or table_name == 'game_stats' or table_name == 'oversee' or table_name == 'refree' or table_name == 'season' or table_name == 'team'):
      table_schema, data = self.db.get_table(table_name)
    
    
      new_window = Tk()
      new_window.title(table_name)

      # Create a frame for the table_schema
      window_frame = Frame(new_window, bg = '#AC99F2')
      window_frame.pack()

      #defining the columns for the table
      my_table = ttk.Treeview(window_frame, columns = table_schema, show = 'headings')
      # my_table['columns'] = table_schema
      # print(my_table['columns'])
      # my_table.column("#0", width = 100, minwidth = 0, stretch = NO)
      for heading in table_schema:
        my_table.heading(heading, text = heading) 

      # Adding data to the table
      for j in range(len(data)):
        my_table.insert(parent='', index='end',iid=j, text='' ,values = data[j])
      
      my_table.pack()
      quit = ttk.Button(new_window, text='Quit', command=new_window.destroy)
      quit.pack()
      
      new_window.mainloop()
    else:
      print("Not a valid table")