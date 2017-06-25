import tkinter as tk
import datetime
import os
import pickle
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt


#add all the frames...
from mistypeCreateFrame import mistypeCreateFrame
from startFrame import startFrame
from retrieveDataFrame import retrieveDataFrame
from mainMenuFrame import mainMenuFrame
from addDailyWeightFrame import addDailyWeightFrame
from addDailyCaloriesFrame import addDailyCaloriesFrame
from visualizeProgressFrame import visualizeProgressFrame
from profileUpdateFrame import profileUpdateFrame

from calorieSubMenuFrame import calorieSubMenuFrame
from modifyCalorieFrame import modifyCalorieFrame
from deleteCalorieFrame import deleteCalorieFrame

from weightSubMenuFrame import weightSubMenuFrame
from modifyWeightFrame import modifyWeightFrame
from deleteWeightFrame import deleteWeightFrame

from modifyActivityLvlFrame import modifyActivityLvlFrame
from modifyCaloricDeficitFrame import modifyCaloricDeficitFrame
from Profile import Profile

"""
Made by Zachary Kim
email: zkim2@illinois.edu

IMPORTANT: THIS IS CONSIDERED TO BE THE CONTROLLER OF THE PROGRAM.

Will change the file name to something more specific after all is finished.


To do:

1. Create the different frames that will be used
2. Stack and link the frames together
3. Combine the GUI with the command line logic 
4. Make a better design
5. Make executable for easy access and use

"""

