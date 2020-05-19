import sys
import threading
from socket import gethostname, gethostbyname, gethostbyaddr, getaddrinfo, getfqdn
import subprocess
# import wexpect
# from pexpect import popen_spawn, TIMEOUT
from pythonping import ping
from PySide2 import QtWidgets
from PySide2 import QtCore
import ui

auto_domain = gethostbyname(gethostname())
try:
    auto_domain = gethostbyaddr(auto_domain)[0].split('.', 1)[1]
except IndexError as IE:
    print(f"[WARNING] {IE}")
    auto_domain = gethostbyaddr(auto_domain)[0]

print(auto_domain)


# def run_command(self, command):
#     tmp = subprocess.run([command],
#                          stdout=subprocess.PIPE,
#                          stderr=subprocess.PIPE,)
#     if tmp.stdout:
#         self.textBrowser_log_fromPS.append(str(tmp.stdout.decode('utf-8')))
#     else:
#         self.textBrowser_log_fromPS.append(str(tmp.stderr.decode('CP866')))
#     return tmp

def transferFSMO(self):
    print(f'''[LOG] execute command - ntdsutil roles connections "connect to server {self.to_domain}" quit {''.join(self.need_send_transfer_FSMO)}''')

    self.turnoffgui()
    self.pushButton_connect.setEnabled(False)
    self.lineEdit_domain.setEnabled(False)
    self.progressBar_waiting.setMaximum(0)

    ntdsutil_procces = QtCore.QProcess()
    # ntdsutil_procces.start(f'''ntdsutil roles connections "connect to server {self.to_domain}" quit {''.join(self.need_send_transfer_FSMO)}''')
    ntdsutil_procces.start("ping google.com -t")

    ntdsutil_procces.waitForFinished(10000)
    try:
        res = bytearray(ntdsutil_procces.readAllStandardOutput()).decode("CP866")
        self.textBrowser_log_fromPS.append(str(res))
    except Exception as ex:
        print(ex)
    finally:
        ntdsutil_procces.terminate()
        if ntdsutil_procces.Running:
            print(f"[WARNING] Каким-то хуем процесс еще работат, id - {ntdsutil_procces.processId()}")

    self.turnongui()
    self.pushButton_connect.setEnabled(True)
    self.lineEdit_domain.setEnabled(True)
    self.progressBar_waiting.setMaximum(1)
    # try:
    #     process = subprocess.run(f'''ntdsutil roles connections "connect to server {self.to_domain}" quit {''.join(self.need_send_transfer_FSMO)}''',
    #                                  stdout=subprocess.PIPE,
    #                                 stderr=subprocess.PIPE,
    #                                 timeout=15,
    #                                 encoding='CP866')
      
    #     if process.stdout:
    #         self.textBrowser_log_fromPS.append(str(process.stdout))
    #     else:
    #         self.textBrowser_log_fromPS.append(str(process.stderr))

    # except FileNotFoundError as FE:
    #     self.textBrowser_log_fromPS.append("Ошибка! Исполнитель ntdsutil не обнаружен.")
    #     print(f"[ERROR] {FE}")

    # except subprocess.TimeoutExpired as TE:
    #     self.textBrowser_log_fromPS.append()
    #     self.textBrowser_log_fromPS.append(f"Ошибка! Подробности указаны здесь:\n{TE}")
    
    # finally:
    #     self.turnongui()
    #     self.progressBar_waiting.setMaximum(1)

# Использывать QProcces

class MainApp(QtWidgets.QMainWindow, ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.auto_domain = auto_domain
        self.domain = None
        self.to_domain = None
        self.need_send_transfer_FSMO = None
        self.transfer_naming_master = False
        self.transfer_pdc = False
        self.transfer_rid_master = False
        self.transfer_schema_master = False
        self.lineEdit_domain.setText(self.auto_domain)
        self.pushButton_connect.clicked.connect(self.checkdomain)
        self.pushButton_ownersOfDomain.clicked.connect(self.ownersOfDomain)
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

    def ownersOfDomain(self):
        try:
            process = subprocess.run("netdom query fsmo", stdout=subprocess.PIPE,
                                                                stderr=subprocess.PIPE,
                                                                encoding='CP866')
            #process = process.communicate()
            #self.textBrowser_log_fromPS.append(str(process.stdout))
            
            if process.stdout:
                self.textBrowser_log_fromPS.append(str(process.stdout))
            else:
                self.textBrowser_log_fromPS.append(str(process.stderr))
                
        except FileNotFoundError as FE:
            print(f"[ERROR] {FE}")
            self.textBrowser_log_fromPS.append("Ошибка! Исполнитель netdom не обнаружен.")


    def changedomain(self):
        need_send = []
        self.need_send_transfer_FSMO = []
        self.to_domain = str(self.lineEdit.text()) 

        if self.checkBox_PDCEmulator.isChecked():
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

        if self.checkBox_RIDMaster.isChecked():
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

        if self.checkBox_InfrastructureMaster.isChecked():
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

        if self.checkBox_SchemaMaster.isChecked():
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

        if self.checkBox_DomainNamingMaster.isChecked():
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
            t1 = threading.Thread(target=transferFSMO, args=(self,), daemon=True)
            t1.start()
        else:
            print('No clicked.\nну ладно')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()
