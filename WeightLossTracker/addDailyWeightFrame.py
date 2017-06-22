import tkinter as tk

class addDailyWeightFrame(tk.Frame):

	def __init__(self, parent, controller):

		tk.Frame.__init__(self,parent)

		self.weightVar = tk.DoubleVar()

		self.enterWeight = tk.Label(self, text="Enter in your daily weight:")
		self.enterWeight.grid(row=0,column=0,sticky="nsew")

		self.enterWeightEntry = tk.Entry(self,textvariable=self.weightVar)
		self.enterWeightEntry.grid(row=1,column=0,sticky="nsew")

		self.submitButton = tk.Button(self, text="Submit")
		self.submitButton.bind("<Button-1>")
		self.submitButton.grid(row=2,column=0,sticky="nsew")
