#!/usr/bin/env python3

import psutil
import logging
import os
import smtplib

log_file = os.path.expanduser('~/system_health.log')
logging.basicConfig(filename=log_file, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
CPU_THRESHOLD = 80.0  
MEMORY_THRESHOLD = 80.0  
DISK_THRESHOLD = 80.0  
PROCESS_COUNT_THRESHOLD = 200  


def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f'CPU usage: {cpu_usage}%')
    if cpu_usage > CPU_THRESHOLD:
        logging.warning(f'High CPU usage detected: {cpu_usage}%')
        print(f'High CPU usage detected: {cpu_usage}%')

def check_memory_usage():
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent
    print(f'Memory usage: {memory_usage}%')
    if memory_usage > MEMORY_THRESHOLD:
        logging.warning(f'High Memory usage detected: {memory_usage}%')
        print(f'High Memory usage detected: {memory_usage}%')

def check_disk_usage():
    disk_info = psutil.disk_usage('/')
    disk_usage = disk_info.percent
    print(f'Disk usage: {disk_usage}%')
    if disk_usage > DISK_THRESHOLD:
        logging.warning(f'High Disk usage detected: {disk_usage}%')
        print(f'High Disk usage detected: {disk_usage}%')

def check_running_processes():
    process_count = len(psutil.pids())
    print(f'Number of running processes: {process_count}')
    if process_count > PROCESS_COUNT_THRESHOLD:
        logging.warning(f'High number of running processes detected: {process_count}')
        print(f'High number of running processes detected: {process_count}')

if __name__ == '__main__':
    check_cpu_usage()
    check_memory_usage()
    check_disk_usage()
    check_running_processes()

 
