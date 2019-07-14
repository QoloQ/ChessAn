
user = "JohnyJJ"
file = open('pgns.pgn')
file_lines = file.readlines()
Lgame, Ldate, Lopening, Lopponent, Ltimecontrol, Lresult, Lmoves, Lcolor, LprovRes, Ltime = [],[],[],[],[],[],[],[],[],[]
num_of =0
dic = {}

import re
# with open('donepgn.txt','w') as done_file:
# 	done_file.writelines(file_lines)




class PGNparser():

	def __init__(self):
		pass
		
	
	def getlists(pgn):	
		global num_of, Lgame, Ldate, Lopening, Lopponent, Ltimecontrol,Lresult, Lmoves, Lcolor, LprovRes, Ltime
		pattern_qts = r'"(.*?)"'


		for line in pgn:
			if "Event" in line:	
				#Game
				num_of += 1
				Lgame.append("game no. {}".format(num_of))
				
			
			elif "ECO " in line and "Control" not in line:
				#Opening
				Lopening.append(str(line[6:9]))
			
			elif "UTCDate" in line:
				#Date
				Ldate.append('\\'.join(str(line.strip('[UTCDate "]\n')).split('.')))
			
			elif "UTCTime" in line:
				#Timede
				Ltime.append(str(line[10:18]))
				
			elif "White " in line and user not in line:		
				#Opponent, color
				Lcolor.append("Black")
				# x = (line.replace('White ','').strip('\ \"[]'))
				x = re.findall(pattern_qts, line).pop()
				Lopponent.append(x)
			elif "Black " in line and user not in line:
				#Opponent, color
				Lcolor.append("White")
				# x = (line.replace('Black ','').strip('\ \"[]'))
				x = re.findall(pattern_qts, line).pop()
				Lopponent.append(x)
				
			elif line.startswith("1") or line.startswith("0",1) or line.startswith("1",1):							
				#Moves, first one is needed for 1. e4... but there are rare cases of 
				#aborted games, which have 0-1 instead of moves (had one in 4000 games...)
				Lmoves.append(line)
				
			elif "Result" in line:
				#Numbers only, dont return
				if "0-1" in line:
					LprovRes.append("0-1")
				elif "1/2-1/2" in line:
					LprovRes.append("1/2 - 1/2")
				else:
					LprovRes.append("1-0")
			else: pass
			
		for num, col in zip(LprovRes, Lcolor):
			if num == "1-0" and col == "White": Lresult.append('Win')
			elif num == "0-1" and col == "Black": Lresult.append('Win')
			elif num == "1/2 - 1/2": Lresult.append('Draw')
			elif num == "1-0" and col == "Black": Lresult.append('Lose')
			elif num == "0-1" and col == "White": Lresult.append('Lose')
			else: 
				print ("something is wrong appending Lresult list; values: ", num, col)
				break
		
		
		
		
		return Lgame, Lopening, Ldate, Lopponent, Lresult, Lmoves, Lcolor, Ldate, Ltime
		
