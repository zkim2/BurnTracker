import os
import datetime
import pickle
import matplotlib.pyplot as plt




"""
Author: Zachary Kim

Weight Loss Tracker 

email: zkim2@illinois.edu



Features I need to implement:

-Visualization of dietary and exercise programs for each profile. (add human body graphic that gets skinnier proportional to user's weight loss)
-Allow users to email an address or text to send in data which is easier than logging into the computer everyday.
-Make this script an executable if possible. 
-Eventually transition from command line to GUI.


PRIORITY

-Save png every time user wants to visualize progress.
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

			mistake = int(input('\n Uh-oh no profile found. \n 1. Create a profile \n 2. Retype profile name \n 3. Quit \n'))

			if(mistake == 1):

				profileLoop = False

			elif(mistake == 2):

				profileLoop = True

			else:

				exit()
		else: #if already in the system, just exit.

			profileLoop = False

	
	#not in the system
	if(inSystem == False): 

		newAge = int(input('\n What is your age?(yrs): '))
		currWeight = float(input('\n What is your current weight?(lbs): '))
		currHeight = float(input('\n What is your current height?(inches): '))
		goalWeight = float(input('\n What is your goal weight?(lbs):  '))
		activityLvl = float(input("\n Enter in your activity level: \n 1 (None) \n 2 (Low) \n 3 (Medium) \n 4 (High) \n 5 (Intense)"))
		desiredIntensity = float(input('\n What do you want your daily caloric deficit to be? \n 1000 \n 750 \n 500 \n '))

		newProfile = Profile(newName,newAge,currWeight,currHeight,goalWeight,activityLvl,desiredIntensity)

		#adds a date key with the value of the currentweight in the dictionary 
		newProfile.weightData[currentDate] = newProfile.currentWeight

		#updates all information about the person
		passed = newProfile.calculateDailyCalories() 

		#give user diet summary
		print("\n Welcome, " + newProfile.name + "." + "\n With the deficit you entered, you should be eating " + str(newProfile.dailyCalories) + " calories per day. \n")

		endDate = (datetime.datetime.today() + (7*datetime.timedelta(days=newProfile.weeksToFinish)))
		endDate = endDate.date()

		print("\n With these calories, you will lose " + str((newProfile.intensity * 7) / 3500) + " pounds per week.")
		print("\n You will reach your goal weight in " + str(newProfile.weeksToFinish) + " weeks on " + endDate.strftime("%m/%d/%y") + ".")


		#pickles the Profile which saves the data associated with it
		pickle_outNewProfile = open(newName + ".pickle", "wb")
		pickle.dump(newProfile, pickle_outNewProfile)
		pickle_outNewProfile.close()


	#already in the system so no need to ask questions again
	
	pickle_inProfile = open(newName + ".pickle", "rb")

	userProfile = pickle.load(pickle_inProfile)

	userProfile.calculateDailyCalories()

	print('\n Profile Login successful.')	

	print("\n You should eat " + str(userProfile.dailyCalories) + " today to maintain your ideal pound loss per week. \n")
	
	subLoopRun = True

	#this loops allows the user to choose the options and also come back to choose another option, extends life of the program.
	while subLoopRun:

		print('\n The date is currently ' + str(currentDate))

		#print(userProfile.weightData)
		#print(userProfile.caloricData)

		choice = int(input('\n Main Menu: \n 1. Add daily weight \n 2. Add daily calories \n 3. Visualize weight loss progress \n 4. Update Profile \n 5. Back \n 6. Quit '))

	
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

			updateChoice = "y" #considered a boolean but this is fine as long as the user knows what input to give.
			
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

			while visualizationLoop: #again, gives user options to go back or forward in the program.

				calOrWeight = int(input('\n Graph Menu: \n 1. Weight Loss \n 2. Calories \n 3. Back'))

				today = currentDate.strftime("%m/%d/%y")

				if(calOrWeight == 1):

					print('\n Loading weight loss graph!')

					#sorts the keys (dateTime objects) in the dictionary.
					sortedData = sorted(userProfile.weightData.items(), key = lambda d: d[0])


					plt.suptitle('Weight Loss Progress for ' + userProfile.name + ' as of ' + today, fontsize=14, fontweight='bold')

					#x are the keys(dateTime objects) and y are the weights
					x,y = zip(*sortedData)

					plt.plot(x,y)
					plt.ylabel('Weight (lbs)')
					plt.xlabel('Time (days)')
					plt.show()

					#print("Saving the file now......")

					#plt.savefig(userProfile.name + str(currentDate) + ".png")

				elif(calOrWeight == 2):

					print('\n Loading calorie graph!')

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

			while modifyLoopRun: #another menu but for updating the profile data.

				#this is too long, need to shorten
				updateProfileChoice = int(input('\n Profile Update Menu: \n 1. Modify weight of specified date \n 2. Delete a date and weight \n 3. Add a missed weight \n 4. Modify calories of a specified date \n 5. Delete a date and calories \n 6. Add missed calories \n 7. Modify caloric deficit \n 8. Modify activity level \n 9. Back \n 10. Quit'))
	
				#need to check if date is valid and in the dict first.

				if(updateProfileChoice >= 1 and updateProfileChoice <= 6):

					dateString = str(input('\n Please enter the desired date to be updated/deleted/added: (ex, 06/07/17) '))

					updatedDateTime = datetime.datetime.strptime(dateString, '%m/%d/%y')


					if(updateProfileChoice == 2):

						userProfile.weightData.pop(updatedDateTime.date(), None) 

						print('\n Date and weight deleted!')

					elif(updateProfileChoice == 5):

						userProfile.caloricData.pop(updatedDateTime.date(), None)

						print('\n Date and calories deleted!')


					elif(updateProfileChoice == 1 or updateProfileChoice == 3):

							overwriteData = "y"

							#check to see if adding a missed weight is incorrect
							if(updateProfileChoice == 3):

								for key in userProfile.weightData:

									if(key == updatedDateTime.date()): #found already

										overwriteData = str(input("\n It seems that there is already a weight in for this date. \n Overwrite it? (y/n) \n"))
	

							if(overwriteData == "y"):

								updatedWeight = float(input('\n Please enter the new weight: '))

								userProfile.weightData[updatedDateTime.date()] = updatedWeight	

								print("\n The date and weight have been overwritten.")

							else:

								print('\n The date and weight have not been overwritten.')


					elif(updateProfileChoice == 4 or updateProfileChoice == 6):	#updatedProfileChoice == 4 or updatedProfileChoice == 6):

							overwriteData = "y"

							#check to see if adding missed calories is incorrect
							if(updateProfileChoice == 6):

								for key in userProfile.caloricData:

									if(key == updatedDateTime.date()):

										overwriteData = str(input("\n It seems that there is already calories in for this date. \n Overwrite it? (y/n) \n"))


							if(overwriteData == "y"):

								updatedCalories = float(input('\n Please enter new calories: '))

								userProfile.caloricData[updatedDateTime.date()] = updatedCalories

								print("\n The date and calories have been overwritten")

							else:

								print('\n The date and calories have not been overwritten.')


					#this will run regardless of the if/elif statements
					pickle_outModify= open(userProfile.name + ".pickle", "wb")
					pickle.dump(userProfile, pickle_outModify)
					pickle_outModify.close()

				elif(updatedProfileChoice = 7):
					newCalories = float(input("Enter in your desired daily caloric deficit: "))

					userProfile.intensity = newCalories
					userProfile.calculateDailyCalories() #update object information in case user wants to remain in the program 

					print("Caloric deficit updated!")

				elif(updatedProfileChoice == 8):

					newActivityLevel = int(input("Enter in your activity level: \n 1 (None) \n 2 (Low) \n 3 (Medium) \n 4 (High) \n 5 (Intense)"))

					userProfile.actLvl = newActivityLevel
					userProfile.calculateDailyCalories() #update object information in case user wants to remain in the program 

				elif(updateProfileChoice == 9):

					modifyLoopRun = False

				elif(updateProfileChoice == 10):

					exit()

				else:

					modifyLoopRun = True

		elif(choice == 5):

			subLoopRun = False

		elif(choice == 6):

			exit()

		else:
			print('Error: Invalid Input, Try again.')
			subLoopRun = True
