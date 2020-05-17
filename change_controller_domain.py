import subprocess
import os
global domain
domain = 'test.com'

#
#Чтобы получить текущих владельцев ролей Владелец схемы и
#Владелец доменных имён в лесу, нужно выполнить команду PoSh:
#
#
#Чтобы получить владельцев ролей Владелец относительных идентификаторов,
#Эмулятор основного контроллера домена и Владелец инфраструктуры домена в домене, выполните:
#
def run_command_in_powershell(command):
    tmp = subprocess.run(['powershell', command],
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,)
    if tmp.stdout:
        print(tmp.stdout.decode('utf-8'))
    else:
        print(tmp.stderr.decode('CP1251'))

run_command_in_powershell(f"Get-ADForest {domain}| ft DomainNamingMaster, SchemaMaster")
run_command_in_powershell(f"Get-ADDomain {domain}| ft InfrastructureMaster, PDCEmulator, RIDMaster")
# run_command_in_powershell(f"Move-ADDirectoryServerOperationMasterRole")
#
#Для передачи ролей FSMO между контроллерами Active Directory
#
#os.system(f"Move-ADDirectoryServerOperationMasterRole")
