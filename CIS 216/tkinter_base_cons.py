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
    
def binary_to_base10():
    bin_string = ent_num_string.get()
    rev_bin_string = ''
    for i in range(-1, -len(bin_string) - 1, -1):
        rev_bin_string += bin_string[i]

    decimal = 0
    for n in range(0, len(rev_bin_string)):
        index = rev_bin_string[n]
        digits = int(2**n) * int((index)) 
        decimal += digits
#    return decimal
    lbl_result_bin["text"] = f"{decimal} in base 10"

root = tk.Tk()
root.title("Base 10 Number Converter")
root.grid()
selected_option = tk.StringVar()
selected_option.set("binary") # default selection

num_type = ''


frame_entry = tk.Frame(root)
frame_entry.grid(row=5, column=0)
ent_num_string = tk.Entry(frame_entry, width=25)
lbl_num_string = tk.Label(frame_entry, text=num_type)

ent_num_string.grid(row=5, column=0, sticky="e")
lbl_num_string.grid(row=5, column=1, sticky="w")

#should this be(master=root) like in the ex?
btn_convert = tk.Button(root, text="\N{RIGHTWARDS BLACK ARROW}", command=binary_to_base10)
btn_convert.grid(row=5, column=2)

#result_bin = tk.Frame(root)
#result_bin.grid(row=5, column=3)
lbl_result_bin = tk.Label(root, text="in base 10")
lbl_result_bin.grid(row=5, column=4)

    


# Create radiobuttons
radiobutton1 = tk.Radiobutton(root, text="binary", variable=selected_option,
value="binary", command=show_selection)
radiobutton1.grid(row=0, column=2, pady=5)
radiobutton2 = tk.Radiobutton(root, text="octal", variable=selected_option,
value="octal", command=show_selection)
radiobutton2.grid(row=1, column=2, pady=5)
radiobutton3 = tk.Radiobutton(root, text="hexadecimal", variable=selected_option,
value="hexadecimal", command=show_selection)
radiobutton3.grid(row=2, column=2, pady=5)
radiobutton4 = tk.Radiobutton(root, text="base5", variable=selected_option,
value="base5", command=show_selection)
radiobutton4.grid(row=3, column=2, pady=5)


    
if selected_option == radiobutton1:
    num_type = 'binary'
elif selected_option == radiobutton2:
    num_type = 'octal'
elif selected_option == radiobutton3:
    num_type = 'hexadecimal'
elif selected_option == radiobutton4:
    num_type = 'base5'
else:
    num_type = 'thinking?'

'''
frame_entry = tk.Frame(root)
frame_entry.grid(row=5, column=5)
output_converted = tk.Entry(frame_entry, width=25)
lbl_output_converted = tk.Label(frame_entry, text=num_type)
'''










root.mainloop()