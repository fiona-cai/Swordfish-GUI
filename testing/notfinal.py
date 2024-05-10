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
        self.tabs = QTabWidget()

        # Create widgets for the tabs
        self.tab1 = QWidget()
        self.tab2 = QWidget()

        # Add tabs
        self.tabs.addTab(self.tab1, "Tab 1")
        self.tabs.addTab(self.tab2, "Tab 2")

        # Create layout for the first tab
        self.tab1.layout1 = QVBoxLayout(self)
        self.tab1.setLayout(self.tab1.layout1)
        self.tab1.layout2 = QVBoxLayout(self)
        self.tab1.setLayout(self.tab1.layout2)
        self.tab1.layout3 = QVBoxLayout(self)
        self.tab1.setLayout(self.tab1.layout3)
        self.tab1.layout4 = QVBoxLayout(self)
        self.tab1.setLayout(self.tab1.layout4)
        self.tab1.layout5 = QVBoxLayout(self)
        self.tab1.setLayout(self.tab1.layout5)


        
        self.setWindowTitle("CanSat GUI - Team Swordfish")
        self.setStyleSheet("background-color: #dddddd;")
        self.showFullScreen()  # Make the application full screen

        # Create some widgets
        self.labelHeader = QLabel("Team Swordfish")
        self.labelHeader.setStyleSheet("font-size: 32px; font-weight: bold; color: white; border-radius: 15px;")  # Make the header text larger and bold

        # Create a grid layout for the button panel
        self.buttonPanel = QGridLayout()

        # Create 9 buttons and add them to the grid layout
        for i in range(3):
            button = QPushButton(text=f"Button {i+1}")
            button.setStyleSheet("font-size: 32px; padding: 10px; margin:10px;")
            self.buttonPanel.addWidget(button, i // 3, i % 3)

        # Create some widgets
        self.labelHeader = QLabel("Team Swordfish")
        self.labelHeader.setStyleSheet("font-size: 32px; font-weight: bold; color: white;")  # Make the header text larger and bold
        self.graphWidget1 = pg.PlotWidget(title="Altitude")  # Add a title to the first graph
        self.graphWidget2 = pg.PlotWidget(title="Graph 2")  # Add a title to the second graph
        self.labelAddress = QLabel("GPS Coordinates: ")
        self.labelLength = QLabel("State: ")
        self.labelData = QLabel("Battery Voltage: ")
        self.labelRSSI = QLabel("Descent Rate: ")
        self.labelSNR = QLabel("Telemetry Data Rate: ")
        self.labelSuccessRate = QLabel("Telemetry Packet Success Rate: ")
        self.labelExtra1 = QLabel("Extra 1")
        self.labelExtra2 = QLabel("Extra 2")
        self.labelExtra3 = QLabel("Extra 3")
        self.labelExtra4 = QLabel("Extra 4")
        self.labelExtra5 = QLabel("Extra 5")
        self.labelExtra6 = QLabel("Extra 6")
        self.button = QPushButton("Switch State")
        self.labelTime = QLabel("Mission Elapsed Time: ")
        self.radio = QLabel("Radio")
        
        self.radio.setStyleSheet("font-size: 32px; font-weight: ; border-radius: 15px;")
        self.labelAddress.setStyleSheet("font-size: 32px; font-weight: ; border-radius: 15px;")
        self.labelLength.setStyleSheet("font-size: 32px; font-weight: ; border-radius: 15px;")
        self.labelData.setStyleSheet("font-size: 32px; font-weight: ; border-radius: 15px;")
        self.labelRSSI.setStyleSheet("font-size: 32px; font-weight: ; border-radius: 15px;")
        self.labelSNR.setStyleSheet("font-size: 32px; font-weight: ; border-radius: 15px;")
        self.labelTime.setStyleSheet("font-size: 32px; font-weight: ; border-radius: 15px;")
        self.labelExtra1.setStyleSheet("font-size: 32px; font-weight: ; border-radius: 15px;")
        self.labelExtra2.setStyleSheet("font-size: 32px; font-weight: ; border-radius: 15px;")
        self.labelExtra3.setStyleSheet("font-size: 32px; font-weight: ; border-radius: 15px;")
        self.labelExtra4.setStyleSheet("font-size: 32px; font-weight: ; border-radius: 15px;")
        self.labelExtra5.setStyleSheet("font-size: 32px; font-weight: ; border-radius: 15px;")
        self.labelExtra6.setStyleSheet("font-size: 32px; font-weight: ; border-radius: 15px;")

        self.button.setStyleSheet("font-size: 32px; padding: 10px; margin:10px; margin-top: 50px;")
        
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
        self.timer.setInterval(50) # in milliseconds
        self.timer.timeout.connect(self.update)
        self.timer.start()
 

        self.tab1.layout1.setContentsMargins(20,20,20,20)
        self.tab1.layout1.setSpacing(20)
        self.tab1.layout2.setContentsMargins(20,20,20,20)
        self.tab1.layout2.setSpacing(20)

        self.tab1.layout4.setContentsMargins(30,30,30,30)
        self.tab1.layout4.setSpacing(10)
        self.tab1.layout5.setContentsMargins(30,30,30,30)
        self.tab1.layout5.setSpacing(10)


        
        

        self.tab1.layout2.addWidget(self.graphWidget1)
        self.tab1.layout2.addWidget(self.graphWidget2)

        self.tab1.layout1.addLayout( self.tab1.layout2 )
        self.tab1.layout1.addLayout( self.tab1.layout3 )

                # Add the button panel to the layout
        self.tab1.layout3.addLayout(self.buttonPanel)
        
        self.tab1.layout3.addLayout( self.tab1.layout4 )
        self.tab1.layout3.addLayout( self.tab1.layout5 )
        
        self.tab1.layout4.addWidget(self.labelAddress)
        self.tab1.layout4.addWidget(self.labelLength)
        self.tab1.layout4.addWidget(self.labelTime)
        self.tab1.layout4.addWidget(self.labelRSSI)
        self.tab1.layout4.addWidget(self.labelSNR)
        #self.tab1.layout4.addWidget(self.labelExtra1)
        #self.tab1.layout4.addWidget(self.labelExtra2)
        #self.tab1.layout4.addWidget(self.labelExtra3)
        
        
        
        self.tab1.layout5.addWidget(self.labelExtra1)
        self.tab1.layout5.addWidget(self.labelExtra2)
        self.tab1.layout5.addWidget(self.labelExtra3)
        self.tab1.layout5.addWidget(self.labelExtra4)
        self.tab1.layout5.addWidget(self.labelExtra5)
        self.tab1.layout5.addWidget(self.labelExtra6)

        # Set a fixed width for the widgets
        self.graphWidget1.setFixedWidth(600)
        self.graphWidget2.setFixedWidth(600)

        
        # Create a 3D plot for the second tab
        self.graphWidget3 = gl.GLViewWidget()
        self.plot3D = gl.GLLinePlotItem(pos=np.array([self.x, self.y1, self.z]).T, color=pg.glColor((0,255,0)), width=2, antialias=True)
        self.graphWidget3.addItem(self.plot3D)

        # Create layout for the second tab
        self.tab2.layout = QVBoxLayout(self)
        self.tab2.setLayout(self.tab2.layout)

        # Add the 3D plot to the second tab
        self.tab2.layout.addWidget(self.graphWidget3)

        # Set QTabWidget as the central widget
        self.setCentralWidget(self.tabs)
        
        
    def update(self):
        self.getData(self.randomData())
        elapsed_time = time.time() - self.start_time

        self.y1 = self.y1[1:]  # remove the first y element
        self.y1.append(random.randint(0,100))  # add a new random value
        self.y2 = self.y2[1:]  # remove the first y element
        self.y2.append(random.randint(0,100))  # add a new random value

        self.data_line1.setData(self.x, self.y1)
        self.data_line2.setData(self.x, self.y2)

        self.labelTime.setText("Time: " + str(elapsed_time))
        self.labelAddress.setText(f"Transmitter Address ID: {self.address}")
        self.labelLength.setText(f"Data Length: {self.length} bytes")
        self.labelRSSI.setText(f"Recieved Signal Strength Indicator: {self.rssi} dBm")
        self.labelSNR.setText(f"Signal-to-Noise Ratio: {self.snr}")
        
        self.labelExtra1.setText(f"Gyro: {self.gyro}")
        self.labelExtra2.setText(f"Accelorometer {self.accelorometer}")
        self.labelExtra3.setText(f"Magnetometer: {self.magnetometer}")
        self.labelExtra4.setText(f"Barometer: {self.barometer}")
        self.labelExtra5.setText(f"GNSS: {self.gnss}")
        self.labelExtra6.setText(f"Temperature: {self.temperature}")
        
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
