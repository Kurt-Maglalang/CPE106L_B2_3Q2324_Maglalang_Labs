import tkinter as tk
from tkinter import filedialog

class FileSelectorApp:
    def __init__(self, master):
        self.master = master
        master.title("File Selector")

        # Create a frame to contain the file label and button
        self.file_frame = tk.Frame(master)
        self.file_frame.pack(padx=10, pady=10)

        # Create the file label
        self.file_label = tk.Label(self.file_frame, text="No file selected", width=40, height=2, anchor="w")
        self.file_label.pack(side="left")

        # Create the select file button
        self.file_button = tk.Button(self.file_frame, text="Select file", command=self.select_file)
        self.file_button.pack(side="left", padx=10)

        # Create the quit button
        self.quit_button = tk.Button(master, text="Quit", command=master.quit, width=10)
        self.quit_button.pack(side="bottom", padx=10, pady=10)

    def select_file(self):
        file_path = filedialog.askopenfilename(
            title="Select a text file",
            filetypes=[("Text files", "*.txt")],
            initialdir="."
        )

        if file_path:
            self.file_label.config(text=file_path)
        else:
            self.file_label.config(text="No file selected")

root = tk.Tk()
app = FileSelectorApp(root)

# Center the window on the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - root.winfo_reqwidth()) // 2
y = (screen_height - root.winfo_reqheight()) // 2
root.geometry("+{}+{}".format(x, y))

root.mainloop()
