import tkinter as tk

class addDailyWeightFrame(tk.Frame):

	def __init__(self, parent, controller):

		tk.Frame.__init__(self,parent)

		self.controller = controller

		self.weightVar = tk.DoubleVar()

		self.enterWeight = tk.Label(self, text="Enter in your daily weight:")
		self.enterWeight.grid(row=0,column=0,sticky="nsew")

		self.success = tk.Label(self,text="")
		self.success.grid(row=0,column=1,sticky="nsew")

		self.enterWeightEntry = tk.Entry(self,textvariable=self.weightVar)
		self.enterWeightEntry.grid(row=1,column=0,sticky="nsew")

		self.submitButton = tk.Button(self, text="Submit")
		self.submitButton.bind("<Button-1>", self.controller.submitDailyWeight)
		self.submitButton.grid(row=2,column=0,sticky="nsew")

		self.backButton = tk.Button(self,text="Back")
		self.backButton.bind("<Button-1>", self.controller.backToMainMenu)
		self.backButton.grid(row=2,column=1,sticky="nsew")

	def clearFrame(self):

		self.weightVar.set(0.0)
		self.success['text'] = ""

	def displaySuccess(self):

		self.success['text'] = "Success!!"