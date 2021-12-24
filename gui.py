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
    top_3_winning = ttk.Button(ws, text = 'Top 3 Teams(Winning)', command = self.top_3_winning).pack()
    top_3_winning_as_away = ttk.Button(ws, text = 'Top 3 Away Teams Winning', command = self.top_3_winning_away).pack()
    top_3_winning_special = ttk.Button(ws, text = 'Top 3 Most Wins and Number of Wins', command = self.top_3_special).pack()
    player_query4 = ttk.Button(ws, text = 'Top 3 Players played most seasons', command = self.player_query4).pack()
    ref_every_game = ttk.Button(ws, text = 'Refree all game', command = self.ref_every_game)
    players_double = ttk.Button(ws, text = 'Players with double-double', command = self.players_double)
    player_triple = ttk.Button(ws, text = 'Players with most triple-double', command = self.player_triple)
    player_closeto_triple = ttk.Button(ws, text = 'Players that are close to the triple-double', command = self.player_closeto_triple)
    arena_most_games = ttk.Button(ws, text = 'Arena with most games', command = self.arena_with_most_games)
    arena_most_points = ttk.Button(ws, text = 'Arena with most points', command = self.arena_most_points)
    arena_least_points = ttk.Button(ws, text = 'Arena with least points', command = self.arena_least_points)
    team_most_points_combined = ttk.Button(ws, text = 'Team with most points combined', command = self.team_most_points_combined)
    
    
    view_table.pack()
    ref_every_game.pack()
    players_double.pack()
    player_triple.pack()
    player_closeto_triple.pack()
    arena_most_games.pack()   
    arena_most_points.pack()
    arena_least_points.pack()
    team_most_points_combined.pack()
    
    quit = ttk.Button(ws, text = 'Quit', command = ws.destroy)
    quit.pack()

    ws.mainloop()

  """"""
  def top_3_winning(self):
    table_schema, data = self.db.return_query_table("SELECT cityName, nickname, count(WL_away) as numWins FROM GAME JOIN team ON idTeamAway=idTeam WHERE WL_away = 'W' GROUP BY idTeam ORDER BY numWins DESC LIMIT 3;")
    # sql_command= input_command
    self.represent_queries('Top 3 Winning Teams', table_schema, data)
    
    
  def top_3_winning_away(self):
    table_schema, data = self.db.return_query_table("SELECT cityName, nickname, count(WL_home) as numWins FROM GAME JOIN team ON idTeamHome=idTeam WHERE WL_home = 'W' GROUP BY idTeam ORDER BY numWins DESC LIMIT 3;")
    self.represent_queries('Top 3 Away Teams that Won', table_schema, data)
    
  def top_3_special(self):
    table_schema, data = self.db.return_query_table("SELECT cityName, nickname, count(WL_home) as numWins FROM (SELECT * FROM GAME JOIN team ON idTeamHome=idTeam WHERE WL_home='W' UNION SELECT * FROM GAME JOIN team ON idTeamAway=idTeam WHERE WL_away='W') GROUP BY idTeam ORDER BY numWins DESC LIMIT 3;")
    self.represent_queries('Top 3 teams with all time most wins and the number of wins', table_schema, data)
    
  def player_query4(self):
    table_schema, data = self.db.return_query_table("SELECT namePlayer, seasons FROM nba_player NATURAL JOIN nba_player_stats group by idPlayer ORDER BY seasons DESC LIMIT 3")
    self.represent_queries('Top 3 Players played played most seasons', table_schema, data)

  def ref_every_game(self):
    table_schema, data = self.db.return_query_table("SELECT * FROM referee WHERE NOT EXISTS (SELECT idGame FROM game EXCEPT SELECT idGame FROM oversee WHERE oversee.idReferee=referee.idReferee);" )
    self.represent_queries('Refree all game', table_schema, data)
    

  def players_double(self):
    table_schema, data = self.db.return_query_table("SELECT namePlayer FROM nba_player NATURAL JOIN nba_player_stats WHERE points>=10 AND rebounds>=10 AND assists>=10;" )
    self.represent_queries('Players Double Double', table_schema, data)
      
  def player_triple(self):
    table_schema, data = self.db.return_query_table("SELECT namePlayer FROM nba_player NATURAL JOIN nba_player_stats WHERE points>=10 AND rebounds>=10 AND assists>=10;")
    self.represent_queries('Players Triple Double', table_schema, data)      
  
  def player_closeto_triple(self):
    table_schema, data = self.db.return_query_table("SELECT * FROM nba_player NATURAL JOIN nba_player_stats WHERE points>=9 AND rebounds>=9 AND assists>=9 LIMIT 1;")
    self.represent_queries('Top 3 Players that are close to the triple-double', table_schema, data)
  
  
  def arena_with_most_games(self):
    table_schema, data = self.db.return_query_table("SELECT arenaName, count(idGame) as numGames FROM arena NATURAL JOIN team JOIN game ON idTeamHome=idTeam NATURAL JOIN game_stats GROUP BY arenaName ORDER BY numGames DESC LIMIT 1;")
    self.represent_queries('Arena with most games', table_schema, data)
    
  def arena_most_points(self):
    table_schema, data = self.db.return_query_table("SELECT arenaName, sum(PTS_away) as numPTSRecieved FROM arena NATURAL JOIN team JOIN game ON idTeamHome=idTeam NATURAL JOIN game_stats GROUP BY arenaName ORDER BY numPTSRecieved DESC LIMIT 1;")
    self.represent_queries('Arena with most points', table_schema, data)
  
  def arena_least_points(self):
    table_schema, data = self.db.return_query_table("SELECT arenaName, avg(PTS_away) as numPTSRecieved FROM arena NATURAL JOIN team JOIN game ON idTeamHome=idTeam NATURAL JOIN game_stats  GROUP BY arenaName ORDER BY numPTSRecieved LIMIT 1;")
    self.represent_queries('Arena with least points', table_schema, data)
  
  def team_most_points_combined(self): 
    table_schema, data = self.db.return_query_table("SELECT cityName, nickname, avg(PTS_home) FROM arena NATURAL JOIN team JOIN game ON idTeamHome=idTeam NATURAL JOIN game_stats GROUP BY arenaName ORDER BY avg(PTS_home) DESC LIMIT 1;")
    self.represent_queries('Team with most points combined', table_schema, data)
  
  """represent queries any query from the database (refactored)
  """
  def represent_queries(self,input_title, input_schema, all_data ):
    player_window = Tk()
    player_window.title(input_title)
    player_window_frame = Frame(player_window, bg = '#AC99F2')
    player_window_frame.pack()

    table_schema, data = input_schema, all_data
    my_table = ttk.Treeview(player_window_frame, columns = table_schema, show = 'headings')
    for heading in table_schema:
        my_table.heading(heading, text = heading) 

      # Adding data to the table
    for j in range(len(data)):
      my_table.insert(parent='', index='end',iid=j, text='' ,values = data[j])
      
    my_table.pack()
    quit = ttk.Button(player_window, text='Quit', command= player_window.destroy)
    quit.pack()
      
    player_window.mainloop() 
  
  
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