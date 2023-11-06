from psutil import *
import platform
#import wmi
from GPUtil import *
NAME = "mymodule"
def cpu_info():
    l=list()
    a=(platform.processor())#имя процессора
    b="Physical cores:"+(str( cpu_count(logical=False)))#число физичсеских ядер процессора
    c=str("Total cores:"+ str(cpu_count(logical=True)))# число всех процессоров
    for i, percentage in enumerate(cpu_percent(percpu=True,interval=1)):#вывод процента загрузки каждого ядра
             l.append(f"Core {i}: {percentage}%")
    d=''.join(f"Total CPU Usage: {cpu_percent()}%")# общая загруженность процессора
    return(a+'\n'+b+'\n'+c+'\n'+str('\n'.join(l))+'\n'+d+'\n'+'\n')
#print(cpu_info())
def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor
    return('')
def memory_info():
# memory info
    svmem = virtual_memory()
    a=(f"Total: {get_size(svmem.total)}")#объём оперативной памяти 
    b=(f"Available: {get_size(svmem.available)}")# объём свободной памяти
    c=(f"Used: {get_size(svmem.used)}")#объём памяти 
    d=(f"Percentage: {svmem.percent}%")#процент занятой памяти
    return(str(a+'\n'+b+'\n'+c+'\n'+d+'\n'+'\n'))
def gpu_info():
    gpus = getGPUs()
    print(gpus)
    list_gpus = []
    for gpu in gpus:
        gpu_name = gpu.name
        gpu_total_memory = f"{gpu.memoryTotal}MB"
        gpu_temperature = f"{gpu.temperature} °C"
        gpu_uuid = gpu.uuid
        a=''.join("Name: ", gpu_name)
        b=''.join("Memory: ", gpu_total_memory)
        c=''.join("Temperature: ", gpu_temperature)
        d=''.join("uuid: ", gpu_uuid)
        return(str((a+'\n'+b+'\n'+c+'\n'+d+'\n'+'\n')))
def sb_info(): #системная плата. Работает только в виндовсе
    a=('Команда работает только в ОС Windows')
    '''c = wmi.WMI()
    for board in c.Win32_BaseBoard():
        print ("\nМодель материнской платы: " + str(board.Model))
        print ("Производитель материнской платы: " + board.Manufacturer)
        print ("Серийный номер материнской платы: " + board.SerialNumber)
'''
    return(str(a+'\n'))
def disk_info():
    d = disk_partitions()
    a=('C диск информация:',(d [0]))
    p = disk_usage(d[0][0]) #C диск
    b=('всего = '+ str(p[0]))
    c=('используется = '+ str(p[1]))
    e=('свободно = '+ str(p[2]))
    n=('процент = '+ str(p[3]))
    
    return(str(str(a)+'\n'+b+'\n'+c+'\n'+e+'\n'+n+'\n'+'\n'))
def record():
    file = open('harakteristiki.txt', 'w+')
    file.write(cpu_info())
    file.write(memory_info())
    file.write(str(gpu_info()))
    file.write(sb_info()) 
    file.write(disk_info())
    file.close()
    range(0)
#print(disk_info())