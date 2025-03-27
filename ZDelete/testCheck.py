import tkinter as tk

def run_for_all_dc_ids():
    print("Running for all DC IDs...")

def run_for_dc_ids():
    print("Running for specific DC IDs...")

def reset():
    print("Resetting the application...")

# Create the main window
root = tk.Tk()
root.title("DC ID Runner")

# Create buttons
button_all = tk.Button(root, text="Run for all DC IDs", command=run_for_all_dc_ids)
button_specific = tk.Button(root, text="Run for DC IDs", command=run_for_dc_ids)
button_reset = tk.Button(root, text="Reset", command=reset)

# Place buttons on the window
button_all.pack(pady=10)
button_specific.pack(pady=10)
button_reset.pack(pady=10)

# Run the application
root.mainloop()
