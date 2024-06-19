#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
from concurrent.futures import ProcessPoolExecutor, as_completed
import subprocess
import sys

def run_script(param, ip_address, port):
    """
    Функция для запуска скрипта kktatol.py с заданными параметрами.

    :param param: Параметр для kktatol.py
    :param ip_address: IP адрес для подключения
    :param port: Порт для подключения
    """
    try:
        # Запуск скрипта kktatol.py с параметрами и захват вывода
        result = subprocess.run(
            [sys.executable, '/usr/lib/zabbix/externalscripts/kktatol.py', param, ip_address, port],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True
        )
        output = f"{result.stdout.strip()}" if result.returncode == 0 else f"{result.stderr.strip()}"
        return output
    except Exception as e:
        # Печать исключений
        print(f"Error running script with param {param}, ip_address {ip_address}, port {port}: {e}")
        return None

def main():
    """
    Основная функция для чтения аргументов командной строки и параллельного запуска задач.
    """
    # Проверка на корректное количество аргументов
    if len(sys.argv) < 4 or len(sys.argv) % 3 != 1:
        print("Invalid arguments. Expected format: param1 ip1 port1 param2 ip2 port2 ...")
        sys.exit()

    # Чтение аргументов командной строки
    args = sys.argv[1:]
    tasks = [(args[i], args[i+1], args[i+2]) for i in range(0, len(args), 3)]

    # Определение максимального количества параллельных задач
    max_workers = len(tasks) if len(tasks) <= 10 else 10

    # Запуск задач в параллельных процессах
    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(run_script, *task): task for task in tasks}

        # Обработка завершения задач
        for future in as_completed(futures):
            task = futures[future]
            try:
                # Получение результата задачи
                result = future.result()
                print(result)
            except Exception as e:
                # Печать исключений для каждой задачи
                print(f"Error for task {task}: {e}")

if __name__ == '__main__':
    main()

