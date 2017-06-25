import tkinter as tk

class addDailyWeightFrame(tk.Frame):

	def __init__(self, parent, controller):

		tk.Frame.__init__(self,parent)

		self.controller = controller

		self.weightVar = tk.DoubleVar()


		self.grid_columnconfigure(0, weight=1)
		self.grid_columnconfigure(1, weight=1)
		self.grid_columnconfigure(2, weight=1)

		self.grid_rowconfigure(0, weight=1)
		self.grid_rowconfigure(1, weight=0)
		self.grid_rowconfigure(2, weight=0)
		self.grid_rowconfigure(3, weight=1)
		self.grid_rowconfigure(4, weight=1)


		self.enterWeight = tk.Label(self, text="Enter in your daily weight(lbs):", font=("Helvetica", 25))
		self.enterWeight.grid(row=0,column=1,sticky="nsew")

		self.success = tk.Label(self,text="", font=("Helvetica", 15))
		self.success.grid(row=1,column=1,sticky="nsew")

		self.enterWeightEntry = tk.Entry(self,textvariable=self.weightVar, font=("Helvetica", 20))
		self.enterWeightEntry.grid(row=2,column=1,sticky="nsew")

		self.submitButton = tk.Button(self, text="Submit", width=20,font=("Helvetica", 15))
		self.submitButton.bind("<Button-1>", self.controller.submitDailyWeight)
		self.submitButton.grid(row=3,column=1)

		self.backButton = tk.Button(self,text="Back", width=20,font=("Helvetica", 15))
		self.backButton.bind("<Button-1>", self.controller.backToMainMenu)
		self.backButton.grid(row=4,column=1)

	def clearFrame(self):

		self.weightVar.set(0.0)
		self.success['text'] = ""

	def displaySuccess(self):

		self.success['text'] = "Success!!"
		self.success['fg'] = "blue"


	def fieldInvalid(self):

		self.success['text'] = "Invalid Weight Entered **"
		self.success['fg'] = "red"