import tkinter as tk

"""
Made by Zachary Kim 
email: zkim2@illinois.edu

IMPORTANT: THIS IS CONSIDERED TO BE A VIEW OF THE PROGRAM.

This frame view communicates with the controller to update the model based upon user input.
"""

class startFrame(tk.Frame):

	def __init__(self, parent, controller):

		tk.Frame.__init__(self, parent)

		self.controller = controller
		self.nameVar = tk.StringVar()


		self.welcomeLabel = tk.Label(self, text="Weight Loss Tracker")
		self.welcomeLabel.grid(row=0,column=0,sticky="W")
		
		self.loginLabel = tk.Label(self,text="Login:")
		self.loginLabel.grid(row=1, column = 0,sticky="W")

		
		self.loginEntry = tk.Entry(self,textvariable=self.nameVar)
		self.loginEntry.grid(row=1,column=1,sticky="W")

		self.submitButton = tk.Button(self, text="Submit")	
		self.submitButton.bind("<Button-1>", self.controller.submitProfileValid)
		self.submitButton.grid(row=3, column=0)


	def clearFrame(self):

		self.nameVar.set("")