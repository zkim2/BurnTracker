import tkinter as tk


class modifyWeightFrame(tk.Frame):

	def __init__(self,parent,controller):

		tk.Frame.__init__(self,parent)

		self.controller = controller

		self.dateString = tk.StringVar() #will parse in controller

		self.weightVar = tk.DoubleVar()

		self.modifyingWeightLabel = tk.Label(self,text="Modifying Weight")
		self.modifyingWeightLabel.grid(row=0,column=0, sticky="nsew")

		self.success = tk.Label(self,text="")
		self.success.grid(row=0,column=1,sticky="nsew")


		self.dateOfWeight = tk.Label(self,text="Date to modify(MM/DD/YY):")
		self.dateOfWeight.grid(row=1,column=0, sticky="nsew")

		self.dateOfWeightEntry = tk.Entry(self, textvariable = self.dateString)
		self.dateOfWeightEntry.grid(row=1,column=1,sticky="nsew")


		self.updatedWeight = tk.Label(self,text="Updated Weight:")
		self.updatedWeight.grid(row=2,column=0,sticky="nsew")


		self.updatedWeightEntry = tk.Entry(self,textvariable=self.weightVar)
		self.updatedWeightEntry.grid(row=2,column=1,sticky="nsew")


		self.submitButton = tk.Button(self,text="Submit")
		self.submitButton.bind("<Button-1>", self.controller.submitModifyWeight)
		self.submitButton.grid(row=3,column=0,sticky="nsew")

		self.backButton = tk.Button(self,text="Back")
		self.backButton.bind("<Button-1>", self.controller.sendToWeightMenu)
		self.backButton.grid(row=3,column=1,sticky="nsew")

		self.quitButton = tk.Button(self,text="Quit")
		self.quitButton.bind("<Button-1>", self.controller.exit)
		self.quitButton.grid(row=3,column=2,sticky="nsew")


	def clearFrame(self):

		self.dateString.set("")
		self.weightVar.set(0.0)

		self.success['text'] = ""


	def displaySuccess(self):

		self.success['text'] = "Success!!!"


