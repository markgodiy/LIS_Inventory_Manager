import tkinter as tk
from tkinter import messagebox

# Function to display the selected item in a dialog
def show_selected_item():
    selected_index = listbox.curselection()
    if selected_index:
        selected_item = listbox.get(selected_index[0])
        messagebox.showinfo("Selected Item", f"You selected: {selected_item}")
    else:
        messagebox.showwarning("No Selection", "Please select an item first.")

# Create the main window
root = tk.Tk()
root.title("Item Selector")

# Create a Listbox to display items
listbox = tk.Listbox(root)
listbox.pack(padx=20, pady=20)

# Add some sample items to the Listbox
sample_items = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]
for item in sample_items:
    listbox.insert(tk.END, item)

# Create a button to show the selected item
select_button = tk.Button(root, text="Select Item", command=show_selected_item)
select_button.pack()

# Run the main loop
root.mainloop()
