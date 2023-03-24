import tkinter as tk
from tkinter import ttk

# Define a custom style for the dark mode theme

def print_selected_option():
    selected_option = dropdown_var.get()
    print("Selected option:", selected_option)
def close_window():
    """Close the main window."""
    root.destroy()    
def toggle_color():
    """Toggle between light and dark background colors."""
    if root.cget("bg") == "white":
        root.configure(bg="#333")
    else:
        root.configure(bg="white")    
def run_script():
    """Run the selected script."""
    script_name = selected_script.get()  # get the selected script name from the dropdown
    print(f"python {script_name}.py")
    #os.system(f"python {script_name}.py") 
# Create the main window
root = tk.Tk()
#set size
root.geometry("500x300")
# Create a label for the dropdown menu
label = tk.Label(root, text="Select an option:")
label.pack()


root.configure(bg="#111")    
button1 = tk.Button(root, text="Click me color", command = toggle_color)
button1.configure(bg="#839")
button1.pack()
# Create a dropdown menu
options = ["Option 1", "Option 2", "Option 3"]
dropdown_var = tk.StringVar(root)
dropdown_var.set(options[0])
dropdown = tk.OptionMenu(root, dropdown_var, *options)
dropdown.pack()

# Create a button to print the selected option
button = tk.Button(root, text="Print selected option", command=print_selected_option)
button.pack()


available_scripts = ["script1", "script2", "script3"]  # replace with your script names
selected_script = tk.StringVar(root)
selected_script.set(available_scripts[0])
script_dropdown = tk.OptionMenu(root, selected_script, *available_scripts)
script_dropdown.configure(bg="#444", fg="white", font=("Arial", 10))
script_dropdown.pack(pady=10)

# Create a button that runs the selected script
run_button = tk.Button(root, text="Run Script", command=run_script)
run_button.configure(bg="#444", fg="white", font=("Arial", 10))
run_button.pack(pady=10)
run_button.place(relx=0.005, rely=0.9, anchor=tk.W)

# Create a button that closes the window
close_button = tk.Button(root, text="Close", command=close_window)
close_button.configure(bg="#444", fg="white", font=("Arial", 10))
close_button.pack(pady=10)

# Run the main loop
root.mainloop()
