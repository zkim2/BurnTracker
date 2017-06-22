import tkinter as tk


class mainMenuFrame(tk.Frame):

	def __init__(self,parent,controller):

		tk.Frame.__init__(self,parent)

		self.controller = controller


		self.toDoLabel = tk.Label(self, text="What would you like to do?")
		self.toDoLabel.grid(row=0,column=0,sticky="nsew")


		self.addDailyWeightButton = tk.Button(self,text="Add daily weight")
		self.addDailyWeightButton.bind("<Button-1>") #bind it to a function in controller
		self.addDailyWeightButton.grid(row=1,column=0,sticky="nsew")

		self.addDailyCaloriesButton = tk.Button(self,text="Add daily calories")
		self.addDailyCaloriesButton.bind("<Button-1>") #bind it to a function in controller
		self.addDailyCaloriesButton.grid(row=1,column=1,sticky="nsew")

		self.visualizeProgressButton = tk.Button(self,text="Visualize progress")
		self.visualizeProgressButton.bind("<Button-1>") #bind it to a function in controller
		self.visualizeProgressButton.grid(row=2,column=0,sticky="nsew")

		self.updateProfileButton = tk.Button(self,text="Update your profile")
		self.updateProfileButton.bind("<Button-1>") #bind it to a function in controller
		self.updateProfileButton.grid(row=2,column=1,sticky="nsew")

		self.backToStartButton = tk.Button(self,text="Back")
		self.backToStartButton.bind("<Button-1>", self.controller.backToStart)
		self.backToStartButton.grid(row=3,column=0,sticky="nsew")

		self.quitButton = tk.Button(self,text="Quit")
		self.quitButton.bind("<Button-1>", self.controller.exit)
		self.quitButton.grid(row=3,column=1,sticky="nsew")