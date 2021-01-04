import subprocess
import asyncio
import requests
import threading

import tkinter as tk
import goblin_bot2 as goblin


class Application(tk.Frame):
	def __init__(self, master=None):	
		super().__init__(master)
		self.master = master
		self.pack()
			
		self.create_widgets()
		
	def create_widgets(self):
		button = tk.Button(text = "on", command = self.on_button)
		button.pack()
	
	
	def on_button(self):
		#await goblin.startup()
		#
		#loop  =  asyncio. get_event_loop () 
		#task  =  loop.create_task(goblin.startup())
		#
		#await task
		#self.thread1 = threading.Thread(target=goblin.startup())
		#self.thread1.start()
		
		#goblin.startup()
		print("testing")

class ThreadedClient:
	def __init__(self, master):
		self.master = master

thread1 = threading.Thread(target=goblin.startup())
thread1.start()

root = tk.Tk()
app = Application(master=root)
app.mainloop()

