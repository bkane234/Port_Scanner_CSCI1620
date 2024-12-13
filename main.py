#This is code for a GUI that runs a nmap scan and displays output in a text file.
#The goal of the code is to remove any hassles that a command line interface has and provide a quick and easy
#way to choose different scan options and see the results. This program is designed to be simple and basic,
#however a good understanding of networking is helpful. I wanted to make the application Windows friendly so some Linux
#specific scans are missing, however all the scans will work with Windows/Linux operating systems.
#This file runs the startup script with PyQt 6 as the
#module used to create the GUI itself.
from Logic import *
def main():
    app = QApplication([])
    window = Logic()
    window.show()
    app.exec()











if __name__ == '__main__':
    main()