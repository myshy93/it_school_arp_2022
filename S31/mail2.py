from welcome_email import send_welcome_email


for i in []:
    try:
        send_welcome_email("mihai.dinu@itschool.ro", "Mihai Dinu")
    except Exception as err:
        print(err)