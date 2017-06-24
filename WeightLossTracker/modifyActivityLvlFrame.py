import tkinter as tk


class modifyActivityLvlFrame(tk.Frame):

	def __init__(self,parent,controller):

		tk.Frame.__init__(self,parent)

		self.controller = controller


		self.actLvlVar = tk.IntVar()


		self.grid_columnconfigure(0,weight=1)
		self.grid_columnconfigure(1,weight=1)
		self.grid_columnconfigure(2,weight=1)

		self.grid_rowconfigure(0,weight=1)
		self.grid_rowconfigure(1,weight=1)
		self.grid_rowconfigure(2,weight=1)
		self.grid_rowconfigure(3,weight=1)
		

		self.modifyActLvlLabel = tk.Label(self,text="What is your new activity level? (1-5)", font=("Helvetica", 20))
		self.modifyActLvlLabel.grid(row=0,column=1,sticky="nsew")


		self.success = tk.Label(self,text="")
		self.success.grid(row=0,column=0,sticky="nsew")

		self.modifyActLvlEntry = tk.Entry(self,textvariable=self.actLvlVar)
		self.modifyActLvlEntry.grid(row=1,column=1,sticky="nsew")

		self.submitButton = tk.Button(self,text="Submit")
		self.submitButton.bind("<Button-1>",self.controller.submitModifyActLvl)
		self.submitButton.grid(row=2,column=1, sticky="nsew")

		self.backButton = tk.Button(self,text="Back")
		self.backButton.bind("<Button-1>", self.controller.updateProfileInfo)
		self.backButton.grid(row=3,column=1,sticky="nsew")


	def clearFrame(self):

		self.actLvlVar.set(0)
		self.success['text'] = ""

	def displaySuccess(self):

		self.success['text'] = "Success!!!"
		self.success['fg'] = "blue"
