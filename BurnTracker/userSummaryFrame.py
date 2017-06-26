import tkinter as tk 

class userSummaryFrame(tk.Frame):

	def __init__(self,parent,controller):

		tk.Frame.__init__(self,parent)

		self.controller = controller

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

		self.summaryLabel = tk.Label(self, text="Summary of profile", font=("Helvetica",25))
		self.summaryLabel.grid(row=0,column=1,sticky="nsew")
		self.profileName = "Profile Name: " + self.controller.userProfile.name 
		self.profileNameLabel = tk.Label(self,textvariable=self.profileName)
		self.profileNameLabel.grid(row=1,column=1,sticky="nsew")

		self.profileAge = "Age: " + str(self.controller.userProfile.age)
		self.profileAgeLabel = tk.Label(self,textvariable=self.profileAge, font=("Helvetica",20))
		self.profileAgeLabel.grid(row=2,column=1,sticky="nsew")


		self.profileWeight = "Weight: " + str(self.controller.userProfile.currentWeight)
		self.profileWeightLabel = tk.Label(self,textvariable=self.profileWeight, font=("Helvetica",20))
		self.profileWeightLabel.grid(row-3,column=1,sticky="nsew")

		self.profileHeight = "Height: " + str(self.controller.userProfile.currentHeight) + " in."
		self.profileHeightLabel = tk.Label(self,textvariable=self.profileHeight, font=("Helvetica",20))
		self.profileHeightLabel.grid(row=4,column=1,sticky="nsew")

		self.profileGWeight = "Goal Weight(lbs): " + str(self.controller.userProfile.goalWeight)
		self.profileGWeightLabel = tk.Label(self,textvariable=self.profileGWeight, font=("Helvetica",20))
		self.profileGWeightLabel.grid(row=5,column=1,sticky="nsew")


		self.profileActLvl = "Activity Level: " + str(self.controller.userProfile.actLvl)
		self.profileActLvl = tk.Label(self,textvariable=self.profileActLvl, font=("Helvetica",20))
		self.profileActLvl.grid(row=6,column=1,sticky="nsew")


		self.continueButton = tk.Button(self,text="Next")
		self.continueButton.bind("<Button-1>", self.controller.backToMainMenu)
		self.continueButton.grid(row=7,column=1)

		self.backButton=tk.Button(self,text="Back to Login")
		self.backButton.bind("<Button-1>", self.controller.backToStart)
		self.backButton.grid(row=8,column=1)



