import redis

from flask import Flask, request, jsonify

from service import post_alarm, get_alarms, update_alarm


r = redis.Redis(host='172.17.0.2', port=6379, decode_responses=True)
app = Flask(__name__)

@app.route('/alarm', methods = ['GET', 'POST'])
def add_alarm():
    """Создание и получение отчетов о превышении лимита памяти"""
    if request.method == "GET":
        return jsonify(get_alarms())
    if request.method == "POST":
        return jsonify(post_alarm(request.get_json()))

@app.route('/alarm/<alarm_id>', methods = ['PUT'])
def alarm_update(alarm_id):
    """Обновление отчета"""
    return jsonify(update_alarm(alarm_id, request.get_json()))

if __name__ == "__main__":
    app.run(app.run(debug=True, host='0.0.0.0', port=8080))

