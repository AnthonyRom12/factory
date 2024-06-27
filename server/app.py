from flask import Flask, render_template, jsonify, request
import time
import random
from threading import Thread
import adbutils

app = Flask(__name__)

points = 0
total_points = 0
button_active = True
last_collect_time = 0
level = 1
upgrade_cooldown = 0


# Добавление очков
def add_points():
    global points
    while True:
        time.sleep(20)
        points += random.randint(0, 15)


Thread(target=add_points, daemon=True).start()


# ADB function
def execute_adb_command(command):
    adb = adbutils.AdbClient()
    devices = adb.device_list()
    if devices:
        device = devices[0]
        device.shell(command)
        return True
    return False


# Отображение
@app.route('/')
def index():
    return render_template('index.html', points=points, total_points=total_points, level=level)


# Забрать очки
@app.route('/collect', methods=['POST'])
def collect_points():
    global points, total_points, button_active, last_collect_time
    if button_active:
        total_points += points
        points = 0
        button_active = False
        last_collect_time = time.time()

        execute_adb_command('input keyevent 26')

        return jsonify(success=True, total_points=total_points)
    return jsonify(success=False)


#
@app.route('/check_timer', methods=['GET'])
def check_timer():
    global button_active, last_collect_time, upgrade_cooldown
    time_since_collect = time.time() - last_collect_time
    time_until_collect = max(0, int(7200 - time_since_collect))  # 2 часа
    time_since_upgrade = time.time() - upgrade_cooldown
    time_until_upgrade = max(0, int(86400 - time_since_upgrade))  # 24 часа
    if not button_active and time_since_collect >= 7200:
        button_active = True
    return jsonify(button_active=button_active, time_until_collect=time_until_collect, time_until_upgrade=time_until_upgrade, points=points, total_points=total_points)


@app.route('/upgrade_level', methods=['POST'])
def upgrade_level():
    global total_points, level, upgrade_cooldown
    if total_points >= 1500 and (time.time() - upgrade_cooldown) >= 86400:
        total_points -= 1500
        level += 1
        upgrade_cooldown = time.time()

        execute_adb_command('input keyevent 3')

        return jsonify(success=True, level=level, total_points=total_points)
    return jsonify(success=False)


if __name__ == '__main__':
    app.run(debug=True)