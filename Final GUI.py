import tkinter as tk
from subprocess import call

def run_cancer_code():
    call(["python3", "/home/momen/Desktop/Afnan/Final GUI cancer.py"])

def run_xray_code():
    call(["python3", "/home/momen/Desktop/Afnan/Final GUI xray.py"])

def run_clinical_code():
    call(["python3", "/home/momen/Desktop/Afnan/Final GUI clinical.py"])

# Create the main window
root = tk.Tk()
root.title("GUI without Background")

# Create buttons
button_cancer = tk.Button(root, text="Cancer", command=run_cancer_code)
button_cancer.pack(pady=20)

button_xray = tk.Button(root, text="X-Ray", command=run_xray_code)
button_xray.pack(pady=20)

button_clinical = tk.Button(root, text="Clinical", command=run_clinical_code)
button_clinical.pack(pady=20)

# Start the GUI main loop
root.mainloop()
