import random
from russian_names import RussianNames


def generate_login():
    rn = RussianNames(count=1, patronymic=False, transliterate=True)
    person = rn.get_batch()[0].replace(' ', '_')
    person = person + str(random.randint(3, 999)) + '@yandex.ru'
    return person


def generate_password():
    password = ''
    for i in range(8):
        password += random.choice('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ')
    return password


def get_name(email_person):
    return email_person.split('_')[0]
