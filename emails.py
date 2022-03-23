#------Import-------#
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import PySimpleGUI as sg
# -------------------------------------


def wow():
    sg.popup("""Let's send Emails
             by Said Mounji""")
    layout = [
        [sg.Text("-Enter your Email :"), sg.InputText()],
        [sg.Text("-Enter your Password :"), sg.InputText()],
        [sg.Text("-Enter The receiver's email :"), sg.InputText()],
        [sg.Text("-Enter your Subject :"), sg.InputText()],
        [sg.Text("-Enter your Body :"), sg.Multiline("")],
        [sg.Button("Ok"), sg.Button("Cancel")],
    ]
    window = sg.Window("emails_SM", layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Cancel":
            break
        gmail_user, gmail_password, to = values[0], values[1], values[2]
        msg = MIMEMultipart()
        msg['From'] = gmail_user
        msg['Subject'] = values[3]
        body = values[4]
        msg.attach(MIMEText(body, 'plain'))
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(gmail_user, gmail_password)
        text = msg.as_string()
        s.sendmail(gmail_user, to, text)
        s.close()

    window.close()


def main():
    wow()


wow()
