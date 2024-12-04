import tkinter as tk

def show_selection():
    print("Selected option:", selected_option.get())

root = tk.Tk()
root.title("Radiobutton Example")

selected_option = tk.StringVar()
selected_option.set("Option 1") # Default selection

# Create radiobuttons
radiobutton1 = tk.Radiobutton(root, text="Option 1", variable=selected_option, value="Option 1", command=show_selection)
radiobutton1.pack(pady=5)

radiobutton2 = tk.Radiobutton(root, text="Option 2", variable=selected_option, value="Option 2", command=show_selection)
radiobutton2.pack(pady=5)

radiobutton3 = tk.Radiobutton(root, text="Option 3", variable=selected_option, value="Option 3", command=show_selection)
radiobutton3.pack(pady=5)

root.mainloop()