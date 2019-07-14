import matplotlib as mtpl
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import numpy as np
import tkinter as tk 
from DatabaseHandle import DatabaseHandle



class Grapher(tk.Frame):

	def __init__(self, master, **kw):
		super().__init__(**kw) 


	def draw_it(self, *args, **kwargs):

		x = [1,2,3,4,5,6,7,8,9,10,11,12,13]
		y = [0,6,4,8,9,8,9,10,8,5,3,2,1]
		fig = Figure(figsize = (1,1), dpi = 100)
		fig.add_subplot(111).plot(x,y)

		self.canvas = FigureCanvasTkAgg(fig, self)
		self.canvas.draw()
		self.canvas.get_tk_widget().pack(fill = 'both', expand= 1)


