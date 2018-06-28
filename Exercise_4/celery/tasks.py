from celery import Celery
import smtplib

app = Celery("example1", backend="amqp://guest:guest@localhost", broker="amqp://localhost")


@app.task()
def sendmail(fromt, to, message):


    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('ivanspoof@gmail.com', 'ghdqzh30db2')
    server.sendmail(fromt, to, message)
    server.quit()






