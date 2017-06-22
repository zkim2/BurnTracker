import tkinter as tk
import time
from mistypeCreateFrame import mistypeCreateFrame
from startFrame import startFrame
from retrieveDataFrame import retrieveDataFrame
from mainMenuFrame import mainMenuFrame
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

		#self.geometry("500x500+300+300")
		self.mainFrame = tk.Frame(self) #all other frames will have this as the parent.

		#self.mainFrame.grid_columnconfigure(0, weight=1)
		#self.mainFrame.grid_rowconfigure(0,weight=1)

		self.userProfile = Profile()

		self.mainFrame.grid(row=0, column=0, sticky="nsew")

		self.subFrames = {}

		self.setUpWidgets()


	def setUpWidgets(self):

		frameBegin = startFrame(self.mainFrame, self)
		
		frameOops = mistypeCreateFrame(self.mainFrame, self)

		frameInfo = retrieveDataFrame(self.mainFrame,self)

		frameMenu = mainMenuFrame(self.mainFrame,self)
		
		self.subFrames[startFrame.__name__] = frameBegin
		self.subFrames[mistypeCreateFrame.__name__] = frameOops
		self.subFrames[retrieveDataFrame.__name__] = frameInfo
		self.subFrames[mainMenuFrame.__name__] = frameMenu
	
		frameBegin.grid(row=0, column=0,sticky="nsew")

		frameOops.grid(row=0, column=0,sticky="nsew")

		frameInfo.grid(row=0,column=0,sticky="nsew")

		frameMenu.grid(row=0,column=0,sticky="nsew")

		self.raiseWidget("startFrame")
		
		
	def raiseWidget(self, name):

		self.subFrames[name].tkraise()
		


#THIS SECTION CONTROLS IF USER INPUTS A PROFILE THAT IS NOT IN THE CURRENT DIRECTORY
	def checkProfileValid(self,event):

		potentialProfileName = self.subFrames["startFrame"].loginEntry.get()

		result = self.userProfile.findProfile(potentialProfileName)

		if(result):
			self.raiseWidget("mainMenuFrame")
		else:
			self.raiseWidget("mistypeCreateFrame")
	
	def infoInput(self,event):

			self.subFrames["retrieveDataFrame"].clearFrame() #always clear it before next input
			self.raiseWidget("retrieveDataFrame")

	def backToStart(self,event):

			self.subFrames["startFrame"].clearFrame()
			self.raiseWidget("startFrame")
			
	def backToProfileValid(self,event):

			self.raiseWidget("mistypeCreateFrame")
			
	def exit(self,event):

			self.exit()
	
#END OF PROFILE NOT IN CURRENT DIRECTORY

	def checkInputValid(self,event): #eager to put it in frame class but need to separate the controller and frame

		inputAge = self.subFrames["retrieveDataFrame"].ageVar.get()
		inputWeight = self.subFrames["retrieveDataFrame"].weightVar.get()
		inputHeight = self.subFrames["retrieveDataFrame"].heightVar.get()
		inputGoalWeight = self.subFrames["retrieveDataFrame"].goalWeightVar.get()
		inputActLvl = self.subFrames["retrieveDataFrame"].activityLvlVar.get()
		inputIntensity = self.subFrames["retrieveDataFrame"].intensityVar.get()

		passed = True

		print(type(inputAge))
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
			print("Success!!!")
			#self.raiseWidget("SuccessCreate") this is where we initialize our profile


runningApp = ProfileWindow()

runningApp.mainloop()