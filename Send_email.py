import smtplib, ssl


def send_email(msg):
    host = "smtp.gmail.com"
    port = 465
    username = 'vitu2002@gmail.com'
    password = 'ndpckxijbsnyzqdk'
    receiver = "vitu2002@gmail.com"
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, msg)
