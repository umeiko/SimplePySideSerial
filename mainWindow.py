# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QMainWindow, QMenu, QMenuBar, QPlainTextEdit,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTextBrowser, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(676, 700)
        self.Format = QAction(MainWindow)
        self.Format.setObjectName(u"Format")
        self.Default = QAction(MainWindow)
        self.Default.setObjectName(u"Default")
        self.Exit = QAction(MainWindow)
        self.Exit.setObjectName(u"Exit")
        self.action300 = QAction(MainWindow)
        self.action300.setObjectName(u"action300")
        self.action1200 = QAction(MainWindow)
        self.action1200.setObjectName(u"action1200")
        self.action2400 = QAction(MainWindow)
        self.action2400.setObjectName(u"action2400")
        self.action4800 = QAction(MainWindow)
        self.action4800.setObjectName(u"action4800")
        self.action9600 = QAction(MainWindow)
        self.action9600.setObjectName(u"action9600")
        self.action19200 = QAction(MainWindow)
        self.action19200.setObjectName(u"action19200")
        self.action38400 = QAction(MainWindow)
        self.action38400.setObjectName(u"action38400")
        self.action57600 = QAction(MainWindow)
        self.action57600.setObjectName(u"action57600")
        self.action74880 = QAction(MainWindow)
        self.action74880.setObjectName(u"action74880")
        self.action115200 = QAction(MainWindow)
        self.action115200.setObjectName(u"action115200")
        self.action230400 = QAction(MainWindow)
        self.action230400.setObjectName(u"action230400")
        self.action250000 = QAction(MainWindow)
        self.action250000.setObjectName(u"action250000")
        self.action500000 = QAction(MainWindow)
        self.action500000.setObjectName(u"action500000")
        self.action1000000 = QAction(MainWindow)
        self.action1000000.setObjectName(u"action1000000")
        self.action2000000 = QAction(MainWindow)
        self.action2000000.setObjectName(u"action2000000")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.sendingTextEdit = QPlainTextEdit(self.centralwidget)
        self.sendingTextEdit.setObjectName(u"sendingTextEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sendingTextEdit.sizePolicy().hasHeightForWidth())
        self.sendingTextEdit.setSizePolicy(sizePolicy)
        self.sendingTextEdit.setMinimumSize(QSize(300, 0))
        self.sendingTextEdit.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout.addWidget(self.sendingTextEdit)

        self.Sending = QPushButton(self.centralwidget)
        self.Sending.setObjectName(u"Sending")
        self.Sending.setMinimumSize(QSize(50, 30))

        self.horizontalLayout.addWidget(self.Sending)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout.addWidget(self.textBrowser)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setMinimumSize(QSize(35, 0))

        self.horizontalLayout_4.addWidget(self.label_2)

        self.port_select = QComboBox(self.centralwidget)
        self.port_select.addItem("")
        self.port_select.setObjectName(u"port_select")
        self.port_select.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_4.addWidget(self.port_select)


        self.horizontalLayout_2.addLayout(self.horizontalLayout_4)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_2.addWidget(self.label)

        self.end_select = QComboBox(self.centralwidget)
        self.end_select.addItem("")
        self.end_select.addItem("")
        self.end_select.addItem("")
        self.end_select.addItem("")
        self.end_select.setObjectName(u"end_select")
        self.end_select.setMinimumSize(QSize(100, 30))
        self.end_select.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_2.addWidget(self.end_select)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)

        self.AutoLast = QRadioButton(self.centralwidget)
        self.AutoLast.setObjectName(u"AutoLast")
        self.AutoLast.setMinimumSize(QSize(120, 0))
        self.AutoLast.setLayoutDirection(Qt.RightToLeft)

        self.horizontalLayout_3.addWidget(self.AutoLast)

        self.Clear = QPushButton(self.centralwidget)
        self.Clear.setObjectName(u"Clear")
        self.Clear.setMinimumSize(QSize(0, 30))
        self.Clear.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_3.addWidget(self.Clear)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 676, 23))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menu)
        self.menu_2.setObjectName(u"menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.Format)
        self.menu.addAction(self.Default)
        self.menu.addAction(self.Exit)
        self.menu_2.addAction(self.action300)
        self.menu_2.addAction(self.action1200)
        self.menu_2.addAction(self.action2400)
        self.menu_2.addAction(self.action4800)
        self.menu_2.addAction(self.action9600)
        self.menu_2.addAction(self.action19200)
        self.menu_2.addAction(self.action38400)
        self.menu_2.addAction(self.action57600)
        self.menu_2.addAction(self.action74880)
        self.menu_2.addAction(self.action115200)
        self.menu_2.addAction(self.action230400)
        self.menu_2.addAction(self.action250000)
        self.menu_2.addAction(self.action500000)
        self.menu_2.addAction(self.action1000000)
        self.menu_2.addAction(self.action2000000)

        self.retranslateUi(MainWindow)
        self.Exit.triggered.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Format.setText(QCoreApplication.translate("MainWindow", u"\u901a\u4fe1\u683c\u5f0f", None))
        self.Default.setText(QCoreApplication.translate("MainWindow", u"\u6062\u590d\u9ed8\u8ba4", None))
        self.Exit.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
        self.action300.setText(QCoreApplication.translate("MainWindow", u"300", None))
        self.action1200.setText(QCoreApplication.translate("MainWindow", u"1200", None))
        self.action2400.setText(QCoreApplication.translate("MainWindow", u"2400", None))
        self.action4800.setText(QCoreApplication.translate("MainWindow", u"4800", None))
        self.action9600.setText(QCoreApplication.translate("MainWindow", u"9600", None))
        self.action19200.setText(QCoreApplication.translate("MainWindow", u"19200", None))
        self.action38400.setText(QCoreApplication.translate("MainWindow", u"38400", None))
        self.action57600.setText(QCoreApplication.translate("MainWindow", u"57600", None))
        self.action74880.setText(QCoreApplication.translate("MainWindow", u"74880", None))
        self.action115200.setText(QCoreApplication.translate("MainWindow", u"115200", None))
        self.action230400.setText(QCoreApplication.translate("MainWindow", u"230400", None))
        self.action250000.setText(QCoreApplication.translate("MainWindow", u"250000", None))
        self.action500000.setText(QCoreApplication.translate("MainWindow", u"500000", None))
        self.action1000000.setText(QCoreApplication.translate("MainWindow", u"1000000", None))
        self.action2000000.setText(QCoreApplication.translate("MainWindow", u"2000000", None))
        self.Sending.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u9001", None))
#if QT_CONFIG(shortcut)
        self.Sending.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u7aef\u53e3", None))
        self.port_select.setItemText(0, QCoreApplication.translate("MainWindow", u"\u4e32\u53e3\u672a\u8fde\u63a5", None))

        self.label.setText(QCoreApplication.translate("MainWindow", u"\u7ed3\u675f\u7b26", None))
        self.end_select.setItemText(0, QCoreApplication.translate("MainWindow", u"\u65e0", None))
        self.end_select.setItemText(1, QCoreApplication.translate("MainWindow", u"\u6362\u884c (\\n)", None))
        self.end_select.setItemText(2, QCoreApplication.translate("MainWindow", u"\u56de\u8f66 (\\r)", None))
        self.end_select.setItemText(3, QCoreApplication.translate("MainWindow", u"CR NL(\\r\\n)", None))

        self.AutoLast.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u8f6c\u5230\u884c\u5c3e", None))
#if QT_CONFIG(shortcut)
        self.AutoLast.setShortcut(QCoreApplication.translate("MainWindow", u"End", None))
#endif // QT_CONFIG(shortcut)
        self.Clear.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a", None))
#if QT_CONFIG(shortcut)
        self.Clear.setShortcut(QCoreApplication.translate("MainWindow", u"Del", None))
#endif // QT_CONFIG(shortcut)
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u83dc\u5355", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u6ce2\u7279\u7387", None))
    # retranslateUi

