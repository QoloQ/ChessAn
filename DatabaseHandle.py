
""" 
This program is created to parse PGN files and provide data analysis of chess games contained.
Free to use for everyone. 
"""

import sqlite3
import collections as col
import tkinter as tk
from os.path import isfile
from PGNparser import PGNparser as pars 
import requests
import time


with open('pgns.pgn') as file:
	r = file.read()

# qr = requests.get('https://lichess.org/api/games/user/JohnyJJ', params = {'vs' : 'profajz'})
# r = qr.text

Lgame, Lopening, Ldate, Lopponent, Lresult, Lmoves, Lcolor, Ldate, Ltime = pars.getlists(r.splitlines())
# print(Lopponent)


class DatabaseHandle():

	def __init__(self):
		
		self.dbfile = 'chess.db'
		self.conn = sqlite3.connect(self.dbfile)
		self.cursor = self.conn.cursor()

	# def create_connection(self):
	# 	self.conn = sqlite3.connect(self.dbfile)
	# 	self.curs = self.conn.cursor()


	def create_table(self):
		try: 
			self.cursor.execute(""" SELECT * FROM chess_table """)
			print("table existed already")
		except sqlite3.OperationalError:
			self.cursor.execute(""" CREATE TABLE chess_table(id INTEGER PRIMARY KEY, oponent, color, opening, result, moves, _date, _time, CONSTRAINT uq_pers UNIQUE(oponent, _date, _time)) """)
			print("table had to be created")
		except:
			print("unknown error on create_table(self)")
	

	def insert_games(self):
		no_g = 0
		while True:
			try:
				self.cursor.execute("INSERT INTO chess_table (oponent, color, opening, result, moves, _date, _time) VALUES( '{}','{}','{}','{}', '{}','{}','{}')".format(Lopponent[no_g], Lcolor[no_g], Lopening[no_g], Lresult[no_g], Lmoves[no_g], Ldate[no_g], Ltime[no_g]))
				no_g += 1
				print("game inserted")

			except IndexError:
				return
			except sqlite3.IntegrityError:
				print("sqlite3 error", Lopponent[no_g], Lcolor[no_g], Lopening[no_g], Lresult[no_g], '',Ldate[no_g], Ltime[no_g])
				no_g +=1
				# time.sleep(0.05)
				continue

	def commit(self):
		self.conn.commit()

	def close_con(self):
		self.conn.close()


class DataHandler():

	def __init__(self):

		self.handle = DatabaseHandle()
		

	def show_everything(self):
		self.fetch = self.handle.cursor.execute("SELECT * FROM chess_table")
		return self.fetch.fetchall()

	def check_ids(self):
		self.fetch = self.handle.cursor.execute("SELECT id FROM chess_table")
		print(self.fetch)
		return self.fetch.fetchall()

	def show_oponent(self, oponent):
		self.fetch = self.handle.cursor.execute("SELECT * FROM chess_table WHERE oponent ='{}'".format(oponent))
		return self.fetch.fetchall()

	def sql_qeue_make(self, **kw):
		qeue = ""
		for pair in kw.items():
			qeue = qeue + pair[0] + "=" + "'{}'".format(pair[1]) + "AND "
		return qeue[:-4]

	def show_filtered(self, diction):
		qq = self.sql_qeue_make(**diction)
		print(qq)
		self.fetch = self.handle.cursor.execute("SELECT * FROM chess_table WHERE {}".format(qq))
		return self.fetch.fetchall()



def main ():
	handle = DatabaseHandle()
	handle.create_table()
	handle.insert_games()
	handle.commit()
	handle.close_con()

if __name__ == '__main__':
	main()
	data = DataHandler()
	print(data.show_everything()[0])
	dic = {
	'oponent' : 'profajz',
	'color' : 'White',
	'opening' : 'A01'
	}
	# print(data.show_everything())
	# print(data.show_filtered(dic))

