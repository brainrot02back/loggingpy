# 📘 log generator

## 🧩 Overview

This tool is a **Python-based log generator** designed to help you quickly record and organize information about operations — for instance, when gathering evidence or documenting incidents. It creates a structured folder for each operation, containing a log file and a photo storage directory.

---

## ⚙️ Requirements

Before using this tool, ensure you have the following installed:

* **Python 3.8+** (Recommended)
* The **Tkinter** library (usually included with Python)

If Tkinter is not installed, you can install it using:

```bash
sudo apt-get install python3-tk  # for Linux
```

For Windows, Tkinter is included by default in standard Python distributions.

---

## 🧰 Features

✅ Create organized folders for each operation.
✅ Automatically generate a timestamped log file.
✅ Include essential details like names, phone numbers, locations, and notes.
✅ Auto-create separate folders for photos and logs.

---

##  How to Use

### 1. **Run the Program**

Save the Python script (e.g., `log_generator.py`) and run it with:

```bash
python logging.py
```

### 2. **Enter Information**

When the window opens, fill in the following fields:

* **Operation Name** → The main folder name (e.g., `Operation_Safeguard`).
* **Name** → The name of the person involved.
* **Phone Number** → Contact number for reference.
* **Address** → Location details.
* **Location** → Where the incident took place.
* **Additional Notes** → Any relevant information or context.
* **Other Logs** → Links, notes, or references to other reports.

### 3. **Generate Log**

Click the **"Generate Log"** button.

The program will:

* Create a folder with the operation name.
* Inside it, make two subfolders:

  * `logs/` → Contains a `log.txt` file.
  * `photos/` → For storing photo evidence.

A success message will confirm creation with the file path.

---

## 📂 Example Output

**Folder Structure:**

```
Operation_Safeguard/
│
├── logs/
│   └── log.txt
│
└── photos/
```

**Sample `log.txt` Content:**

```
folder name: Operation_Safeguard
Date and Time: 2025-10-16 21:10:00
Name: John Doe
Phone Number: 555-1234
Address: 123 Maple Street
Location: Downtown Cafe
Additional Notes: Suspect was using fake identity.
Other Logs: Linked to previous report #32.
```

---

##  Notes for Use

* Always verify the data before saving logs.
* Keep sensitive information encrypted or stored securely.
* Use responsibly — for legitimate reporting or documentation purposes only.

---

##  Tips

* You can customize the folders or add automatic image-saving scripts later.
* To export logs into a ZIP archive, use Python’s built-in `shutil.make_archive()`.
* Consider using `datetime` naming for separate operation runs.

---

##  Future Additions

* Cloud sync for logs.
* Encrypted note storage.
* Built-in evidence uploader.

---

###  Author

me brainrot02
