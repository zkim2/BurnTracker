import tkinter as tk


class mainMenuFrame(tk.Frame):

	def __init__(self,parent,controller):

		tk.Frame.__init__(self,parent)

		self.controller = controller
		self.configure(bg="#586BE4")
		self.grid_columnconfigure(0, weight=1)
		self.grid_columnconfigure(1, weight=1)
		self.grid_columnconfigure(2, weight=1)
		
		self.grid_rowconfigure(0,weight=1)
		self.grid_rowconfigure(1,weight=1)
		self.grid_rowconfigure(2,weight=1)
		self.grid_rowconfigure(3,weight=1)
		self.grid_rowconfigure(4,weight=1)
		self.grid_rowconfigure(5,weight=1)
		self.grid_rowconfigure(6,weight=1)
		


		self.toDoLabel = tk.Label(self, text="What would you like to do?", font=("Helvetica", 25),bg="#586BE4")
		self.toDoLabel.grid(row=0,column=1,sticky="nsew")


		self.addDailyWeightButton = tk.Button(self,text="Add daily weight",font = ("Helvetica", 15), width=20,highlightbackground="#586BE4")
		self.addDailyWeightButton.bind("<Button-1>",self.controller.addDailyWeight) #bind it to a function in controller
		self.addDailyWeightButton.grid(row=1,column=1)

		self.addDailyCaloriesButton = tk.Button(self,text="Add daily calories",font = ("Helvetica", 15),width=20,highlightbackground="#586BE4")
		self.addDailyCaloriesButton.bind("<Button-1>", self.controller.addDailyCalories) #bind it to a function in controller
		self.addDailyCaloriesButton.grid(row=2,column=1)

		self.visualizeProgressButton = tk.Button(self,text="Visualize progress",font = ("Helvetica", 15),width=20,highlightbackground="#586BE4")
		self.visualizeProgressButton.bind("<Button-1>", self.controller.visualizeProgress) #bind it to a function in controller
		self.visualizeProgressButton.grid(row=3,column=1)

		self.updateProfileButton = tk.Button(self,text="Update your profile",font = ("Helvetica", 15),width=20,highlightbackground="#586BE4")
		self.updateProfileButton.bind("<Button-1>", self.controller.updateProfileInfo) #bind it to a function in controller
		self.updateProfileButton.grid(row=4,column=1)

		self.backToStartButton = tk.Button(self,text="Back",font = ("Helvetica", 15),width=20,highlightbackground="#586BE4")
		self.backToStartButton.bind("<Button-1>", self.controller.backToSummary)
		self.backToStartButton.grid(row=5,column=1)

		self.quitButton = tk.Button(self,text="Quit",font = ("Helvetica", 15),width=20,highlightbackground="#586BE4")
		self.quitButton.bind("<Button-1>", self.controller.exit)
		self.quitButton.grid(row=6,column=1)