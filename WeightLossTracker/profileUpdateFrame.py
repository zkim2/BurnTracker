import tkinter as tk


class profileUpdateFrame(tk.Frame):

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
		self.grid_rowconfigure(4,weight=1)
		self.grid_rowconfigure(5,weight=1)

		self.toUpdateLabel = tk.Label(self, text="Which part of your profile do you want to update??", font=("Helvetica", 20))
		self.toUpdateLabel.grid(row=0,column=1,sticky="nsew")


		self.updateCaloriesButton = tk.Button(self,text="Calories")
		self.updateCaloriesButton.bind("<Button-1>", self.controller.sendToCalorieMenu)
		self.updateCaloriesButton.grid(row=1,column=1,sticky="nsew")

		self.updateWeightButton = tk.Button(self, text="Weight")
		self.updateWeightButton.bind("<Button-1>",self.controller.sendToWeightMenu)
		self.updateWeightButton.grid(row=2,column=1,sticky="nsew")

		self.updateActLvlButton = tk.Button(self,text="Activity Level")
		self.updateActLvlButton.bind("<Button-1>", self.controller.sendToModifyActLvl)
		self.updateActLvlButton.grid(row=3,column=1,sticky="nsew")


		self.updateDeficitButton = tk.Button(self,text="Caloric Deficit")
		self.updateDeficitButton.bind("<Button-1>", self.controller.sendToModifyIntensity)
		self.updateDeficitButton.grid(row=4,column=1,sticky="nsew")

		self.backButton = tk.Button(self,text="Back")
		self.backButton.bind("<Button-1>", self.controller.backToMainMenu)
		self.backButton.grid(row=5,column=1,sticky="nsew")