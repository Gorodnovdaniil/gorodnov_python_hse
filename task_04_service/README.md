# gorodnov_python_hse

# Проект сервиса на FastAPI и Streamlit

Это проект сервиса, который работает используя FastAPI фреймворк Streamlit.

## Скелет проекта:
task_04_service/
├── backend/
│ ├── main.py # вся программа бэкэнда
│ └── data.csv # данные, скачанные по ссылке
├── frontend/
│ └── app.py # вся программа фронтенда
├── requirements.txt # все зависимости которые необходимо загрузить при развертывании сервиса
└── README.md

### Файлы:
- **app.py**: файл приложения streamlit
- **main.py**: файл с pydantic валидацией и эндпоинтами FastAPI
- **data.csv**: файл с данными
- **requirements.txt**: файлы требований к пакету

## Запустите демо-версию локально

Чтобы запустить Streamlit локально, перейдите в корневую папку репозитория и выполните следующие действия:

# Создание виртуального окружения
python -m venv venv

# Активация виртуального окружения
source venv/bin/activate  # для Linux/Mac

# Установка зависимостей
pip install -r requirements.txt

# Запуск FastAPI сервера (из корневой папки)
uvicorn backend.main:app --reload

Далее перейдите в папку frontend и выполните:

cd frontend

streamlit run app.py

Откройте http://localhost:8501, чтобы просмотреть приложение.
