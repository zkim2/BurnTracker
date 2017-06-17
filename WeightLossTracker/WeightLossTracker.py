import os
import datetime
import pickle
import matplotlib.pyplot as plt


"""
Author: Zachary Kim

Weight Loss Tracker 

email: zkim2@illinois.edu



Features I need to implement:


-Give user a summary of their diet plan after creating a new profile.
-Calculation of carbohydrates, fats, and proteins for each profile.
-Visualization of dietary and exercise programs for each profile. (add human body graphic that gets skinnier proportional to user's weight loss)
-Each day, users will input weight and caloric intake (later on exercise) - caloric intake stored as dictionary too?
-Add more graph data such as calories consumed per week (data gained from the above added feature)
-In order to prevent weight plateau's from users, we have to recalculate their BMR and adjust their deficit according to their weight loss.
 (we can perform this operation every time the user inputs their weight and caloric intake data everyday)
-Allow users to email an address or text to send in data which is easier than logging into the computer everyday.
-Make this script an executable if possible. 
-Eventually transition from command line to GUI.

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

mainLoopRun = True

while mainLoopRun:

	profileLoop = True

	#handles the case when user types profile name incorrectly.
	while profileLoop:
		newName = str(input('What is your full name?: '))

		#can handle capitalization and spaces
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

		if(inSystem == False):
			mistake = int(input('\n Uh-oh no profile found. \n 1. Create a profile \n 2. Retype profile name \n'))

			if(mistake == 1):
				profileLoop = False
			else:
				profileLoop = True
		else:
			profileLoop = False

	

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
		pickle_outNewProfile = open(newName + ".pickle", "wb")
		pickle.dump(newProfile, pickle_outNewProfile)
		pickle_outNewProfile.close()

		#the user has the option to go back and enter in another name or to have access to options bc already in the system.


	#already in the system so no need to ask questions again
	
	pickle_inProfile = open(newName + ".pickle", "rb")

	userProfile = pickle.load(pickle_inProfile)

	print('Profile Login successful.')	
	
	subLoopRun = True

	while subLoopRun:

		choice = int(input('\n What would you like to do? \n 1. Add daily weight \n 2. Visualize weight loss progress \n 3. Update Profile \n 4. Back \n 5. Quit '))

		if(choice == 1):

			print('\n The date is currently ' + str(currentDate))

			weight = float(input('\n What is your current weight in lbs?'))

			#default value is to update the weight despite multiple weight entries on the same day
			updateChoice = "y"
			
			#handles case of multiple weight entries on the same day
			for key in userProfile.data:
				if(key == currentDate):
					updateChoice = str(input(" \n You have already input your weight for today, update it? (y/n)"))
					break
			
			if(updateChoice == "y"):
				userProfile.data[currentDate] = weight
				userProfile.currentWeight = weight
				pickle_out2 = open(userProfile.name + ".pickle", "wb")
				pickle.dump(userProfile, pickle_out2)
				pickle_out2.close()
				print('\n Thanks! Recorded.')

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


		elif(choice == 3):

			
			modifyLoopRun = True

			while modifyLoopRun:

				updateProfileChoice = int(input('\n 1. Modify weight of specified date \n 2. Delete a date and weight \n 3. Add a missed weight \n 4. Back \n 5. Quit '))

			
				#need to check if date is valid and in the dict first.

				if(updateProfileChoice >= 1 and updateProfileChoice <= 3):

					dateString = str(input('\n Please enter the desired date to be updated/deleted/added: (ex, 06/07/17) '))

					updatedDateTime = datetime.datetime.strptime(dateString, '%m/%d/%y')

					if(updateProfileChoice == 2):
						userProfile.data.pop(updatedDateTime.date(), None) 
					else:
						updatedWeight = float(input('\n Please enter the new weight: '))

						userProfile.data[updatedDateTime.date()] = updatedWeight	


					pickle_outModify= open(userProfile.name + ".pickle", "wb")
					pickle.dump(userProfile, pickle_outModify)
					pickle_outModify.close()

					print('\n Successfully changed!')

				elif(updateProfileChoice == 4):
					modifyLoopRun = False
				elif(updateProfileChoice == 5):
					exit()
				else:
					modifyLoopRun = True


		elif(choice == 4):
			subLoopRun = False
		elif(choice == 5):
			exit()
		else:
			subLoopRun = True
