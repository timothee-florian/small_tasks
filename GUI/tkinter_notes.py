import tkinter as tk
from tkinter import ttk
import os
# Define a custom style for the dark mode theme

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
    env_name = selected_env.get()
    script_name = selected_script.get()  # get the selected script name from the dropdown
    # print(f"{env_name}python {script_name}.py")
    os.system(f"{env_name} {script_name}") 
# Create the main window
root = tk.Tk()
#set size
root.geometry("500x300")
# Create a label for the dropdown menu
label = tk.Label(root, text="Operation room")

label.configure(bg="#511", fg="white", font=("Arial", 15)) 
label.pack()


root.configure(bg="#115")    


available_scripts = [r"C:\...\script1.py", r"C:\...\script2.py"] 
selected_script = tk.StringVar(root)
selected_script.set(available_scripts[0])
script_dropdown = tk.OptionMenu(root, selected_script, *available_scripts)
script_dropdown.configure(bg="#444", fg="white", font=("Arial", 10))
script_dropdown.pack(pady=10)
script_dropdown.configure(bg="#829")
script_dropdown.place(relx=0.05, rely=0.4, anchor=tk.W)

available_envs = [r"C:\...\env1\python.exe", r"C:\...\env2\python.exe"] 
selected_env = tk.StringVar(root)
selected_env.set(available_envs[0])
env_dropdown = tk.OptionMenu(root, selected_env, *available_envs)
env_dropdown.configure(bg="#444", fg="white", font=("Arial", 10))
env_dropdown.pack(pady=10)
env_dropdown.configure(bg="#849")
env_dropdown.place(relx=0.05, rely=0.2, anchor=tk.W)

# Create a button that runs the selected script
run_button = tk.Button(root, text="Run Script", command=run_script)
run_button.configure(bg="#444", fg="white", font=("Arial", 10))
run_button.pack(pady=10)
run_button.place(relx=0.005, rely=0.9, anchor=tk.W)

# Create a button that closes the window
close_button = tk.Button(root, text="Close", command=close_window)
close_button.configure(bg="#444", fg="white", font=("Arial", 10))
close_button.pack(pady=10)
close_button.place(relx=0.995, rely=0.9, anchor=tk.E)
# Run the main loop
root.mainloop()