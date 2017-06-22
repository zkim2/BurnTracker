import tkinter as tk


class mainMenuFrame(tk.Frame):

	def __init__(self,parent,controller):

		tk.Frame.__init__(self,parent)

		self.controller = controller


		toDoLabel = tk.Label(self, text="What would you like to do?")
		toDoLabel.grid(row=0,column=0,sticky="nsew")


		addDailyWeightButton = tk.Button(self,text="Add daily weight")
		addDailyWeightButton.bind("<Button-1>") #bind it to a function in controller
		addDailyWeightButton.grid(row=1,column=0,sticky="nsew")

		addDailyCaloriesButton = tk.Button(self,text="Add daily calories")
		addDailyCaloriesButton.bind("<Button-1>") #bind it to a function in controller
		addDailyCaloriesButton.grid(row=1,column=1,sticky="nsew")

		visualizeProgressButton = tk.Button(self,text="Visualize progress")
		visualizeProgressButton.bind("<Button-1>") #bind it to a function in controller
		visualizeProgressButton.grid(row=2,column=0,sticky="nsew")

		updateProfileButton = tk.Button(self,text="Update your profile")
		updateProfileButton.bind("<Button-1>") #bind it to a function in controller
		updateProfileButton.grid(row=2,column=1,sticky="nsew")

		backToStartButton = tk.Button(self,text="Back")
		backToStartButton.bind("<Button-1>", self.controller.backToStart)
		backToStartButton.grid(row=3,column=0,sticky="nsew")

		quitButton = tk.Button(self,text="Quit")
		quitButton.bind("<Button-1>", self.controller.exit)
		quitButton.grid(row=3,column=1,sticky="nsew")