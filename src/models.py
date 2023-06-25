from mongoengine import Document
from mongoengine.fields import ListField, StringField, ReferenceField, BooleanField, EmailField


class Authors(Document):
    fullname: StringField = StringField(required=True, unique=True)
    born_date: StringField = StringField()
    born_location: StringField = StringField()
    description: StringField = StringField()


class Quotes(Document):
    tags:  ListField = ListField(StringField())
    author: ReferenceField = ReferenceField(Authors, required=True)
    quote: StringField = StringField()


class Contacts(Document):
    fullname: StringField = StringField(required=True)
    email: EmailField = EmailField(required=True)
    address: StringField = StringField()
    email_sent: BooleanField = BooleanField(default=False)
