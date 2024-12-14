#This logic file handles all the nmap logic, input validation, and file writing for the program.
from PyQt6.QtWidgets import *
from PortScan1 import *
from PortScan2 import *
import nmap
import datetime
import re





class Logic(QMainWindow, Ui_MainWindow) :
    def __init__(self)-> None:
        """
        This __init__ method initializes the UI for the scanner, while also defining some of the variables


        """
        super().__init__()
        self.setupUi(self)
        self.type: str = ''
        self.scanner = nmap.PortScanner()
        self.prot: str= ''
        self.load = Load()
        self.IP_Entry.setCursorPosition(0) #I decided to define the cursor positions in this class,
        # since it was giving me issues in the PortScan1 file
        self.port1.setCursorPosition(0)
        self.port2.setCursorPosition(0)
        self.scan_button.clicked.connect(lambda : self.scan())# This line connects the scan button to the below scan function


       


    def scan(self) -> None:
        """
        This where the scan itself happens. "scan" will take all the input, sanitize, and then store the output
        of the nmap scan into a text file. The self.load variable initializes the loading window where needed.



        :return: Output to outcome.txt.
        """
        try:
            target_ip: str = self.IP_Entry.text().strip('.') # The strip statements help the program to validate data since an Input mask is used.
            ip_regex: str = r'(\b25[0-5]|\b2[0-4][0-9]|\b[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}' # Regex for checking IPv4
            port1: int = self.port1.text().strip()
            port2: int = self.port2.text().strip()

            if not target_ip: #The following address any kind of invalid input made by a user, most of this is handled in the
                #PortScan file.
                raise ValueError("IP address field cannot be empty")
            if not re.fullmatch(ip_regex, target_ip):
                raise ValueError("Please input an IP address in IPv4 Format")
            if not self.SYN_radio.isChecked() and not self.UDP_radio.isChecked() and not self.TCP_radio.isChecked() and not self.ping_radio.isChecked() and not self.idle_radio.isChecked():
                raise ValueError("Please choose a scan type")
            if not port1 or not port2:
                raise ValueError("Port range fields cannot be empty")


            target_ip = self.IP_Entry.text() # These lines retrieve the data and store them as a string and two integers
            port1 = int(self.port1.text())
            port2 = int(self.port2.text())
            if port2 < port1: # Port range check
                raise ValueError("Please enter a valid range")
            self.prot = 'tcp'
            if self.SYN_radio.isChecked(): # The following if statements change the "self.type" variable, which is one of
                # the variables used in the nmap scan argument below. Depending on which button is chosen, the variable will change its
                # value.
                self.type = '-v -sS'
            if self.UDP_radio.isChecked():
                self.type = '-v -sU'
                self.prot = 'udp' # All other scans use TCP connections.
            if self.TCP_radio.isChecked():
                self.type = "-v -sT"
            if self.idle_radio.isChecked():
                self.type = "-v -sI 192.168.56.1"
            if self.ping_radio.isChecked():
                self.type = "-v -sP"
            if self.os_scan_check.isChecked():
                self.type += ' -O'
            self.load.show() # This method starts the loading screen window, as well as the animation
            self.load.gif.start()
            with open('outcome.txt', 'a', newline='') as file: # outcome.txt holds the scan results which can be viewed in the file itself
                now = datetime.datetime.now() #Gets the date and time to help differentiate between scans.
                counter: int = 0 # keeps track of the open ports
                file.write(f"----------------New Scan @ {now}----------------\n") #Writes a separating header
                for port in range(port1, port2 + 1): # for statement loops through the various ports until it is finished
                    try:
                        result = self.scanner.scan(target_ip, str(port), arguments=self.type)# This is where the magic happens.
                        #result stores the "scan" method from the Scanner object, and takes the IP, ports, and type of scan given from
                        #before.
                        scan_data = result.get('scan', {}).get(target_ip, {}) # The following commands get each of the needed dictionaries
                        #from the scan method and takes values from them to be displayed below.
                        port_info: dict = scan_data.get(self.prot, {}).get(port, {})
                        port_state: str = port_info.get('state', 'unknown')
                        if port_state == "open":
                            counter += 1
                            port_reason: str = port_info.get('reason', 'N/A')
                            port_service: str= port_info.get('name', 'unknown')
                            os_matches: list = scan_data.get('osmatch', [])
                            os_info: list = os_matches[0]['name'] if os_matches else 'unknown' # os_matches uses lists instead of a dictionary
                            port_status: str = f"Port {port} ({port_service}): {port_state} (Reason: {port_reason}) OS info: {os_info}\n" # this variable stores the output that will be
                            #printed into a txt file.
                            file.write(port_status) # Writes the variable to the file.



                    except Exception as e: # this helps to handle any errors while scanning is being completed.
                        port_status = f"Error scanning port {port}: {e}"
                    QApplication.processEvents() # QApplication helps to keep both windows open while the data is being
                    #written to the file
                file.write(f'There are/is {counter} open port(s).\n')  # Shows the amount of ports open
            self.load.close() #Closes the loading window
        except ValueError as ve: #Handles any kind of input errors.
            self.show_error(str(ve))









    def show_error(self, message) -> None:
        """
        This function initializes an error box in case of misinput
        :param message: A string value that displays which kind of error message
        :return: An error dialog box
        """
        error_dialog = QMessageBox(self) #QMessage box is a handy tool to create a quick window to make an error message.
        error_dialog.setIcon(QMessageBox.Icon.Critical)
        error_dialog.setWindowTitle("Input Error")
        error_dialog.setText(message)
        error_dialog.setStandardButtons(QMessageBox.StandardButton.Ok)
        error_dialog.exec()
class Load(QMainWindow, Ui_SubScanningWindow):
    def __init__(self) -> None:
        """
        Initializes the SubScanningWindow within the Logic file.
        """
        super().__init__()
        self.setupUi(self)

















