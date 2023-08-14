# !/usr/bin/env python
# coding:utf-8

from ATAttack.framework.prints import *
import winreg
import os

key = r"Software\Microsoft\Terminal Server Client\Servers"
values = []
K = 0

class login_():

    @staticmethod
    def ListLogged_inUsers():
        #User = getpass.getuser()

        try:
            open_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key)
            countkey = winreg.QueryInfoKey(open_key)[0]
            for i in range(int(countkey)):
                db = winreg.EnumKey(open_key, i)
                servers = winreg.OpenKey(
                    winreg.HKEY_CURRENT_USER, key + "\\" + db)
                name, value, type = winreg.EnumValue(servers, K)
                values.append(str(db) + "|" + str(value))
                #values['current_user'] = User
                #values['Server'] = db
                #values['UsernameHint'] = value
            winreg.CloseKey(open_key)
        except WindowsError:
            pass

    # ListAllUsers RDP Connections History
    def powershell(self, cmd):
        powershell = os.popen(r"powershell.exe " + cmd).read()
        stdout = powershell.split('\n')
        return stdout

    def AllUser(self):

        cmd = "$AllUser = Get-WmiObject -Class Win32_UserAccount;" \
              "foreach($User in $AllUser)" \
              "{Write-Host $User.Caption};"
        cmder = "$AllUser = Get-WmiObject -Class Win32_UserAccount;" \
            "foreach($User in $AllUser)" \
            "{Write-Host $User.SID};"

        user_name = self.powershell(cmd)
        sid = self.powershell(cmder)

        num = {}
        for y in range(len(user_name)):
            num[user_name[y]] = sid[y]

        for id in sid:
            try:
                dba = winreg.OpenKey(winreg.HKEY_USERS, id + "\\" + key)
                count = winreg.QueryInfoKey(dba)[0]
                for s in range(int(count)):
                    dbs = winreg.EnumKey(dba, s)
                    server = winreg.OpenKey(
                        winreg.HKEY_USERS,
                        id + os.sep + key + "\\" + dbs)
                    name, value, type = winreg.EnumValue(server, K)

                    # print values
                    for www in num:
                        if num[www] == id:
                            # print "SID :" + id
                            values.append(str(dbs) + "|" + str(value))
                            # print "User:" + www + ":" + value + ":" + dbs
            except WindowsError:
                pass

    def rdplogin_(self):

        print_warning("列出登录的用户RDP连接历史记录")
        self.ListLogged_inUsers()
        print_warning("列出所有的用户RDP连接历史记录")
        self.AllUser()
        print (list(set(values)))
