import tkinter as tk
'''
user input space for the base 10 number to convert
Entry ent_base10
Label lbl_result
Button btn_convert
window = tk.Tk()
window.title("Base 10 Number Converter")
window.resizable(width=True, height=True)
'''
def show_selection():
    print("Selected option:", selected_option.get())
    
def base10_to_binary():
    

root = tk.Tk()
root.title("Base 10 Number Converter")
root.grid()
selected_option = tk.StringVar()
selected_option.set("Option 1") # default selection


# Create radiobuttons
radiobutton1 = tk.Radiobutton(root, text="Option 1", variable=selected_option,
value="Option 1", command=show_selection)
radiobutton1.grid(row=0, column=2, pady=5)
radiobutton2 = tk.Radiobutton(root, text="Option 2", variable=selected_option,
value="Option 2", command=show_selection)
radiobutton2.grid(row=1, column=2, pady=5)
radiobutton3 = tk.Radiobutton(root, text="Option 3", variable=selected_option,
value="Option 3", command=show_selection)
radiobutton3.grid(row=2, column=2, pady=5)
radiobutton4 = tk.Radiobutton(root, text="Option 4", variable=selected_option,
value="Option 4", command=show_selection)
radiobutton4.grid(row=3, column=2, pady=5)


frame_entry = tk.Frame(root)
frame_entry.grid(row=5, column=0)
ent_base10num = tk.Entry(frame_entry, width=25)
lbl_base10 = tk.Label(frame_entry, text="in base 10")

ent_base10num.grid(row=5, column=0, sticky="e")
lbl_base10.grid(row=5, column=1, sticky="w")

btn_convert = tk.Button(root, text="\N{RIGHTWARDS BLACK ARROW}")
btn_convert.grid(row=5, column=2)

lbl_result_bin = tk.Label(root, text="binary")
lbl_result_bin.grid(row=5, column=4)
lbl_result_oct = tk.Label(root, text="octal")
lbl_result_oct.grid(row=5, column=4)
lbl_result_base5 = tk.Label(root, text="base5")
lbl_result_base5.grid(row=5, column=4)
lbl_result_hexa = tk.Label(root, text="hexadecimal")
lbl_result_hexa.grid(row=5, column=4)



root.mainloop()

