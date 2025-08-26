from tkinter import *
from tkinter import ttk, messagebox
import time
import random

class TypingSpeedTest:
	global root
	root = Tk()
	def __init__(self, root):
		self.root = root
		self.root.title("Typing Speed Test")
		try:
			self.root.iconbitmap("pics/my_nick_name.ico")
		except:
			pass

		self.level_var = StringVar()
		self.level_var.set("Easy")
		self.sentences = {
			"Easy": [
			"I am who I am.",
			"You can't beat me.",
			"Sleep when you can.",
			"There is no time.",
			"This is too easy."
		],
		"Medium": [
			"No reward for laziness you lazy.",
			"Make hay while the sun shines.",
			"No room for failure, always win.",
			"I am professional Web developer."
			
		],
		"Hard": [
			"When Money Speak Nobody Check it's grammar no one.",
			"Python is a great programming language for beginners.",
			"Typing speed is measured in words per minute or WPM.",
			"Never speak Negative About Yourself Words have power."
		]
	}

		self.setup_welcome_screen()
		self.root.bind("<Return>", self.start_game)

	def setup_welcome_screen(self):
		"""Create initial welcome screen with level selection"""
		self.clear_screen()
		self.root.geometry('274x220')
		self.root.resizable(width="false", height="false")		
		title = Label(self.root, text="Typing Speed Test", bg="#ff0000", relief=SUNKEN)
		title.grid(row=0, column=0, columnspan=3, pady=(10, 10), sticky="ew")
		
		level_label = Label(self.root, text="Choose the level you want to practice!")
		level_label.grid(row=1, column=0, columnspan=3, pady=(0, 20))

		levels = [("Easy", "Easy"), ("Medium", "Medium"), ("Hard", "Hard")]
		for i, (text, level) in enumerate(levels):
			rb = Radiobutton(
				self.root, 
				text=text, 
				variable=self.level_var, 
				value=level
			)
			rb.grid(row=i+2, column=0, columnspan=3, sticky="w", padx=100)

		start_btn = Button(self.root, text="Start", command=self.start_game)
		start_btn.grid(row=5, column=0, columnspan=3, pady=20)

	def setup_game_screen(self):
		"""Create the game interface"""
		self.clear_screen()
		self.root.geometry("270x300")
		self.start_time = time.time()
		
		# Challenge text
		level = self.level_var.get()
		self.challenge_text = random.choice(self.sentences[level])
		self.challenge = Label(
			self.root, 
			text=self.challenge_text, 
			bg="#000000", 
			fg="#ffffff",
			wraplength=500
		)
		self.challenge.grid(row=1, column=1, columnspan=3, padx=(50,0), pady=10, sticky="ew")
		
		# User input
		self.user_input = Entry(self.root)
		self.user_input.grid(row=2, column=1, columnspan=3, padx=(50,0), pady=10, sticky="ew")
		self.user_input.focus()
		
		# Submit button
		self.submit_btn = Button(
			self.root, 
			text="Submit", 
			command=self.check_typing
		)
		self.submit_btn.grid(row=3, column=1, columnspan=3, padx=10, pady=10)
		
		# Theme buttons
		self.theme_frame = Frame(self.root)
		self.theme_frame.grid(row=4, column=0, columnspan=3, pady=10)
		
		Button(self.theme_frame, text="Yellow", bg="#ffff00", command=lambda: self.root.config(bg="yellow")).grid(row=5,column=1,padx=(60,2))
		Button(self.theme_frame, text="White", bg="#ffffff", command=lambda: self.root.config(bg="white")).grid(row=5, column=2)
		Button(self.theme_frame, text="Restart", bg="#c0c0c0", command=self.restart_game).grid(row=5, column=3)
		Button(self.theme_frame, text="Exit",bg="#ff0000", command=self.root.destroy).grid(row=5, column=4)

	def update_timer(self):
		"""Update the running timer display"""
		elapsed = int(time.time() - self.start_time)
		mins, secs = divmod(elapsed, 60)
		try:
			self.timer_label.config(text=f"{mins:02d}:{secs:02d}")
			self.root.after(1000, self.update_timer)
		except:
			pass
			
	def check_typing(self):
		"""Evaluate user's typing performance"""
		user_text = self.user_input.get().strip()
		if not user_text:
			return
			
		elapsed = time.time() - self.start_time
		wpm = round((len(user_text) / elapsed) * 60)

		if user_text == self.challenge_text:
			result = f"You won!\nTime: {int(elapsed)} seconds\nWPM: {wpm}"
		else:
			result = "You lost! Try again."

		self.show_results(result)

	def show_results(self, result):
		"""Display results screen"""
		self.clear_screen()
		self.root.geometry('300x300')
		
		Label(self.root, text="Results", font=("Arial", 19, "bold")).grid(padx=(100, 10))
		
		result_label = Label(self.root, text=result, justify=LEFT)
		result_label.grid(padx=(100,0),pady=(30,10))
		
		Button(
			self.root, 
			text="Play Again", 
			command=self.restart_game
		).grid(padx=(100,0),pady=(30,10))
		
		Button(
			self.root, 
			text="Change Level", 
			command=self.setup_welcome_screen
		).grid(padx=(100,0),pady=(30,10))

	def restart_game(self):
		"""Restart the game with same level"""
		self.setup_game_screen()
		self.size_decide()

	def clear_screen(self):
		"""Remove all widgets from the screen"""
		for widget in self.root.winfo_children():
			widget.destroy()
	
	def size_decide(self):
		# ~ this function controls the geometry size and padding according to option choosen
		if self.level_var.get() == "Easy":
			self.root.geometry('274x220')
			# Timer display
			self.timer_label = Label(self.root, text="00:00", bg="#000000", fg="#ffffff",font=("Arial", 14, "bold"))
			self.timer_label.grid(row=0, column=0, columnspan=3, padx=(45,0), pady=10, sticky="ew")
			self.challenge.grid(row=1, column=0, columnspan=3, padx=(45,0), pady=10, sticky="ew")
			self.user_input.grid(row=2, column=0, columnspan=3, padx=(45,0), pady=10, sticky="ew")
			self.submit_btn.grid(row=3, column=0, columnspan=3, padx=(45,0), pady=10)
			self.theme_frame.grid(row=4, column=0, columnspan=3, pady=10)
			self.update_timer()
			
		elif self.level_var.get() == "Medium":
			self.root.geometry("270x300")
			# Timer display
			self.timer_label = Label(self.root, text="00:00", bg="#000000", fg="#ffffff",font=("Arial", 14, "bold"))
			self.timer_label.grid(row=0, column=0, columnspan=3, padx=(50,0), pady=10, sticky="ew")
			self.challenge.grid(row=1, column=0, columnspan=3, padx=(45,0), pady=10, sticky="ew")
			self.user_input.grid(row=2, column=0, columnspan=3, padx=(45,0), pady=10, sticky="ew")
			self.submit_btn.grid(row=3, column=0, columnspan=3, padx=(45,0), pady=10)
			self.theme_frame.grid(row=4, column=0, columnspan=3, pady=10)
			self.update_timer()
			
		else:
			self.root.geometry("400x300")
			# Timer display
			self.timer_label = Label(self.root, text="00:00", bg="#000000", fg="#ffffff",font=("Arial", 14, "bold"))
			self.timer_label.grid(row=0, column=0, columnspan=3, padx=(50,0), pady=10, sticky="ew")
			self.challenge.grid(row=1, column=0, columnspan=3, padx=(45,0), pady=10, sticky="ew")
			self.user_input.grid(row=2, column=0, columnspan=3, padx=(45,0), pady=10, sticky="ew")
			self.submit_btn.grid(row=3, column=0, columnspan=3, padx=(45,0), pady=10)
			self.theme_frame.grid(row=4, column=0, columnspan=3, pady=10)
			self.update_timer()

	def start_game(self, event=None):
		"""Start the game with selected level"""
		self.root.geometry('474x320')
		self.setup_game_screen()
		self.size_decide()
	
if __name__ == "__main__":
    
    app = TypingSpeedTest(root)
    root.mainloop()
