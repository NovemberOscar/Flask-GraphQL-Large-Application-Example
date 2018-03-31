from datetime import datetime
from mongoengine import Document
from mongoengine.fields import (
    DateTimeField, StringField, ReferenceField
)


class Department(Document):
    meta = {'collection': 'department'}
    name = StringField()


class Role(Document):
    meta = {"collection": 'role'}
    name = StringField()


class Employee(Document):
    meta = {"collection": 'role'}
    name = StringField()
    hired_on = DateTimeField(default=datetime.now)
    department = ReferenceField(Department)
    role = ReferenceField(Role)
    