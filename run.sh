
export REDIS_URL=redis://127.0.0.1:6379
export FLASK_ENV=development
# gunicorn -w 4 mwe:app -b :8000 -k flask_sockets.worker

# gunicorn -k flask_sockets.worker app:app

# python app.py
 flask run --port=8000