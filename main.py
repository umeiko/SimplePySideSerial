from mainWindow import Ui_MainWindow
import serial_core
from PySide6.QtGui import QIcon, QShortcut
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
import sys

main_window = Ui_MainWindow() # 主界面
app = QApplication(sys.argv)
w = QMainWindow()
main_window.setupUi(w)
main_window.baudrates = [
    main_window.action300,
    main_window.action1200,
    main_window.action2400,
    main_window.action4800,
    main_window.action9600,
    main_window.action19200,
    main_window.action38400,
    main_window.action57600,
    main_window.action74880,
    main_window.action115200,
    main_window.action230400,
    main_window.action250000,
    main_window.action500000,
    main_window.action1000000,
    main_window.action2000000,
]
main_window.formats = [
    main_window.action5N1,
    main_window.action5N2,
    main_window.action6N1,
    main_window.action6N2,
    main_window.action7N1,
    main_window.action7N2,
    main_window.action8N1,
    main_window.action8N2,
    main_window.action5E1,
    main_window.action5E2,
    main_window.action6E1,
    main_window.action6E2,
    main_window.action7E1,
    main_window.action7E2,
    main_window.action8E1,
    main_window.action8E2,
    main_window.action5O1,
    main_window.action5O2,
    main_window.action6O1,
    main_window.action6O2,
    main_window.action7O1,
    main_window.action7O2,
    main_window.action8O1,
    main_window.action8O2,
]
serial_manager = serial_core.Serial_Manager()
serial_thread = serial_core.Serial_Thread(serial_manager)
Cursor = main_window.recv_Text.textCursor()

global_options = {
    "temp_ports_list": [],
    "last_port"      : 0,
    "end_char"       : 0,
    "auto_last"      : False,
    "baudrate"       : 9,
    "format"         : 6,
    "skin_mode"      : "Classic",
}

def init_methods():
    load_options()
    main_window.statusbar.showMessage("Designed By Umeko")
    serial_thread.start()

def close_methods(*args):
    save_options()
    serial_thread.isRunning = False
    serial_manager.close_port()

def bind_methods():
    """为组件绑定功能"""
    serial_manager.port_erro_signal.connect(func_for_serial_erro)
    main_window.port_select.mousePressEvent = func_for_show_ports
    main_window.port_select.currentIndexChanged.connect(func_for_select_port) 
    main_window.port_select.wheelEvent=lambda *args: None
    main_window.end_select.currentIndexChanged.connect(func_for_select_end_char)
    
    shortcut = QShortcut(w)
    shortcut.setKey(u'Return')
    shortcut.activated.connect(func_for_send_serial_msg)
    shortcut_TAB = QShortcut(w)
    shortcut_TAB.setKey(u'Tab')
    shortcut_TAB.activated.connect(func_for_auto_complete)
    shortcut_Break = QShortcut(w)
    shortcut_Break.setKey(u'Ctrl+B')
    shortcut_Break.activated.connect(func_for_break)

    main_window.Sending.clicked.connect(func_for_send_serial_msg)
    main_window.Clear.clicked.connect(main_window.recv_Text.clear)
    main_window.AutoLast.toggled.connect(func_jump_to_last_line)

    main_window.menu_2.triggered.connect(func_for_change_baudrate)
    main_window.menu_3.triggered.connect(func_for_change_format)
    main_window.Default.triggered.connect(set_defaut)

    main_window.style_dark.triggered.connect(lambda: change_style("MaterialDark"))
    main_window.style_classic.triggered.connect(lambda: change_style("Classic"))
    
    serial_thread.text_sig.connect(func_highlightRecvText)
    serial_thread.jump_sig.connect(func_jump_to_last_line)



def func_for_show_ports(*args):
    """展示串口的函数"""
    fresh_ports()
    print(global_options)
    main_window.port_select.showPopup()

def fresh_ports():
    """刷新系统当前连接的串口设备"""
    global main_window
    main_window.port_select.setItemText(0, "断开连接")
    ports, names = serial_manager.scan_ports()

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

def func_for_select_port(*args):
    """选择连接到某个串口"""
    index = args[0]
    if index > 0:
        serial_manager.open_port(global_options["temp_ports_list"][index-1])
    else:
        serial_manager.close_port()
    global_options["last_port"] = index
    print(index)

