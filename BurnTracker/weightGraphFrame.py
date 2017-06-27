import tkinter as tk
import matplotlib
matplotlib.use("TkAgg")

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib import pyplot as plt
from matplotlib.figure import Figure



class weightGraphFrame(tk.Frame):


	def __init__(self,parent,controller):

		tk.Frame.__init__(self,parent)

		self.controller = controller

		self.configure(bg="#586BE4")


		self.displayStr= "Graph of " + self.controller.userProfile.name + " as of " + str(self.controller.todaysDate)

		self.displayStrLabel = tk.Label(self,text=self.displayStr)

		self.displayStrLabel.grid(row=0,column=1,sticky="nsew")


		f = Figure(figsize=(5,5), dpi=100)

		a = f.add_subplot(111)

		a.plot([1,2,3,4,5,6,7,8],[2,5,4,3,6,7,8,9])


		canvas = FigureCanvasTkAgg(f,self)
		canvas.show()
		canvas.get_tk_widget.grid(row=1)

		"""
		toolbar = NavigationToolbar2TkAgg(canvas,self)

		toolbar.update()
		canvas._tk
		"""