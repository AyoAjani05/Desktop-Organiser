from tkinter import Tk, Label, IntVar, ttk, PhotoImage
from tkinter.filedialog import askdirectory
import pathlib
import os
from shutil import move
from time import sleep  # Optional for visual delay

class PROMPT:
    """
    A class representing a custom prompt interface using tkinter for file organization.

    Attributes:
        master (Tk): The tkinter root window.
    """

    def __init__(self, master):
        """
        Initializes the prompt window and displays the selected directory.

        Args:
            master (Tk): The tkinter root window.
        """

        self.master = master
        self.master.title('Organizer')
        self.master.geometry("300x120")
        data = b'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'
        p1 = PhotoImage(data=data)
        # Setting icon of master window
        self.master.iconphoto(False, p1)

        # Get the selected directory path
        self.dir = pathlib.Path(askdirectory(initialdir=pathlib.Path.home()))

        # Display selected directory label
        self.dir_label = Label(
            master=self.master,
            text='Cleaning ' + self.dir.name,
            width=200
        ).place(x=50, y=20)

        # Initialize progress bar for visual feedback
        self.progress = IntVar()
        self.progressbar = ttk.Progressbar(
            maximum=100, variable=self.progress
        )
        self.progressbar.place(x=50, y=50, width=200)

    def cleaner(self):
        """
        Organizes files in the selected directory by moving them to specific subfolders.

        Raises:
            OSError: Potential file system errors during move operations.
        """

        destination = self.dir
        os.chdir(destination)  # Change working directory to selected path

        # Define a dictionary mapping file extensions to category labels
        file_type = {
            'access': "Access Files",
            'pptx': "Powerpoint Files",
            'exe': "Executable Files",
            'lnk': "Shortcut Files",
            'docx': "Word Files",
            'pdf': "Pdf Files",
            'ini': "Init Files",
            'py': "Python Files",
            'xlsx': "Excel Files",
            'pptm': "Powerpoint Files",
            'msi': "Installer Files",
            'rar': "Zipped Files",
            'txt': "Text Files",
            'doc': "Word Files",
            'zip': "Zipped Files",
            'sql': "Sql Files",
            'gz': "Zipped Files"
        }

        # Track file processing progress
        count, total_files = 0, len(os.listdir())
        for filename in os.listdir():
            # Split filename to get extension
            file_parts = filename.split(".")

            if len(file_parts) > 1:
                extension = file_parts[-1]
                category = file_type.get(extension, None)

                if category:
                    # Create category subfolder if it doesn't exist
                    new_path_dir = destination / category
                    if not os.path.exists(new_path_dir):
                        os.makedirs(new_path_dir)

                    # Move file to its category subfolder
                    old_path = destination / filename
                    new_path = new_path_dir / filename
                    try:
                        move(old_path, new_path)
                        print(f"Successfully moved {filename}")
                    except OSError:
                        pass  # Handle potential file move errors silently

                else:
                    print(f"File type '{extension}' not categorized.")

            else:
                print(f"{filename} is a folder (not processed).")

            count += 1
            percent_complete = (count / total_files) * 100

            # Update progress bar and potentially add visual delay for effect
            self.progress.set(percent_complete)
            self.progressbar.update_idletasks()
            # sleep(0.1)  # Optional delay for visual feedback (uncomment if desired)

        # Close the prompt window after organization is complete
        self.master.destroy()

    def main(self):
        """
        Starts the application by running the organization logic and entering the main event loop.
        """

        self.cleaner()
        self.master.mainloop()
