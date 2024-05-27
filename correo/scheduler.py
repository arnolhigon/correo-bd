# correo/scheduler.py
from apscheduler.schedulers.background import BackgroundScheduler
from .tasks import sumar_numeros, restar_numeros, multiplicar, import_emails

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(funciones, 'interval', seconds=5)
    scheduler.start()

def funciones():
    #sumar_numeros()
    #restar_numeros()
    #multiplicar()
    import_emails()

    


