import os
import customtkinter as ctk

# ** scan the computer for files that contain prompt
# put them into a list
# delete all those files
# delete them from trash bin as well

class BatchDeleteComponent:
    def __init__(self, root):
        self.root = root
        self.all_files = []
        print("Initializing Batch Delete")
        self.frame = ctk.CTkFrame(master=root).pack(padx=20, pady=20)

        self.label = ctk.CTkLabel(master=self.frame, text="Delete Files")
        self.label.pack(padx=12, pady=10)

        self.pattern = ctk.CTkEntry(master=self.frame, placeholder_text='Input Pattern')
        self.pattern.pack(padx=12, pady=10)

        self.button = ctk.CTkButton(master=self.frame, text='Run', command=self.collectFiles)
        self.button.pack()

        print("Batch Delete initialized")

    def collectFiles(self):
        search_pattern = self.pattern.get()
        for directory, _, files in os.walk('/'):
            print(directory)
            for file in files:
                if search_pattern in file:
                    self.all_files.append(os.path.join(directory, file))
        print(self.all_files)

