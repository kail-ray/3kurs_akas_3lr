import time
import psutil
import platform
import threading
NAME = "fun"
def time_():            # функция формирует системное время
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S")
    return(current_time)
#print(time_())

# Calling psutil.cpu_precent() for 4 seconds
def proc():#функция формирует загруженность процессора
    return('Загрузка процеесора: '+str(psutil.cpu_percent(4))+'%')
#print(proc())
def memory():
    svmem = psutil.virtual_memory()
    return(f"Percentage: {svmem.percent}%")#процент занятой памяти
#print(memory())
def log():#функция формирует лог из трёх предыдущих функций
    log=[time_(),proc(),memory()]
    return(log)
def is_int(test):#функция проверяет можно ли придать значению введённому пользователем целочисленный тип
        test = str(test)
        if len(test) != 0 and test[0] == "-":
            test = test[1:]
        return test.isnumeric()
def update(d):#функция записывает логи в файл 
    file = open('logi.txt', 'a')
    i=0
    list1=list()
    list2=list()
    while True:
        i+=1
        if i>10:          #задаётся количество логов которые можно записать
            break
        a=log()
        file.write(str(a)+'\n')
        print(a)
        #print(log())
        time.sleep(d-4)         #формируется частота записи, не менее 4 секунд
        list1.append(a[0])       #формируется список данных необходимый для построения графика
        list2.append(a[1].partition(': ')[2].partition('%')[0])
    return(list1,list2)
#update()













