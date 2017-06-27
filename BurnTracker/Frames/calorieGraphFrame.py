import tkinter as tk

import matplotlib
matplotlib.use("TkAgg")

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib import pyplot as plt
from matplotlib.figure import Figure



class calorieGraphFrame(tk.Frame):


	def __init__(self,parent,controller):

		tk.Frame.__init__(self,parent)

		self.controller = controller

		self.configure(bg="#586BE4")

		self.grid_columnconfigure(0,weight=1)
		self.grid_columnconfigure(1,weight=1)
		self.grid_columnconfigure(2,weight=1)


		self.displayStr= "Graph of " + self.controller.userProfile.name + " as of " + str(self.controller.todaysDate)

		self.displayStrLabel = tk.Label(self,text=self.displayStr)

		self.displayStrLabel.grid(row=0,column=1,sticky="nsew")


		self.backButton = tk.Button(self,text="Back",width=5, highlightbackground="#586BE4")
		self.backButton.bind("<Button-1>", self.controller.backToVisualizationMenu)
		self.backButton.grid(row=0,column=0)

		f = Figure(figsize=(5,5), dpi=80)

		a = f.add_subplot(111)

		sortedData = sorted(self.controller.userProfile.caloricData.items(), key = lambda d: d[0])
		x,y = zip(*sortedData)
		a.plot(x,y)
		a.set_ylabel('Calories')
		a.set_xlabel('Time (days)')
		canvas = FigureCanvasTkAgg(f,self)

		canvas.show()
		canvas.get_tk_widget().grid(row=1,column=1,sticky="nsew")