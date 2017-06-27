import tkinter as tk
import datetime
import os
import pickle


#add all the frames...
from Frames.mistypeCreateFrame import mistypeCreateFrame
from Frames.startFrame import startFrame
from Frames.retrieveDataFrame import retrieveDataFrame
from Frames.mainMenuFrame import mainMenuFrame
from Frames.addDailyWeightFrame import addDailyWeightFrame
from Frames.addDailyCaloriesFrame import addDailyCaloriesFrame
from Frames.visualizeProgressFrame import visualizeProgressFrame
from Frames.profileUpdateFrame import profileUpdateFrame
from Frames.calorieSubMenuFrame import calorieSubMenuFrame
from Frames.modifyCalorieFrame import modifyCalorieFrame
from Frames.deleteCalorieFrame import deleteCalorieFrame
from Frames.weightSubMenuFrame import weightSubMenuFrame
from Frames.modifyWeightFrame import modifyWeightFrame
from Frames.deleteWeightFrame import deleteWeightFrame
from Frames.modifyActivityLvlFrame import modifyActivityLvlFrame
from Frames.modifyCaloricDeficitFrame import modifyCaloricDeficitFrame
from Frames.userSummaryFrame import userSummaryFrame
from Frames.weightGraphFrame import weightGraphFrame
from Frames.calorieGraphFrame import calorieGraphFrame

#add model
from Profile import Profile

"""
Made by Zachary Kim
email: zkim2@illinois.edu
"""

class ProfileWindow(tk.Tk): #this is inheriting from the top most level and will be "controller" of other frame instances

	def __init__(self, *args, **kwargs):

		tk.Tk.__init__(self, *args, **kwargs)

		self.mainFrame = tk.Frame(self,width=800,height=500) #all other frames will have this as the parent.

		self.geometry("800x500+500+300") #doesn't expand with resize currently.

		self.title("BurnTracker")

		#not necessary there is only 1 row and 1 column being filled anyway.
		self.mainFrame.grid_columnconfigure(0, weight=1)
		self.mainFrame.grid_rowconfigure(0, weight=1)
		
		self.mainFrame.grid_propagate(False) #frames resize to mainFrame

		#self.protocol("WM_DELETE_WINDOW", self.xButton)

		self.mainFrame.grid(row=0,column=0,sticky="nsew")

		self.subFrames = {}

		self.userProfile = None 

		self.setUpWidgets()

		self.todaysDate = datetime.date.today() #in this class because an instance is created everytime the user logs in so the datetime will be updated.


	def printProfile(self):

		print(self.userProfile.name)
		print(self.userProfile.caloricData)
		print(self.userProfile.weightData)


#initializations of frames

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
	

	def setUpRaiseSummary(self): #information from the userProfile isn't initialized yet so we can't grid them or we will get an error bc self.userProfile = None

		self.userProfile.calculateDailySummary()

		summaryFrame = userSummaryFrame(self.mainFrame,self)

		self.subFrames[userSummaryFrame.__name__] = summaryFrame

		summaryFrame.grid(row=0,column=0,sticky="nsew")

		self.raiseWidget("userSummaryFrame")


	def setUpWeightGraph(self,event): #information from the userProfile isn't initialized yet so we can't grid them or we will get an error bc self.userProfile = None

		weightFrame = weightGraphFrame(self.mainFrame,self)
		self.subFrames[weightGraphFrame.__name__] = weightFrame
		weightFrame.grid(row=0,column=0,sticky="nsew")

		self.raiseWidget("weightGraphFrame")


	def setUpCalorieGraph(self,event):

		calorieFrame = calorieGraphFrame(self.mainFrame,self)
		self.subFrames[calorieGraphFrame.__name__] = calorieFrame
		calorieFrame.grid(row=0,column=0,sticky="nsew")

		self.raiseWidget("calorieGraphFrame")

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

#button actions

	#start frame field submit

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


				self.setUpRaiseSummary() #finally grids the userSummary and raises it

			
	#create a new profile submit
	def infoInput(self,event):

		self.subFrames["retrieveDataFrame"].clearFrame() #always clear it before next input
		self.raiseWidget("retrieveDataFrame")


