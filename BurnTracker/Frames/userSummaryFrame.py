import tkinter as tk 

class userSummaryFrame(tk.Frame):

	def __init__(self,parent,controller):

		tk.Frame.__init__(self,parent)

		self.controller = controller
		self.configure(bg="#586BE4")
		self.grid_columnconfigure(0,weight=1)
		self.grid_columnconfigure(1,weight=1)
		self.grid_columnconfigure(2,weight=1)

		self.grid_rowconfigure(0,weight=1)
		self.grid_rowconfigure(1,weight=1)
		self.grid_rowconfigure(2,weight=1)
		self.grid_rowconfigure(3,weight=1)
		self.grid_rowconfigure(4,weight=1)
		self.grid_rowconfigure(5,weight=1)
		self.grid_rowconfigure(6,weight=1)
		self.grid_rowconfigure(7,weight=1)
		self.grid_rowconfigure(8,weight=1)

		self.summaryLabel = tk.Label(self, text="Summary of profile", font=("Helvetica",25),bg="#586BE4")
		self.summaryLabel.grid(row=0,column=1,sticky="nsew")

		self.profileName = "Profile Name: " + self.controller.userProfile.name 

		self.profileNameLabel = tk.Label(self,text=self.profileName, font=("Helvetica", 15),bg="#586BE4")
		self.profileNameLabel.grid(row=1,column=0,sticky="nsew")

		self.profileAge = "Age: " + str(self.controller.userProfile.age)
		self.profileAgeLabel = tk.Label(self,text=self.profileAge, font=("Helvetica",15),bg="#586BE4")
		self.profileAgeLabel.grid(row=2,column=0,sticky="nsew")


		self.profileWeight = "Start Weight: " + str(self.controller.userProfile.startWeight)
		self.profileWeightLabel = tk.Label(self,text=self.profileWeight, font=("Helvetica",15),bg="#586BE4")
		self.profileWeightLabel.grid(row=3,column=0,sticky="nsew")

		self.profileHeight = "Height: " + str(self.controller.userProfile.currentHeight) + " in."
		self.profileHeightLabel = tk.Label(self,text=self.profileHeight, font=("Helvetica",15),bg="#586BE4")
		self.profileHeightLabel.grid(row=4,column=0,sticky="nsew")

		self.profileGWeight = "Goal Weight(lbs): " + str(self.controller.userProfile.goalWeight)
		self.profileGWeightLabel = tk.Label(self,text=self.profileGWeight, font=("Helvetica",15),bg="#586BE4")
		self.profileGWeightLabel.grid(row=5,column=0,sticky="nsew")


		self.profileActLvl = "Activity Level: " + str(self.controller.userProfile.actLvl)
		self.profileActLvlLabel = tk.Label(self,text=self.profileActLvl, font=("Helvetica",15),bg="#586BE4")
		self.profileActLvlLabel.grid(row=6,column=0,sticky="nsew")

		self.profileDeficit = "Caloric Deficit: " + str(self.controller.userProfile.intensity)
		self.profileDeficitLabel = tk.Label(self,text=self.profileDeficit, font=("Helvetica",15),bg="#586BE4")
		self.profileDeficitLabel.grid(row=7,column=0)


		self.profileCurrWeight = "Current Weight: " + str(self.controller.userProfile.currentWeight)
		self.profileCurrWeightLabel = tk.Label(self,text=self.profileCurrWeight, font=("Helvetica",15),bg="#586BE4")
		self.profileCurrWeightLabel.grid(row=1, column=1,sticky="nsew")

		self.profileWeightLost = "Weight Lost(lbs): " + str(int(self.controller.userProfile.startWeight - self.controller.userProfile.currentWeight))
		self.profileWeightLostLabel = tk.Label(self,text=self.profileWeightLost, font=("Helvetica", 15),bg="#586BE4")
		self.profileWeightLostLabel.grid(row=2,column=1,sticky="nsew")

		
		self.profileBMR = "Your basal metabolic rate(bmr) is " + str(self.controller.userProfile.BMRmaintenance) + " calories"
		self.profileBMRLabel = tk.Label(self,text=self.profileBMR,font=("Helvetica",15),bg="#586BE4")
		self.profileBMRLabel.grid(row=3,column=1,sticky="nsew")

		self.profileCalories = "With your deficit, you need to consume " + str(self.controller.userProfile.dailyCalories) + " per day."
		self.profileCaloriesLabel= tk.Label(self,text=self.profileCalories,font=("Helvetica",15),bg="#586BE4")
		self.profileCaloriesLabel.grid(row=4,column=1,sticky="nsew")

		self.profileTime = "You will reach your goal weight in " + str(self.controller.userProfile.weeksToFinish) + " weeks."
		self.profileTimeLabel = tk.Label(self,text=self.profileTime, font=("Helvetica",15),bg="#586BE4")
		self.profileTimeLabel.grid(row=5,column=1,sticky="nsew")

		self.profileAdvice = "To lose weight faster, either lower your caloric deficit or increase activity level."
		self.profileAdviceLabel = tk.Label(self,text=self.profileAdvice, font=("Helvetica",15),bg="#586BE4")
		self.profileAdviceLabel.grid(row=6,column=1,sticky="nsew")

		self.continueButton = tk.Button(self,text="Next",highlightbackground="#586BE4")
		self.continueButton.bind("<Button-1>", self.controller.backToMainMenu)
		self.continueButton.grid(row=7,column=1)

		self.backButton=tk.Button(self,text="Back to Login",highlightbackground="#586BE4")
		self.backButton.bind("<Button-1>", self.controller.backToStart)
		self.backButton.grid(row=8,column=1)




