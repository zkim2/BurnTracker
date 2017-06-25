import tkinter as tk 

class visualizeProgressFrame(tk.Frame):

	def __init__(self,parent,controller):

		tk.Frame.__init__(self,parent)

		self.controller = controller

		self.grid_columnconfigure(0,weight=1)
		self.grid_columnconfigure(1,weight=1)
		self.grid_columnconfigure(2,weight=1)

		self.grid_rowconfigure(0,weight=1)
		self.grid_rowconfigure(1,weight=1)
		self.grid_rowconfigure(2,weight=1)
		self.grid_rowconfigure(3,weight=1)

		self.whichVisualizationLabel = tk.Label(self,text="Which graph would you like to see?", font=("Helvetica", 25))
		self.whichVisualizationLabel.grid(row=0,column=1,sticky="nsew")


		self.weightGraphButton = tk.Button(self, text="Weight Graph", width=20, font=("Helvetica", 15))
		self.weightGraphButton.bind("<Button-1>", self.controller.graphWeightLoss)
		self.weightGraphButton.grid(row=1,column=1)


		self.calorieGraphButton = tk.Button(self,text="Calorie Graph", width=20, font=("Helvetica", 15))
		self.calorieGraphButton.bind("<Button-1>", self.controller.graphCalories)
		self.calorieGraphButton.grid(row=2,column=1)


		self.backButton = tk.Button(self,text="Back", width=20, font=("Helvetica", 15))
		self.backButton.bind("<Button-1>", self.controller.backToMainMenu)
		self.backButton.grid(row=3,column=1)

