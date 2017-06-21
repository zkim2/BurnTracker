import tkinter as tk

"""
Made by Zachary Kim 
email: zkim2@illinois.edu

IMPORTANT: THIS IS CONSIDERED TO BE A VIEW OF THE PROGRAM.

This frame view communicates with the controller to update the model based upon user input.
"""


class mistypeCreateFrame(tk.Frame):

	def __init__(self,parent,controller):

		tk.Frame.__init__(self,parent)

		self.controller = controller

		self.noProfileLabel = tk.Label(self, text="Uh-oh, no profile found.")
		self.noProfileLabel.grid(row=0,column=0,sticky="W")

		self.retypeButton = tk.Button(self, text="Retype profile name")
		self.retypeButton.bind("<Button-1>",self.controller.backToStart)
		self.retypeButton.grid(row=1,column=0, sticky="W")

		self.createProfileButton = tk.Button(self, text="Create a new profile")
		self.createProfileButton.bind("<Button-1>", self.controller.infoInput)
		self.createProfileButton.grid()