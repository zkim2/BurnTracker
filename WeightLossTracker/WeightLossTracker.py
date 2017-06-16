import os
import datetime
import pickle
import matplotlib.pyplot as plt


"""
Author: Zachary Kim
email: zkim2@illinois.edu
"""

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
		self.data = {} #daily weight and date dictionary

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
		self.dailyCalories = self.BMRmaintenance - self.intensity

		poundsLose = self.currentWeight - self.goalWeight

		totalPoundDeficit = poundsLose * 3500

		self.weeksToFinish= totalPoundDeficit / (7 * self.intensity)

		
#need to store dates as datetime object so I can sort them when graphing
currentDate = datetime.date.today()

newName = str(input('What is your full name?: '))

newName = newName.replace(' ' , '')

newName = newName.lower()


#finds the pickled file in project directory
file_name = newName.lower() + '.pickle'

cur_dir = os.getcwd()

inSystem = False

file_list = os.listdir(cur_dir)

for file in file_list:
	if(file == file_name):
		inSystem = True
		break


#not in the system
if(inSystem == False): #

	newAge = int(input('What is your age?(yrs): '))
	currWeight = float(input('What is your current weight?(lbs): '))
	currHeight = float(input('What is your current height?(inches): '))
	goalWeight = float(input('What is your goal weight?(lbs):  '))
	activityLvl = float(input('What is your activity level? 1-5 from low to high): '))
	desiredIntensity = float(input('What do you want your daily caloric deficit to be? \n 1000 \n 750 \n 500 \n '))

	newProfile = Profile(newName,newAge,currWeight,currHeight,goalWeight,activityLvl,desiredIntensity)

	#adds a date key with the value of the currentweight in the dictionary 
	newProfile.data[currentDate] = newProfile.currentWeight

	#updates all information about the person
	passed = newProfile.calculateDailyCalories() 

	#pickles the Profile which saves the data associated with it
	pickle_out = open(newName + ".pickle", "wb")
	pickle.dump(newProfile, pickle_out)
	pickle_out.close()

#already in the system so no need to ask questions again
else: 

	#loads the user profile data
	pickle_in = open(newName + ".pickle", "rb")

	userProfile = pickle.load(pickle_in)
	

	print('You have a profile with us already', newName, '!')

	choice = int(input('What would you like to do? \n 1. Add daily weight \n 2. Visualize weight loss progress \n 3. Update Profile \n 4. Quit '))

	if(choice == 1):

		print('The date is currently', currentDate)

		print(userProfile.data)
		weight = float(input('What is your current weight in lbs?'))

		#default value is to update the weight despite multiple weight entries on the same day
		updateChoice = "y"
		
		#handles case of multiple weight entries on the same day
		for key in userProfile.data:
			print(key)
			if(key == currentDate):
				updateChoice = str(input("You have already input your weight for today, update it? (y/n)"))
				break
		
		if(updateChoice == "y"):
			userProfile.data[currentDate] = weight
			userProfile.currentWeight = weight
			pickle_out2 = open(userProfile.name + ".pickle", "wb")
			pickle.dump(userProfile, pickle_out2)
			pickle_out2.close()
			print('Thanks! Recorded.')

		#do nothing if they decide to not update the current weight.

	elif(choice == 2):

		print('Loading Visualization!')

		today = currentDate.strftime("%Y/%m/%d")

		#sorts the keys (dateTime objects) in the dictionary.
		sortedData = sorted(userProfile.data.items(), key = lambda d: d[0])


		plt.suptitle('Weight Loss Progress for ' + userProfile.name + ' as of ' + today, fontsize=14, fontweight='bold')

		#x are the keys(dateTime objects) and y are the weights
		x,y = zip(*sortedData)

		plt.plot(x,y)
		plt.ylabel('Weight (lbs)')
		plt.xlabel('Time (days)')
		plt.show()
