#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Импортируем необходимые модули
from libfptr10 import IFptr
import sys
import datetime
import time

# Инициализируем объект работы с ККТ
fptr = IFptr("")

# Функция подключения к ККТ
def connectToKKT():
    # Проверяем, переданы ли IP адрес и порт в аргументах командной строки
    if len(sys.argv) == 4:
        # Устанавливаем параметры подключения по IP
        fptr.setSingleSetting(IFptr.LIBFPTR_SETTING_PORT, str(IFptr.LIBFPTR_PORT_TCPIP))
        fptr.setSingleSetting(IFptr.LIBFPTR_SETTING_IPADDRESS, sys.argv[2])
        fptr.setSingleSetting(IFptr.LIBFPTR_SETTING_IPPORT, sys.argv[3])
        fptr.applySingleSettings()
    # Пытаемся подключиться к ККТ 10 раз с интервалом в 5 секунд
    i = 1
    while i < 10:
        fptr.open()     # Открываем соединение
        if fptr.isOpened():     # Проверяем, удалось ли открыть соединение
            return 1
        else:
            time.sleep(5)
            i = i + 1

# Функция для вычисления разницы в днях между текущей датой и заданной
def deltadate(paramAsDateTime):
    now = datetime.datetime.now()
    deltaindays = (paramAsDateTime - now).days
    if deltaindays < -10000:
        return 0
    else:
        return deltaindays + 1

