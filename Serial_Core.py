import threading
from PySide6.QtCore import Signal, QObject
from PySide6.QtGui import QTextCursor


class jump_worker(QObject):
    """一个提供信号的模块"""
    jump_sig  = Signal(QTextCursor)
    send_char_sig = Signal(str, bool)
    erro_sig  = Signal()
    def sendCursor(self, Cursor):
        self.jump_sig.emit(Cursor)
    def sendChar(self, char, mode):
        self.send_char_sig.emit(char, mode)