def func_highlightRecvText(text:str, isHtml:bool=False):
    """高亮显示接收到的信息"""
    if isHtml:
        Cursor.insertHtml(text)
    else:
        Cursor.insertText(text)

def func_for_select_end_char(*args):
    '''串口监视器选择结束符的函数'''
    ends = [b"", b"\n", b"\r", b"\r\n"]
    global_options["end_char"]=args[0]
    serial_manager.end_char = ends[args[0]]

def func_for_send_serial_msg(*args):
    """发送串口信息的函数"""
    msg = main_window.sendingTextEdit.text()
    serial_manager.write_ser(msg)
    main_window.sendingTextEdit.clear()

def func_jump_to_last_line(*args):
    """跳到最后一行的函数"""
    if args:
        serial_thread.jump_last = args[0]
        global_options["auto_last"] = args[0]
    main_window.recv_Text.setTextCursor(Cursor)

def func_for_serial_erro(*args):
    """串口异常处理的函数"""
    print(args)
    serial_manager.close_port()
    main_window.port_select.setItemText(0, "连接失败, 请重试")
    main_window.port_select.setCurrentIndex(0)

def load_options():
    global global_options
    import json as json
    try:
        with open("main_config.json", 'r') as js_file:
            temp_robo_options = json.load(js_file)
    
    except BaseException as e:
        with open("main_config.json", 'w') as js_file:
            js_string = json.dumps(global_options, sort_keys=True, indent=4, separators=(',', ': '))
            js_file.write(js_string)
        temp_robo_options = global_options.copy()
    
    fresh_ports()
    for key in global_options:
        try:
            temp_robo_options[key]
        except Exception:
            temp_robo_options[key] = global_options[key]
    
    if temp_robo_options["temp_ports_list"] == global_options["temp_ports_list"]:
        main_window.port_select.setCurrentIndex(temp_robo_options["last_port"])

    main_window.end_select.setCurrentIndex(temp_robo_options["end_char"])
    main_window.AutoLast.setChecked(temp_robo_options["auto_last"])
    serial_thread.jump_last = temp_robo_options["auto_last"]
    change_style(temp_robo_options["skin_mode"])
    func_for_change_baudrate(main_window.baudrates[temp_robo_options["baudrate"]])
    func_for_change_format(main_window.formats[temp_robo_options["format"]])

def change_style(style:str):
    """设置皮肤"""
    import qss
    if global_options["skin_mode"] != style:
        global_options["skin_mode"] = style
        w.setStyleSheet(qss.styles[style])

def save_options():
    """导出主窗口的配置到文件中"""
    import json as json
    with open("main_config.json", 'w') as js_file:
        js_string = json.dumps(global_options, sort_keys=True, indent=4, separators=(',', ': '))
        js_file.write(js_string)

def func_for_change_baudrate(Qaction):
    [i.setChecked(False) for i in main_window.baudrates]
    Qaction.setChecked(True)
    serial_manager.set_baudrate(int(Qaction.text()))
    global_options["baudrate"] = main_window.baudrates.index(Qaction)

def func_for_auto_complete(*args):
    '''命令行代码补全函数'''
    global serial_manager
    if serial_manager.ser.isOpen():
        msg = main_window.sendingTextEdit.text()
        serial_manager.ser.write(msg.encode()+b"\t")
        main_window.sendingTextEdit.clear()  

def func_for_break(*args):
    '''Ctrl+B 函数'''
    global serial_manager
    if serial_manager.ser.isOpen():
        serial_manager.ser.write(b"\r\x03\x03")

def func_for_change_format(Qaction):
    [i.setChecked(False) for i in main_window.formats]
    Qaction.setChecked(True)
    b, p, s = Qaction.text()[0], Qaction.text()[1], Qaction.text()[2]
    serial_manager.set_format(int(b), p, int(s))
    global_options["format"] = main_window.formats.index(Qaction)

def set_defaut():
    """恢复初始通讯设置"""
    func_for_change_baudrate(main_window.action115200)
    func_for_change_format(main_window.action8N1)

def main():
    bind_methods()
    init_methods()
    w.closeEvent = close_methods
    w.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()