import redis


r = redis.Redis(host='172.17.0.2', port=6379, decode_responses=True)

def post_alarm(request: dict) -> dict:
    """Добовление нового отчета о превышении лимита памяти"""
    value = r.incr('id')
    data = request
    r.hmset(f"alarm_{value}", data)
    r.hgetall(value)
    response = {'id': value, 'time': request['time'], 'number_of_bytes': request['number_of_bytes']}
    return response

def get_alarms() -> list:
    """Список всех отчетов о превышении памяти"""
    response = []
    for i in r.scan_iter("alarm*"):
        alarm_id = str(i).split('alarm_')[1]
        print(r.hgetall(i), i)
        alarm = {"id": alarm_id, "time": r.hgetall(i)["time"], "number_of_bytes": r.hgetall(i)["number_of_bytes"]}
        response.append(alarm)
    return response

def update_alarm(alarm_id: str, request: dict) -> dict:
    """Обновление отчета"""
    alarm_id = alarm_id
    data = request
    r.hmset(f"alarm_{alarm_id}", data)
    response = {'id': alarm_id, 'time': request['time'], 'number_of_bytes': request['number_of_bytes']}
    return response