#back actions 

	def backToStart(self,event):

		self.subFrames["startFrame"].clearFrame()
		self.save()
		self.raiseWidget("startFrame")

	def backToStartNoSave(self,event):

		self.subFrames["startFrame"].clearFrame()
		self.raiseWidget("startFrame")
			
	def backToProfileValid(self,event):

		self.raiseWidget("mistypeCreateFrame")

	#show mainMenu if going back 

	def backToMainMenu(self,event):

		self.raiseWidget("mainMenuFrame")

	def backToSummary(self,event): #button event of back on mainmenu

		self.setUpRaiseSummary()

	def backToVisualizationMenu(self,event):

		self.raiseWidget("visualizeProgressFrame")
			
	def exit(self,event): #have to exit throught quit button to save.

		self.printProfile()
		pickle_Save = open(self.userProfile.name + ".pickle", "wb")
		pickle.dump(self.userProfile, pickle_Save)
		pickle_Save.close()

		#add saveFeature
		exit()

	def save(self):

		self.printProfile()
		pickle_Save = open(self.userProfile.name + ".pickle", "wb")
		pickle.dump(self.userProfile, pickle_Save)
		pickle_Save.close()

	

	#new profile field submit

	def submitInputValid(self,event): 


		try:
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

			if(inputIntensity > 1100):

				self.subFrames["retrieveDataFrame"].fieldInvalid(6)
				passed=False

		
			if(passed):

				#update the model aka profile object
				self.userProfile.age = inputAge
				self.userProfile.startWeight = inputWeight
				self.userProfile.currentWeight = inputWeight
				self.userProfile.currentHeight = inputHeight
				self.userProfile.goalWeight = inputGoalWeight
				self.userProfile.actLvl = inputActLvl
				self.userProfile.intensity = inputIntensity

				#save and pickle it
				pickle_Save = open(self.userProfile.name + ".pickle", "wb")
				pickle.dump(self.userProfile, pickle_Save)
				pickle_Save.close()

			
				#go to summary 
				self.setUpRaiseSummary()

		except:

			self.subFrames["retrieveDataFrame"].mismatchInvalid()




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


	#calorie submenu button actions
	def sendToCalorieMenu(self,event):

		self.raiseWidget("calorieSubMenuFrame")

	
	def sendToModifyCalories(self,event):

		self.subFrames["modifyCalorieFrame"].clearFrame()
		self.raiseWidget("modifyCalorieFrame")

	def sendToDeleteCalories(self,event):

		self.subFrames["deleteCalorieFrame"].clearFrame()
		self.raiseWidget("deleteCalorieFrame")


	#weight submenu button actions
	def sendToWeightMenu(self,event):

		self.raiseWidget("weightSubMenuFrame")

	def sendToModifyWeight(self,event):

		self.subFrames["modifyWeightFrame"].clearFrame()
		self.raiseWidget("modifyWeightFrame")

	def sendToDeleteWeight(self,event):

		self.subFrames["deleteWeightFrame"].clearFrame()
		self.raiseWidget("deleteWeightFrame")

	#activity level and cal deficit button actions
	def sendToModifyActLvl(self,event):

		self.subFrames["modifyActivityLvlFrame"].clearFrame()
		self.raiseWidget("modifyActivityLvlFrame")


	def sendToModifyIntensity(self,event):

		self.subFrames["modifyCaloricDeficitFrame"].clearFrame()
		self.raiseWidget("modifyCaloricDeficitFrame")


	#Daily weight and calorie fieldsubmits (check input)

	def submitDailyWeight(self,event):

		try:
			userDailyWeight = self.subFrames["addDailyWeightFrame"].weightVar.get()

			if(userDailyWeight >= 90):

				self.userProfile.weightData[self.todaysDate] = userDailyWeight
				self.userProfile.currentWeight = userDailyWeight
				self.subFrames["addDailyWeightFrame"].displaySuccess()

			else:
				self.subFrames["addDailyWeightFrame"].fieldInvalid()
			
		except:

			self.subFrames["addDailyWeightFrame"].fieldInvalid()




	#addDailyWeightFrame submit action which will update model.

	def submitDailyCalories(self,event):


		try:

			userDailyCalories = self.subFrames["addDailyCaloriesFrame"].caloriesVar.get()

			if(userDailyCalories >= 1000):

				self.userProfile.caloricData[self.todaysDate] = userDailyCalories
				self.subFrames["addDailyCaloriesFrame"].displaySuccess()
				self.printProfile()

			else:

				self.subFrames["addDailyCaloriesFrame"].fieldInvalid()

		except:

			self.subFrames["addDailyCaloriesFrame"].fieldInvalid()


		
	#calorie modify submit
	def submitModifyCalories(self,event):

		dateOfCalories = self.subFrames["modifyCalorieFrame"].dateString.get()

		try:

			dateOfCalories = datetime.datetime.strptime(dateOfCalories, '%m/%d/%y') #changes to datetime object

			try:
			
				caloriesToChange = self.subFrames["modifyCalorieFrame"].calorieVar.get()

				if(caloriesToChange > 1000):

					self.userProfile.caloricData[dateOfCalories.date()] = caloriesToChange
					self.subFrames["modifyCalorieFrame"].displaySuccess()

				else:

					self.subFrames["modifyCalorieFrame"].fieldInvalid()

			except:

				self.subFrames["modifyCalorieFrame"].fieldInvalid()

		except:

			self.subFrames["modifyCalorieFrame"].fieldInvalid()


	#calorie delete submit
	def submitDeleteCalories(self,event):

		dateToDelete = self.subFrames["deleteCalorieFrame"].dateString.get()

		try:

			dateToDelete = datetime.datetime.strptime(dateToDelete, '%m/%d/%y')

			dateValid = False

			for key in self.userProfile.caloricData:

				if(key == dateToDelete.date()):
						
					dateValid = True
	

			if(dateValid == False):

				self.subFrames["deleteCalorieFrame"].fieldInvalid()

			else:

				self.userProfile.caloricData.pop(dateToDelete.date(), None) 
				self.subFrames["deleteCalorieFrame"].displaySuccess()


		except:

			self.subFrames["deleteCalorieFrame"].fieldInvalid()

		


	#weight submenu field submit
	def submitModifyWeight(self,event):

		dateOfWeight = self.subFrames["modifyWeightFrame"].dateString.get()

		try:

			dateOfWeight = datetime.datetime.strptime(dateOfWeight, '%m/%d/%y')


			try:

				weightToChange = self.subFrames["modifyWeightFrame"].weightVar.get()

			

				if(weightToChange >= 90):

					self.userProfile.weightData[dateOfWeight.date()] = weightToChange

					self.subFrames["modifyWeightFrame"].displaySuccess()

				else:

					self.subFrames["modifyWeightFrame"].fieldInvalid()

			except:

				self.subFrames["modifyWeightFrame"].fieldInvalid()


		except:

			self.subFrames["modifyWeightFrame"].fieldInvalid()

		


	def submitDeleteWeight(self,event):

		dateToDelete = self.subFrames["deleteWeightFrame"].dateString.get()

		try:

			dateToDelete = datetime.datetime.strptime(dateToDelete, '%m/%d/%y')

			dateValid = False

			for key in self.userProfile.weightData:

				if(key == dateToDelete.date()):

					dateValid = True

			if(dateValid == False):

				self.subFrames["deleteWeightFrame"].fieldInvalid()

			else:

				self.userProfile.weightData.pop(dateToDelete.date(), None) 

				self.subFrames["deleteWeightFrame"].displaySuccess()

		except:

			self.subFrames["deleteWeightFrame"].fieldInvalid()


	#act level and cal def field submit
	def submitModifyActLvl(self,event):

		try:

			newActLvl = self.subFrames["modifyActivityLvlFrame"].actLvlVar.get()

			if(newActLvl >= 1 and newActLvl <=5):

				self.userProfile.actLvl = newActLvl

				self.subFrames["modifyActivityLvlFrame"].displaySuccess()
			
			else:

				self.subFrames["modifyActivityLvlFrame"].fieldInvalid()
		except:

			self.subFrames["modifyActivityLvlFrame"].fieldInvalid()

	def submitModifyIntensity(self,event):

		try:

			newIntensity = self.subFrames["modifyCaloricDeficitFrame"].intensityVar.get()

			if(newIntensity <= 1100):

				self.userProfile.intensity = newIntensity

				self.subFrames["modifyCaloricDeficitFrame"].displaySuccess()	

			else:

				self.subFrames["modifyCaloricDeficitFrame"].fieldInvalid()

		except:

			self.subFrames["modifyCaloricDeficitFrame"].fieldInvalid()
