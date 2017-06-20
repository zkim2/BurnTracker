# The Profile object maintains the fitness information of each user. 

class Profile:

	def __init__(self, name, age, currentWeight, currentHeight, goalWeight, actLvl, intensity):

		self.name = name
		self.age = age
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

	def calculateDailyCalories(self):

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


		self.BMRmaintenance = activeBMR
		self.dailyCalories = int(self.BMRmaintenance - self.intensity)

		poundsLose = self.currentWeight - self.goalWeight

		totalPoundDeficit = poundsLose * 3500

		self.weeksToFinish= int(totalPoundDeficit / (7 * self.intensity))
