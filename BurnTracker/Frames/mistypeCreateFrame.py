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

		self.configure(bg="#586BE4")
		self.grid_columnconfigure(0, weight=1)
		self.grid_columnconfigure(1, weight=1)
		self.grid_columnconfigure(2, weight=1)

		self.grid_rowconfigure(0, weight=1)
		self.grid_rowconfigure(1, weight=1)
		self.grid_rowconfigure(2, weight=1)


		self.noProfileLabel = tk.Label(self, text="Uh-oh, no profile found.", font=("Helvectica",25),bg="#586BE4")
		self.noProfileLabel.grid(row=0,column=1)

		self.retypeButton = tk.Button(self, text="Retype profile name",width=20 ,font = ("Helvetica", 20),highlightbackground="#586BE4")
		self.retypeButton.bind("<Button-1>",self.controller.backToStartNoSave)
		self.retypeButton.grid(row=1,column=1)

		self.createProfileButton = tk.Button(self, text="Create a new profile", width=20,font = ("Helvetica", 20),highlightbackground="#586BE4")
		self.createProfileButton.bind("<Button-1>", self.controller.infoInput)
		self.createProfileButton.grid(row=2,column=1)
