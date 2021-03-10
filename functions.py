import random
import string
import os

ver_login = ''
ver_password = ''

pp_login = ''
pp_password = ''

VerUrl = ''
PpUrl = ''


UserVer = ''


def random_string() -> object:
    letters = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    return "".join(random.choice(letters) for i in range(10))


def random_phone():
    digits = string.digits
    return "+7999" + "".join(random.choice(digits) for i in range(7))


def passport():
    digits = string.digits
    number = "9977" + "".join(random.choice(digits) for i in range(6))
    file = open("passport.txt", "w")
    file.write(number)
    file.close()
    return number


def read(name: object) -> object:
    file = open(name)
    number = file.read(10)
    return number


def write_url(url):
    file = open("./url.txt", "w")
    file.write(url)
    file.close()


def file():
    path = ""
    dir_list = [os.path.join(path, x) for x in os.listdir(path)]
    if dir_list:
        date_list = [[x, os.path.getctime(x)] for x in dir_list]
        sort_date_list = sorted(date_list, key=lambda x: x[1], reverse=True)
    return sort_date_list [0] [0]
