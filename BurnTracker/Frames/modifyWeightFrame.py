import tkinter as tk


class modifyWeightFrame(tk.Frame):

	def __init__(self,parent,controller):

		tk.Frame.__init__(self,parent)

		self.controller = controller

		self.dateString = tk.StringVar() #will parse in controller

		self.weightVar = tk.DoubleVar()

		self.configure(bg="#586BE4")

		self.grid_columnconfigure(0,weight=1)
		self.grid_columnconfigure(1,weight=1)
		self.grid_columnconfigure(2,weight=1)

		self.grid_rowconfigure(0,weight=1)
		self.grid_rowconfigure(1,weight=0)
		self.grid_rowconfigure(2,weight=0)
		self.grid_rowconfigure(3,weight=1)
		self.grid_rowconfigure(4,weight=1)
		self.grid_rowconfigure(5,weight=1)


		self.modifyingWeightLabel = tk.Label(self,text="Modifying Weight", font=("Helvetica",25),bg="#586BE4")
		self.modifyingWeightLabel.grid(row=0,column=1, sticky="nsew")

		self.success = tk.Label(self,text="", font=("Helvetica", 15),bg="#586BE4")
		self.success.grid(row=1,column=1,sticky="nsew")


		self.dateOfWeight = tk.Label(self,text="Date to modify(MM/DD/YY):",  font=("Helvetica", 20),bg="#586BE4")
		self.dateOfWeight.grid(row=2,column=0, sticky="nsew")

		self.dateOfWeightEntry = tk.Entry(self, textvariable = self.dateString, font=("Helvetica", 20),bd=1)
		self.dateOfWeightEntry.grid(row=2,column=1,sticky="nsew")


		self.updatedWeight = tk.Label(self,text="Updated Weight:", font=("Helvetica", 20),bg="#586BE4")
		self.updatedWeight.grid(row=3,column=0,sticky="nsew")


		self.updatedWeightEntry = tk.Entry(self,textvariable=self.weightVar, font=("Helvetica", 20),bd=1)
		self.updatedWeightEntry.grid(row=3,column=1,sticky="nsew")


		self.submitButton = tk.Button(self,text="Submit", width=20, font=("Helvetica", 15),highlightbackground="#586BE4")
		self.submitButton.bind("<Button-1>", self.controller.submitModifyWeight)
		self.submitButton.grid(row=4,column=1)

		self.backButton = tk.Button(self,text="Back", width=20, font=("Helvetica", 15),highlightbackground="#586BE4")
		self.backButton.bind("<Button-1>", self.controller.sendToWeightMenu)
		self.backButton.grid(row=5,column=1)



	def clearFrame(self):

		self.dateString.set("")
		self.weightVar.set(0.0)

		self.success['text'] = ""


	def displaySuccess(self):

		self.success['text'] = "Success!!!"
		self.success['fg'] = "blue"

	def fieldInvalid(self):

		self.success['text'] = "Invalid date or invalid weight **"
		self.success['fg'] = "red"


