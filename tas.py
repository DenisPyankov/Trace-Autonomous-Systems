import subprocess
import re
import requests
import json
import socket


def main():
    # Запросить у пользователя доменное имя или IP-адрес
    host = input("Введите доменное имя или IP-адрес: ")

    try:
        socket.gethostbyname(host)
    except socket.gaierror:
        print("Некорректный домен или IP-адрес")
        return

    # Запустить команду tracert и получить ее вывод
    tracert_process = subprocess.Popen(["tracert", host], stdout=subprocess.PIPE)
    output = tracert_process.communicate()[0].decode('cp866')

    # Найти все IP-адреса в выводе tracert
    ip_addresses = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", output)

    # Создать таблицу для вывода результатов
    print("№ по порядку\tIP\t\t\tСтрана\tAS\tПровайдер")
    for i, ip in enumerate(ip_addresses):
        if i == 0:
            continue
        # Если IP-адрес является "белым", то определить номер автономной системы
        if not ip.startswith("192.168.") and not ip.startswith("10.") and not ip.startswith("172."):
            # Отправить запрос к API ipinfo.io
            response = requests.get(f"https://ipinfo.io/{ip}/json")
            if response.status_code == 200:
                # Получить данные из ответа API
                data = json.loads(response.content)
                country = data.get("country", "")
                asn = data.get("asn", "")
                provider = data.get("org", "")

                # Вывести результаты
                print(f"{i}\t\t{ip}\t{asn}\t{country}\t{provider}")
            else:
                print(f"{i}\t\t{ip}\t\t\t\t\tОшибка при получении данных")
        else:
            # Вывести результаты для "не-белых" IP-адресов
            print(f"{i}\t\t{ip}")


if __name__ == "__main__":
    main()
