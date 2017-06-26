# The Profile object maintains the fitness information of each user. 
import os
import datetime
import pickle
#import matplotlib.pyplot as plt



"""
Made by Zachary Kim
email: zkim2@illinois.edu

IMPORTANT: THIS IS CONSIDERED TO BE THE MODEL OF THE PROGRAM.

This Profile model handles all logic and operations of the program and communicates with the controller to 
update the view accordingly.

To do:

-Transfer all code over from WeightLossTracker.py and embed it within the object itself.
-Create more functions that make it easier for the controller to retrieve and set information.
-Eventually deal with making variables private

"""

class Profile:

	def __init__(self, name="", age=0, startWeight= 0,currentWeight=0, currentHeight=0, goalWeight=0, actLvl=1, intensity=1):

		
		self.name = name
		self.age = age
		self.startWeight = startWeight
		self.currentWeight = currentWeight
		self.currentHeight = currentHeight
		self.goalWeight = goalWeight
		self.actLvl = actLvl
		self.intensity = intensity

		self.BMRmaintenance = 2000 #default
		self.dailyCalories = 2000 #default
		self.weeksToFinish = 12 #default
		self.weightData = {} #daily weight and date dictionary
		self.caloricData = {} #daily calories and date dictionary
		
		"""
	def saveProfile(self): #broken for now

		pickle_save = open(self.name + ".pickle", "wb")
		pickle.dump(self, pickle_save)
		pickle_save.close()
	
	"""

	def calculateDailySummary(self):

		inactiveBMR = 66.0 + (6.23 * self.currentWeight) + (12.7 * self.currentHeight) - (6.8 * self.age)

		if(self.actLvl == 1):
			activeBMR = inactiveBMR * 1.2

		elif(self.actLvl == 2):
			activeBMR = inactiveBMR * 1.375

		elif(self.actLvl == 3):
			activeBMR = inactiveBMR * 1.55

		elif(self.actLvl == 4):
			activeBMR = inactiveBMR * 1.725

		else:
			activeBMR = inactiveBMR * 1.9


		self.BMRmaintenance = int(activeBMR)
		self.dailyCalories = int(self.BMRmaintenance - self.intensity)

		poundsLose = self.currentWeight - self.goalWeight

		totalPoundDeficit = poundsLose * 3500

		self.weeksToFinish= int(totalPoundDeficit / (7 * self.intensity))

