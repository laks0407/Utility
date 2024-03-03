import customtkinter as ctk
from batchDelete import BatchDeleteComponent

def main():
    root = ctk.CTk()
    root.geometry("500x500")
    root.title("Utoolity")
    app = BatchDeleteComponent(root)
    root.mainloop()

if __name__ == "__main__":
    main()
