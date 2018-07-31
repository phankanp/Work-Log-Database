from datetime import datetime

from peewee import *

db = SqliteDatabase('entries.db')


class Entry(Model):
    employee_name = CharField(max_length=255)
    task_name = CharField(max_length=255)
    mins = IntegerField()
    notes = CharField(max_length=255)
    date = DateField(default=datetime.today)

    class Meta:
        database = db


def initialize():
    db.connect()
    db.create_tables([Entry], safe=True)