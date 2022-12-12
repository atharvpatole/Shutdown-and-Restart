# import modules
from tkinter import *
import os


# user define function
def shutdown():
	return os.system("shutdown /s /t 1")

def restart():
	return os.system("shutdown /r /t 1")

def logout():
	return os.system("shutdown -l")


root = Tk()
root.title("Shutdown & Restart")
root.geometry("300x90")
root.configure(bg='light grey')

Button(root, text="Shutdown", command=shutdown, fg="red").pack(pady=1, padx=1)
Button(root, text="Restart", command=restart, fg="#8B6914").pack(pady=1, padx=1)
Button(root, text="Logout", command=logout, fg="green").pack(pady=1, padx=1)

mainloop()
