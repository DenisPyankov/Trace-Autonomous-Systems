# Trace-Autonomous-Systems

Данная программа выполняет трассировку маршрута до заданного доменного имени или IP-адреса, а затем выводит информацию об IP-адресах, через которые проходит путь до заданного адреса. Для каждого IP-адреса программа пытается определить номер автономной системы (AS), страну и провайдера.

=========================================================================================
Перед запуском этой программы необходимо убедиться в наличии установленных следующих компонентов:

Библиотеки requests, json, socket (установка командой pip install requests json socket)

Команда tracert (ддоступна в операционной системе Windows)

=========================================================================================
Инструкция по использованию:

Запустите командную строку в Windows.

Перейдите в каталог, в котором находится файл программы tas.py.

Запустите программу командой "python tas.py".

Введите доменное имя или IP-адрес, для которого нужно выполнить трассировку.

Программа начнет выполнять трассировку маршрута и выводить результаты в консоль.

=========================================================================================
Примеры вывода программы:


C:\2023>python tas.py

Введите доменное имя или IP-адрес: google.com

№ по порядку    IP                      Страна  AS      Провайдер

1               192.168.1.1

2               10.242.255.255

3               10.7.32.185

4               10.7.32.170

5               188.43.231.74           RU      AS20485 Joint Stock Company TransTeleCom

6               217.150.55.234          RU      AS20485 Joint Stock Company TransTeleCom

7               188.43.10.141           RU      AS20485 Joint Stock Company TransTeleCom

8               108.170.250.66          RU      AS15169 Google LLC

9               142.250.238.214         US      AS15169 Google LLC

10              142.250.235.62          FI      AS15169 Google LLC

11              142.250.56.217          FI      AS15169 Google LLC

12              108.177.14.138          FI      AS15169 Google LLC

=========================================================================================
C:\2023>python tas.py

Введите доменное имя или IP-адрес: 108.177.14.138

№ по порядку    IP                      Страна  AS      Провайдер

1               192.168.1.1

2               10.242.255.255

3               10.7.32.185

4               10.7.32.170

5               188.43.231.74           RU      AS20485 Joint Stock Company TransTeleCom

6               217.150.55.234          RU      AS20485 Joint Stock Company TransTeleCom

7               188.43.10.141           RU      AS20485 Joint Stock Company TransTeleCom

8               108.170.250.66          RU      AS15169 Google LLC
9               142.250.238.214         US      AS15169 Google LLC
10              142.250.235.62          FI      AS15169 Google LLC
11              142.250.56.217          FI      AS15169 Google LLC
12              108.177.14.138          FI      AS15169 Google LLC
