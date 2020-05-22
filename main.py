import sys
import threading
from socket import gethostname, gethostbyname, gethostbyaddr, getaddrinfo, getfqdn
from subprocess import STDOUT, check_output, run, PIPE, TimeoutExpired, Popen
# import wexpect
# from pexpect import popen_spawn, TIMEOUT
from pythonping import ping
from PySide2 import QtWidgets
# from PySide2 import QtCore
from PySide2.QtCore import QThread
import ui

auto_domain = gethostbyname(gethostname())
try:
    auto_domain = gethostbyaddr(auto_domain)[0].split('.', 1)[1]
except IndexError as IE:
    print(f"[WARNING] {IE}")
    auto_domain = gethostbyaddr(auto_domain)[0]

print(auto_domain)


class TransferFSMOThread(QThread):
    def __init__(self, mainwindow, parent=None):
        super().__init__()
        self.mainwindow = mainwindow
        
    
    def run(self):
        print(self.mainwindow.need_send_transfer_FSMO)
        command = f'''ntdsutil roles connections "connect to server {self.mainwindow.to_domain}" quit {' '.join(self.mainwindow.need_send_transfer_FSMO)} quit quit'''
        print(command)
        
        self.mainwindow.turnoffgui()
        self.mainwindow.pushButton_connect.setEnabled(False)
        self.mainwindow.lineEdit_domain.setEnabled(False)
        self.mainwindow.progressBar_waiting.setMaximum(0)

        try:
            sub_process = Popen(command, stdout=PIPE, encoding="CP866")
            # print(sub_process)
            while True:
                output = sub_process.stdout.readline()
                if output == '' and sub_process.poll() is not None:
                    break
                elif output:
                    self.mainwindow.textBrowser_log_fromPS.append(output.strip())
            rc = sub_process.poll()
            print(rc)
            
        except TimeoutExpired as ex:
            print(ex)
            self.mainwindow.textBrowser_log_fromPS.append(f"Ошибка!Время ожидание истекло..\n{str(sub_process)}")

        self.mainwindow.textBrowser_log_fromPS.append(str('------------------------'))

        self.mainwindow.turnongui()
        self.mainwindow.pushButton_connect.setEnabled(True)
        self.mainwindow.lineEdit_domain.setEnabled(True)
        self.mainwindow.progressBar_waiting.setMaximum(1)

def ownersOfDomain(self):
    self.turnoffgui()
    self.pushButton_connect.setEnabled(False)
    self.lineEdit_domain.setEnabled(False)
    self.progressBar_waiting.setMaximum(0)
    try:
        process = run("netdom query fsmo", stdout=PIPE,
                                            stderr=PIPE,
                                            encoding='CP866')
        
        #process = process.communicate()
        #self.textBrowser_log_fromPS.append(str(process.stdout))
            
        if process.stdout:
            self.textBrowser_log_fromPS.append(str(process.stdout))
        else:
            self.textBrowser_log_fromPS.append(str(process.stderr))

        self.textBrowser_log_fromPS.append(str('------------------------'))
                
    except FileNotFoundError as FE:
        print(f"[ERROR] {FE}")
        self.textBrowser_log_fromPS.append("Ошибка! Исполнитель netdom не обнаружен.")
        
    self.turnongui()
    self.pushButton_connect.setEnabled(True)
    self.lineEdit_domain.setEnabled(True)
    self.progressBar_waiting.setMaximum(1)




