# Nmap Script Kiddies Dialog Box (NSKDB)
NSKDB is a graphical user interface (GUI) tool built with Python's tkinter library to simplify the use of the powerful nmap network scanning tool. It allows users to easily select various scan options, specify an IP address, and run nmap commands without needing to memorize the terminal command-line options.  

## Features  
Checkboxes for Common Scans:  

TCP SYN Scan (-sS): Stealthy TCP scan.  
UDP Scan (-sU): Scan open UDP ports.  
Service Version Detection (-sV): Detect service versions running on open ports.  
OS Detection (-O): Identify the operating system of the target.  
Default Scripts (-sC): Run nmap's default scripts for extra info.  
Aggressive Scan (-A): Combines OS detection, service detection, and more.  
Timing Options:  

T1 to T5: Select different timing profiles for scanning speed.  
Additional Options Input: Enter any additional nmap options manually.  

Error Handling:  

Displays appropriate error messages for missing IP addresses or nmap tool not installed.  

## Prerequisites    
Python 3.x: Ensure you have Python installed. Download it from here.    

nmap: This tool requires nmap to be installed on your system.

On Debian/Ubuntu: sudo apt-get install nmap
On Red Hat/CentOS: sudo yum install nmap
On Windows: Download from nmap's official site.

## Installation
### Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/nskdb.git
cd nskdb
### Install required Python libraries:

The only library required is tkinter, which comes pre-installed with Python. If not installed, you can install it with:

bash
Copy code
sudo apt-get install python3-tk
### Run the program:

To start the GUI, run the following command in your terminal:

bash
Copy code
python nskdb.py
### Usage
Launch the application: Once the application window appears, enter the IP address of the target machine in the input field labeled "Enter IP address for scanning".

Select scan options:

Choose from available scan options using the checkboxes.
If needed, specify a timing profile using the radio buttons.
Add additional options (optional): You can input additional nmap options manually.

Submit: Press the "Submit" button to start the scan. The results will be displayed in a pop-up window.

## Example
Scenario: You want to run a TCP SYN scan with OS detection and default scripts, targeting 192.168.1.1.

Steps:

Enter 192.168.1.1 in the IP address field.
Check the checkboxes for:
TCP SYN Scan
OS Detection
Default Scripts
Press the "Submit" button.
The scan results will be shown in a pop-up window.

## Known Issues
Ensure that nmap is installed correctly. If not, an error message will appear, and the scan won't proceed.
This tool currently doesn't support scanning multiple IP addresses or IP ranges.

## Contribution
Feel free to fork this repository and submit pull requests. Contributions to improve the tool are always welcome!

## License
This project is licensed under the MIT License - see the LICENSE file for details.

