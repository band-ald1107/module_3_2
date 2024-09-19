def send_email(message, recipient, sender="university.help@gmail.com"):
    valid_domains = (".com", ".ru", ".net")

    def is_valid_email(email):
        return "@" in email and email.endswith(valid_domains)

    if not is_valid_email(sender) or not is_valid_email(recipient):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")
        return

    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        return

    if sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")


send_email("Привет! Как дела?", "recipient@example.com")
send_email("Привет! Как дела?", "recipient@example.com", "custom.sender@gmail.com")
send_email("Привет! Как дела?", "recipient@example")
send_email("Привет! Как дела?", "university.help@gmail.com") 
