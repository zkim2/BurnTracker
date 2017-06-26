import tkinter as tk


class retrieveDataFrame(tk.Frame):

	def __init__(self, parent, controller):

		tk.Frame.__init__(self,parent)
		self.controller = controller



		self.grid_columnconfigure(0,weight=1)
		self.grid_columnconfigure(1,weight=1)
		self.grid_columnconfigure(2,weight=1)


		self.grid_rowconfigure(0,weight=1)
		self.grid_rowconfigure(1,weight=0)
		self.grid_rowconfigure(2,weight=1)
		self.grid_rowconfigure(3,weight=1)
		self.grid_rowconfigure(4,weight=1)
		self.grid_rowconfigure(5,weight=1)
		self.grid_rowconfigure(6,weight=1)
		self.grid_rowconfigure(7,weight=1)
		self.grid_rowconfigure(8,weight=1)



		self.ageVar = tk.IntVar()
		self.weightVar = tk.DoubleVar()
		self.heightVar = tk.DoubleVar()
		self.goalWeightVar = tk.DoubleVar()
		self.activityLvlVar = tk.IntVar()
		self.intensityVar = tk.IntVar()

		self.title = tk.Label(self, text="Creating new profile:", font = ("Helvetica", 25))
		self.title.grid(column=1,row=0,sticky="nsew")

		self.invalidInputLabel = tk.Label(self, text="",font=("Helvetica", 15))
		self.invalidInputLabel.grid(column=1,row=1,sticky="nsew")

		self.askAge = tk.Label(self,text="Age:",font = ("Helvetica", 20) )
		self.askAge.grid(column=0,row=2,sticky="nsew")

		self.ageEntry = tk.Entry(self, textvariable=self.ageVar,font = ("Helvetica", 20))
		self.ageEntry.grid(column=1,row=2,sticky="nsew")

		self.askWeight = tk.Label(self,text="Weight(lbs):",font = ("Helvetica", 20))
		self.askWeight.grid(column=0,row=3,sticky="nsew")

		self.weightEntry = tk.Entry(self, textvariable=self.weightVar,font = ("Helvetica", 20))
		self.weightEntry.grid(column=1,row=3,sticky="nsew")


		self.askHeight = tk.Label(self,text="Height(inches):",font = ("Helvetica", 20))
		self.askHeight.grid(column=0,row=4,sticky="nsew")

		self.heightEntry = tk.Entry(self, textvariable=self.heightVar, font = ("Helvetica", 20))
		self.heightEntry.grid(column=1,row=4,sticky="nsew")


		self.askGoalWeight = tk.Label(self,text="Goal Weight(lbs):" ,font = ("Helvetica", 20))
		self.askGoalWeight.grid(column=0,row=5,sticky="nsew")

		self.goalWeightEntry = tk.Entry(self, textvariable=self.goalWeightVar,font = ("Helvetica", 20))
		self.goalWeightEntry.grid(column=1,row=5,sticky="nsew")

		self.askActLvl = tk.Label(self,text="Activity Level (1-5):" ,font = ("Helvetica", 20))
		self.askActLvl.grid(column=0,row=6,sticky="nsew")

		self.actLvlEntry = tk.Entry(self, textvariable=self.activityLvlVar ,font = ("Helvetica", 20))
		self.actLvlEntry.grid(column=1,row=6,sticky="nsew")

		self.askIntensity = tk.Label(self,text="Caloric Deficit:" ,font = ("Helvetica", 20))
		self.askIntensity.grid(column=0,row=7,sticky="nsew")

		self.intensityEntry = tk.Entry(self, textvariable=self.intensityVar ,font = ("Helvetica", 20))
		self.intensityEntry.grid(column=1,row=7,sticky="nsew")

		self.submitButton = tk.Button(self, text="Submit",width = 20,font = ("Helvetica", 15))
		self.submitButton.bind("<Button-1>", self.controller.submitInputValid)
		self.submitButton.grid(column=1, row=8)

		self.backButton = tk.Button(self, text="Back",width=20,font = ("Helvetica", 15))
		self.backButton.bind("<Button-1>", self.controller.backToProfileValid)
		self.backButton.grid(column=1, row=9)

	def fieldInvalid(self, number):

		self.invalidInputLabel['text'] = "One of the fields is invalid in size **"
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


	def mismatchInvalid(self):

		self.invalidInputLabel['text'] = "There is a type mismatch in one of the fields **"
		self.invalidInputLabel['fg'] = "red"


	def clearFrame(self):

		self.ageVar.set(0)
		self.weightVar.set(0.0)
		self.heightVar.set(0.0)
		self.goalWeightVar.set(0.0)
		self.activityLvlVar.set(0)
		self.intensityVar.set(0)

		self.askAge['text'] = "Age:"
		self.askWeight['text'] = "Start Weight(lbs):"
		self.askHeight['text'] = "Height(in): "
		self.askGoalWeight['text'] = "Goal Weight(lbs):"
		self.askActLvl['text'] = "Activity Level(1-5):"
		self.askIntensity['text'] = "Caloric Deficit:"

		self.invalidInputLabel['text'] = ""



