# Nmap Script Kiddies Dialog Box or NSKDB
import tkinter as tk
from tkinter import messagebox
import subprocess

def submit_ip_and_scan():
    # Get the IP address and additional options input
    ip_address = entry_ip.get()
    additional_options = entry_additional_options.get()

    if not ip_address:
        messagebox.showwarning("Input Error", "Please enter a valid IP address.")
        return

    # Initialize nmap command
    nmap_command = ['nmap']

    # Add options based on selected checkboxes
    if var_syn_scan.get():
        nmap_command.append('-sS')  # TCP SYN scan
    if var_udp_scan.get():
        nmap_command.append('-sU')  # UDP scan
    if var_service_scan.get():
        nmap_command.append('-sV')  # Service/version detection
    if var_os_detection.get():
        nmap_command.append('-O')   # OS detection
    if var_default_scripts.get():
        nmap_command.append('-sC')  # Default scripts
    if var_aggressive_scan.get():
        nmap_command.append('-A')   # Aggressive scan

    # Add timing option based on selected radio button (T1, T2, T3, etc.)
    timing_option = var_timing.get()
    if timing_option != 0:
        nmap_command.append(f'-T{timing_option}')

    # Append any additional options manually entered
    if additional_options:
        nmap_command.extend(additional_options.split())

    # Append the IP address to the command
    nmap_command.append(ip_address)

    # Run the nmap command with the selected options
    try:
        scan_result = subprocess.check_output(nmap_command, stderr=subprocess.STDOUT, text=True)
        full_message = f"Scan Results:\n{scan_result}"
        messagebox.showinfo("Scan Results", full_message)
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Scan Error", f"An error occurred while running nmap:\n{e.output}")
    except FileNotFoundError:
        messagebox.showerror("Error", "nmap tool not found. Please ensure nmap is installed.")

# Create the main window
root = tk.Tk()
root.title("Nmap IP Scanner with Options")

# Set window size (width x height)
root.geometry("600x600")

# Define variables for checkboxes (TCP SYN Scan, UDP Scan, Service Scan, OS Detection, Default Scripts, Aggressive Scan)
var_syn_scan = tk.BooleanVar()
var_udp_scan = tk.BooleanVar()
var_service_scan = tk.BooleanVar()
var_os_detection = tk.BooleanVar()
var_default_scripts = tk.BooleanVar()
var_aggressive_scan = tk.BooleanVar()

# Define variable for timing options (Radio Buttons)
var_timing = tk.IntVar(value=0)  # Default to no timing option selected

# Create checkboxes for features
cb_syn_scan = tk.Checkbutton(root, text="TCP SYN Scan (-sS)", variable=var_syn_scan)
cb_udp_scan = tk.Checkbutton(root, text="UDP Scan (-sU)", variable=var_udp_scan)
cb_service_scan = tk.Checkbutton(root, text="Service Version Detection (-sV)", variable=var_service_scan)
cb_os_detection = tk.Checkbutton(root, text="OS Detection (-O)", variable=var_os_detection)
cb_default_scripts = tk.Checkbutton(root, text="Default Scripts (-sC)", variable=var_default_scripts)
cb_aggressive_scan = tk.Checkbutton(root, text="Aggressive Scan (-A)", variable=var_aggressive_scan)

# Create radio buttons for timing options (-T1, -T2, -T3, etc.)
label_timing = tk.Label(root, text="Timing options:")
rb_t1 = tk.Radiobutton(root, text="T1 (Slow)", variable=var_timing, value=1)
rb_t2 = tk.Radiobutton(root, text="T2", variable=var_timing, value=2)
rb_t3 = tk.Radiobutton(root, text="T3 (Default)", variable=var_timing, value=3)
rb_t4 = tk.Radiobutton(root, text="T4 (Faster)", variable=var_timing, value=4)
rb_t5 = tk.Radiobutton(root, text="T5 (Aggressive)", variable=var_timing, value=5)

# Create a label and entry for additional options
label_additional_options = tk.Label(root, text="Enter additional nmap options (optional):")
entry_additional_options = tk.Entry(root)

# Create a label and entry for the IP address input (placed at the bottom)
label_ip = tk.Label(root, text="Enter IP address for scanning:")
entry_ip = tk.Entry(root)

# Create a submit button
submit_button = tk.Button(root, text="Submit", command=submit_ip_and_scan)

# Place the widgets in the window
cb_syn_scan.pack()
cb_udp_scan.pack()
cb_service_scan.pack()
cb_os_detection.pack()
cb_default_scripts.pack()
cb_aggressive_scan.pack()
label_timing.pack()
rb_t1.pack()
rb_t2.pack()
rb_t3.pack()
rb_t4.pack()
rb_t5.pack()
label_additional_options.pack()
entry_additional_options.pack()

# Place IP address input at the bottom
label_ip.pack(pady=10)
entry_ip.pack(pady=5)
submit_button.pack(pady=10)

# Start the GUI event loop
root.mainloop()
