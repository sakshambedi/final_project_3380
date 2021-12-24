from tkinter import Tk, Label, Button, StringVar, Frame, OptionMenu 
from tkinter import ttk
from database import DataBase


class Gui:
  def __init__(self):
    self.db = DataBase(False)

    ws = Tk()
    ws.title('NBA Database Management')
    ws.geometry('800x600')

    view_table = ttk.Button(ws, text = 'View Tables', command = self.view_table)
    top_3_winning = ttk.Button(ws, text = 'Top 3 Teams(Winning)', command = self.top_3_winning)
    top_3_winning_away = ttk.Button(ws, text = 'Top 3 Away Teams Winning', command = self.top_3_winning_away)
    top_3_winning_special = ttk.Button(ws, text = 'Top 3 Most Wins and Number of Wins', command = self.top_3_special)
    player_query4 = ttk.Button(ws, text = 'Top 3 Players played most seasons', command = self.player_query4)
    ref_every_game = ttk.Button(ws, text = 'All referees that have overseen all games', command = self.ref_every_game)
    players_double = ttk.Button(ws, text = 'Players with double-double', command = self.players_double)
    player_triple = ttk.Button(ws, text = 'Players with most triple-double', command = self.player_triple)
    player_closeto_triple = ttk.Button(ws, text = 'Players that are close to the triple-double', command = self.player_closeto_triple)
    arena_most_games = ttk.Button(ws, text = 'Arena with most games', command = self.arena_with_most_games)
    arena_most_points = ttk.Button(ws, text = 'Arena with most points', command = self.arena_most_points)
    arena_least_points = ttk.Button(ws, text = 'Arena with least points', command = self.arena_least_points)
    team_most_points_combined = ttk.Button(ws, text = 'Team with most points combined', command = self.team_most_points_combined)
    non_nba_not_drafted = ttk.Button(ws, text = 'Non-NBA Team Player not drafted', command = self.non_NBA_not_drafted)
    average_weight_player = ttk.Button(ws, text = 'Average weight of drafted players', command = self.average_weight_players)
    ref_seen_most_points = ttk.Button(ws, text = 'Referee that saw most points', command = self.ref_seen_most_points)
    player_query26 = ttk.Button(ws, text = 'Countries with most NBA players and number of players', command = self.player_query26)
    average_points_1st = ttk.Button(ws, text = 'Average points of 1st round 1st pick of all draft', command = self.average_points_1st)
    average_1st_round_30th_pick = ttk.Button(ws, text = 'Average points of 1st round 30th pick of all draft', command = self.average_1st_round_30th_pick)
    find_dallas_player = ttk.Button(ws, text = 'Dallas player playing for 10 years ', command = self.find_dallas_player)
    count_num_player_country = ttk.Button(ws, text = 'Count number of players in each country ordered desc', command = self.count_num_player_country)
    player_attende_7_allstar = ttk.Button(ws, text = 'Players that attended all 7-star games', command = self.player_attende_7_allstar)
    most_all_star = ttk.Button(ws, text = 'Team with most all-star players in history', command = self.most_all_star)
    player_longest_played = ttk.Button(ws, text = 'Player with longest played years in NBA', command = self.player_longest_played)
    team_highest_mark_game = ttk.Button(ws, text = 'Team with highest mark in a game in history', command = self.team_highest_mark_game)
    top_5_oversea_players = ttk.Button(ws, text = 'Top 5 players from oversea countries and their teams', command = self.top_5_oversea_players)
    best_player_NBA = ttk.Button(ws, text = 'Best player in NBA history using given formula', command = self.best_player_NBA)
    worst_team_NBA = ttk.Button(ws, text = 'Worst team in NBA history using given formula', command = self.worst_team_NBA)
    team_wins_home_season = ttk.Button(ws, text = 'Team with most wins in home in a certain season', command = self.team_wins_home_season)
     
    view_table.pack()
    top_3_winning.pack()
    top_3_winning_away.pack()
    top_3_winning_special.pack()
    player_query4.pack()
    ref_every_game.pack()
    players_double.pack()
    player_triple.pack()
    player_closeto_triple.pack()
    arena_most_games.pack()   
    arena_most_points.pack()
    arena_least_points.pack()
    team_most_points_combined.pack()
    non_nba_not_drafted.pack()
    average_weight_player.pack()
    ref_seen_most_points.pack()
    player_query26.pack()
    average_points_1st.pack()
    average_1st_round_30th_pick.pack()
    find_dallas_player.pack()
    count_num_player_country.pack()
    player_attende_7_allstar.pack()
    most_all_star.pack()
    player_longest_played.pack()
    team_highest_mark_game.pack()
    top_5_oversea_players.pack()
    best_player_NBA.pack()
    worst_team_NBA.pack()
    team_wins_home_season.pack()
    
    quit = ttk.Button(ws, text = 'Quit', command = ws.destroy)
    quit.pack()

    ws.mainloop()

  """"""
  def top_3_winning(self):
    table_schema, data = self.db.return_query_table("SELECT cityName, nickname, count(WL_away) as numWins FROM GAME JOIN team ON idTeamAway=idTeam WHERE WL_away = 'W' GROUP BY idTeam ORDER BY numWins DESC LIMIT 3;")
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
  
  
  def non_NBA_not_drafted(self):
    table_schema, data = self.db.return_query_table("SELECT nameNonPlayer FROM nonNBA_player EXCEPT SELECT nameNonPlayer FROM nonNBA_player JOIN draft_player ON idNonPlayer=idPlayer;")
    self.represent_queries('Non-NBA players not drafted', table_schema, data)
  
  def average_weight_players(self):
    table_schema, data = self.db.return_query_table("SELECT avg(weight) FROM nonNBA_player JOIN draft_player ON idNonPlayer=idPlayer;")
    self.represent_queries('Average weight of players', table_schema, data)
  
  def ref_seen_most_points(self):
    table_schema, data = self.db.return_query_table("SELECT SELECT firstName, lastName, sum(PTS_home+PTS_away) as numPointsSeen FROM referee NATURAL JOIN oversee NATURAL JOIN game NATURAL JOIN game_stats GROUP BY idReferee ORDER BY numPointsSeen DESC LIMIT 1;")
    self.represent_queries('Referee with most points', table_schema, data)
  
  def player_query26(self):
    table_schema, data = self.db.return_query_table("SELECT countryName, count(idPlayer) as numPlayers FROM nba_player JOIN country on nba_player.country=countryName GROUP BY countryName ORDER BY numPlayers DESC LIMIT 10;")
    self.represent_queries('Country with most players in NBA and their names ', table_schema, data)
  
  
  def average_points_1st(self):
    table_schema, data = self.db.return_query_table("SELECT namePlayer, avg(points)  FROM draft_player NATURAL JOIN nba_player NATURAL JOIN nba_player_stats WHERE numberRound = 1 AND numberRoundPick = 1;")
    self.represent_queries('Average points of the 1st round 1st pick of all draft', table_schema, data)
  
  def average_1st_round_30th_pick(self):
    table_schema, data = self.db.return_query_table("SELECT namePlayer, avg(points)  FROM draft_player NATURAL JOIN nba_player NATURAL JOIN nba_player_stats WHERE numberRound = 1 AND numberRoundPick = 30;")
    self.represent_queries('Average points of the 1st round 30th pick of all draft', table_schema, data)
  
  def find_dallas_player(self):
    table_schema, data = self.db.return_query_table("SELECT idPlayer as id, namePlayer as name, toYear - fromYear as playIn from nba_player natural join team where cityName = 'Dallas' and playIn > 10 order by playIn DESC")
    self.represent_queries('Players who play for Dallas more than 10 years order desc', table_schema, data)
 
  def count_num_player_country(self):
    table_schema, data = self.db.return_query_table("Select idPlayer as id, namePlayer as name, toYear - fromYear as playedYear from nba_player where isActive = 'Active' order by toYear - fromYear DESC limit 10")
    self.represent_queries('Count the number of players from each country order by number of players desc', table_schema, data)
    
  def player_attende_7_allstar(self):
    table_schema, data = self.db.return_query_table("CREATE VIEW 'Q3' AS Select idPlayer as id, namePlayer as name, toYear - fromYear as playedYear from nba_player where isActive = 'Active' order by toYear - fromYear DESC limit 10")
    self.represent_queries('Players who attended more than 7 allstar games', table_schema, data)
  
  def most_all_star(self):
    table_schema, data = self.db.return_query_table("SELECT namePlayer, count(idPlayer) as numAllStarGames FROM allstar_player NATURAL JOIN nba_player GROUP BY idPlayer ORDER BY numAllStarGames DESC LIMIT 1;")
    self.represent_queries('Most teams with all star games', table_schema, data)
  
  
  def player_longest_played(self):
    table_schema, data = self.db.return_query_table("Select idPlayer as id, namePlayer as name, toYear - fromYear as playedYear from nba_player where isActive = 'Active' order by toYear - fromYear DESC limit 10")
    self.represent_queries('Player with longest played years in NBA', table_schema, data)
  
  
  def team_highest_mark_game(self):
    table_schema, data = self.db.return_query_table("SELECT count(idPlayer) as playerNumber, nickname as teamName, sum(points) from nba_player natural join team natural join nba_player_stats where isActive ='Active' group by nickname order by sum(points) DESC")
    self.represent_queries('Team with highest average mark in game in current', table_schema, data)
    
  def top_5_oversea_players(self):
    table_schema, data = self.db.return_query_table("SELECT idplayer as id, namePlayer, country, nickname, points from nba_player natural join nba_player_stats natural join team where isActive ='Active' and country != 'USA' order by points DESC limit 5")
    self.represent_queries('Top 5 players from oversea countries', table_schema, data)
    
  def best_player_NBA(self):
    table_schema, data = self.db.return_query_table("SELECT idplayer as id, namePlayer, nickname, points*0.4+ assists*0.3 + rebounds*0.3  OVA from nba_player NATURAL join nba_player_stats natural join team where isActive ='Active' order by OVA DESC limit 5")
    self.represent_queries('Best player in NBA using given formula', table_schema, data)
    
  def worst_team_NBA(self):
    table_schema, data = self.db.return_query_table("SELECT nickname as team, sum(points)*0.5+sum(rebounds)*0.4+ sum(assists)*0.3 as teamOVA FROM team NATURAL JOIN nba_player_stats natural JOIN nba_player where isActive = 'Active' group by team order by teamOVA")
    self.represent_queries('Worst team in NBA using given formula', table_schema, data)
  
  def team_wins_home_season(self):
    table_schema, data = self.db.return_query_table("Select nickname as team, count(WL_home = 'W') as homeWIN from team NATURAL JOIN game NATURAL JOIN season where year = '2019' and team.idTeam = game.idTeamHome group by team order by homeWIN")
    self.represent_queries('Team get how many wins in their home in a certain season', table_schema, data)
    
    
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