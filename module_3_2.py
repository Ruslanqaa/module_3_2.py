def is_valid_email(email):
    """Проверяет, является ли строка допустимым адресом электронной почты."""
    return "@" in email and (email.endswith('.com') or email.endswith('.ru') or email.endswith('.net'))


def send_email(message, recipient, *, sender="university.help@gmail.com"):
    """
    Функция для отправки электронных писем с учетом различных проверок.

    :param message: Текст сообщения
    :param recipient: Адрес получателя
    :param sender: Адрес отправителя (по умолчанию "university.help@gmail.com")
    """

    # Проверка на корректность электронной почты отправителя и получателя
    if not is_valid_email(sender) or not is_valid_email(recipient):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")
        return

    # Проверка на отправку самому себе
    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        return

    # Проверка на отправителя по умолчанию
    if sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")


# Примеры вызова функции и вывод на консоль
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
