import tkinter as tk


class retrieveDataFrame(tk.Frame):

	def __init__(self, parent, controller):

		tk.Frame.__init__(self,parent)
		self.controller = controller



		self.grid_columnconfigure(0,weight=1)
		self.grid_columnconfigure(1,weight=1)
		


		self.grid_rowconfigure(0,weight=1)
		self.grid_rowconfigure(1,weight=1)
		self.grid_rowconfigure(2,weight=1)
		self.grid_rowconfigure(3,weight=1)
		self.grid_rowconfigure(4,weight=1)
		self.grid_rowconfigure(5,weight=1)
		self.grid_rowconfigure(6,weight=1)
		self.grid_rowconfigure(7,weight=1)



		self.ageVar = tk.IntVar()
		self.weightVar = tk.DoubleVar()
		self.heightVar = tk.DoubleVar()
		self.goalWeightVar = tk.DoubleVar()
		self.activityLvlVar = tk.IntVar()
		self.intensityVar = tk.IntVar()

		self.title = tk.Label(self, text="Creating new profile: ")
		self.title.grid(column=1,row=0,sticky="nsew")

		self.invalidInputLabel = tk.Label(self, text="")
		self.invalidInputLabel.grid(column=0,row=0,sticky="nsew")

		self.askAge = tk.Label(self,text="Age:")
		self.askAge.grid(column=0,row=1,sticky="nsew")

		self.ageEntry = tk.Entry(self, textvariable=self.ageVar)
		self.ageEntry.grid(column=1,row=1,sticky="nsew")

		self.askWeight = tk.Label(self,text="Weight:")
		self.askWeight.grid(column=0,row=2,sticky="nsew")

		self.weightEntry = tk.Entry(self, textvariable=self.weightVar)
		self.weightEntry.grid(column=1,row=2,sticky="nsew")


		self.askHeight = tk.Label(self,text="Height:")
		self.askHeight.grid(column=0,row=3,sticky="nsew")

		self.heightEntry = tk.Entry(self, textvariable=self.heightVar)
		self.heightEntry.grid(column=1,row=3,sticky="nsew")


		self.askGoalWeight = tk.Label(self,text="Goal Weight:")
		self.askGoalWeight.grid(column=0,row=4,sticky="nsew")

		self.goalWeightEntry = tk.Entry(self, textvariable=self.goalWeightVar)
		self.goalWeightEntry.grid(column=1,row=4,sticky="nsew")

		self.askActLvl = tk.Label(self,text="Activity Level (1-5):")
		self.askActLvl.grid(column=0,row=5,sticky="nsew")

		self.actLvlEntry = tk.Entry(self, textvariable=self.activityLvlVar)
		self.actLvlEntry.grid(column=1,row=5,sticky="nsew")

		self.askIntensity = tk.Label(self,text="Caloric Deficit:")
		self.askIntensity.grid(column=0,row=6,sticky="nsew")

		self.intensityEntry = tk.Entry(self, textvariable=self.intensityVar)
		self.intensityEntry.grid(column=1,row=6,sticky="nsew")

		self.submitButton = tk.Button(self, text="Submit")
		self.submitButton.bind("<Button-1>", self.controller.submitInputValid)
		self.submitButton.grid(column=0, row=7, sticky="nsew")

		self.backButton = tk.Button(self, text="Back")
		self.backButton.bind("<Button-1>", self.controller.backToProfileValid)
		self.backButton.grid(column=1, row=7, sticky="nsew")

	def fieldInvalid(self, number):

		self.invalidInputLabel['text'] = "One of the fields is invalid (**)"
		self.invalidInputLabel['fg'] = "red"

		if(number == 1):
			self.askAge['text'] = "Age: **"

		elif(number == 2):
			self.askWeight['text'] = "Weight: **"

		elif(number == 3):
			self.askHeight['text'] = "Height: **"

		elif(number == 4):
			self.askGoalWeight['text'] = "Goal Weight: **"

		elif(number == 5):
			self.askActLvl['text'] = "Activity Level(1-5): **"
 
		elif(number == 6):
			self.askIntensity['text'] = "Caloric Deficit: **"

		else:
			# do nothing
			print('There is no field with that number.')


	def clearFrame(self):

		self.ageVar.set(0)
		self.weightVar.set(0.0)
		self.heightVar.set(0.0)
		self.goalWeightVar.set(0.0)
		self.activityLvlVar.set(0)
		self.intensityVar.set(0)

		self.askAge['text'] = "Age:"
		self.askWeight['text'] = "Weight:"
		self.askHeight['text'] = "Height: "
		self.askGoalWeight['text'] = "Goal Weight:"
		self.askActLvl['text'] = "Activity Level(1-5):"
		self.askIntensity['text'] = "Caloric Deficit:"

		self.invalidInputLabel['text'] = ""



