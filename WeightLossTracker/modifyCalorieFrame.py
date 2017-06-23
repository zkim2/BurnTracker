import tkinter as tk


class modifyCalorieFrame(tk.Frame):

	def __init__(self,parent,controller):

		tk.Frame.__init__(self,parent)

		self.controller = controller

		self.dateString = tk.StringVar() #will parse in controller

		self.calorieVar = tk.DoubleVar()

		self.modifyingCalorieLabel = tk.Label(self,text="Modifying Calories")
		self.modifyingCalorieLabel.grid(row=0,column=0, sticky="nsew")

		self.success = tk.Label(self,text="")
		self.success.grid(row=0,column=1,sticky="nsew")


		self.dateOfCalories = tk.Label(self,text="Date to modify(MM/DD/YY):")
		self.dateOfCalories.grid(row=1,column=0, sticky="nsew")

		self.dateOfCaloriesEntry = tk.Entry(self, textvariable = self.dateString)
		self.dateOfCaloriesEntry.grid(row=1,column=1,sticky="nsew")


		self.updatedCalories = tk.Label(self,text="Updated Calories:")
		self.updatedCalories.grid(row=2,column=0,sticky="nsew")


		self.updatedCaloriesEntry = tk.Entry(self,textvariable=self.calorieVar)
		self.updatedCaloriesEntry.grid(row=2,column=1,sticky="nsew")


		self.submitButton = tk.Button(self,text="Submit")
		self.submitButton.bind("<Button-1>")
		self.submitButton.grid(row=3,column=0,sticky="nsew")


	def clearFrame(self):

		self.dateString.set("")
		self.calorieVar.set(0.0)

		self.success['text'] = ""


	def displaySuccess(self):

		self.success['text'] = "Success!!!"

