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


		self.grid_columnconfigure(0, weight=1)
		self.grid_columnconfigure(1,weight=1)
		self.grid_columnconfigure(2, weight=1)
		
		
		self.grid_rowconfigure(0, weight=1)
		self.grid_rowconfigure(1, weight=0)
		self.grid_rowconfigure(2, weight=0)
		self.grid_rowconfigure(3, weight=1)
		

		self.controller = controller

		self.nameVar = tk.StringVar()


		self.welcomeLabel = tk.Label(self, text="TrackThat", font=("Helvectica",25))
		self.welcomeLabel.grid(row=0,column=1,sticky="nsew")

		self.nameEmpty = tk.Label(self,text="", font=("Helvetica",15))
		self.nameEmpty.grid(row=1, column=1, sticky="nsew")
		
		self.loginLabel = tk.Label(self,text="Profile Name:", font=("Helvectica",20))
		self.loginLabel.grid(row=2,column=0,sticky="nsew")

		
		self.loginEntry = tk.Entry(self,textvariable=self.nameVar, font=("Helvetica", 20))
		self.loginEntry.grid(row=2,column=1,sticky="nsew")

		self.submitButton = tk.Button(self, text="Submit",font = ("Helvetica", 15))	
		self.submitButton.bind("<Button-1>", self.controller.submitProfileValid)
		#self.submitButton.focus_set()

		self.submitButton.grid(row=3,column=1)


	def clearFrame(self):

		self.nameVar.set("")
		self.nameEmpty['text'] = ""


	def fieldInvalid(self):

		self.nameEmpty['text'] = "No name entered **"
		self.nameEmpty['fg'] = "red"

