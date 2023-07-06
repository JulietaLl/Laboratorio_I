
import pygame
import sys
import sqlite3



class RankingOutput():
    
    def parse_tuple_list(self,tuple_list):
        return "#1 - " + tuple_list[0][0] + "    " +  str(tuple_list[0][1]) +  " \n" + "#2 - " + tuple_list[1][0] + "    " + str(tuple_list[1][1]) + "\n" + "3# - " + tuple_list[2][0] + "    " + str(tuple_list[2][1])


    def parse_top_one(self,tuple_list):
        return "#1 - " + tuple_list[0][0] + "    " +  str(tuple_list[0][1])
    

    def parse_top_two(self,tuple_list):
        return "#2 - " + tuple_list[1][0] + "       " +  str(tuple_list[1][1])
    
    
    def parse_top_three(self,tuple_list):
        return "#3 - " + tuple_list[2][0] + "       " +  str(tuple_list[2][1])