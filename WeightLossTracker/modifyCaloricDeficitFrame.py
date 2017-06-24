import tkinter as tk


class modifyCaloricDeficitFrame(tk.Frame):

	def __init__(self,parent,controller):

		tk.Frame.__init__(self,parent)

		self.controller = controller

		self.intensityVar = tk.IntVar()

		self.grid_columnconfigure(0,weight=1)
		self.grid_columnconfigure(1,weight=1)
		self.grid_columnconfigure(2,weight=1)

		self.grid_rowconfigure(0,weight=1)
		self.grid_rowconfigure(1,weight=1)
		self.grid_rowconfigure(2,weight=1)
		self.grid_rowconfigure(3,weight=1)

		self.modifyIntensityLabel = tk.Label(self,text="What is your new caloric deficit?", font=("Helvetica", 20))
		self.modifyIntensityLabel.grid(row=0,column=1,sticky="nsew")

		self.success = tk.Label(self,text="")
		self.success.grid(row=0,column=0,sticky="nsew")

		self.modifyIntensityEntry = tk.Entry(self,textvariable=self.intensityVar)
		self.modifyIntensityEntry.grid(row=1,column=1,sticky="nsew")


		self.submitButton = tk.Button(self,text="Submit")
		self.submitButton.bind("<Button-1>", self.controller.submitModifyIntensity)
		self.submitButton.grid(row=2,column=1, sticky="nsew")

		self.backButton = tk.Button(self,text="Back")
		self.backButton.bind("<Button-1>", self.controller.updateProfileInfo)
		self.backButton.grid(row=3,column=1,sticky="nsew")


	def clearFrame(self):

		self.intensityVar.set(0)
		self.success['text'] = ""

	def displaySuccess(self):

		self.success['text'] = "Success!!!"
		self.success['fg'] = "blue"