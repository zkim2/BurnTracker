import tkinter as tk

class deleteCalorieFrame(tk.Frame):

	def __init__(self,parent,controller):

		tk.Frame.__init__(self,parent)

		self.controller = controller

		self.dateString = tk.StringVar() 

		self.grid_columnconfigure(0,weight=1)
		self.grid_columnconfigure(1,weight=2)
		self.grid_columnconfigure(2,weight=2)

		self.grid_rowconfigure(0,weight=1)
		self.grid_rowconfigure(1,weight=1)
		self.grid_rowconfigure(2,weight=1)
		self.grid_rowconfigure(3,weight=1)
		
		
		self.deleteCalorieLabel = tk.Label(self,text="Deleting Calories", font=("Helvetica", 20))
		self.deleteCalorieLabel.grid(row=0,column=1, sticky="nsew")

		self.success = tk.Label(self,text="")
		self.success.grid(row=0,column=0,sticky="nsew")


		self.dateToDelete= tk.Label(self,text="Date of calories(MM/DD/YY):")
		self.dateToDelete.grid(row=1,column=0, sticky="nsew")


		self.dateToDeleteEntry= tk.Entry(self, textvariable = self.dateString)
		self.dateToDeleteEntry.grid(row=1,column=1,sticky="nsew")


		self.submitButton = tk.Button(self,text="Submit")
		self.submitButton.bind("<Button-1>",self.controller.submitDeleteCalories)
		self.submitButton.grid(row=2,column=1,sticky="nsew")


		self.backButton = tk.Button(self,text="Back")
		self.backButton.bind("<Button-1>", self.controller.sendToCalorieMenu)
		self.backButton.grid(row=3,column=1,sticky="nsew")



	def clearFrame(self):

		self.dateString.set("")
	
		self.success['text'] = ""

	def displaySuccess(self):

		self.success['text'] = "Success!!!"
		self.success['fg'] = "blue"