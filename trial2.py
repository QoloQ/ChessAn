import tkinter as tk
from tkinter import ttk
from Grapher import Grapher


HEIGHT = 500
WIDTH = 700



class MainApp():

	def __init__(self, master = None, y = 10, x = "sample string"):

		print('initing MainApp')
		self.master = master  
		self.y = y
		self.x = x

		""" Creating Menu """

		self.menu = tk.Menu(self.master)
		self.master.config(menu = self.menu)
		self.master.geometry("{}x{}+0+0".format(WIDTH, HEIGHT))
		self.menu.add_command(label="Import")
		self.checkvar = tk.IntVar()
		self.menu.add_checkbutton(label = "Check", command = lambda: print(self.checkvar.get()), variable = self.checkvar, onvalue = 1, offvalue = 0, indicatoron = False)
		self.menu.add_radiobutton(label = "Radio")

		self.filemenu = tk.Menu(self.menu, tearoff = 0, takefocus = 0)
		self.filemenu.add_command(label = "Open")
		self.filemenu.add_command(label = "Edit")
		self.filemenu.add_command(label = "Exit", command = self.master.quit)
		self.menu.add_cascade(label = "Cascade", menu = self.filemenu)


		""" Creating Frame Layout """

		self.leftFrame = tk.Frame(self.master, bg = "black")
		self.leftFrame.grid(rowspan = 4, sticky = "nsew")
		self.leftFrame.rowconfigure(0, weight = 1)
		self.leftFrame.columnconfigure(0, weight = 1)
		

		""" Inserting Widgets"""	
		def change():
			if isinstance(self.cinema, Grapher):
				self.cinema = InsideButtFrame(self.master, bg = "pink")
				self.cinema.grid(row = 1, column = 2, rowspan = 3, columnspan = 2, sticky = "nsew")
				self.master.update()

			elif isinstance(self.cinema, InsideButtFrame):
				self.cinema= Grapher(self.master)
				self.cinema.draw_it()
				self.cinema.grid(row = 1, column = 2, rowspan = 3, columnspan = 2, sticky = "nsew")
				self.master.update()

			else:
				print("Unknown instance")



		self.butt1 = tk.Button(self.leftFrame, text="Deep Shit", bg = "darkgrey", relief = "groove", bd = 1, font = ("Verdana", 8))
		self.butt2 = tk.Button(self.leftFrame, text="CHNG", bg = "darkgrey", relief = "groove", bd = 1, font = ("Verdana", 8))
		self.butt3 = ttk.Button(self.leftFrame, text = "CHANGE", command = change )
		self.butt4 = tk.Button(self.leftFrame, text = "Deep Stuff")
		self.butt1.pack(fill = "x")
		self.butt2.pack(fill = "x")
		self.butt3.pack(fill = "x")
		self.butt4.pack(fill = "x")

		""" STATIV """

		self.ins_but = InsideButtFrame(self.master, bg = "lightgreen")
		self.ins_but.grid(row = 1, column = 1, rowspan = 3, sticky = "nsew")



		""" CINEMA """		
		# self.cinema =tk.Label(self.master, text = "Don Carlos", bg = "darkgrey")
		# self.cinema.grid(row = 1, column = 2, rowspan = 3, columnspan = 2, sticky = "nsew")

		self.cinema = Grapher(self.master, bg = "green")
		self.cinema.draw_it(x = "random test shit")
		self.cinema.grid(row = 1, column = 2, rowspan = 3, columnspan = 2, sticky = "nsew")



		self.master.rowconfigure(0, weight = 1)
		self.master.rowconfigure(1, weight = 1)
		self.master.rowconfigure(2, weight = 1)
		self.master.rowconfigure(3, weight = 1)
		self.master.columnconfigure(0, weight = 1)
		self.master.columnconfigure(1, weight = 4)
		self.master.columnconfigure(2, weight = 4)
		self.master.columnconfigure(3, weight = 4)



		""" Creating layout"""

		# frame = StartPage(self.container, self)
		# frame.tkraise()



class InsideButtFrame(tk.Frame):
	def __init__(self, master, **kw):
		super().__init__(**kw)

		# self.options = tk.Listbox(self, selectmode = "nrowse")
		# self.options.insert(1, "Player")
		# self.options.insert(2, "Color")
		# self.options.insert(3, "Opening")
		# self.options.pack(fill = "both", expand = False)

		self.variable = tk.StringVar(self.master)
		self.variable.set("one") # default value

		self.w = tk.OptionMenu(self, self.variable, "one", "two", "threeeeeeeeeeeee")
		self.w.configure(width = 1)
		self.w.pack(fill = 'x')	




		def chng(self):
			self.inside_label = tk.Button(self, text = "not op", bg = "orange")
			self.inside_label.pack(fill = "both")
			self.master.update()

class Replica(MainApp):
	def __init__(self, *args, **kw):
		print("initing Replica")
		super().__init__(*args, **kw)
		# MainApp.__init__(self, *args, **kw)
		print(args)
		print(kw)
		self.why = "gg why works"
	
class Triplica(Replica):
	pass




if __name__ =="__main__":

	root = tk.Tk()
	ttk.Style(root).theme_use('alt')
	app = Triplica(root)
	root.mainloop()
