## Документация к Flask-приложению

### Описание

Это Flask-приложение представляет собой веб-страницу с функциональностью сбора баллов, их накопления и улучшения уровня пользователя. Приложение также включает взаимодействие с ADB (Android Debug Bridge) для выполнения команд на подключенных Android-устройствах.

### Требования

- Python 3.x
- Flask
- adbutils
- jQuery

### Установка

1. Клонирование репозитория:

   
    git clone <repository-url>
    cd <repository-directory>
    
2. Создание виртуального окружения и активация:

   
    python -m venv venv
    source venv/bin/activate  # Для macOS/Linux
    .\venv\Scripts\activate  # Для Windows
    
3. Установка необходимых библиотек:

   
    pip install flask adbutils
    
4. Установка ADB (если не установлен):

    - Windows: Скачайте SDK Platform Tools [отсюда](https://developer.android.com/studio/releases/platform-tools) и добавьте путь к platform-tools в системный PATH.
    - macOS: 

       
        brew install android-platform-tools
        
    - Linux (Ubuntu/Debian):

       
        sudo apt-get update
        sudo apt-get install android-tools-adb
        
5. Проверка установки ADB:

   
    adb version
    
### Запуск приложения

1. Убедитесь, что виртуальное окружение активировано.
2. Запустите Flask приложение:

   
    python app.py
    
3. Откройте веб-браузер и перейдите по адресу http://127.0.0.1:5000.

### Структура проекта

project_directory/
│
├── app.py
├── templates/
│   └── index.html
└── static/
    └── script.js
- app.py: Главный файл приложения Flask, содержащий маршруты и логику приложения.
- templates/index.html: HTML-шаблон для отображения веб-страницы.
- static/script.js: JavaScript для взаимодействия с сервером и обновления данных на странице в реальном времени.

### API Маршруты

- GET /: Главная страница приложения.
- POST /collect: Маршрут для сбора баллов. Активирует команду ADB для включения/выключения экрана.
- GET /check_timer: Маршрут для проверки оставшегося времени для кнопки "Забрать" и улучшения уровня. Возвращает текущие баллы и состояние таймеров.
- POST /upgrade_level: Маршрут для улучшения уровня. Активирует команду ADB для возврата на главный экран.

### JavaScript функции

- updateTimers: Функция для обновления таймеров и баллов в реальном времени.
- formatTime: Форматирует время в часы, минуты и секунды.
- collectPoints: Отправляет запрос на сервер для сбора баллов.
- upgradeLevel: Отправляет запрос на сервер для улучшения уровня.
- openModal: Открывает модальное окно для улучшения уровня.
- closeModal: Закрывает модальное окно.

### Пример использования

1. Откройте веб-страницу по адресу http://127.0.0.1:5000.
2. Баллы будут автоматически начисляться каждые 20 секунд.
3. Нажмите кнопку "Забрать", чтобы собрать баллы. Кнопка станет неактивной на 2 часа.
4. Откройте модальное окно, нажав на ссылку "Вёрстка". Если у вас достаточно баллов, вы можете улучшить уровень, нажав кнопку "Улучшить уровень". Улучшение уровня будет доступно через 24 часа.

### Проверка наличия ADB и установка

Функция is_adb_installed проверяет наличие ADB на системе. Если ADB не установлен, приложение не будет выполнять команды ADB.

def is_adb_installed():
    try:
        result = os.popen('adb version').read()
        return 'Android Debug Bridge' in result
    except Exception as e:
        print(f"Error checking adb: {e}")
        return False
### Заключение

Это Flask-приложение предоставляет функциональность для сбора и накопления баллов, улучшения уровня пользователя и интеграцию с ADB для выполнения команд на подключенных Android-устройствах. Используйте предоставленные инструкции для установки и запуска приложения.