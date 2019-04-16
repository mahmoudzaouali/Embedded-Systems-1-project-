from tkinter import *
import os
import sqlite3
import time
import sys
import pyqrcode
from cryptography.fernet import Fernet
from firebase import firebase

def sendmail():
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    from email.mime.base import MIMEBase
    from email import encoders

    email_user = 'tpython014@gmail.com'
    email_password = '123456789rouhrahez'
    email_send = 'tpython014@gmail.com'

    subject = 'subject'

    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_send
    msg['Subject'] = subject

    body = 'Hi there, sending this email from Python!'
    msg.attach(MIMEText(body, 'plain'))

    filename = 'big-number.png'
    attachment = open(filename, 'rb')

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= " + filename)

    msg.attach(part)
    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_user, email_password)

    server.sendmail(email_user, email_send, text)
    server.quit()

def qrcode_generator():

    fb = firebase.FirebaseApplication('https://empedded-system-vise-project.firebaseio.com/')

    qr = qr_example.get()
    #number = pyqrcode.create(qr)
    #number.png('big-number.png', scale=10)
    #number.show()
    #sendmail()
    #qr_entry.delete(0, END)


    key = "yj7lkrUlbUHYLpB2o7_zCEFw5RysDUEQ76PeHacHs0c="
    encoded = qr.encode()
    # Encrypt the message
    f = Fernet(key)
    encrypted = f.encrypt(encoded)
    print(encrypted)

    gQrcode = pyqrcode.create(encrypted)
    gQrcode.png('big-number.png', scale=10)
    gQrcode.show()
    sendmail()
    qr_entry.delete(0, END)

    with sqlite3.connect("RegistrationDatabase") as conn:
        c = conn.cursor()


    c.execute("SELECT * FROM user WHERE username=:username",{'username':username1})
    result = c.fetchall()
    firstName= result[0][2]
    lastName= result[0][3]


    resultPut1 = fb.put('users', encrypted, {'userName': username1, 'firstname':firstName,'lastname':lastName,'flag':'0'})#######


def delete4():
    screen5.destroy()


def session():
    global screen6
    screen6 = Toplevel(screen)
    screen6.title("QR generator")
    screen6.geometry("250x250")
    Label(screen6, text="").pack()
    Label(screen6, text="**welcome to QR code generator**").pack()
    Label(screen6, text="").pack()
    Label(screen6, text="").pack()

    global qr_example
    global qr_entry
    global qr
    qr_example = StringVar()

    Label(screen6, text="Enter your QR code example").pack()
    qr_entry = Entry(screen6, textvariable=qr_example)
    qr = str(qr_entry)
    qr_entry.pack()
    Button(screen6, text="Create QR", command=qrcode_generator).pack()
    qr_entry.delete(0, END)
    #sendmail()


def login_success():
    session()

    # global screen3
    # screen3 = Toplevel(screen)
    # screen3.title("success")
    # screen3.geometry("150x100")
    # Label(screen3, text="Login success").pack()
    # Button(screen3, text="OK", command=delete2).pack()


# def password_not_recognised():
#   global screen4
#  screen4 = Toplevel(screen)
# screen4.title("Error")
# screen4.geometry("150x100")
# Label(screen4, text="Password Error").pack()
# Button(screen4, text="OK", command=delete3).pack()


def user_not_found():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("Error")
    screen5.geometry("150x100")
    Label(screen5, text="User not found").pack()
    Button(screen5, text="OK", command=delete4).pack()


def fetch_things():
    with sqlite3.connect("RegistrationDatabase") as conn:
        c = conn.cursor()
    c.execute("SELECT * FROM user ")
    print(c.fetchall())


