import tkinter as tk

class addDailyCaloriesFrame(tk.Frame):

	def __init__(self, parent, controller):

		tk.Frame.__init__(self,parent)

		self.controller = controller

		self.caloriesVar = tk.DoubleVar()

		self.enterCalories = tk.Label(self, text="Enter in your daily caloric intake:")
		self.enterCalories.grid(row=0,column=0,sticky="nsew")

		self.success = tk.Label(self,text="")
		self.success.grid(row=0,column=1, sticky="nsew")

		self.enterCaloriesEntry = tk.Entry(self,textvariable=self.caloriesVar)
		self.enterCaloriesEntry.grid(row=1,column=0,sticky="nsew")

		self.submitButton = tk.Button(self, text="Submit")
		self.submitButton.bind("<Button-1>", self.controller.submitDailyCalories)
		self.submitButton.grid(row=2,column=0,sticky="nsew")

		self.backButton = tk.Button(self,text="Back")
		self.backButton.bind("<Button-1>", self.controller.backToMainMenu)
		self.backButton.grid(row=2,column=1,sticky="nsew")


	def clearFrame(self):

		self.caloriesVar.set(0.0)
		self.success['text'] = ""


	def displaySuccess(self):

		self.success['text'] = "Success!!!"