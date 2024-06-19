# KKTATOL

Скрипт для мониторинга ККТ АТОЛ в Zabbix по IP

## Описание

Этот проект содержит скрипты для мониторинга ККТ АТОЛ через Zabbix. Скрипты позволяют получать информацию о состоянии ККТ и перезагружать устройства по IP.

## Требования

- Zabbix 5.4 или выше
- Драйвер ККТ АТОЛ версии 10.10.3.0

## Установка

1. **Импорт шаблона Zabbix**

   Загрузите шаблон `KKTATOL.yaml` в Zabbix через импорт (РАБОТАЕТ ТОЛЬКО С ВЕРСИИ ZABBIX 5.4).

   ![изображение](https://github.com/shendr404/KKTATOL/assets/143122797/7735892f-7420-4cd6-8f75-2e2340ef21e2)

2. **Размещение скриптов**

   Скопируйте файлы `kktatol.py`, `multikktatol.py` и `rebootkkt.py` в директорию `/usr/lib/zabbix/externalscripts/` и дайте файлам права на выполнение:

   ```bash
   sudo chmod +x /usr/lib/zabbix/externalscripts/kktatol.py
   sudo chmod +x /usr/lib/zabbix/externalscripts/multikktatol.py
   sudo chmod +x /usr/lib/zabbix/externalscripts/rebootkkt.py

3. **Установка драйвера для ККТ АТОЛ**

Загрузите драйвер для работы с ККТ АТОЛ с ![этой страницы](https://fs.atol.ru/SitePages/%D0%A6%D0%B5%D0%BD%D1%82%D1%80%20%D0%B7%D0%B0%D0%B3%D1%80%D1%83%D0%B7%D0%BA%D0%B8.aspx). Внутри архива с драйвером Драйвер ККТ 10.10.3.0 в папке installer найдите пакеты для deb и rpm. Установите пакет libfptr10_10.10.3.0, подходящий для вашей системы.
