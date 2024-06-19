# KKTATOL
Скрипт для мониторинга ККТ АТОЛ в Zabbix по IP

Шаблон KKTATOL.yaml необходимо загрузить в zabbix через импорт (РАБОТАЕТ ТОЛЬКО С ВЕРСИИ ZABBIX 5.4)
![изображение](https://github.com/shendr404/KKTATOL/assets/143122797/7735892f-7420-4cd6-8f75-2e2340ef21e2)

Файлы kktatol.py , multikktatol.py , rebootkkt.py необходимо загрузить по пути /usr/lib/zabbix/externalscripts/ и дать файлам права на выполнение с помощью chmod +x
