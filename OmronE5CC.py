# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 22:26:51 2018

@author: Yuya Shimazaki
"""

import minimalmodbus
import serial

SETPOINT_MAX = 200

class OmronE5CC(object):
    def __init__(self, serialPortString = "COM5", slaveaddress = 1):
        try:
            self.__inst__ = minimalmodbus.Instrument(serialPortString, slaveaddress)
            self.__inst__.serial.baudrate = 38400   # Baud
            self.__inst__.serial.bytesize = 8
            self.__inst__.serial.parity   = serial.PARITY_EVEN #.PARITY_NONE
            self.__inst__.serial.stopbits = 1
            self.__inst__.serial.timeout  = 0.1   # seconds
            self.setpoint_max = SETPOINT_MAX
            self.enable_writing()
        except Exception:
            print('Could not connect to serial Port %s' % serialPortString)
            
    def write_registers(self, address, values):
        self.__inst__.write_registers(address, values)

    def write_register(self, address, value):
        self.__inst__.write_register(address, value, functioncode = 6)
        
    def operation(self, code):
        self.write_register(0x0000, code)
        
    def read_registers(self, address):
        return self.__inst__.read_registers(address, 2)
    
    def read_register(self, address):
        return self.__inst__.read_register(address)
    
    def read_status(self, address):
        return list(map(hex, self.__inst__.read_registers(address, 8)))
    
    def get_pv(self):
        return self.read_register(0x2000)/10.0

    def get_setpoint(self):
        return self.read_register(0x2103)/10.0
    
    def set_setpoint(self, val):
        if val <= SETPOINT_MAX and val >= 0:
            set_val = int(val * 10)
            self.write_register(0x2103, set_val)
        elif val > SETPOINT_MAX:
            print('ERROR: Exceeding SETPOINT_MAX = %.1f' % (SETPOINT_MAX))
        elif val < 0:
            print('ERROR: Set point must be a positive value')
    
    def enable_writing(self):
        self.operation(0x0001)
    
    def disable_writing(self):
        self.operation(0x0000)
    
    def run(self):
        self.operation(0x0100)

    def stop(self):
        self.operation(0x0101)

    def reset(self):
        self.operation(0x0600)
    
    def move_to_setup_area_1(self):
        self.operation(0x0700)
    
    def move_to_protect_level(self):
        self.operation(0x0800)
        
# omron = OmronE5CC("COM5", 1)
