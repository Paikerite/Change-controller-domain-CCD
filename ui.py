# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'controller_ui.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 640)
        icon = QIcon()
        icon.addFile(u"server.svg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.action_about = QAction(MainWindow)
        self.action_about.setObjectName(u"action_about")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit_domain = QLineEdit(self.centralwidget)
        self.lineEdit_domain.setObjectName(u"lineEdit_domain")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_domain.sizePolicy().hasHeightForWidth())
        self.lineEdit_domain.setSizePolicy(sizePolicy)
        self.lineEdit_domain.setFrame(False)

        self.horizontalLayout.addWidget(self.lineEdit_domain)

        self.pushButton_connect = QPushButton(self.centralwidget)
        self.pushButton_connect.setObjectName(u"pushButton_connect")
        self.pushButton_connect.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_connect.sizePolicy().hasHeightForWidth())
        self.pushButton_connect.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.pushButton_connect)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_ownersOfDomain = QPushButton(self.centralwidget)
        self.pushButton_ownersOfDomain.setObjectName(u"pushButton_ownersOfDomain")
        self.pushButton_ownersOfDomain.setEnabled(False)
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Ignored)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton_ownersOfDomain.sizePolicy().hasHeightForWidth())
        self.pushButton_ownersOfDomain.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setItalic(False)
        font.setStyleStrategy(QFont.PreferDefault)
        self.pushButton_ownersOfDomain.setFont(font)
        self.pushButton_ownersOfDomain.setStyleSheet(u"QPushButton {\n"
"	font-size: 24px;\n"
"}")

        self.gridLayout.addWidget(self.pushButton_ownersOfDomain, 0, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_info_aboutanotherdomain = QLabel(self.centralwidget)
        self.label_info_aboutanotherdomain.setObjectName(u"label_info_aboutanotherdomain")
        self.label_info_aboutanotherdomain.setEnabled(False)
        font1 = QFont()
        font1.setPointSize(13)
        self.label_info_aboutanotherdomain.setFont(font1)
        self.label_info_aboutanotherdomain.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_info_aboutanotherdomain)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEnabled(False)
        self.lineEdit.setFrame(False)
        self.lineEdit.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.lineEdit.setClearButtonEnabled(False)

        self.verticalLayout_4.addWidget(self.lineEdit)


        self.verticalLayout_3.addLayout(self.verticalLayout_4)

        self.pushButton_changedomain = QPushButton(self.centralwidget)
        self.pushButton_changedomain.setObjectName(u"pushButton_changedomain")
        self.pushButton_changedomain.setEnabled(False)

        self.verticalLayout_3.addWidget(self.pushButton_changedomain)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.checkBox_PDCEmulator = QCheckBox(self.centralwidget)
        self.checkBox_PDCEmulator.setObjectName(u"checkBox_PDCEmulator")
        self.checkBox_PDCEmulator.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.checkBox_PDCEmulator)

        self.checkBox_RIDMaster = QCheckBox(self.centralwidget)
        self.checkBox_RIDMaster.setObjectName(u"checkBox_RIDMaster")
        self.checkBox_RIDMaster.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.checkBox_RIDMaster)

        self.checkBox_InfrastructureMaster = QCheckBox(self.centralwidget)
        self.checkBox_InfrastructureMaster.setObjectName(u"checkBox_InfrastructureMaster")
        self.checkBox_InfrastructureMaster.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.checkBox_InfrastructureMaster)

        self.checkBox_SchemaMaster = QCheckBox(self.centralwidget)
        self.checkBox_SchemaMaster.setObjectName(u"checkBox_SchemaMaster")
        self.checkBox_SchemaMaster.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.checkBox_SchemaMaster)

        self.checkBox_DomainNamingMaster = QCheckBox(self.centralwidget)
        self.checkBox_DomainNamingMaster.setObjectName(u"checkBox_DomainNamingMaster")
        self.checkBox_DomainNamingMaster.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.checkBox_DomainNamingMaster)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addLayout(self.verticalLayout_3)

        self.progressBar_waiting = QProgressBar(self.centralwidget)
        self.progressBar_waiting.setObjectName(u"progressBar_waiting")
        self.progressBar_waiting.setEnabled(True)
        self.progressBar_waiting.setMinimum(0)
        self.progressBar_waiting.setMaximum(1)
        self.progressBar_waiting.setValue(0)
        self.progressBar_waiting.setTextVisible(False)
        self.progressBar_waiting.setOrientation(Qt.Horizontal)
        self.progressBar_waiting.setInvertedAppearance(False)

        self.verticalLayout_2.addWidget(self.progressBar_waiting)

        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget = QDockWidget(MainWindow)
        self.dockWidget.setObjectName(u"dockWidget")
        self.dockWidget.setFeatures(QDockWidget.DockWidgetFloatable|QDockWidget.DockWidgetMovable)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.verticalLayout = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textBrowser_log_fromPS = QTextBrowser(self.dockWidgetContents)
        self.textBrowser_log_fromPS.setObjectName(u"textBrowser_log_fromPS")
        self.textBrowser_log_fromPS.setMouseTracking(False)
        self.textBrowser_log_fromPS.setAutoFillBackground(False)
        self.textBrowser_log_fromPS.setStyleSheet(u"QTextBrowser {\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: rgb(238, 237, 240);\n"
"	font: bold 10px;\n"
"}")
        self.textBrowser_log_fromPS.setOverwriteMode(True)

        self.verticalLayout.addWidget(self.textBrowser_log_fromPS)

        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(Qt.BottomDockWidgetArea, self.dockWidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043c\u0435\u043d\u0430 \u043a\u043e\u043d\u0442\u0440\u043e\u043b\u043b\u0435\u0440\u0430 \u0434\u043e\u043c\u0435\u043d\u0430", None))
        self.action_about.setText(QCoreApplication.translate("MainWindow", u"\u041e \u043d\u0430\u0441...", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_domain.setToolTip(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f \u0434\u043e\u043c\u0435\u043d\u0430, \u043e\u0442\u043a\u0443\u0434\u0430 \u0431\u0443\u0434\u0435\u0442 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0430 \u043f\u0435\u0440\u0435\u0434\u0430\u0447\u0430.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.lineEdit_domain.setStatusTip(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f \u0434\u043e\u043c\u0435\u043d\u0430, \u043e\u0442\u043a\u0443\u0434\u0430 \u0431\u0443\u0434\u0435\u0442 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0430 \u043f\u0435\u0440\u0435\u0434\u0430\u0447\u0430.", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.lineEdit_domain.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.lineEdit_domain.setInputMask("")
        self.lineEdit_domain.setPlaceholderText(QCoreApplication.translate("MainWindow", u"domain.com", None))
#if QT_CONFIG(statustip)
        self.pushButton_connect.setStatusTip(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u043a\u043b\u044e\u0447\u0438\u0442\u0441\u044f \u043a \u0434\u043e\u043c\u0435\u043d\u0443", None))
#endif // QT_CONFIG(statustip)
        self.pushButton_connect.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u043a\u043b\u044e\u0447\u0438\u0442\u0441\u044f", None))
#if QT_CONFIG(tooltip)
        self.pushButton_ownersOfDomain.setToolTip(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u041f\u043e\u043b\u0443\u0447\u0438\u0442\u044c \u0442\u0435\u043a\u0443\u0449\u0435\u0433\u043e \u0445\u043e\u0437\u044f\u0438\u043d\u0430 \u0440\u043e\u043b\u0435\u0439 \u0432 \u0434\u043e\u043c\u0435\u043d\u0435</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Open Sans,sans-serif'; font-size:10pt; font-weight:600; color:#313131; background-color:#ffffff;\">\u0411\u0443\u0434\u0435\u0442 \u0432\u044b\u043f"
                        "\u043e\u043b\u043d\u0435\u043d\u0430 \u043a\u043e\u043c\u0430\u043d\u0434\u0430:</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; color:#0000ff;\">netdom query fsmo</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.pushButton_ownersOfDomain.setStatusTip(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u0443\u0447\u0438\u0442\u044c \u0442\u0435\u043a\u0443\u0449\u0435\u0433\u043e \u0445\u043e\u0437\u044f\u0438\u043d\u0430 \u0440\u043e\u043b\u0435\u0439 \u0432 \u0434\u043e\u043c\u0435\u043d\u0435", None))
#endif // QT_CONFIG(statustip)
        self.pushButton_ownersOfDomain.setText(QCoreApplication.translate("MainWindow", u"\u0425\u043e\u0437\u044f\u0438\u043d \u0440\u043e\u043b\u0435\u0439 \u0434\u043e\u043c\u0435\u043d\u0430", None))
        self.label_info_aboutanotherdomain.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f \u0438\u043d\u043e\u0433\u043e \u0434\u043e\u043c\u0435\u043d\u0430, \u043a\u0443\u0434\u0430 \u043d\u0443\u0436\u043d\u043e \u043f\u0435\u0440\u0435\u0434\u0430\u0442\u044c", None))
#if QT_CONFIG(tooltip)
        self.lineEdit.setToolTip(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f \u0434\u043e\u043c\u0435\u043d\u0430, \u043a\u0443\u0434\u0430 \u0431\u0443\u0434\u0435\u0442 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0430 \u043f\u0435\u0440\u0435\u0434\u0430\u0447\u0430.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.lineEdit.setStatusTip(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f \u0434\u043e\u043c\u0435\u043d\u0430, \u043a\u0443\u0434\u0430 \u0431\u0443\u0434\u0435\u0442 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0430 \u043f\u0435\u0440\u0435\u0434\u0430\u0447\u0430.", None))
#endif // QT_CONFIG(statustip)
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"2n", None))
#if QT_CONFIG(tooltip)
        self.pushButton_changedomain.setToolTip(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u041f\u0435\u0440\u0435\u0434\u0430\u0447\u0438 \u0440\u043e\u043b\u0435\u0439 FSMO \u043c\u0435\u0436\u0434\u0443 \u043a\u043e\u043d\u0442\u0440\u043e\u043b\u043b\u0435\u0440\u0430\u043c\u0438 Active Directory.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">\u0411\u0443\u0434\u0435\u0442 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u044b \u043a\u043e\u043c\u0430\u043d\u0434\u044b"
                        ":</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas'; font-size:10pt; font-weight:600; color:#0000ff; background-color:#f9f2f4;\">1. ntdsutil</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas'; font-size:10pt; font-weight:600; color:#0000ff; background-color:#f9f2f4;\">2. roles</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas'; font-size:10pt; font-weight:600; color:#0000ff; background-color:#f9f2f4;\">3. connections</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas'; font-size:10pt; font-weight:600; color:#0000ff; bac"
                        "kground-color:#f9f2f4;\">4. connect to server &lt;name of server&gt;</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas'; font-size:10pt; font-weight:600; color:#0000ff; background-color:#f9f2f4;\">5. transfer ...</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.pushButton_changedomain.setStatusTip(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0434\u0430\u0447\u0438 \u0440\u043e\u043b\u0435\u0439 FSMO \u043c\u0435\u0436\u0434\u0443 \u043a\u043e\u043d\u0442\u0440\u043e\u043b\u043b\u0435\u0440\u0430\u043c\u0438 Active Directory.", None))
#endif // QT_CONFIG(statustip)
        self.pushButton_changedomain.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0434\u0430\u0442\u044c \u0440\u043e\u043b\u0438", None))
#if QT_CONFIG(tooltip)
        self.checkBox_PDCEmulator.setToolTip(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0434\u0430\u0442\u044c PDCEmulator. \u041a\u043e\u043c\u0430\u043d\u0434\u0430: transfer pdc", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.checkBox_PDCEmulator.setStatusTip(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0434\u0430\u0442\u044c PDCEmulator. \u041a\u043e\u043c\u0430\u043d\u0434\u0430: transfer pdc", None))
#endif // QT_CONFIG(statustip)
        self.checkBox_PDCEmulator.setText(QCoreApplication.translate("MainWindow", u"PDCEmulator", None))
#if QT_CONFIG(tooltip)
        self.checkBox_RIDMaster.setToolTip(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0434\u0430\u0442\u044c RIDMaster \u041a\u043e\u043c\u0430\u043d\u0434\u0430: transfer rid master", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.checkBox_RIDMaster.setStatusTip(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0434\u0430\u0442\u044c RIDMaster. \u041a\u043e\u043c\u0430\u043d\u0434\u0430: transfer rid master", None))
#endif // QT_CONFIG(statustip)
        self.checkBox_RIDMaster.setText(QCoreApplication.translate("MainWindow", u"RIDMaster", None))
#if QT_CONFIG(tooltip)
        self.checkBox_InfrastructureMaster.setToolTip(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0434\u0430\u0442\u044c InfrastructureMaster. \u041a\u043e\u043c\u0430\u043d\u0434\u0430: transfer infrastructure master", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.checkBox_InfrastructureMaster.setStatusTip(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0434\u0430\u0442\u044c InfrastructureMaster. \u041a\u043e\u043c\u0430\u043d\u0434\u0430: transfer infrastructure master", None))
#endif // QT_CONFIG(statustip)
        self.checkBox_InfrastructureMaster.setText(QCoreApplication.translate("MainWindow", u"InfrastructureMaster", None))
#if QT_CONFIG(tooltip)
        self.checkBox_SchemaMaster.setToolTip(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0434\u0430\u0442\u044c SchemaMaster. \u041a\u043e\u043c\u0430\u043d\u0434\u0430: transfer schema master", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.checkBox_SchemaMaster.setStatusTip(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0434\u0430\u0442\u044c SchemaMaster. \u041a\u043e\u043c\u0430\u043d\u0434\u0430: transfer schema master", None))
#endif // QT_CONFIG(statustip)
        self.checkBox_SchemaMaster.setText(QCoreApplication.translate("MainWindow", u"SchemaMaster", None))
#if QT_CONFIG(tooltip)
        self.checkBox_DomainNamingMaster.setToolTip(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0434\u0430\u0442\u044c DomainNamingMaster. \u041a\u043e\u043c\u0430\u043d\u0434\u0430: transfer naming master", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.checkBox_DomainNamingMaster.setStatusTip(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0434\u0430\u0442\u044c DomainNamingMaster. \u041a\u043e\u043c\u0430\u043d\u0434\u0430: transfer naming master", None))
#endif // QT_CONFIG(statustip)
        self.checkBox_DomainNamingMaster.setText(QCoreApplication.translate("MainWindow", u"DomainNamingMaster", None))
        self.dockWidget.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433 \u0441 \u043a\u043e\u043c\u0430\u043d\u0434\u043d\u043e\u0439 \u0441\u0442\u0440\u043e\u043a\u0438", None))
        self.textBrowser_log_fromPS.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:10px; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt; font-weight:400;\"><br /></p></body></html>", None))
        self.textBrowser_log_fromPS.setPlaceholderText("")
    # retranslateUi

