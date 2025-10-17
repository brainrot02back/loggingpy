import os
import datetime
import tkinter as tk
from tkinter import messagebox

def generate_log():
    operation_name = entry_operation.get().strip()
    name = entry_name.get().strip()
    phone_number = entry_phone.get().strip()
    address = entry_address.get().strip()
    location = entry_location.get().strip()
    notes = entry_notes.get().strip()
    other_logs = entry_other_logs.get().strip()

    if not operation_name:
        messagebox.showerror("Missing Field", "Operation Name is required.")
        return

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log_content = f"""
folder name: {operation_name}
Date and Time: {timestamp}
Name: {name}
Phone Number: {phone_number}
Address: {address}
Location: {location}
Additional Notes: {notes}
Other Logs: {other_logs}
""".strip()

    
    base_dir = operation_name.replace(" ", "_")
    logs_dir = os.path.join(base_dir, "logs")
    photos_dir = os.path.join(base_dir, "photos")

    try:
        os.makedirs(logs_dir, exist_ok=True)
        os.makedirs(photos_dir, exist_ok=True)

        log_path = os.path.join(logs_dir, "log.txt")
        with open(log_path, "w", encoding="utf-8") as file:
            file.write(log_content)

        messagebox.showinfo("Success", f"Log saved in {log_path}\nPhotos folder created.")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{e}")


root = tk.Tk()
root.title("Log Generator")


tk.Label(root, text="Operation Name:").grid(row=0, column=0, sticky="e")
entry_operation = tk.Entry(root, width=40)
entry_operation.grid(row=0, column=1)

tk.Label(root, text="Name:").grid(row=1, column=0, sticky="e")
entry_name = tk.Entry(root, width=40)
entry_name.grid(row=1, column=1)

tk.Label(root, text="Phone Number:").grid(row=2, column=0, sticky="e")
entry_phone = tk.Entry(root, width=40)
entry_phone.grid(row=2, column=1)

tk.Label(root, text="Address:").grid(row=3, column=0, sticky="e")
entry_address = tk.Entry(root, width=40)
entry_address.grid(row=3, column=1)

tk.Label(root, text="Location:").grid(row=4, column=0, sticky="e")
entry_location = tk.Entry(root, width=40)
entry_location.grid(row=4, column=1)

tk.Label(root, text="Additional Notes:").grid(row=5, column=0, sticky="e")
entry_notes = tk.Entry(root, width=40)
entry_notes.grid(row=5, column=1)

tk.Label(root, text="Other Logs:").grid(row=6, column=0, sticky="e")
entry_other_logs = tk.Entry(root, width=40)
entry_other_logs.grid(row=6, column=1)


generate_button = tk.Button(root, text="Generate Log", command=generate_log, bg="green", fg="white")
generate_button.grid(row=7, columnspan=2, pady=10)

root.mainloop()
