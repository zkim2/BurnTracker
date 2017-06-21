import tkinter as tk


class retrieveDataFrame(tk.Frame):

	def __init__(self, parent, controller):

		tk.Frame.__init__(self,parent)
		self.controller = controller

		self.ageVar = tk.IntVar()
		self.weightVar = tk.DoubleVar()
		self.heightVar = tk.DoubleVar()
		self.goalWeightVar = tk.DoubleVar()
		self.activityLvlVar = tk.IntVar()
		self.intensityVar = tk.IntVar()

		title = tk.Label(self, text="Creating new profile: ")
		title.grid(column=0,row=0,sticky="nsew")

		askAge = tk.Label(self,text="Age:")
		askAge.grid(column=0,row=1,sticky="nsew")

		ageEntry = tk.Entry(self, textvariable=self.ageVar)
		ageEntry.grid(column=1,row=1,sticky="nsew")

		askWeight = tk.Label(self,text="Weight:")
		askWeight.grid(column=0,row=2,sticky="nsew")

		weightEntry = tk.Entry(self, textvariable=self.weightVar)
		weightEntry.grid(column=1,row=2,sticky="nsew")


		askHeight = tk.Label(self,text="Height:")
		askHeight.grid(column=0,row=3,sticky="nsew")

		heightEntry = tk.Entry(self, textvariable=self.heightVar)
		heightEntry.grid(column=1,row=3,sticky="nsew")


		askGoalWeight = tk.Label(self,text="Goal Weight:")
		askGoalWeight.grid(column=0,row=4,sticky="nsew")

		goalWeightEntry = tk.Entry(self, textvariable=self.goalWeightVar)
		goalWeightEntry.grid(column=1,row=4,sticky="nsew")

		askActLvl = tk.Label(self,text="Activity Level (1-5):")
		askActLvl.grid(column=0,row=5,sticky="nsew")

		actLvlEntry = tk.Entry(self, textvariable=self.activityLvlVar)
		actLvlEntry.grid(column=1,row=5,sticky="nsew")

		askIntensity = tk.Label(self,text="Caloric Deficit:")
		askIntensity.grid(column=0,row=6,sticky="nsew")

		intensityEntry = tk.Entry(self, textvariable=self.intensityVar)
		intensityEntry.grid(column=1,row=6,sticky="nsew")

		submitButton = tk.Button(self, text="Submit")
		submitButton.bind("<Button-1>")
		submitButton.grid(column=0, row=7, sticky="nsew")

		backButton = tk.Button(self, text="Back")
		backButton.bind("<Button-1>", self.controller.backToProfileValid)
		backButton.grid(column=1, row=7, sticky="nsew")



