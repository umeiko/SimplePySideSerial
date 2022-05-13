from ctypes import Union
import threading
import serial
import serial.tools.list_ports
from PySide6.QtCore import Signal, QObject
from PySide6.QtGui import QTextCursor
from typing import Union
import time


class Serial_Thread(threading.Thread, QObject):
    """串口调试助手的收信线程"""
    jump_sig = Signal()
    text_sig = Signal(str)
    def __init__(self, ser_manager):
        threading.Thread.__init__(self)
        QObject.__init__(self)
        self.isRunning = False
        self.serial_manager = ser_manager
        self.ser = ser_manager.ser
        self.jump_last = False
    
    def run(self):
        temp = b""
        text = b""
        self.isRunning = True
        
        while self.isRunning:
            self.serial_manager.read_lock.acquire()
            if self.ser.isOpen():
                try:
                    text = self.ser.read()
                except BaseException as e:
                    self.serial_manager.port_erro_signal.emit("From Thread:"+str(e))
            self.serial_manager.read_lock.release()

            if text:
                temp += text
                text = b""
                try:  # 解决汉字等二进制转换的问题
                    decode_str = temp.decode(encoding="utf-8")
                    for k, i in enumerate(decode_str):
                        if i in "\x00\x01\x02\x03\x04\x05\x06\x07\x08\x0e\x0f":
                            decode_str = decode_str[:k] + "\\x" + temp[k:k+1].hex() + decode_str[k+1:]
                    self.text_sig.emit(decode_str)
                    temp = b""
                
                except BaseException as e:
                    msg = str(e).split(":")[-1]
                    if msg == " unexpected end of data":
                        if len(temp) >3:
                            decode_str = ""
                            for k, _ in enumerate(temp):
                                decode_str += "\\x" + temp[k:k+1].hex()
                            self.text_sig.emit(decode_str)
                            temp = b""
                    else:
                        decode_str = ""
                        for k, _ in enumerate(temp):
                            decode_str += "\\x" + temp[k:k+1].hex()
                        self.text_sig.emit(decode_str)
                        temp = b""
                
                if self.jump_last:
                    self.jump_sig.emit() 
        print("串口打印线程被终止")    


class Serial_Manager(QObject):
    """串口资源管理器"""
    port_erro_signal = Signal(str)
    port_switch_signal = Signal(bool)
    baudrates = [300, 1200, 2400, 4800, 9600, 19200,
                38400, 57600, 74880, 115200, 230400, 
                250000, 500000, 1000000, 2000000,]
    formats = [ (5, "N", 1), (5, "N", 2), (6, "N", 1), (6, "N", 1),
                (7, "N", 1), (7, "N", 2), (8, "N", 1), (8, "N", 2),
                (5, "E", 1), (5, "E", 2), (6, "E", 1), (6, "E", 1),
                (7, "E", 1), (7, "E", 2), (8, "E", 1), (8, "E", 2),
                (5, "O", 1), (5, "O", 2), (6, "O", 1), (6, "O", 1),
                (7, "O", 1), (7, "O", 2), (8, "O", 1), (8, "O", 2),
                ]
    def __init__(self) -> None:
        super().__init__()
        self.ser = serial.Serial()
        self.ser.baudrate = 115200
        self.ser.timeout = 0
        self.read_lock = threading.Lock()
        self.write_lock = threading.Lock() 
        self.end_char = b""
        
    
    def set_format(self, bytesize, parity, stopbits):
        """设置串口格式：数据位，校验，停止位"""
        print(bytesize, parity, stopbits)
        self.ser.bytesize, self.ser.parity, self.ser.stopbits = bytesize, parity, stopbits

    def set_baudrate(self, baudrate):
        print(baudrate)
        self.ser.baudrate = baudrate
    
    def scan_ports(self)->tuple:
        """查询有哪些串口可用, 返回两个列表"""
        options = serial.tools.list_ports.comports()
        ports = [i.device for i in options]
        names = [i.description for i in options]
        return ports, names

    def open_port(self, port:str):
        if (self.ser.isOpen() and port != self.ser.port):
            self.read_lock.acquire()
            self.write_lock.acquire()            
            self.ser.close()
            self.read_lock.release()
            self.write_lock.release() 
        self.ser.port = port
        if not self.ser.isOpen():
            try:
                self.ser.open()
                self.port_switch_signal.emit(True)
            except BaseException as e:
                self.port_erro_signal.emit(str(e))

    def close_port(self):
        """关闭串口"""
        self.read_lock.acquire()
        self.write_lock.acquire()
        if self.ser.isOpen():
            self.ser.close()
            self.port_switch_signal.emit(False)
        self.read_lock.release()
        self.write_lock.release()
    
    def write_ser(self, content:Union[str, bytes])->bool:
        """直接写内容到串口"""
        if isinstance(content, bytes):
            content = content
        elif isinstance(content, str):
            content = content.encode()
        else:
            return False
        if self.ser.isOpen():
            self.write_lock.acquire()
            try:
                self.ser.write(content+self.end_char)
            except BaseException as e:
                self.port_erro_signal.emit(str(e))
            self.write_lock.release()
            return True
        else:
            return False

