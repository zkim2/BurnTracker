import tkinter as tk

class deleteWeightFrame(tk.Frame):

	def __init__(self,parent,controller):

		tk.Frame.__init__(self,parent)

		self.controller = controller

		self.dateString = tk.StringVar() 


		self.grid_columnconfigure(0,weight=1)
		self.grid_columnconfigure(1,weight=1)
		self.grid_columnconfigure(2,weight=1)

		self.grid_rowconfigure(0,weight=1)
		self.grid_rowconfigure(1,weight=0)
		self.grid_rowconfigure(2,weight=0)
		self.grid_rowconfigure(3,weight=1)
		self.grid_rowconfigure(4,weight=1)
		


		self.deleteWeightLabel = tk.Label(self,text="Deleting Weight", font=("Helvetica", 25))
		self.deleteWeightLabel.grid(row=0,column=1, sticky="nsew")

		self.success = tk.Label(self,text="", font=("Helvetica", 15))
		self.success.grid(row=1,column=1,sticky="nsew")


		self.dateToDelete= tk.Label(self,text="Date to delete(MM/DD/YY):", font=("Helvetica", 20))
		self.dateToDelete.grid(row=2,column=0, sticky="nsew")


		self.dateToDeleteEntry= tk.Entry(self, textvariable = self.dateString ,font=("Helvetica", 20))
		self.dateToDeleteEntry.grid(row=2,column=1,sticky="nsew")


		self.submitButton = tk.Button(self,text="Submit", width=20, font=("Helvetica", 15))
		self.submitButton.bind("<Button-1>", self.controller.submitDeleteWeight)
		self.submitButton.grid(row=3,column=1)


		self.backButton = tk.Button(self,text="Back", width=20, font=("Helvetica", 15))
		self.backButton.bind("<Button-1>", self.controller.sendToWeightMenu)
		self.backButton.grid(row=4,column=1)



	def clearFrame(self):

		self.dateString.set("")
	
		self.success['text'] = ""

	def displaySuccess(self):

		self.success['text'] = "Success!!!"
		self.success['fg'] = "blue"

	def fieldInvalid(self):

		self.success['text'] = "Invalid Date or no such date **"
		self.success['fg'] = "red"
		