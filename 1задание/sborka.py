import sys
from mymodule import *
if len(sys.argv) == 1:
    print('Привет!!! тебе доступны следующие команты:'
          '\n-help - вывод инструкции по работе программы;'
          '\n-full – вывод всех сведений о системе и аппаратной конфигурации'
          '\n-cpu – вывод сведений о процессоре'
          '\n-gpu – вывод сведений о видеокарте'
          '\n-disk – вывод сведений о жёстком диске'
          '\n-sb – вывод сведений о системной плате'
          '\n-save – сохранение результатов в файл')
else:
    flag=sys.argv
    for i in range(len(flag)-1): #массив по определению каждого из введённых флагов
        if flag[i+1]=='-help':
            print('Привет!!! тебе доступны следующие команты:'
          '\n-help - вывод инструкции по работе программы;'
          '\n-full – вывод всех сведений о системе и аппаратной конфигурации'
          '\n-cpu – вывод сведений о процессоре'
          '\n-gpu – вывод сведений о видеокарте'
          '\n-disk – вывод сведений о жёстком диске'
          '\n-sb – вывод сведений о системной плате'
          '\n-save – сохранение результатов в файл')
        elif flag[i+1]=='-full':
            print(cpu_info())
            print(gpu_info())
            print(disk_info())
            print(sb_info())
        elif flag[i+1]=='-cpu':
            print(cpu_info())
        elif flag[i+1]=='-gpu':
            print(gpu_info())
        elif flag[i+1]=='-disk':
            print(disk_info())
        elif flag[i+1]=='-sb':
            print(sb_info())
        elif flag[i+1]=='-save':
            print(record())
        else:
            print('команда введена не корректно, введите -help')
        
  