class ProfileWindow(tk.Tk): #this is inheriting from the top most level and will be "controller" of other frame instances

	def __init__(self, *args, **kwargs):

		tk.Tk.__init__(self, *args, **kwargs)

		self.mainFrame = tk.Frame(self,width=800,height=500) #all other frames will have this as the parent.

		self.geometry("800x500+500+300")
		self.title("TrackThat")
		#not necessary there is only 1 row and 1 column being filled anyway.
		self.mainFrame.grid_columnconfigure(0, weight=1)
		self.mainFrame.grid_rowconfigure(0, weight=1)
		
		self.mainFrame.grid_propagate(False) #frames resize to mainFrame
		#self.protocol("WM_DELETE_WINDOW", self.xButton)

		self.mainFrame.grid(row=0,column=0,sticky="nsew")

		self.subFrames = {}

		self.setUpWidgets()

		self.todaysDate = datetime.date.today() #in this class because an instance is created everytime the user logs in so the datetime will be updated.

	def setUpWidgets(self):

		for eachFrame in (startFrame, mistypeCreateFrame, retrieveDataFrame, mainMenuFrame, addDailyWeightFrame, addDailyCaloriesFrame, visualizeProgressFrame, profileUpdateFrame, calorieSubMenuFrame, modifyCalorieFrame,deleteCalorieFrame, weightSubMenuFrame, modifyWeightFrame, deleteWeightFrame, modifyActivityLvlFrame, modifyCaloricDeficitFrame):

			currentFrame = eachFrame(self.mainFrame, self)

			self.subFrames[eachFrame.__name__] = currentFrame

			currentFrame.grid(row=0,column=0,sticky="nsew") 

			"""
			IMPORTANT NOTE: sticky="nsew" does center frame however in this case we are putting ALL frames on a single mainframe and so all frames are as wide as the biggest one.
			 SO, the frames appear to be not centered because their widths are stretched. removing the bigger frames results in the frame being correctly centered. 
	
			To overcome this, we will use grid_columnconfigure and grid_rowconfigure on each frame to ensure a centered layout AND have each frame be of set width and height.
			"""
		
		self.raiseWidget("startFrame")
		
		
	def raiseWidget(self, name):

		self.subFrames[name].tkraise()
		
		"""
	def xButton(self): #different from exit() function because this isn't the result of a button press.

		pickle_Save = open(self.userProfile.name + ".pickle", "wb")
		pickle.dump(self.userProfile, pickle_Save)
		pickle_Save.close()

		#add saveFeature
		exit()
		"""

	#THIS SECTION CONTROLS IF USER INPUTS A PROFILE THAT IS NOT IN THE CURRENT DIRECTORY
	def submitProfileValid(self,event): 

		#checks current directory to see if a profile is created under this user. supposed to be in the model but it's easier to load object in the controller
		#in the profile model i would be doing self = pickle.load() which doesn't work.

		potentialProfileName = self.subFrames["startFrame"].loginEntry.get()

		potentialProfileName = potentialProfileName.replace(' ' , '')

		potentialProfileName= potentialProfileName.lower()

		if(len(potentialProfileName) == 0):

			self.subFrames["startFrame"].fieldInvalid()

		else:

			file_name = potentialProfileName + '.pickle'

			cur_dir = os.getcwd()

			inSystem = False

			file_list = os.listdir(cur_dir)

			for file in file_list:

				if(file == file_name):

					inSystem = True
					break

			if(inSystem == False):

				self.userProfile = Profile(name=potentialProfileName) #normal constructor
				self.raiseWidget("mistypeCreateFrame")

			else:
				
				pickle_inProfile = open(potentialProfileName + ".pickle", "rb")

				self.userProfile = pickle.load(pickle_inProfile) #previous object


				self.raiseWidget("mainMenuFrame")

	
	#this button sends to the frame that gets user data
	def infoInput(self,event):

		self.subFrames["retrieveDataFrame"].clearFrame() #always clear it before next input
		self.raiseWidget("retrieveDataFrame")


	def backToStart(self,event):

		self.subFrames["startFrame"].clearFrame()
		self.raiseWidget("startFrame")
			
	def backToProfileValid(self,event):

		self.raiseWidget("mistypeCreateFrame")

	#show mainMenu if going back 

	def backToMainMenu(self,event):

		self.raiseWidget("mainMenuFrame")
			
	def exit(self,event): #have to exit throught quit button to save.

		pickle_Save = open(self.userProfile.name + ".pickle", "wb")
		pickle.dump(self.userProfile, pickle_Save)
		pickle_Save.close()

		#add saveFeature
		exit()
	

	#submit on retrieveDataFrame checks the info.

	def submitInputValid(self,event): 

		inputAge = self.subFrames["retrieveDataFrame"].ageVar.get() #getting info from the view 
		inputWeight = self.subFrames["retrieveDataFrame"].weightVar.get()
		inputHeight = self.subFrames["retrieveDataFrame"].heightVar.get()
		inputGoalWeight = self.subFrames["retrieveDataFrame"].goalWeightVar.get()
		inputActLvl = self.subFrames["retrieveDataFrame"].activityLvlVar.get()
		inputIntensity = self.subFrames["retrieveDataFrame"].intensityVar.get()

		passed = True

		#makes sure input is valid before updating model

		if(inputAge <= 0 or inputAge >=130):
	
			self.subFrames["retrieveDataFrame"].fieldInvalid(1)
			passed=False

		if(inputWeight <=0 or inputWeight >= 1000):
		
			self.subFrames["retrieveDataFrame"].fieldInvalid(2)
			passed=False

		if(inputHeight <= 0 or inputHeight >= 84):

			self.subFrames["retrieveDataFrame"].fieldInvalid(3)
			passed=False

		if(inputGoalWeight >= inputWeight or inputGoalWeight <=0 or inputGoalWeight >= 1000):

			self.subFrames["retrieveDataFrame"].fieldInvalid(4)
			passed=False

		if(inputActLvl < 1 or inputActLvl > 5):

			self.subFrames["retrieveDataFrame"].fieldInvalid(5)
			passed=False

		if(inputIntensity != 500 and inputIntensity != 750 and inputIntensity != 1000):

			self.subFrames["retrieveDataFrame"].fieldInvalid(6)
			passed=False

	
		if(passed):

			#update the model aka profile object
			self.userProfile.age = inputAge
			self.userProfile.currentWeight = inputWeight
			self.userProfile.currentHeight = inputHeight
			self.userProfile.goalWeight = inputGoalWeight
			self.userProfile.actLvl = inputActLvl
			self.userProfile.intensity = inputIntensity

			#save and pickle it
			pickle_Save = open(self.userProfile.name + ".pickle", "wb")
			pickle.dump(self.userProfile, pickle_Save)
			pickle_Save.close()

		

			#go to mainMenu
			self.raiseWidget("mainMenuFrame") 


	#Main menu button actions

	def addDailyWeight(self,event):

		self.subFrames["addDailyWeightFrame"].clearFrame()
		self.raiseWidget("addDailyWeightFrame")

	def addDailyCalories(self,event):

		self.subFrames["addDailyCaloriesFrame"].clearFrame()
		self.raiseWidget("addDailyCaloriesFrame")

	def visualizeProgress(self,event):

		self.raiseWidget("visualizeProgressFrame")

	def updateProfileInfo(self,event):

		self.raiseWidget("profileUpdateFrame")



	#profile update button actions

	def sendToCalorieMenu(self,event):

		self.raiseWidget("calorieSubMenuFrame")

	#calorie submenu button actions
	def sendToModifyCalories(self,event):

		self.subFrames["modifyCalorieFrame"].clearFrame()
		self.raiseWidget("modifyCalorieFrame")

	def sendToDeleteCalories(self,event):

		self.subFrames["deleteCalorieFrame"].clearFrame()
		self.raiseWidget("deleteCalorieFrame")

	def sendToWeightMenu(self,event):

		self.raiseWidget("weightSubMenuFrame")

	def sendToModifyWeight(self,event):

		self.subFrames["modifyWeightFrame"].clearFrame()
		self.raiseWidget("modifyWeightFrame")

	def sendToDeleteWeight(self,event):

		self.subFrames["deleteWeightFrame"].clearFrame()
		self.raiseWidget("deleteWeightFrame")


	def sendToModifyActLvl(self,event):

		self.subFrames["modifyActivityLvlFrame"].clearFrame()
		self.raiseWidget("modifyActivityLvlFrame")


	def sendToModifyIntensity(self,event):

		self.subFrames["modifyCaloricDeficitFrame"].clearFrame()
		self.raiseWidget("modifyCaloricDeficitFrame")
	#addDaillyWeightFrame submit action which will update model.

	def submitDailyWeight(self,event):

		userDailyWeight = self.subFrames["addDailyWeightFrame"].weightVar.get()

		if(userDailyWeight >= 90):
			self.userProfile.weightData[self.todaysDate] = userDailyWeight
			self.subFrames["addDailyWeightFrame"].displaySuccess()

		else:
			self.subFrames["addDailyWeightFrame"].fieldInvalid()
		#add feature that warns user about adding multiple entries on the same day.

		


	#addDailyWeightFrame submit action which will update model.

	def submitDailyCalories(self,event):

		userDailyCalories = self.subFrames["addDailyCaloriesFrame"].caloriesVar.get()

		if(userDailyCalories >= 1000):

			self.userProfile.caloricData[self.todaysDate] = userDailyCalories
			self.subFrames["addDailyCaloriesFrame"].displaySuccess()

		else:

			self.subFrames["addDailyCaloriesFrame"].fieldInvalid()

		#add feature that warns user about adding multiple entries on the same day.
		
		


	def submitModifyCalories(self,event):

		dateOfCalories = self.subFrames["modifyCalorieFrame"].dateString.get()

		dateOfCalories = datetime.datetime.strptime(dateOfCalories, '%m/%d/%y') #changes to datetime object

		caloriesToChange = self.subFrames["modifyCalorieFrame"].calorieVar.get()

		self.userProfile.caloricData[dateOfCalories] = caloriesToChange

		#print(self.userProfile.caloricData)

		self.subFrames["modifyCalorieFrame"].displaySuccess()

	def submitDeleteCalories(self,event):

		dateToDelete = self.subFrames["deleteCalorieFrame"].dateString.get()

		dateToDelete = datetime.datetime.strptime(dateToDelete, '%m/%d/%y')

		self.userProfile.caloricData.pop(dateToDelete, None) 

		self.subFrames["deleteCalorieFrame"].displaySuccess()

	def submitModifyWeight(self,event):

		dateOfWeight = self.subFrames["modifyWeightFrame"].dateString.get()

		dateOfWeight = datetime.datetime.strptime(dateOfWeight, '%m/%d/%y')

		weightToChange = self.subFrames["modifyWeightFrame"].weightVar.get()

		self.userProfile.weightData[dateOfWeight] = weightToChange

		#print(self.userProfile.weightData)
		#print(self.userProfile.caloricData)

		self.subFrames["modifyWeightFrame"].displaySuccess()

	def submitDeleteWeight(self,event):

		dateToDelete = self.subFrames["deleteWeightFrame"].dateString.get()

		dateToDelete = datetime.datetime.strptime(dateToDelete, '%m/%d/%y')

		self.userProfile.weightData.pop(dateToDelete, None) 

		self.subFrames["deleteWeightFrame"].displaySuccess()


	def submitModifyActLvl(self,event):

		newActLvl = self.subFrames["modifyActivityLvlFrame"].actLvlVar.get()

		self.userProfile.actLvl = newActLvl

		self.subFrames["modifyActivityLvlFrame"].displaySuccess()

	def submitModifyIntensity(self,event):

		newIntensity = self.subFrames["modifyCaloricDeficitFrame"].intensityVar.get()

		self.userProfile.intensity = newIntensity

		self.subFrames["modifyCaloricDeficitFrame"].displaySuccess()	


	def graphWeightLoss(self,event):

		sortedData = sorted(self.userProfile.weightData.items(), key = lambda d: d[0])

		
		plt.suptitle('Weight Loss Progress for ' + self.userProfile.name + ' as of ' + self.todaysDate.strftime("%m/%d/%y"), fontsize=14, fontweight='bold')
		"""
		#x are the keys(dateTime objects) and y are the weights
		x,y = zip(*sortedData)
		plt.plot(x,y)
		plt.ylabel('Weight (lbs)')
		plt.xlabel('Time (days)')
	"""
		plt.show()
		

	def graphCalories(self,event):

		sortedData = sorted(self.userProfile.caloricData.items(), key = lambda d: d[0])

		plt.suptitle('Calories over time for ' + self.userProfile.name + ' as of' + self.todaysDate.strftime("%m/%d/%y"), fontsize=14, fontweight='bold')

		x,y = zip(*sortedData)
		plt.plot(x,y)
		plt.ylabel('Calories')
		plt.xlabel('Time (days)')
		plt.show()


runningApp = ProfileWindow()


runningApp.mainloop()