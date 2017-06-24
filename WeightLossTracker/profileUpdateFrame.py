import tkinter as tk


class profileUpdateFrame(tk.Frame):

	def __init__(self,parent,controller):

		tk.Frame.__init__(self,parent)

		self.controller = controller

		self.toUpdateLabel = tk.Label(self, text="Which part of your profile do you want to update??")
		self.toUpdateLabel.grid(row=0,column=0,sticky="nsew")


		self.updateCaloriesButton = tk.Button(self,text="Calories")
		self.updateCaloriesButton.bind("<Button-1>", self.controller.sendToCalorieMenu)
		self.updateCaloriesButton.grid(row=1,column=0,sticky="nsew")

		self.updateWeightButton = tk.Button(self, text="Weight")
		self.updateWeightButton.bind("<Button-1>",self.controller.sendToWeightMenu)
		self.updateWeightButton.grid(row=1,column=1,sticky="nsew")

		self.updateActLvlButton = tk.Button(self,text="Activity Level")
		self.updateActLvlButton.bind("<Button-1>")
		self.updateActLvlButton.grid(row=2,column=0,sticky="nsew")


		self.updateDeficitButton = tk.Button(self,text="Caloric Deficit")
		self.updateDeficitButton.bind("<Button-1>")
		self.updateDeficitButton.grid(row=2,column=1,sticky="nsew")

		self.backButton = tk.Button(self,text="Back")
		self.backButton.bind("<Button-1>", self.controller.backToMainMenu)
		self.backButton.grid(row=3,column=0,sticky="nsew")