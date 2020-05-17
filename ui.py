# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'controller_ui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 640)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("server.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_domain = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_domain.sizePolicy().hasHeightForWidth())
        self.lineEdit_domain.setSizePolicy(sizePolicy)
        self.lineEdit_domain.setWhatsThis("")
        self.lineEdit_domain.setInputMask("")
        self.lineEdit_domain.setFrame(False)
        self.lineEdit_domain.setObjectName("lineEdit_domain")
        self.horizontalLayout.addWidget(self.lineEdit_domain)
        self.pushButton_connect = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_connect.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_connect.sizePolicy().hasHeightForWidth())
        self.pushButton_connect.setSizePolicy(sizePolicy)
        self.pushButton_connect.setObjectName("pushButton_connect")
        self.horizontalLayout.addWidget(self.pushButton_connect)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_ownersOfDomain = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_ownersOfDomain.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_ownersOfDomain.sizePolicy().hasHeightForWidth())
        self.pushButton_ownersOfDomain.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setItalic(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.pushButton_ownersOfDomain.setFont(font)
        self.pushButton_ownersOfDomain.setStyleSheet("QPushButton {\n"
"    font-size: 24px;\n"
"}")
        self.pushButton_ownersOfDomain.setObjectName("pushButton_ownersOfDomain")
        self.gridLayout.addWidget(self.pushButton_ownersOfDomain, 0, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_info_aboutanotherdomain = QtWidgets.QLabel(self.centralwidget)
        self.label_info_aboutanotherdomain.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_info_aboutanotherdomain.setFont(font)
        self.label_info_aboutanotherdomain.setAlignment(QtCore.Qt.AlignCenter)
        self.label_info_aboutanotherdomain.setObjectName("label_info_aboutanotherdomain")
        self.verticalLayout_4.addWidget(self.label_info_aboutanotherdomain)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setFrame(False)
        self.lineEdit.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_4.addWidget(self.lineEdit)
        self.verticalLayout_3.addLayout(self.verticalLayout_4)
        self.pushButton_changedomain = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_changedomain.setEnabled(False)
        self.pushButton_changedomain.setObjectName("pushButton_changedomain")
        self.verticalLayout_3.addWidget(self.pushButton_changedomain)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checkBox_PDCEmulator = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_PDCEmulator.setEnabled(False)
        self.checkBox_PDCEmulator.setObjectName("checkBox_PDCEmulator")
        self.horizontalLayout_2.addWidget(self.checkBox_PDCEmulator)
        self.checkBox_RIDMaster = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_RIDMaster.setEnabled(False)
        self.checkBox_RIDMaster.setObjectName("checkBox_RIDMaster")
        self.horizontalLayout_2.addWidget(self.checkBox_RIDMaster)
        self.checkBox_InfrastructureMaster = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_InfrastructureMaster.setEnabled(False)
        self.checkBox_InfrastructureMaster.setObjectName("checkBox_InfrastructureMaster")
        self.horizontalLayout_2.addWidget(self.checkBox_InfrastructureMaster)
        self.checkBox_SchemaMaster = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_SchemaMaster.setEnabled(False)
        self.checkBox_SchemaMaster.setObjectName("checkBox_SchemaMaster")
        self.horizontalLayout_2.addWidget(self.checkBox_SchemaMaster)
        self.checkBox_DomainNamingMaster = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_DomainNamingMaster.setEnabled(False)
        self.checkBox_DomainNamingMaster.setObjectName("checkBox_DomainNamingMaster")
        self.horizontalLayout_2.addWidget(self.checkBox_DomainNamingMaster)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget.setFeatures(QtWidgets.QDockWidget.DockWidgetFloatable|QtWidgets.QDockWidget.DockWidgetMovable)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser_log_fromPS = QtWidgets.QTextBrowser(self.dockWidgetContents)
        self.textBrowser_log_fromPS.setMouseTracking(False)
        self.textBrowser_log_fromPS.setAutoFillBackground(False)
        self.textBrowser_log_fromPS.setStyleSheet("QTextBrowser {\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: rgb(238, 237, 240);\n"
"    font: bold 10px;\n"
"}")
        self.textBrowser_log_fromPS.setOverwriteMode(True)
        self.textBrowser_log_fromPS.setPlaceholderText("")
        self.textBrowser_log_fromPS.setObjectName("textBrowser_log_fromPS")
        self.verticalLayout.addWidget(self.textBrowser_log_fromPS)
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.dockWidget)
        self.action_about = QtWidgets.QAction(MainWindow)
        self.action_about.setObjectName("action_about")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Смена контроллера домена"))
        self.lineEdit_domain.setToolTip(_translate("MainWindow", "Имя домена, откуда будет выполнена передача."))
        self.lineEdit_domain.setStatusTip(_translate("MainWindow", "Имя домена, откуда будет выполнена передача."))
        self.lineEdit_domain.setPlaceholderText(_translate("MainWindow", "domain.com"))
        self.pushButton_connect.setStatusTip(_translate("MainWindow", "Подключится к домену"))
        self.pushButton_connect.setText(_translate("MainWindow", "Подключится"))
        self.pushButton_ownersOfDomain.setToolTip(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Получить текущего хозяина ролей в домене</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Open Sans,sans-serif\'; font-size:10pt; font-weight:600; color:#313131; background-color:#ffffff;\">Будет выполнена команда:</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; color:#0000ff;\">netdom query fsmo</span></p></body></html>"))
        self.pushButton_ownersOfDomain.setStatusTip(_translate("MainWindow", "Получить текущего хозяина ролей в домене"))
        self.pushButton_ownersOfDomain.setText(_translate("MainWindow", "Хозяин ролей домена"))
        self.label_info_aboutanotherdomain.setText(_translate("MainWindow", "Имя иного домена, куда нужно передать"))
        self.lineEdit.setToolTip(_translate("MainWindow", "Имя домена, куда будет выполнена передача."))
        self.lineEdit.setStatusTip(_translate("MainWindow", "Имя домена, куда будет выполнена передача."))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "2n"))
        self.pushButton_changedomain.setToolTip(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Передачи ролей FSMO между контроллерами Active Directory.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Будет выполнены команды:</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Consolas\'; font-size:10pt; font-weight:600; color:#0000ff; background-color:#f9f2f4;\">1. ntdsutil</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Consolas\'; font-size:10pt; font-weight:600; color:#0000ff; background-color:#f9f2f4;\">2. roles</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Consolas\'; font-size:10pt; font-weight:600; color:#0000ff; background-color:#f9f2f4;\">3. connections</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Consolas\'; font-size:10pt; font-weight:600; color:#0000ff; background-color:#f9f2f4;\">4. connect to server &lt;name of server&gt;</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Consolas\'; font-size:10pt; font-weight:600; color:#0000ff; background-color:#f9f2f4;\">5. transfer ...</span></p></body></html>"))
        self.pushButton_changedomain.setStatusTip(_translate("MainWindow", "Передачи ролей FSMO между контроллерами Active Directory."))
        self.pushButton_changedomain.setText(_translate("MainWindow", "Передать роли"))
        self.checkBox_PDCEmulator.setToolTip(_translate("MainWindow", "Передать PDCEmulator. Команда: transfer pdc"))
        self.checkBox_PDCEmulator.setStatusTip(_translate("MainWindow", "Передать PDCEmulator. Команда: transfer pdc"))
        self.checkBox_PDCEmulator.setText(_translate("MainWindow", "PDCEmulator"))
        self.checkBox_RIDMaster.setToolTip(_translate("MainWindow", "Передать RIDMaster Команда: transfer rid master"))
        self.checkBox_RIDMaster.setStatusTip(_translate("MainWindow", "Передать RIDMaster. Команда: transfer rid master"))
        self.checkBox_RIDMaster.setText(_translate("MainWindow", "RIDMaster"))
        self.checkBox_InfrastructureMaster.setToolTip(_translate("MainWindow", "Передать InfrastructureMaster. Команда: transfer infrastructure master"))
        self.checkBox_InfrastructureMaster.setStatusTip(_translate("MainWindow", "Передать InfrastructureMaster. Команда: transfer infrastructure master"))
        self.checkBox_InfrastructureMaster.setText(_translate("MainWindow", "InfrastructureMaster"))
        self.checkBox_SchemaMaster.setToolTip(_translate("MainWindow", "Передать SchemaMaster. Команда: transfer schema master"))
        self.checkBox_SchemaMaster.setStatusTip(_translate("MainWindow", "Передать SchemaMaster. Команда: transfer schema master"))
        self.checkBox_SchemaMaster.setText(_translate("MainWindow", "SchemaMaster"))
        self.checkBox_DomainNamingMaster.setToolTip(_translate("MainWindow", "Передать DomainNamingMaster. Команда: transfer naming master"))
        self.checkBox_DomainNamingMaster.setStatusTip(_translate("MainWindow", "Передать DomainNamingMaster. Команда: transfer naming master"))
        self.checkBox_DomainNamingMaster.setText(_translate("MainWindow", "DomainNamingMaster"))
        self.dockWidget.setWindowTitle(_translate("MainWindow", "Лог с командной строки"))
        self.textBrowser_log_fromPS.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10px; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt; font-weight:400;\"><br /></p></body></html>"))
        self.action_about.setText(_translate("MainWindow", "О нас..."))
