import pygame
import sys
import sqlite3


class User():

    def __init__(self,username):
        
        self.username = username
        user = self.read()

        
        if (user != None):
            self.id = user[0]
            self.score = user[2]
        else:
            self.create()
            user = self.read()
            self.id = user[0]
            self.score = user[2]
            

    def read(self):
        with sqlite3.connect("breakout_db.db") as conexion:
            results = conexion.execute("SELECT * FROM users WHERE username = ?", (self.username, ))
            return results.fetchone()
        
    
    def create(self):
        try:
            with sqlite3.connect("breakout_db.db") as conexion:
                conexion.execute("INSERT INTO users (username,score) values (?,?)", (self.username,0,))
                conexion.commit()
        except:
            print("Error")

    def __str__(self):
        return "Id: " + str(self.id) + ", Username: " + self.username + ", Score: " + str(self.score)


    def update_score(self,current_score):
        
        if current_score > self.score:
            with sqlite3.connect("breakout_db.db") as conexion:
                cursor = conexion.execute("UPDATE users SET score = ? WHERE id = ?",(current_score,self.id,))
                conexion.commit()


        