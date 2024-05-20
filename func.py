import datetime


def frenchy_format(date: str):
    datetime_object = datetime.datetime.strptime(date, "%Y-%m-%d")
    return datetime_object.strftime("%d-%m-%Y")
