from SupplyMe.celery import app

from .service import send

@app.task 
def send_registration_confirmation(user_email):
    send(user_email)