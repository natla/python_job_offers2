web: python manage.py collectstatic --noinput; gunicorn --workers=4 --bind=0.0.0.0:$PORT scraper/settings.py 
