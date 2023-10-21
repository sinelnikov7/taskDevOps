import datetime
import psutil
import requests
import time


url = 'http://localhost:8080/alarm'
# Лимит выше которого формируется запрос
memory_max = 1000000000
while True:
    # Текущее потребления памяти
    using_memory = psutil.virtual_memory().used
    if using_memory > memory_max:
        try:
            time_alarm = datetime.datetime.now()
            data = {"time": str(time_alarm.now()), "number_of_bytes": using_memory}
            response = requests.post(url, json=data, headers={"Content-Type": "application/json"})
            if response.status_code == 200:
                print("Запрос отправлен.")
            else:
                print(f"Зарос завершился с ошибкой: {response.status_code}")
        except Exception:
            print(f"Ошибка сервера")
    # Интервал проверки
    time.sleep(15)
