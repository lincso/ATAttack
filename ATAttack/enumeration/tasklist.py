#! /usr/bin/python
# -*- coding: utf-8 -*-

import platform
import string
import os
import re
import json
import ctypes
from ATAttack.framework.constant import constant
from ATAttack.framework.prints import print_success,print_error

temp_list = []

def get_platform():
    return platform.uname()

def admin():
    return bool(ctypes.windll.shell32.IsUserAnAdmin())

def disk():

    disk_list = []
    for c in string.ascii_uppercase:
        disk = c + ':'
        if os.path.isdir(disk):
            disk_list.append(disk)
    return disk_list

def tasklist():
    if not admin():
        print_error("无法执行，可能没有足够的权限！")
        exit()
    load = os.popen('tasklist').read()
    tasklist = re.findall(r'\w+.exe', load, re.S)
    ing = []
    print_success('当前系统存在的盘符 ' + str(disk()))
    print_success('当前系统的版本'+ str(get_platform()))
    try:
        for av in list(constant.av_json.keys()):
            for task in tasklist:
                if task in av:
                    process = (constant.av_json.setdefault(task, 0))
                    if process != 0:
                        ing.append(process)
        return json.dumps(ing, ensure_ascii=False)
    except Exception as e:
        return e


def token():
    tasklist_v_fo_csv = os.popen('tasklist /v /fo csv').read()
    tasklist_v_fo_csv_list = tasklist_v_fo_csv.split("\n")
    try:

        for tasklist in tasklist_v_fo_csv_list:
            tasklist = tasklist.replace("[", "").replace("]", "").replace("\"", "")
            temp = tasklist.split(",")
            sessions = re.findall('[a-zA-Z]+.+', temp[7], re.S)
            if sessions:
                for session in sessions:
                    session = re.sub('CPU.+', '', session)
                    if r"Running" not in session:
                        temp_list.append(session)
    except Exception:
        pass
    finally:
        return ([i for i in list(set(temp_list)) if i != ''])

