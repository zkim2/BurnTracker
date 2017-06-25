import tkinter as tk 

class calorieSubMenuFrame(tk.Frame):

	def __init__(self, parent, controller):

		tk.Frame.__init__(self,parent)

		self.controller = controller

		self.grid_columnconfigure(0,weight=1)
		self.grid_columnconfigure(1,weight=1)
		self.grid_columnconfigure(2,weight=1)

		self.grid_rowconfigure(0,weight=1)
		self.grid_rowconfigure(1,weight=1)
		self.grid_rowconfigure(2,weight=1)
		self.grid_rowconfigure(3,weight=1)


		self.whatToChangeLabel = tk.Label(self, text="What do you want to do with your caloric data?", font=("Helvetica",25))
		self.whatToChangeLabel.grid(row=0,column=1,sticky="nsew")


		self.deleteCalorieButton = tk.Button(self,text="Delete calories of a specific date", width=40, font=("Helvetica", 15))
		self.deleteCalorieButton.bind("<Button-1>", self.controller.sendToDeleteCalories)
		self.deleteCalorieButton.grid(row=1,column=1)

		self.modifyCalorieButton = tk.Button(self,text="Modify calories of a specific date", width=40, font=("Helvetica", 15))
		self.modifyCalorieButton.bind("<Button-1>", self.controller.sendToModifyCalories)
		self.modifyCalorieButton.grid(row=2,column=1)


		self.backButton = tk.Button(self,text="Back", width=40, font=("Helvetica", 15))
		self.backButton.bind("<Button-1>", self.controller.updateProfileInfo)
		self.backButton.grid(row=3,column=1)
