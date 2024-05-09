import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QPushButton, QGridLayout, QTabWidget
from PyQt6.QtCore import QTimer
import pyqtgraph as pg
import pyqtgraph.opengl as gl
import numpy as np

import time
import random
import csv


class MainWindow(QMainWindow):
    def randomData(self):
        string = "+RCV="
        string = string + str(random.randint(1,100)) + ","+ str(random.randint(1,100)) + ","+ str(random.randint(1,100)) +"$" +str(random.randint(1,100))+"$" +str(random.randint(1,100))+"$" +str(random.randint(1,100))+"$" +str(random.randint(1,100))+"$" +str(random.randint(1,100))+"$" +str(random.randint(1,100))+"$" +str(random.randint(1,100))+"$" +str(random.randint(1,100))+"$" +str(random.randint(1,100))+"$" +str(random.randint(1,100))+"$" +str(random.randint(1,100))+"$" +str(random.randint(1,100)) + "$" +str(random.randint(1,100))  + ","+ str(random.randint(1,100)) + ","+ str(random.randint(1,100))
        return(string)
    def getData(self, received):
        # Remove the '+RCV=' part from the received string
        received = received.replace('+RCV=', '')

        # Split the string into a list of values
        values = received.split(',')

        # Assign the values to the corresponding attributes
        self.address = values[0]
        self.length = values[1]
        self.data = values[2]
        self.rssi = values[3]
        self.snr = values[4]
        
        contents = self.data.split('$')
        self.gyro = ", ".join(contents[:3])
        self.accelorometer = ", ".join(contents[3:6])
        self.magnetometer = ", ".join(contents[6:8])
        self.barometer = ", ".join(contents[8:9])
        self.gnss = ", ".join(contents[9:13])
        self.temperature = ", ".join(contents[13:])

    def __init__(self, parent=None):

        self.start_time = time.time()
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("CanSat GUI - Team Swordfish")
        self.setStyleSheet("background-color: #dddddd;")
        self.showFullScreen()  # Make the application full screen

        # Create some widgets
        self.labelHeader = QLabel("Team Swordfish")
        
        super(MainWindow, self).__init__(parent)
        self.tabs = QTabWidget()

        # Create widgets for the tabs
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        
         # Add tabs
        self.tabs.addTab(self.tab1, "Tab 1")
        self.tabs.addTab(self.tab2, "Tab 2")
        
        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()
        layout4 = QVBoxLayout()
        layout5 = QHBoxLayout()
        layout6 = QVBoxLayout()
        layout7 = QVBoxLayout()

        # Create layout for the first tab
        self.tab1.layout1 = QVBoxLayout(self)
        self.tab1.setLayout(layout1)
        self.tab1.layout2 = QVBoxLayout(self)
        self.tab1.setLayout(layout2)
        self.tab1.layout3 = QVBoxLayout(self)
        self.tab1.setLayout(layout3)
        self.tab1.layout4 = QVBoxLayout(self)
        self.tab1.setLayout(layout4)
        self.tab1.layout5 = QHBoxLayout(self)
        self.tab1.setLayout(layout5)
        self.tab1.layout6 = QVBoxLayout(self)
        self.tab1.setLayout(layout6)
        self.tab1.layout7 = QVBoxLayout(self)
        self.tab1.setLayout(layout7)
        
         # Create some widgets
        self.labelHeader = QLabel("Team Swordfish")
        self.labelHeader.setStyleSheet("font-size: 32px; font-weight: bold; color: white;")  # Make the header text larger and bold
        self.graphWidget1 = pg.PlotWidget(title="Altitude")  # Add a title to the first graph
        self.graphWidget2 = pg.PlotWidget(title="Graph 2")  # Add a title to the second graph
        self.labelAddress = QLabel("Transmitter Address ID: ")
        self.labelLength = QLabel("Data Length: ")
        self.labelData = QLabel("Battery Voltage: ")
        self.labelRSSI = QLabel("RSSI:  ")
        self.labelSNR = QLabel("Signal-to-Noise Ratio: ")
        self.labelSuccessRate = QLabel("Telemetry Packet Success Rate: ")
        self.nlabelAddress = QLabel("GPS Coordinates: ")
        self.nlabelLength = QLabel("State: ")
        self.nlabelData = QLabel("Battery Voltage: ")
        self.nlabelRSSI = QLabel("Descent Rate: ")
        self.nlabelSNR = QLabel("Telemetry Data Rate: ")
        self.nlabelSuccessRate = QLabel("Telemetry Packet Success Rate: ")
        self.labelExtra1 = QLabel("Gyro: ")
        self.labelExtra2 = QLabel("Accelorometer: ")
        self.labelExtra3 = QLabel("Magnetometer: ")
        self.labelExtra4 = QLabel("Barometer: ")
        self.labelExtra5 = QLabel("GNSS: ")
        self.labelExtra6 = QLabel("Temperature: ")
        self.nlabelExtra1 = QLabel("Extra 1")
        self.nlabelExtra2 = QLabel("Extra 2")
        self.nlabelExtra3 = QLabel("Extra 3")
        self.nlabelExtra4 = QLabel("Extra 4")
        self.nlabelExtra5 = QLabel("Extra 5")
        self.nlabelExtra6 = QLabel("Extra 6")
        self.button = QPushButton("Switch State")
        self.labelTime = QLabel("Mission Elapsed Time: ")
        self.nlabelTime = QLabel("Mission Elapsed Time: ")
        
        self.labelAddress.setStyleSheet("font-size: 24px; font-weight: ; border-radius: 15px;")
        self.labelLength.setStyleSheet("font-size: 24px; font-weight: ; border-radius: 15px;")
        self.labelData.setStyleSheet("font-size: 24px; font-weight: ; border-radius: 15px;")
        self.labelRSSI.setStyleSheet("font-size: 24px; font-weight: ; border-radius: 15px;")
        self.labelSNR.setStyleSheet("font-size: 24px; font-weight: ; border-radius: 15px;")
        self.labelTime.setStyleSheet("font-size: 48px; font-weight: ; border-radius: 15px;")
        self.labelExtra1.setStyleSheet("font-size: 24px; font-weight: ; border-radius: 15px;")
        self.labelExtra2.setStyleSheet("font-size: 24px; font-weight: ; border-radius: 15px;")
        self.labelExtra3.setStyleSheet("font-size: 24px; font-weight: ; border-radius: 15px;")
        self.labelExtra4.setStyleSheet("font-size: 24px; font-weight: ; border-radius: 15px;")
        self.labelExtra5.setStyleSheet("font-size: 24px; font-weight: ; border-radius: 15px;")
        self.labelExtra6.setStyleSheet("font-size: 24px; font-weight: ; border-radius: 15px;")
        
        self.nlabelAddress.setStyleSheet("font-size: 32px; font-weight: ; border-radius: 15px;")
        self.nlabelLength.setStyleSheet("font-size: 32px; font-weight: ; border-radius: 15px;")
        self.nlabelData.setStyleSheet("font-size: 32px; font-weight: ; border-radius: 15px;")
        self.nlabelRSSI.setStyleSheet("font-size: 32px; font-weight: ; border-radius: 15px;")
        self.nlabelSNR.setStyleSheet("font-size: 32px; font-weight: ; border-radius: 15px;")
        self.nlabelTime.setStyleSheet("font-size: 32px; font-weight: ; border-radius: 15px;")
        self.nlabelExtra1.setStyleSheet("font-size: 32px; font-weight: ; border-radius: 15px;")
        self.nlabelExtra2.setStyleSheet("font-size: 32px; font-weight: ; border-radius: 15px;")
        self.nlabelExtra3.setStyleSheet("font-size: 32px; font-weight: ; border-radius: 15px;")
        self.nlabelExtra4.setStyleSheet("font-size: 32px; font-weight: ; border-radius: 15px;")
        self.nlabelExtra5.setStyleSheet("font-size: 32px; font-weight: ; border-radius: 15px;")
        self.nlabelExtra6.setStyleSheet("font-size: 32px; font-weight: ; border-radius: 15px;")
        
        
        
        # Create a grid layout for the button panel
        self.buttonPanel = QGridLayout()
        self.buttonPanel.addWidget(self.labelTime, 0,0)

        # Create 9 buttons and add them to the grid layout
        for i in range(2):
            button = QPushButton(text=f"Button {i+1}")
            button.setStyleSheet("font-size: 32px; padding: 10px; margin:10px;")
            self.buttonPanel.addWidget(button, 0, i+1)
            
            
        # Set up plot
        self.x = list(range(100))  # 100 time points
        self.y1 = [random.randint(0,100) for _ in range(100)]  # 100 data points for the first graph
        self.y2 = [random.randint(0,100) for _ in range(100)]  # 100 data points for the second graph

        self.graphWidget1.setBackground('w')
        self.graphWidget2.setBackground('w')
        pen = pg.mkPen(color=(255, 0, 0))
        self.data_line1 =  self.graphWidget1.plot(self.x, self.y1, pen=pen)
        self.data_line2 =  self.graphWidget2.plot(self.x, self.y2, pen=pen)

        # Set up timer
        self.timer = QTimer()
        self.timer.setInterval(100) # in milliseconds
        self.timer.timeout.connect(self.update)
        self.timer.start()
        
        

        layout1.setContentsMargins(20,20,20,20)
        layout1.setSpacing(20)
        layout2.setContentsMargins(20,20,20,20)
        layout2.setSpacing(20)

        layout4.setContentsMargins(30,30,30,30)
        layout4.setSpacing(10)
        layout5.setContentsMargins(30,30,30,30)
        layout5.setSpacing(10)
        
        layout2.addWidget(self.graphWidget1)
        layout2.addWidget(self.graphWidget2)

        layout1.addLayout( layout2 )
        layout1.addLayout( layout3 )
        

                # Add the button panel to the layout
        layout3.addLayout(self.buttonPanel)
        
        
        layout3.addLayout( layout5 )
        layout5.addLayout( layout6 )
        layout5.addLayout( layout7 )
        
        layout6.addWidget(self.labelAddress)
        layout6.addWidget(self.labelLength)
        
        layout6.addWidget(self.labelRSSI)
        layout6.addWidget(self.labelSNR)
        
        layout7.addWidget(self.nlabelAddress)
        layout7.addWidget(self.nlabelLength)
        layout7.addWidget(self.nlabelRSSI)
        layout7.addWidget(self.nlabelSNR)
        #layout4.addWidget(self.labelExtra1)
        #layout4.addWidget(self.labelExtra2)
        #layout4.addWidget(self.labelExtra3)
        
        
        
        layout6.addWidget(self.labelExtra1)
        layout6.addWidget(self.labelExtra2)
        layout6.addWidget(self.labelExtra3)
        layout6.addWidget(self.labelExtra4)
        layout6.addWidget(self.labelExtra5)
        layout6.addWidget(self.labelExtra6)

        layout7.addWidget(self.nlabelExtra1)
        layout7.addWidget(self.nlabelExtra2)
        layout7.addWidget(self.nlabelExtra3)
        layout7.addWidget(self.nlabelExtra4)
        layout7.addWidget(self.nlabelExtra5)
        layout7.addWidget(self.nlabelExtra6)
        
        # Set a fixed width for the widgets
        self.graphWidget1.setFixedWidth(500)
        self.graphWidget2.setFixedWidth(500)


        widget = QWidget()
        widget.setLayout(layout1)
        self.setCentralWidget(widget)
    def update(self):
        self.getData(self.randomData())
        elapsed_time = time.time() - self.start_time

        self.y1 = self.y1[1:]  # remove the first y element
        self.y1.append(random.randint(0,100))  # add a new random value
        self.y2 = self.y2[1:]  # remove the first y element
        self.y2.append(random.randint(0,100))  # add a new random value

        self.data_line1.setData(self.x, self.y1)
        self.data_line2.setData(self.x, self.y2)

        self.labelTime.setText(f"MET: {(round(elapsed_time))}")
        self.nlabelAddress.setText(f"{self.address}")
        self.nlabelLength.setText(f"{self.length} bytes")
        self.nlabelRSSI.setText(f"{self.rssi} dBm")
        self.nlabelSNR.setText(f"{self.snr}")
        
        self.nlabelExtra1.setText(f"{self.gyro}")
        self.nlabelExtra2.setText(f"{self.accelorometer}")
        self.nlabelExtra3.setText(f"{self.magnetometer}")
        self.nlabelExtra4.setText(f"{self.barometer}")
        self.nlabelExtra5.setText(f"{self.gnss}")
        self.nlabelExtra6.setText(f"{self.temperature}")
        
        # Open our existing CSV file in append mode
        # Create a file object for this file
        with open('data.csv', 'a') as f_object:
        
            # Pass this file object to csv.writer()
            # and get a writer object
            writer_object = csv.writer(f_object)
        
            # Pass the list as an argument into
            # the writerow()
            writer_object.writerow([str(elapsed_time),self.address,self.length,self.rssi,self.snr,self.gyro,self.accelorometer,self.magnetometer,self.barometer,self.gnss,self.temperature])
        
            # Close the file object
            f_object.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    main = MainWindow()
    main.randomData()
    main.show()
    
    sys.exit(app.exec())