# Функция для получения данных с ККТ в зависимости от переданного параметра
def getDataFromKKT(param):
    # Заводской номер ККТ
    if param == "1":
        fptr.setParam(IFptr.LIBFPTR_PARAM_DATA_TYPE, IFptr.LIBFPTR_DT_SERIAL_NUMBER)
        fptr.queryData()
        print(fptr.getParamString(IFptr.LIBFPTR_PARAM_SERIAL_NUMBER))
    # Регистрационный номер ККТ
    if param == "2":
        fptr.setParam(IFptr.LIBFPTR_PARAM_FN_DATA_TYPE, IFptr.LIBFPTR_FNDT_REG_INFO)
        fptr.fnQueryData()
        print(fptr.getParamString(1037))
    # Серийный номер ФН
    if param == "3":
        fptr.setParam(IFptr.LIBFPTR_PARAM_FN_DATA_TYPE, IFptr.LIBFPTR_FNDT_FN_INFO)
        fptr.fnQueryData()
        print(fptr.getParamString(IFptr.LIBFPTR_PARAM_SERIAL_NUMBER))
    # Осталось дней до окончания ФН
    if param == "4":
        fptr.setParam(IFptr.LIBFPTR_PARAM_FN_DATA_TYPE, IFptr.LIBFPTR_FNDT_VALIDITY)
        fptr.fnQueryData()
        print(deltadate(fptr.getParamDateTime(IFptr.LIBFPTR_PARAM_DATE_TIME)))
    # Возраст в днях первого не отправленного документа в ФН
    if param == "5":
        fptr.setParam(IFptr.LIBFPTR_PARAM_FN_DATA_TYPE, IFptr.LIBFPTR_FNDT_OFD_EXCHANGE_STATUS)
        fptr.fnQueryData()
        print(deltadate(fptr.getParamDateTime(IFptr.LIBFPTR_PARAM_DATE_TIME))*(-1))
    # Модель ККТ
    if param == "6":
        fptr.setParam(IFptr.LIBFPTR_PARAM_DATA_TYPE, IFptr.LIBFPTR_DT_STATUS)
        fptr.queryData()
        print(fptr.getParamString(IFptr.LIBFPTR_PARAM_MODEL_NAME))
    # Версия прошивки
    if param == "7":
        fptr.setParam(IFptr.LIBFPTR_PARAM_DATA_TYPE, IFptr.LIBFPTR_DT_STATUS)
        fptr.queryData()
        print(fptr.getParamString(IFptr.LIBFPTR_PARAM_UNIT_VERSION))
    # Лицензия №1
    if param == "8":
        fptr.setParam(IFptr.LIBFPTR_PARAM_DATA_TYPE, IFptr.LIBFPTR_DT_LICENSE_ACTIVATED)
        # Указываем параметр в LIBFPTR_PARAM_LICENSE_NUMBER, где 1 номер кода лицензии
        fptr.setParam(IFptr.LIBFPTR_PARAM_LICENSE_NUMBER, 1)
        fptr.queryData()
        # Количество дней до окончания действия лицензии от текущей даты
        print(deltadate(fptr.getParamDateTime(IFptr.LIBFPTR_PARAM_LICENSE_VALID_UNTIL)))
    # Лицензия №2
    if param == "9":
        fptr.setParam(IFptr.LIBFPTR_PARAM_DATA_TYPE, IFptr.LIBFPTR_DT_LICENSE_ACTIVATED)
        # Указываем параметр в LIBFPTR_PARAM_LICENSE_NUMBER, где 2 номер кода лицензии
        fptr.setParam(IFptr.LIBFPTR_PARAM_LICENSE_NUMBER, 2)
        fptr.queryData()
        # Количество дней до окончания действия лицензии от текущей даты
        print(deltadate(fptr.getParamDateTime(IFptr.LIBFPTR_PARAM_LICENSE_VALID_UNTIL)))
    # Лицензия №3
    if param == "10":
        fptr.setParam(IFptr.LIBFPTR_PARAM_DATA_TYPE, IFptr.LIBFPTR_DT_LICENSE_ACTIVATED)
        # Указываем параметр в LIBFPTR_PARAM_LICENSE_NUMBER, где 3 номер кода лицензии
        fptr.setParam(IFptr.LIBFPTR_PARAM_LICENSE_NUMBER, 3)
        fptr.queryData()
        # Количество дней до окончания действия лицензии от текущей даты
        print(deltadate(fptr.getParamDateTime(IFptr.LIBFPTR_PARAM_LICENSE_VALID_UNTIL)))
    # Лицензия №4
    if param == "11":
        fptr.setParam(IFptr.LIBFPTR_PARAM_DATA_TYPE, IFptr.LIBFPTR_DT_LICENSE_ACTIVATED)
        # Указываем параметр в LIBFPTR_PARAM_LICENSE_NUMBER, где 4 номер кода лицензии
        fptr.setParam(IFptr.LIBFPTR_PARAM_LICENSE_NUMBER, 4)
        fptr.queryData()
        # Количество дней до окончания действия лицензии от текущей даты
        print(deltadate(fptr.getParamDateTime(IFptr.LIBFPTR_PARAM_LICENSE_VALID_UNTIL)))
    # Лицензия №5
    if param == "12":
        fptr.setParam(IFptr.LIBFPTR_PARAM_DATA_TYPE, IFptr.LIBFPTR_DT_LICENSE_ACTIVATED)
        # Указываем параметр в LIBFPTR_PARAM_LICENSE_NUMBER, где 5 номер кода лицензии
        fptr.setParam(IFptr.LIBFPTR_PARAM_LICENSE_NUMBER, 5)
        fptr.queryData()
        # Количество дней до окончания действия лицензии от текущей даты
        print(deltadate(fptr.getParamDateTime(IFptr.LIBFPTR_PARAM_LICENSE_VALID_UNTIL)))
    # Перезагрузка ККТ
    if param == "13":
        fptr.deviceReboot()

def main():
    # Проверяем, переданы ли параметры командной строки
    if len(sys.argv) == 1:
        print("No parameter")
        sys.exit()
    # Пытаемся подключиться к ККТ
    connectResult = connectToKKT()
    if connectResult == 1:
        # Получаем данные с ККТ в зависимости от переданного параметра
        getDataFromKKT(sys.argv[1])
    else:
        print("No connection")
    # Закрываем соединение с ККТ
    fptr.close()

if __name__ == '__main__':
    main()