def register_user():
    with sqlite3.connect("RegistrationDatabase") as conn:
        c = conn.cursor()

    found = 0

    while found == 0:

        id_info = ID.get()
        username_info = username.get()

        c.execute("SELECT * FROM user WHERE userID = :userID AND username = :username",
                  {'userID': id_info, 'username': username_info})

        if c.fetchall():
            Label(screen1, text="the user name or userID taken, please try again ")

        else:
            found = 1

    firstname_info = first_name.get()
    lastname_info = last_name.get()
    password_info = password.get()
    npassword_info = password_new.get()

    while password_info != npassword_info:
        Label(screen1, text="passwords don\'t match! please write them again.. ")
        password_info = password.get()
        npassword_info = password_new.get()
    # file = open(username_info, "w")
    # file.write(username_info + "\n")
    # file.write(password_info + "\n")
    # file.write(id_info + "\n")
    # file.write(npassword_info)

    # file.close()

    c.execute("INSERT INTO user VALUES(:userID,:username,:first_name,:surname,:password)",
              {'userID': id_info, 'username': username_info, 'first_name': firstname_info, 'surname': lastname_info,
               'password': password_info})
    conn.commit()

    username_entry.delete(0, END)
    password_entry.delete(0, END)
    ID_entry.delete(0, END)
    npassword_entry.delete(0, END)
    firstname_entry.delete(0, END)
    lastname_entry.delete(0, END)

    Label(screen1, text="Registration Success", fg="green", font=("calibri", 11)).pack()


def login_verify():
    # while TRUE:
    global username1
    global password1
    username1 = username_verify.get()
    password1 = password_verify.get()

    with sqlite3.connect("RegistrationDatabase") as conn:
        c = conn.cursor()
    c.execute("SELECT * FROM user WHERE username = :username AND password = :password",
              {'username': username1, 'password': password1})

    result = c.fetchall()
    if result:
        for i in result:
            login_success()


    else:
        user_not_found()
        username_entry1.delete(0, END)
        password_entry1.delete(0, END)

def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("400x400")
    global username
    global password
    global username_entry
    global password_entry
    global ID_entry
    global ID
    global password_new
    global npassword_entry
    global first_name
    global last_name
    global firstname_entry
    global lastname_entry

    ID = StringVar()
    username = StringVar()
    password = StringVar()
    first_name = StringVar()
    last_name = StringVar()
    password_new = StringVar()

    Label(screen1, text="Please enter details below").pack()
    Label(screen1, text="").pack()
    Label(screen1, text="Username ID *").pack()
    ID_entry = Entry(screen1, textvariable=ID)
    ID_entry.pack()
    Label(screen1, text="Username *").pack()
    username_entry = Entry(screen1, textvariable=username)
    username_entry.pack()

    Label(screen1, text="First name *").pack()
    firstname_entry = Entry(screen1, textvariable=first_name)
    firstname_entry.pack()

    Label(screen1, text="Last name *").pack()
    lastname_entry = Entry(screen1, textvariable=last_name)
    lastname_entry.pack()

    Label(screen1, text="Password *").pack()
    password_entry = Entry(screen1, textvariable=password, show="*")
    password_entry.pack()

    Label(screen1, text="Confirm new Password*").pack()
    npassword_entry = Entry(screen1, textvariable=password_new, show="*")
    npassword_entry.pack()

    Label(screen1, text="").pack()
    Button(screen1, text="Register", width=10, height=1, command=register_user).pack()


def login():
    global screen2

    screen2 = Toplevel(screen)
    screen2.title = ("Login")
    screen2.geometry("300x250")
    Label(screen2, text="Please enter details below to login").pack()
    Label(screen2, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_entry1
    global password_entry1

    Label(screen2, text="Username *").pack()
    username_entry1 = Entry(screen2, textvariable=username_verify)
    username_entry1.pack()
    Label(screen2, text="").pack()

    Label(screen2, text="password *").pack()
    password_entry1 = Entry(screen2, textvariable=password_verify, show="*")
    password_entry1.pack()
    Label(screen2, text="").pack()
    Button(screen2, text="Login", width=10, height=1, command=login_verify).pack()

def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("Notes 1.0")
    Label(text="notes 1.0", bg="grey", width="300", height="2", font=("calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="1", width="30", command=login).pack()
    Label(text="").pack()
    Button(text="Register", height="1", width="30", command=register).pack()

    screen.mainloop()


main_screen()
