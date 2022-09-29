import os
#from selectors import SelectorKey
#from pynput.keyboard import *
import platform as plt

print(plt.system())

class shutdown:
    'shutdown computer'
    def __init__(self , operatingSYS):
        self.operatingSYS = plt.system()
        if operatingSYS == 'Windows':
            os.system('cmd /k "Shutdown.exe -s -t 00"')
            #print('Works')
        elif operatingSYS == 'Linux':
            os.system("shutdown now -h")
        elif operatingSYS == 'Darwin':
            pass


class sleepMode:
    'Sleep Mode'
    def __init__(self , operatingSYS):
        self.operatingSYS = plt.system()
        if operatingSYS == 'Windows':
            os.system('cmd /k "RUNDLL32.EXE powrprof.dll,SetSuspendState 0,1,0"')
        elif operatingSYS == 'Linux':
            os.system('systemctl suspend -i ')
        elif operatingSYS == 'Darwin':
            pass


class LogOff:
   'Logoff user'
   def __init__(self , operatingSYS):
        self.operatingSYS = plt.system()
        if operatingSYS == 'Windows':
            os.system('cmd /k "shutdown -L ')
        elif operatingSYS == 'Linux':
            pass
            #os.system('sudo pkill -u username')#Username'i getirecek bir fonksiyon yaz
        elif operatingSYS == 'Darwin':
            pass

class LockScreen:
    'Locks Screen'
    def __init__(self , operatingSYS):
        self.operatingSYS = plt.system()
        if operatingSYS == 'Windows':
            os.system('cmd /k "Rundll32.exe user32.dll,LockWorkStation"')
        elif operatingSYS == 'Linux':
            pass
        elif operatingSYS == 'Darwin':
            pass
            
        