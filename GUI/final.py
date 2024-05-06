import sys
import random
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QLabel,
    QPushButton,
    QGridLayout,
)
from PyQt6.QtCore import QTimer
import pyqtgraph as pg
import time
import random
import csv


class MainWindow(QMainWindow):
    def __init__(self, parent=None):

        self.start_time = time.time()

        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("CanSat GUI - Team Swordfish")
        self.setStyleSheet("background-color: #dddddd;")
        self.showFullScreen()  # Make the application full screen

        # Create the layout
        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()
        layout4 = QVBoxLayout()
        layout5 = QVBoxLayout()
        layout6 = QVBoxLayout()

        # Set margins and spacing for layouts
        layout1.setContentsMargins(20, 20, 20, 20)
        layout1.setSpacing(20)
        layout2.setContentsMargins(20, 20, 20, 20)
        layout2.setSpacing(20)
        layout4.setContentsMargins(30, 30, 30, 30)
        layout4.setSpacing(10)
        layout5.setContentsMargins(30, 30, 30, 30)
        layout5.setSpacing(10)

        # Create labels for data
        self.label_address = QLabel("Transmitter Address ID:")
        self.label_length = QLabel("Data Length:")
        self.label_data = QLabel("Data Content:")
        self.label_rssi = QLabel("Recieved Signal Strength Indicator:")
        self.label_snr = QLabel("Signal-to-Noise Ratio:")
        self.label_time = QLabel("Mission Elapsed Time:")
        self.label_gyro = QLabel("Gyro:")
        self.label_accelorometer = QLabel("Accelorometer:")
        self.label_magnetometer = QLabel("Magnetometer:")
        self.label_barometer = QLabel("Barometer:")
        self.label_gnss = QLabel("GNSS:")
        self.label_temperature = QLabel("Temperature:")

        # Set font style for labels (optional)
        self.label_address.setStyleSheet("font-size: 32px;")
        self.label_length.setStyleSheet("font-size: 32px;")
        # ... (similarly set styles for other labels)

        # Create labels for values (initially empty)
        self.value_address = QLabel("")
        self.value_length = QLabel("")
        self.value_data = QLabel("")
        self.value_rssi = QLabel("")
        self.value_snr = QLabel("")
        self.value_time = QLabel("")
        self.value_gyro = QLabel("")
        self.value_accelorometer = QLabel("")
        self.value_magnetometer = QLabel("")
        self.value_barometer = QLabel("")
        self.value_gnss = QLabel("")
        self.value_temperature = QLabel("")

        # Set font style for value labels (optional)
        self.value_address.setStyleSheet("font-size: 32px;")
        self.value_length.setStyleSheet("font-size: 32px;")
        # ... (similarly set styles for other value labels)

        # Add labels to layouts
        layout4.addWidget(self.label_address)
        layout4.addWidget(self.label_length)
        layout4.addWidget(self.label_time)
        layout4.addWidget(self.label_rssi)
        layout4.addWidget(self.label_snr)
        # layout4.addWidget(self.label_extra1)
        # layout4.addWidget(self.label_extra2)
        # layout4.addWidget(self.label_extra3)

        layout5.addWidget(self.label_gyro)
        layout5.addWidget(self.label_accelorometer)
        layout5.addWidget(self.label_magnetometer)
        layout5.addWidget(self.label_barometer)
        layout5.addWidget(self.label_gnss)
        layout5.addWidget(self.label_temperature)

        # Add value labels to layouts
        layout4.addWidget(self.value_address)
        layout4.addWidget(self.value_length)
        layout4.addWidget(self.value_time)
        layout4.addWidget(self.value_rssi)
        layout4.addWidget(self.value_snr)
        # layout4.addWidget(self.value_extra1)
        # layout4.addWidget(self.value_extra2)
        # layout4.addWidget(self.value_extra3)

        layout5.addWidget(self.value_gyro)
        layout5.addWidget(self.value_accelorometer)
        layout5.addWidget(self.value_magnetometer)
        layout5.addWidget(self.value_barometer)
        layout5.addWidget(self.value_gnss)
        layout5.addWidget(self.value_temperature)

        # Create graphs and plot widgets
        self.graphWidget1 = pg.PlotWidget(title="Altitude")  # Add a title to the first graph
        self.graphWidget2 = pg.PlotWidget(title="Graph 2")  # Add a title to the second graph

        # Set up plot
        self.x = list(range(100))  # 100 time points
        self.y1 = [random.randint(0, 100) for _ in range(100)]  # 100 data points for the first graph
        self.y2 = [random.randint(0, 100) for _ in range(100)]  # 100 data points for the second graph

        self.graphWidget1.setBackground("w")
        self.graphWidget2.setBackground("w")
        pen = pg.mkPen(color=(255, 0, 0))
        self.data_line1 = self.graphWidget1.plot(self.x, self.y1, pen=pen)
        self.data_line2 = self.graphWidget2.plot(self.x, self.y2, pen=pen)

        # Add graphs to layout
        layout2.addWidget(self.graphWidget1)
        layout2.addWidget(self.graphWidget2)

        # Create a button (optional)
        self.button = QPushButton("Switch State")
        self.button.setStyleSheet("font-size: 32px; padding: 10px; margin:10px; margin-top: 50px;")

        # Add button to layout (optional)
        layout3.addLayout(self.buttonPanel)

        # Combine layouts
        layout1.addLayout(layout2)
        layout1.addLayout(layout3)

        widget = QWidget()
        widget.setLayout(layout1)
        self.setCentralWidget(widget)

        # Define functions for random data generation, data parsing, and GUI update
        def randomData(self):
            string = "+RCV="
            string = string + str(random.randint(1, 100)) + "," + str(
                random.randint(1, 100)
            ) + "," + str(random.randint(1, 100)) + str(random.randint(1, 100)) + "</span>" + str(random.randint(1, 100))  + str(
random.randint(1, 100)
) + "</span>" + str(random.randint(1, 100))  + str(
random.randint(1, 100)
) + "</span>" + str(random.randint(1, 100))  + str(
random.randint(1, 100)
) + "</span>" + str(random.randint(1, 100))  + str(
random.randint(1, 100)
) + "</span>" + str(random.randint(1, 100))  + str(
random.randint(1, 100)
) + "</span>" + str(random.randint(1, 100))  + str(
random.randint(1, 100)
) + "</span>" + str(random.