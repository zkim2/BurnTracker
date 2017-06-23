import tkinter as tk 

class visualizeProgressFrame(tk.Frame):

	def __init__(self,parent,controller):

		tk.Frame.__init__(self,parent)

		self.controller = controller

		self.whichVisualizationLabel = tk.Label(self,text="Which graph would you like to see?")
		self.whichVisualizationLabel.grid(row=0,column=0,sticky="nsew")


		self.weightGraphButton = tk.Button(self, text="Weight Graph")
		self.weightGraphButton.bind("<Button-1>")
		self.weightGraphButton.grid(row=1,column=0,sticky="nsew")


		self.calorieGraphButton = tk.Button(self,text="Calorie Graph")
		self.calorieGraphButton.bind("<Button-1>")
		self.calorieGraphButton.grid(row=2,column=0,sticky="nsew")

