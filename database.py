"""
Team : Team-59

"""

import sqlite3
import pandas as pd 

class DataBase:
  def __init__(self, create=True):
    self.current = None
    try: 
      # print("Connecting to database...")
      self.con = sqlite3.connect('database.db')
      self.current = self.con.cursor()
      if create :
        self.create_tables()
        self.read_in_data()
        self.con.commit()
    except Exception as e:
      print("Cannot connect to the database")
      print("Here is the detailed log :  ")
      print(e)
      
    
  """
  Summary : Closing the connection to the database
  """
  def close(self):
    self.con.close() 
    
  
  """
  Summary : getting a table based upon the name of the table 
            refactored code from 
  """
  def get_table(self, table_name):
    sql = "SELECT * FROM " + table_name
    # print("Query : " + sql) 
    # just to get the column names , no other use atm 
    schema = pd.read_sql_query(sql, self.con)
    self.current.execute(sql)
    rows = self.current.fetchall()
    
    
    table_schema = []
    for each_row in schema:
      table_schema.append(each_row) 
    
    # print(table_schema)
    return table_schema, rows 
  

  def return_query_table(self, sql_command):
    sql = str(sql_command)
    # "SELECT cityName, nickname, count(WL_away) as numWins FROM GAME JOIN team ON idTeamAway=idTeam WHERE WL_away = 'W' GROUP BY idTeam ORDER BY numWins DESC LIMIT 3;"
    schema = pd.read_sql_query(sql, self.con)
    self.current.execute(sql)
    rows = self.current.fetchall()
    
    
    table_schema = []
    for each_row in schema:
      table_schema.append(each_row) 
    
    # print(table_schema)
    return table_schema, rows 