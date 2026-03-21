#!/usr/bin/env python3
import shutil
import psutil
import socket
import time
import requests

def check_disk_usage(disk):
    """Verifies that there's enough free space on disk"""
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20


def check_cpu_usage():
    """Verifies that there's enough unused CPU"""
    usage = psutil.cpu_percent(1)
    return usage < 80

def check_available_memory():
    """Verifies that there's enough RAM memory"""
    memory  = psutil.virtual_memory()
    free_memory = memory.available
    return free_memory > 500 *2**20

def check_localhost():
    return socket.gethostbyaddr("127.0.0.1")[0] == 'localhost'

def check_conectivity():
    url ='https://www.google.com'
    response = requests.get(url)
    return response.ok


messages = []
if not check_cpu_usage():
    message = 'Error - CPU usage is over 80%'
    messages += [message]
if not check_disk_usage('/'):
    message = 'Error - Available disk space is less than 20%'
    messages += [message]
if not check_available_memory():
    message = 'Error - Available memory is less than 500MB'
    messages += [message]
if not check_localhost():
    message = 'Error - localhost cannot be resolved to 127.0.0.1'
    messages += [message]
if not check_conectivity():
    message = 'Error - cannot connect to internet'
    messages += [message]
# time.sleep(60)
# * * * * * /home/student-01-fa9067c15551/health_check.py
print('\n'.join(messages))
