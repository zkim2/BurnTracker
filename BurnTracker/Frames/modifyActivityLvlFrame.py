import tkinter as tk


class modifyActivityLvlFrame(tk.Frame):

	def __init__(self,parent,controller):

		tk.Frame.__init__(self,parent)

		self.controller = controller

		self.configure(bg="#586BE4")
		self.actLvlVar = tk.IntVar()


		self.grid_columnconfigure(0,weight=1)
		self.grid_columnconfigure(1,weight=1)
		self.grid_columnconfigure(2,weight=1)

		self.grid_rowconfigure(0,weight=1)
		self.grid_rowconfigure(1,weight=0)
		self.grid_rowconfigure(2,weight=0)
		self.grid_rowconfigure(3,weight=1)
		self.grid_rowconfigure(4,weight=1)
		

		self.modifyActLvlLabel = tk.Label(self,text="What is your new activity level? (1-5)", font=("Helvetica", 25),bg="#586BE4")
		self.modifyActLvlLabel.grid(row=0,column=1,sticky="nsew")


		self.success = tk.Label(self,text="" ,font=("Helvetica", 15),bg="#586BE4")
		self.success.grid(row=1,column=1,sticky="nsew")

		self.modifyActLvlEntry = tk.Entry(self,textvariable=self.actLvlVar,font=("Helvetica", 20),bd=0)
		self.modifyActLvlEntry.grid(row=2,column=1,sticky="nsew")

		self.submitButton = tk.Button(self,text="Submit",width=20, font=("Helvetica", 15),highlightbackground="#586BE4")
		self.submitButton.bind("<Button-1>",self.controller.submitModifyActLvl)
		self.submitButton.grid(row=3,column=1)

		self.backButton = tk.Button(self,text="Back",width=20, font=("Helvetica", 15),highlightbackground="#586BE4")
		self.backButton.bind("<Button-1>", self.controller.updateProfileInfo)
		self.backButton.grid(row=4,column=1)


	def clearFrame(self):

		self.actLvlVar.set(0)
		self.success['text'] = ""

	def displaySuccess(self):

		self.success['text'] = "Success!!!"
		self.success['fg'] = "blue"

	def fieldInvalid(self):

		self.success['text'] = "Invalid Activity Level (1-5) **"
		self.success['fg'] = "red"