class MainApp(QtWidgets.QMainWindow, ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.auto_domain = auto_domain
        
        self.domain = None
        self.to_domain = None
        self.need_send_transfer_FSMO = None
        self.transferThread = TransferFSMOThread(mainwindow=self)
        
        self.transfer_naming_master = False
        self.transfer_pdc = False
        self.transfer_rid_master = False
        self.transfer_schema_master = False
        self.transfer_infrastructure_master = False
        
        self.lineEdit_domain.setText(self.auto_domain)
        self.pushButton_connect.clicked.connect(self.checkdomain)
        self.pushButton_ownersOfDomain.clicked.connect(self.ownersOfDomain_thread)
        # self.pushButton_InfrastructureMaster_and_PDCEmulator_RIDMaster.clicked.connect(self.InfrastructureMaster_and_PDCEmulator_RIDMaster)
        self.pushButton_changedomain.clicked.connect(self.changedomain)
        self.lineEdit_domain.textChanged.connect(self.turnoffgui)
        self.lineEdit.textChanged.connect(self.turnoffbutton)
        

    def turnoffbutton(self):
        if self.lineEdit.text():
            self.pushButton_changedomain.setEnabled(True)
        else:
            self.pushButton_changedomain.setEnabled(False)


    def turnongui(self):
        self.label_info_aboutanotherdomain.setEnabled(True)
        self.pushButton_ownersOfDomain.setEnabled(True)
        self.lineEdit.setEnabled(True)
        self.pushButton_changedomain.setEnabled(True)
        self.checkBox_DomainNamingMaster.setEnabled(True)
        self.checkBox_InfrastructureMaster.setEnabled(True)
        self.checkBox_PDCEmulator.setEnabled(True)
        self.checkBox_SchemaMaster.setEnabled(True)
        self.checkBox_RIDMaster.setEnabled(True)

    def turnoffgui(self):
        self.label_info_aboutanotherdomain.setEnabled(False)
        self.pushButton_ownersOfDomain.setEnabled(False)
        self.lineEdit.setEnabled(False)
        self.pushButton_changedomain.setEnabled(False)
        self.checkBox_DomainNamingMaster.setEnabled(False)
        self.checkBox_InfrastructureMaster.setEnabled(False)
        self.checkBox_PDCEmulator.setEnabled(False)
        self.checkBox_SchemaMaster.setEnabled(False)
        self.checkBox_RIDMaster.setEnabled(False)   

    def checkdomain(self):
        self.domain = self.lineEdit_domain.text()
        try:
            a = ping(self.domain, verbose=True)
            if a.success:
                self.textBrowser_log_fromPS.append(str(a))
                self.textBrowser_log_fromPS.append('Success\n------------------------')
                print('Success')
                self.pushButton_ownersOfDomain.setEnabled(True)
                self.lineEdit.setEnabled(True)
                # self.pushButton_changedomain.setEnabled(True)
                self.checkBox_DomainNamingMaster.setEnabled(True)
                self.checkBox_InfrastructureMaster.setEnabled(True)
                self.checkBox_PDCEmulator.setEnabled(True)
                self.checkBox_SchemaMaster.setEnabled(True)
                self.checkBox_RIDMaster.setEnabled(True)
                self.label_info_aboutanotherdomain.setEnabled(True)

        except OSError as os:
            self.textBrowser_log_fromPS.append(a,str(os))
        except RuntimeError as re:
            self.textBrowser_log_fromPS.append(str(re))
            
        print(self.domain)

    def ownersOfDomain_thread(self):
        t2 = threading.Thread(target=ownersOfDomain, args=(self,), daemon=True)
        t2.start()

    def changedomain(self):
        PDCEmulator = self.checkBox_PDCEmulator.isChecked()
        RIDMaster = self.checkBox_RIDMaster.isChecked()
        InfrastructureMaster = self.checkBox_InfrastructureMaster.isChecked()
        SchemaMaster = self.checkBox_SchemaMaster.isChecked()
        DomainNaminMaster = self.checkBox_DomainNamingMaster.isChecked()
        
        if PDCEmulator or RIDMaster or InfrastructureMaster or SchemaMaster or DomainNaminMaster:
            self.anyCheckBox = True
        else:
            self.anyCheckBox = False
            
        if self.anyCheckBox is True:
            need_send = []
            self.need_send_transfer_FSMO = []
            self.to_domain = str(self.lineEdit.text()) 

            if PDCEmulator:
                self.transfer_pdc = True
                need_send.append("\ntransfer pdc")
                self.need_send_transfer_FSMO.append('''"transfer pdc"''')
                
            else:
                self.transfer_pdc = False
                try:
                    need_send.pop(need_send.index("\ntransfer pdc"))
                    self.need_send_transfer_FSMO.pop(self.need_send_transfer_FSMO.index('''"transfer pdc"'''))
                except ValueError as ve:
                    print(ve)

            if RIDMaster:
                self.transfer_rid_master = True
                need_send.append("\ntransfer rid master")
                self.need_send_transfer_FSMO.append('''"transfer rid master"''')
                
            else:
                self.transfer_rid_master = False
                try:
                    need_send.pop(need_send.index("\ntransfer rid master"))
                    self.need_send_transfer_FSMO.pop(self.need_send_transfer_FSMO.index('''"transfer rid master"'''))
                except ValueError as ve:
                    print(ve)

            if InfrastructureMaster:
                self.transfer_infrastructure_master = True
                need_send.append("\ntransfer infrastructure master")
                self.need_send_transfer_FSMO.append('''"transfer infrastructure master"''')
                
            else:
                self.transfer_infrastructure_master = False
                try:
                    need_send.pop(need_send.index("\ntransfer infrastructure master"))
                    self.need_send_transfer_FSMO.pop(self.need_send_transfer_FSMO.index('''"transfer infrastructure master"'''))
                except ValueError as ve:
                    print(ve)

            if SchemaMaster:
                self.transfer_schema_master = True
                need_send.append("\ntransfer schema master")
                self.need_send_transfer_FSMO.append('''"transfer schema master"''')
                
            else:
                self.transfer_schema_master = False
                try:
                    need_send.pop(need_send.index("\ntransfer schema master"))
                    self.need_send_transfer_FSMO.pop(self.need_send_transfer_FSMO.index('''"transfer schema master"'''))
                except ValueError as ve:
                    print(ve)

            if DomainNaminMaster:
                self.transfer_naming_master = True
                need_send.append("\ntransfer naming master")
                self.need_send_transfer_FSMO.append('''"transfer naming master"''')
                
            else:
                self.transfer_naming_master = False
                try:
                    need_send.pop(need_send.index("\ntransfer naming master"))
                    self.need_send_transfer_FSMO.pop(self.need_send_transfer_FSMO.index('''"transfer naming master"'''))
                except ValueError as ve:
                    print(ve)

            print(self.need_send_transfer_FSMO)

            # need_send = ','.join(need_send)
            buttonReply = QtWidgets.QMessageBox.question(self, 'Передача роли',
            f"Будет выполнены команды:\nntdsutil\nroles\nconnections\nconnect to server {self.to_domain}{''.join(need_send)}\nПродолжить?",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)

            if buttonReply == QtWidgets.QMessageBox.Yes:
                self.transferThread.start()
                #t1 = threading.Thread(target=transferFSMO, args=(self,), daemon=True)
                #t1.start()
            else:
                print('No clicked.\nну ладно')
                
        else:
            print("[ERROR] Роли не выбраны")
            
            a = QtWidgets.QMessageBox()
            a.setIcon(QtWidgets.QMessageBox.Information)
            a.setWindowTitle("Ошибка")
            a.setText("А передовать-то что?")
            a.setInformativeText("Нужно выбрать роли, для передачи.")
            a.setStandardButtons(QtWidgets.QMessageBox.Ok)

            retval = a.exec_()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()
