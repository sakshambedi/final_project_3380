"""
Team : Team-59

"""

import sqlite3
import json

class DataBase:
  def __init__(self, create=True):
    self.current = None
    try: 
      print("Connecting to database...")
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
    
    
  def all_players(self):
    sql = "SELECT * FROM nba_player limit 10"
    self.current.execute(sql)
    rows = self.current.fetchall()
    for row in rows:
      print(row)