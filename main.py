from tkinter import Tk

from File_Cleaner_Gui import PROMPT  # type: ignore

# Create the main Tkinter window
root = Tk()

# Create an instance of the PROMPT class and start the GUI
p = PROMPT(root)
p.main()
