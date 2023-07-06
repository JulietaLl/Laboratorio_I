
import pygame
import sys
import sqlite3


class RankingReader():

    def readTopThree(self):
        with sqlite3.connect("breakout_db.db") as conexion:
           result = conexion.execute("SELECT username, score FROM users ORDER BY score DESC LIMIT 3")
           return result.fetchall()
        


