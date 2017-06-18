import os
import datetime
import pickle
import matplotlib.pyplot as plt


"""
Author: Zachary Kim

Weight Loss Tracker 

email: zkim2@illinois.edu



Features I need to implement:


-Give user a summary of their diet plan after creating a new profile. x
-Visualization of dietary and exercise programs for each profile. (add human body graphic that gets skinnier proportional to user's weight loss)
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
	if(inSystem == False): 

		newAge = int(input('\n What is your age?(yrs): '))
		currWeight = float(input('\n What is your current weight?(lbs): '))
		currHeight = float(input('\n What is your current height?(inches): '))
		goalWeight = float(input('\n What is your goal weight?(lbs):  '))
		activityLvl = float(input('\n What is your activity level? (1-5 from low to high): '))
		desiredIntensity = float(input('\n What do you want your daily caloric deficit to be? \n 1000 \n 750 \n 500 \n '))

		newProfile = Profile(newName,newAge,currWeight,currHeight,goalWeight,activityLvl,desiredIntensity)

		#adds a date key with the value of the currentweight in the dictionary 
		newProfile.weightData[currentDate] = newProfile.currentWeight

		#updates all information about the person
		passed = newProfile.calculateDailyCalories() 


		print("\n Welcome, " + newProfile.name + "." + "\n With the deficit you entered, you should be eating " + str(newProfile.dailyCalories) + " calories per day. \n")

		endDate = (datetime.datetime.today() + (7*datetime.timedelta(days=newProfile.weeksToFinish)))
		endDate = endDate.date()

		print("\n With these calories, you will lose " + str((newProfile.intensity * 7) / 3500) + " pounds per week.")
		print("\n You will reach your goal weight in " + str(newProfile.weeksToFinish) + " weeks on " + endDate.strftime("%m/%d/%y") + ".")

		#pickles the Profile which saves the data associated with it
		pickle_outNewProfile = open(newName + ".pickle", "wb")
		pickle.dump(newProfile, pickle_outNewProfile)
		pickle_outNewProfile.close()

		#the user has the option to go back and enter in another name or to have access to options bc already in the system.


	#already in the system so no need to ask questions again
	
	pickle_inProfile = open(newName + ".pickle", "rb")

	userProfile = pickle.load(pickle_inProfile)

	print('\n Profile Login successful.')	

	userProfile.calculateDailyCalories()

	print("\n You should eat " + str(userProfile.dailyCalories) + " today to maintain your ideal pound loss per week.")
	
	subLoopRun = True

	while subLoopRun:

		choice = int(input('\n What would you like to do? \n 1. Add daily weight \n 2. Add daily calories \n 3. Visualize weight loss progress \n 4. Update Profile \n 5. Back \n 6. Quit '))

		print(userProfile.weightData)
		print(userProfile.caloricData)

		print('\n The date is currently ' + str(currentDate))

		if(choice == 1):

			weight = float(input('\n What is your current weight in lbs?'))

			#default value is to update the weight despite multiple weight entries on the same day
			updateChoice = "y"
			
			#handles case of multiple weight entries on the same day
			for key in userProfile.weightData:

				if(key == currentDate):

					updateChoice = str(input(" \n You have already input your weight for today, update it? (y/n)"))
					break
			
			if(updateChoice == "y"):

				userProfile.weightData[currentDate] = weight
				userProfile.currentWeight = weight
				pickle_out2 = open(userProfile.name + ".pickle", "wb")
				pickle.dump(userProfile, pickle_out2)
				pickle_out2.close()
				print('\n Thanks! Recorded.')

		elif(choice == 2):

			todaysCalories = float(input('\n How many calories did you eat today?'))

			updateChoice = "y"
			
			#handles case of multiple weight entries on the same day
			for key in userProfile.caloricData:

				if(key == currentDate):

					updateChoice = str(input(" \n You have already input your calories for today, update it? (y/n)"))
					break
			
			if(updateChoice == "y"):

				userProfile.caloricData[currentDate] = todaysCalories
				pickle_out2 = open(userProfile.name + ".pickle", "wb")
				pickle.dump(userProfile, pickle_out2)
				pickle_out2.close()
				print('\n Thanks! Recorded.')

		elif(choice == 3):

			visualizationLoop = True

			while visualizationLoop:

				calOrWeight = int(input('Which graph would you like to see? \n 1. Weight Loss \n 2. Calories \n 3. Back'))

				today = currentDate.strftime("%Y/%m/%d")

				if(calOrWeight == 1):

					print('Loading weight loss graph!')

					#sorts the keys (dateTime objects) in the dictionary.
					sortedData = sorted(userProfile.weightData.items(), key = lambda d: d[0])


					plt.suptitle('Weight Loss Progress for ' + userProfile.name + ' as of ' + today, fontsize=14, fontweight='bold')

					#x are the keys(dateTime objects) and y are the weights
					x,y = zip(*sortedData)

					plt.plot(x,y)
					plt.ylabel('Weight (lbs)')
					plt.xlabel('Time (days)')
					plt.show()

				elif(calOrWeight == 2):

					print('Loading calorie graph!')

					sortedData = sorted(userProfile.caloricData.items(), key = lambda d: d[0])

					plt.suptitle('Caloric Intake for ' + userProfile.name + ' as of ' + today, fontsize=14, fontweight='bold')

					x,y = zip(*sortedData)

					plt.plot(x,y)
					plt.ylabel('Caloric Intake (cal)')
					plt.xlabel('Time (days)')
					plt.show()

				elif(calOrWeight == 3):

					visualizationLoop = False

				else:

					visualizationLoop = True

		elif(choice == 4):

			modifyLoopRun = True

			while modifyLoopRun:

				updateProfileChoice = int(input('\n 1. Modify weight of specified date \n 2. Delete a date and weight \n 3. Add a missed weight \n 4. Modify calories of a specified date \n 5. Delete a date and calories \n 6. Add missed calories \n 7. Back \n 8. Quit '))

			
				#need to check if date is valid and in the dict first.

				if(updateProfileChoice >= 1 and updateProfileChoice <= 6):

					dateString = str(input('\n Please enter the desired date to be updated/deleted/added: (ex, 06/07/17) '))

					updatedDateTime = datetime.datetime.strptime(dateString, '%m/%d/%y')

					if(updateProfileChoice == 2):

						userProfile.weightData.pop(updatedDateTime.date(), None) 

					elif(updateProfileChoice == 5):

						userProfile.caloricData.pop(updatedDateTime.date(), None)

					elif(updateProfileChoice == 1 or updateProfileChoice == 3):

							updatedWeight = float(input('\n Please enter the new weight: '))

							userProfile.weightData[updatedDateTime.date()] = updatedWeight	

					else: 	#updatedProfileChoice == 4 or updatedProfileChoice == 6):

							updatedCalories = float(input('\n Please enter new calories: '))

							userProfile.caloricData[updatedDateTime.date()] = updatedCalories


					pickle_outModify= open(userProfile.name + ".pickle", "wb")
					pickle.dump(userProfile, pickle_outModify)
					pickle_outModify.close()

					print('\n Successfully changed!')

				elif(updateProfileChoice == 7):

					modifyLoopRun = False

				elif(updateProfileChoice == 8):

					exit()

				else:

					modifyLoopRun = True

		elif(choice == 5):

			subLoopRun = False

		elif(choice == 6):

			exit()

		else:

			subLoopRun = True
