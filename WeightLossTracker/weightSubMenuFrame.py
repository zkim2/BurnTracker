import tkinter as tk 

class weightSubMenuFrame(tk.Frame):

	def __init__(self,parent,controller):

		tk.Frame.__init__(self,parent)

		self.controller = controller


		self.whatToChangeLabel = tk.Label(self, text="What do you want to do with your weight data?")
		self.whatToChangeLabel.grid(row=0,column=0,sticky="nsew")


		self.deleteWeightButton = tk.Button(self,text="Delete weight of a specific date")
		self.deleteWeightButton.bind("<Button-1>", self.controller.sendToDeleteWeight)
		self.deleteWeightButton.grid(row=1,column=0,sticky="nsew")

		self.modifyWeightButton = tk.Button(self,text="Modify weight of a specific date")
		self.modifyWeightButton.bind("<Button-1>", self.controller.sendToModifyWeight)
		self.modifyWeightButton.grid(row=1,column=1,sticky="nsew")


		self.backButton = tk.Button(self,text="Back")
		self.backButton.bind("<Button-1>", self.controller.updateProfileInfo)
		self.backButton.grid(row=2,column=0,sticky="nsew")