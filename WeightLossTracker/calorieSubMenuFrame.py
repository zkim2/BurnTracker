import tkinter as tk 

class calorieSubMenuFrame(tk.Frame):

	def __init__(self, parent, controller):

		tk.Frame.__init__(self,parent)

		self.controller = controller

		self.whatToChangeLabel = tk.Label(self, text="What do you want to do with your caloric data?")
		self.whatToChangeLabel.grid(row=0,column=0,sticky="nsew")


		self.deleteCalorieButton = tk.Button(self,text="Delete calories of a specific date")
		self.deleteCalorieButton.bind("<Button-1>")
		self.deleteCalorieButton.grid(row=1,column=0,sticky="nsew")

		self.modifyCalorieButton = tk.Button(self,text="Modify calories of a specific date")
		self.modifyCalorieButton.bind("<Button-1>", self.controller.sendToModifyCalories)
		self.modifyCalorieButton.grid(row=1,column=1,sticky="nsew")


