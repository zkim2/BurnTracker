from tkinter import *


"""
Made by Zachary Kim
email: zkim2@illinois.edu


I want to turn my command line weight loss tracker program into one with a GUI. 

Currently learning how tkinter works..

To do:

1. Create the different frames that will be used
2. Stack and link the frames together
3. Combine the GUI with the command line logic 
4. Make a better design
5. Make executable for easy access and use

"""

class ProfileWindow(Frame):

	def __init__(self, master = None):

		super().__init__(master)
		self.pack()

		self.setUpWidgets()

	def setUpWidgets(self):

		self.welcomeLabel = Label(self, text="Weight Loss Tracker")
		self.welcomeLabel.grid(row=0,column=0,sticky=W)
		
		self.loginLabel = Label(self,text="Login:")
		self.loginLabel.grid(row=1, column = 0,sticky=W)

		self.nameVar = StringVar()
		self.loginEntry = Entry(self,textvariable=self.nameVar)
		self.loginEntry.grid(row=1,column=1,sticky=W)

		self.submitButton = Button(self, text="Submit")	
		self.submitButton.bind("<Button-1>", self.findProfile)
		self.submitButton.grid(row=2, column=0)

	def findProfile(self, event): #just playing around for now.

		if(self.loginEntry.get().lower() == "zachary kim"):

			print("Yes!")

		else:

			print("No!")


root = Tk()

runningApp = ProfileWindow(master = root)

runningApp.mainloop()