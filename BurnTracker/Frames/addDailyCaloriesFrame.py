import tkinter as tk

class addDailyCaloriesFrame(tk.Frame):

	def __init__(self, parent, controller):

		tk.Frame.__init__(self,parent)

		self.controller = controller

		self.caloriesVar = tk.DoubleVar()
		self.configure(bg="#586BE4")

		self.grid_columnconfigure(0, weight=1)
		self.grid_columnconfigure(1, weight=1)
		self.grid_columnconfigure(2, weight=1)

		self.grid_rowconfigure(0, weight=1)
		self.grid_rowconfigure(1, weight=0)
		self.grid_rowconfigure(2, weight=0)
		self.grid_rowconfigure(3, weight=1)
		self.grid_rowconfigure(4, weight=1)

		self.enterCalories = tk.Label(self, text="Enter in your daily caloric intake:", font=("Helvetica", 25),bg="#586BE4")
		self.enterCalories.grid(row=0,column=1, sticky="nsew")

		self.success = tk.Label(self,text="",font=("Helvetica", 15),bg="#586BE4")
		self.success.grid(row=1,column=1, sticky="nsew")

		self.enterCaloriesEntry = tk.Entry(self,textvariable=self.caloriesVar,  font=("Helvetica", 20), bd=0)
		self.enterCaloriesEntry.grid(row=2,column=1, sticky="nsew")

		self.submitButton = tk.Button(self, text="Submit", width=20, font=("Helvetica", 15),highlightbackground="#586BE4")
		self.submitButton.bind("<Button-1>", self.controller.submitDailyCalories)
		self.submitButton.grid(row=3,column=1)

		self.backButton = tk.Button(self,text="Back", width=20, font=("Helvetica", 15),highlightbackground="#586BE4")
		self.backButton.bind("<Button-1>", self.controller.backToMainMenu)
		self.backButton.grid(row=4,column=1)


	def clearFrame(self):

		self.caloriesVar.set(0.0)
		self.success['text'] = ""


	def displaySuccess(self):

		self.success['text'] = "Success!!!"
		self.success['fg'] = "blue"


	def fieldInvalid(self):

		self.success['text'] = "Invalid Calories Entered **"
		self.success['fg'] = "red"