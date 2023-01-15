import customtkinter # Need this to create GUI
import tkinter # Need this to create an image for my you got pranked
from PIL import ImageTk, Image

#Functions for the buttons
def press():
    global image # Image wasn't loading to canvas without global image (Look up why)
    canvas = tkinter.Canvas(master=root, width=267, height=189)
    canvas.create_image(150, 100, image=image)
    canvas.pack(padx=50, pady=100)
    exit_button = customtkinter.CTkButton(master=root, width=100, height=50, text="Press to end", command=exit)
    prank_button.destroy()
    return exit_button.pack()
# Function creates the exit button while getting rid of the prior button and loadin the meme image
def end():
    exit()
# Functions is for button to exit the program


root = customtkinter.CTk() # Need to make the GUI window
root.geometry("300x300")

prank_button = customtkinter.CTkButton(master=root, width =300, height=300,text="Press!!! ;)", command=press) # Create button and use press function
prank_button.pack()


image = ImageTk.PhotoImage(Image.open("You_Just_got_pranked.gif"))


root.mainloop() # Need at the end to run the window
