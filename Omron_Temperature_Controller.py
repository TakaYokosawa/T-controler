# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 04:00:34 2018

@author: Yuya Shimazaki
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from UI_OmronE5CC import Ui_OmronMainWindow

import sys
import threading
import time
from OmronE5CC import OmronE5CC

class main_window(QtWidgets.QMainWindow, Ui_OmronMainWindow):
    def __init__(self, parent = None):
        super(main_window, self).__init__(parent)
        self.setupUi(self)
        
        self.omron = OmronE5CC("COM6", 1)
        self._is_subprocess_running = True
        self._rlock = threading.RLock()
        
        self.actionAbout_Hardware.triggered.connect(self.show_hardware_info)
        
        self.Power_button.toggled.connect(self.power_toggle)
        self.Timer_button.toggled.connect(self.timer_toggle)
        self.SetPoint_control.valueChanged.connect(self.set_setpoint)
        self.Timer_control.timeChanged.connect(self.set_timer)
        self.set_timer()
        self.get_setpoint()
        self.run_pv_indicator()
        self._is_power_on = True
        self._is_timer_on = False        
        self.power_on()
        self.timer_off()
        
    def close(self):
        self._is_subprocess_running = False
        self.power_off()
                
    def get_pv(self):
        while self._is_subprocess_running:
            self._rlock.acquire()
            pv = self.omron.get_pv()
            self._rlock.release()
            pv_str = "{0:.1f}".format(pv)
            self.PV_indicator.display(pv_str)
            time.sleep(0.5)

    def proceed_timer(self):
        while self._is_timer_on:
            time.sleep(1)
            self._remaining_time = self._remaining_time.addSecs(-1)
            self.Timer_indicator.setText(self._remaining_time.toString())
            if self._remaining_time == QtCore.QTime(0, 0, 0):
                self.power_toggle()
                self.timer_toggle()
            
    def get_setpoint(self):
        self._rlock.acquire()
        setpoint = self.omron.get_setpoint()
        self._rlock.release()
        setpoint_str = "{0:.1f}".format(setpoint)
        self.SetPoint_indicator.display(setpoint_str)
        self.SetPoint_control.setValue(setpoint)
    
    def run_pv_indicator(self):
        self.pv_thread = threading.Thread(target=self.get_pv)
        self.pv_thread.start()

    def run_timer(self):
        self.timer_thread = threading.Thread(target=self.proceed_timer)
        self.timer_thread.start()
        
    def set_setpoint(self):
        setpoint = self.SetPoint_control.value()
        self._rlock.acquire()
        self.omron.set_setpoint(setpoint)
        self._rlock.release()
        self.get_setpoint()

    def set_timer(self):
        self._remaining_time = self.Timer_control.time()
        self.Timer_indicator.setText(self._remaining_time.toString())
        
    def power_on(self):
        self._rlock.acquire()
        self.omron.run()
        self._rlock.release()
        self.Power_button.setStyleSheet("background-color:rgb(255,0,0)")

    def timer_on(self):
        self.Timer_button.setStyleSheet("background-color:rgb(255,0,0)")
        self.run_timer()

    def power_off(self):
        self._rlock.acquire()
        self.omron.stop()
        self._rlock.release()
        self.Power_button.setStyleSheet("background-color:rgb(0,255,0)")

    def timer_off(self):
        self.Timer_button.setStyleSheet("background-color:rgb(0,255,0)")

    def power_toggle(self):
        self._is_power_on = not self._is_power_on
        if self._is_power_on:
            self.power_on()
        else:
            self.power_off()

    def timer_toggle(self):
        self._is_timer_on = not self._is_timer_on
        if self._is_timer_on:
            self.timer_on()
        else:
            self.timer_off()
        
    def show_hardware_info(self):
        message = "{hardware: <17} : {product: <40}\n".format(hardware = "Controller", product = "Omron E5CC-QX3A5M-003") + \
                  "{hardware: <17} : {product: <40}\n".format(hardware = "Heater", product = "Sakaguchi E.H. Micro Ceramic Heater MS-2") + \
                  "{hardware: <17} : {product: <40}\n".format(hardware = "Thermo Couple", product = "RS Pro J Type Thermocouple") + \
                  "{hardware: <17} : {product: <40}\n".format(hardware = "Solid State Relay", product = "Omron G3NA-210B-UTU DC5-24") + \
                  "{hardware: <17} : {product: <40}\n".format(hardware = "Fuse", product = "8A Fast-blow (5 x 20 mm)")
        
        QtWidgets.QMessageBox.about(self, "Hardware information", message)
        
        
def main():
    app = QtWidgets.QApplication(sys.argv)
    Omron_main = main_window()
    Omron_main.show()
    app.exec_()
    Omron_main.close()
    
    exit()
    
if __name__ == "__main__":
    main()
