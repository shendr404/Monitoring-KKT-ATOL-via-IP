# Zabbix KKT ATOL via IP

Скрипт для мониторинга ККТ АТОЛ в Zabbix по IP

## Описание

Этот проект содержит скрипты для мониторинга ККТ АТОЛ через Zabbix. Скрипты позволяют получать информацию о состоянии ККТ и перезагружать устройства по IP.

## Требования

- Zabbix 5.4 или выше
- Драйвер ККТ АТОЛ версии 10.10.3.0

## Установка

1. **Импорт шаблона Zabbix**

   Загрузите шаблон `KKTATOL.yaml` в Zabbix через импорт (РАБОТАЕТ ТОЛЬКО С ВЕРСИИ ZABBIX 5.4).

2. **Размещение скриптов**

   Скопируйте файлы `kktatol.py`, `multikktatol.py` и `rebootkkt.py` в директорию `/usr/lib/zabbix/externalscripts/` на сервере Zabbix и дайте файлам права на выполнение:

   ```bash
   sudo chmod +x /usr/lib/zabbix/externalscripts/kktatol.py
   sudo chmod +x /usr/lib/zabbix/externalscripts/multikktatol.py
   sudo chmod +x /usr/lib/zabbix/externalscripts/rebootkkt.py
   ```
   
3. **Установка драйвера для ККТ АТОЛ**

   Загрузите драйвер на сервер Zabbix для работы с ККТ АТОЛ с [этой страницы](https://fs.atol.ru/SitePages/%D0%A6%D0%B5%D0%BD%D1%82%D1%80%20%D0%B7%D0%B0%D0%B3%D1%80%D1%83%D0%B7%D0%BA%D0%B8.aspx). Внутри архива с драйвером `Драйвер ККТ 10.10.3.0` в папке `installer` найдите пакеты для deb и rpm. Установите пакет `libfptr10_10.10.3.0`, подходящий для вашей системы.

## Использование
- **kktatol.py**

   Скрипт `kktatol.py` предназначен для получения различных данных с ККТ. Он принимает параметры командной строки, которые определяют тип запрашиваемых данных.

   Пример использования:
   ```bash
   python /usr/lib/zabbix/externalscripts/kktatol.py <param> <IP-адрес> <порт>
   ```

- **multikktatol.py**

   Скрипт `multikktatol.py` позволяет параллельно запускать несколько экземпляров `kktatol.py` для разных ККТ.


   Пример использования:
   ```bash
   python /usr/lib/zabbix/externalscripts/multikktatol.py <param1> <IP1> <порт1> <param2> <IP2> <порт2> ...
   ```

- **rebootkkt.py**

   Скрипт `rebootkkt.py` предназначен для перезагрузки ККТ.

   Пример использования:
   ```bash
   python /usr/lib/zabbix/externalscripts/rebootkkt.py <IP-адрес> <порт>
   ```

## Параметры

   Параметры, которые можно передать в `kktatol.py` и `multikktatol.py`:

   1. Заводской номер ККТ
   2. Регистрационный номер ККТ
   3. Серийный номер ФН
   4. Осталось дней до окончания ФН
   5. Возраст в днях первого не отправленного документа в ФН
   6. Модель ККТ
   7. Версия прошивки
   8. Лицензия №1
   9. Лицензия №2
   10. Лицензия №3
   11. Лицензия №4
   12. Лицензия №5
   13. Перезагрузка ККТ

## Лицензия
   Этот проект лицензирован под лицензией GPL-3.0 - подробности см. в файле [LICENSE](https://github.com/shendr404/Zabbix-KKT-ATOL-via-IP/blob/main/LICENSE).

## Поддержка

   Если у вас возникли вопросы или предложения, вы можете связаться с автором через [GitHub Issues](https://github.com/shendr404/Zabbix-KKT-ATOL-via-IP/issues).

Автор: [shendr404](https://github.com/shendr404)
