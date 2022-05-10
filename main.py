from mainWindow import Ui_MainWindow
import Serial_Core
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
import sys

main_window = Ui_MainWindow() # 主界面
app = QApplication(sys.argv)
w = QMainWindow()
main_window.setupUi(w)
serial_maneger = Serial_Core.Serial_Maneger()

global_options = {
    "temp_ports_list": [],
    "last_port"      : 0,
    "end_char"       : 0,
    "skin_mode"      : "classic",
}

def init_methods():
    pass

def close_methods(*args):
    pass

def bind_methods():
    pass

def fresh_ports():
    global main_window
    """刷新系统当前连接的串口设备"""
    
    main_window.port_select.setItemText(0, "断开连接")
    ports, names = serial_maneger.scan_ports()

    for k, i in enumerate(global_options["temp_ports_list"]):
        # 删除已不存在的端口
        if i not in ports:
            main_window.port_select.removeItem(k+1)
            if global_options["temp_ports_list"]:
                global_options["temp_ports_list"].pop(k)
    
    for k, i in enumerate(names):
        # 添加新出现的端口
        if ports[k] not in global_options["temp_ports_list"]:
            main_window.port_select.addItem(i)
            if global_options["temp_ports_list"]:
                global_options["temp_ports_list"].append(ports[k])
    
    if not global_options["temp_ports_list"]:
        global_options["temp_ports_list"] = ports


def main():
    w.closeEvent = close_methods
    w.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()